import os

from vistrails.core import debug
from vistrails.core.modules.basic_modules import Boolean, Float, Integer, \
    String
from vistrails.core.modules.module_registry import get_module_registry
from vistrails.core.modules.package import Package
from vistrails.core.system import current_dot_vistrails, \
    get_elementtree_library

from . import identifiers
from .module_runtime import GetterModuleMixin, ConstructorModuleMixin, \
    JavaBaseModule
from .structs import PackageInfos


class JavaPackage(object):
    def __init__(self, pkgname):
        self.pkgname = pkgname

        debug.log("Creating Java package for %s" % pkgname)

        ElementTree = get_elementtree_library()

        # Find the XML file
        xmlfile = os.path.join(current_dot_vistrails(),
                                'Java',
                                pkgname + '.xml')
        tree = ElementTree.parse(xmlfile)
        package_infos = PackageInfos.from_xml(tree.getroot())

        # This is copied from SUDS
        pkg_signature = 'Java#%s' % pkgname
        pkg_version = '1'
        reg = get_module_registry()
        if pkg_signature in reg.packages:
            reg.remove_package(reg.packages[pkg_signature])
        package_id = reg.idScope.getNewId(Package.vtType)
        package = Package(id=package_id,
                          load_configuration=False,
                          name='Java#' + pkgname,
                          identifier=pkg_signature,
                          version='1')
        java_package = reg.get_package_by_name(identifiers.identifier)
        package._module = java_package.module
        package._init_module = java_package.init_module
        self.package = package
        reg.add_package(package)
        reg.signals.emit_new_package(pkg_signature)
        #
        package.prefix = ''
        package.codepath = 'java'

        try:
            creator = ModuleCreator(package_infos, pkg_signature, pkg_version)
            creator.create_all_modules()
        except:
            self.disable()
            raise

    def disable(self):
        reg = get_module_registry()
        reg.remove_package(self.package)


_type_to_module = {
        'int': Integer, 'long': Integer, 'Integer': Integer, 'Long': Integer,
        'float': Float, 'double': Float, 'Float': Float, 'Double': Float,
        'boolean': Boolean, 'Boolean': Boolean,
        'java.lang.String': String}


def fullname_to_pair(fullname):
    """Turns a full Java name (pkg.Class) into a namespace/module tuple.

    >>> fullname_to_pair('java.lang.String')
    ('java|lang', 'String')
    >>> fullname_to_pair('int')
    (None, 'int')
    """
    try:
        sep = fullname.rindex('.')
        return (
                fullname[:sep].replace('.', '|'),
                fullname[sep+1:])
    except ValueError:
        return (None, fullname)


class ModuleCreator(object):
    """Walk over the module info structure and emit the Modules in order.

    Here, the objective is to create all the Modules associated with each Java
    class.
    The structure is as follow:
      - An abstract module is created for the class, which represents this
          datatype. It also has all the getters (converted into output ports),
          and inherits from the abstract module associated with the parent
          class, or WekaBaseModule.
      - A concrete module used to call getters. It inherits from the abstract
          module, so it has the getter ports, and has a single input port
          'this'.
          The module name is appended '_get'.
      - For each constructor, a concrete module is created. It inherits from
          the abstract module, so it has all the getter ports, and has an input
          port for each constructor parameter. It also has the setters.
          An output port 'this' returns the object constructed with the
          parameters and after the setters have been called.
          The module name is appended an underscore and a number.
      - For each static method, a concrete module is created. It inherits
          from the WekaBaseModule directly, not from the abstract module.
          The module name is appended an underscore and the method name.

    _create_module is used to create all the abstract modules, creating the
    parent first if it exists.
    Then, _populate_modules is used to add the getter ports to the abstract
    modules and to create the concrete modules.
    This is done in two steps because the modules might be referenced as a
    datatype by a port on another module.
    """
    class CyclicInheritance(Exception):
        """We found a cycle in the inheritance graph.

        Weird. Java would complain.
        """
        pass

    class MissingParent(Exception):
        """Some class inherits from a class we don't know about.
        """
        # FIXME : shouldn't we just ignore that dependency and add the module
        # as a top-level module?
        pass

    def __init__(self, package_infos, pkg_signature, pkg_version):
        self._package_infos = package_infos
        self._created_modules = dict()
        self._module_registry = get_module_registry()
        self._used_methods = 0
        self._ignored_methods = 0

        self.pkg_opts = {'package': pkg_signature,
                         'package_version': pkg_version}

    def _get_type_module(self, typename):
        """Return the VisTrails module that represents the given typename.
        """
        # If this is one of the Java classes, we can return the abstract
        # module associated with it
        if typename in self._created_modules:
            return self._created_modules[typename]
        # Else we look it up in our map of standard types
        elif typename in _type_to_module:
            return _type_to_module[typename]
        # No match; default on the base Java module
        else:
            return JavaBaseModule

    def _create_module(self, clasz):
        if clasz.fullname in self._created_modules:
            # Already created
            return

        if clasz.fullname in self._creating_modules:
            # Already being created! We stumbled on the same module while
            # following the 'extends' relations! This is bad!
            raise ModuleCreator.CyclicInheritance
        self._creating_modules.add(clasz.fullname)

        # Process the parent class first
        parent = JavaBaseModule
        if clasz.superclass is not None:
            if clasz.superclass not in self._created_modules:
                try:
                    parent = self._package_infos.classes[clasz.superclass]
                except KeyError:
                    raise ModuleCreator.MissingParent(
                            "%s extends %s but it couldn't be found" % (
                                    clasz.fullname,
                                    clasz.superclass))
                self._create_module(parent)
            parent = self._created_modules[clasz.superclass]

        (namespace, name) = fullname_to_pair(clasz.fullname)

        # Create the abstract module
        mod = type(str(name), (parent,), dict(
                _classname=clasz.fullname,
                _namespace=namespace))
        self._module_registry.add_module(mod, abstract=True,
                                         namespace=namespace,
                                         **self.pkg_opts)
        self._created_modules[clasz.fullname] = mod

    def _populate_modules(self, clasz):
        mod = self._created_modules[clasz.fullname]
        name = mod.__name__
        namespace = mod._namespace

        # We identify the input ports for the setters, and the output ports for
        # the getters
        # Note that we only add the getters as ports of the Module!
        setters = dict()
        getters = set()
        for method in clasz.methods:
            # Setters
            if (method.name.startswith('set') and
                    len(method.parameters) == 1):
                setters[method.name] = (
                        self._get_type_module(method.parameters[0].type),
                        method.parameters[0].name)
                self._used_methods += 1
            # Getters
            elif (method.name.startswith('get') and
                    len(method.parameters) == 0):
                getters.add(method.name)
                self._module_registry.add_output_port(
                        mod, method.name,
                        (
                                self._get_type_module(method.return_type),
                                method.return_type))
                self._used_methods += 1
            else:
                self._ignored_methods += 1
        mod._setters = set(setters.keys())
        mod._getters = getters

        # Create the getter module
        if getters:
            cname = '%s_get' % name
            cmod = type(
                    str(cname),
                    (GetterModuleMixin, mod),
                    dict())
            self._module_registry.add_module(cmod, namespace=namespace,
                                             **self.pkg_opts)
            self._module_registry.add_input_port(
                    cmod, 'this',
                    (mod, 'the object to call getters on'))

        # Now, we need to create a new concrete module for each constructor
        if not clasz.is_abstract:
            i = 0
            for ctor in clasz.constructors:
                i += 1
                cname = '%s_%d' % (name, i)
                cmod = type(
                        str(cname),
                        (ConstructorModuleMixin, mod),
                        dict(_ctor_params=ctor.parameters))
                self._module_registry.add_module(cmod, namespace=namespace,
                                                 **self.pkg_opts)
                # Constructor parameters
                for param in ctor.parameters:
                    self._module_registry.add_input_port(
                            cmod, ("ctor_%s" % param.name),
                            (
                                    self._get_type_module(param.type),
                                    param.name))
                # Setters
                for sname, (t, n) in setters.iteritems():
                    self._module_registry.add_input_port(
                            cmod, sname,
                            (t, n))
                # The 'this' output port, that returns the created object
                self._module_registry.add_output_port(
                        cmod, 'this',
                        (mod, 'the created object'))

        # TODO : static methods

    def create_all_modules(self):
        # Create the abstract modules
        for clasz in self._package_infos.classes.itervalues():
            # This field is used to detect cycles in the dependency graph
            self._creating_modules = set()

            self._create_module(clasz)

        # Add the input/output ports and create the concrete modules
        for clasz in self._package_infos.classes.itervalues():
            self._populate_modules(clasz)

##############################################################################

import doctest
import unittest


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(None))
    return tests


if __name__ == '__main__':
    unittest.main()
############################################################################
##
## Copyright (C) 2006-2007 University of Utah. All rights reserved.
##
## This file is part of VisTrails.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following to ensure GNU General Public
## Licensing requirements will be met:
## http://www.opensource.org/licenses/gpl-license.php
##
## If you are unsure which license is appropriate for your use (for
## instance, you are interested in developing a commercial derivative
## of VisTrails), please contact us at vistrails@sci.utah.edu.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################
"""ImageMagick package for VisTrails.

This package defines a set of modules that perform some of the
operations exposed by the ImageMagick package.

"""

import core.modules
import core.modules.module_registry
import core.modules.basic_modules
from core.modules.vistrails_module import Module, ModuleError, newModule, IncompleteImplementation
import core.requirements
import core.system
from core.system import list2cmdline
import core.bundles
import os

import popen2

identifier = 'edu.utah.sci.vistrails.imagemagick'
name = 'ImageMagick'
version = '0.9.0'

################################################################################

class ImageMagick(Module):
    """ImageMagick is the base Module for all Modules in the ImageMagick
package. It simply defines some helper methods for subclasses."""

    def compute(self):
        raise IncompleteImplementation

    def input_file_description(self):
        """Returns a fully described name in the ImageMagick format. For example,
a file stored in PNG format may be described by its extension

        - 'graphic.png' indicates the filename 'graphic.png', using the PNG
        file format.

        - 'graphic:png' indicates the filename 'graphic', still using the PNG
        file format."""
        i = self.getInputFromPort("input")
        if self.hasInputFromPort('inputFormat'):
            return self.getInputFromPort('inputFormat') + ':' + i.name
        else:
            return i.name


class Convert(ImageMagick):
    """Convert is the base Module for VisTrails Modules in the ImageMagick
package that deal with operations on images. Convert is a bit of a misnomer since
the 'convert' tool does more than simply file format conversion. Each subclass
has a descriptive name of the operation it implements."""

    __quiet = True

    def create_output_file(self):
        """Creates a File with the output format given by the
outputFormat port."""
        if self.hasInputFromPort('outputFormat'):
            s = '.' + self.getInputFromPort('outputFormat')
            return self.interpreter.filePool.create_file(suffix=s)

    def geometry_description(self):
        """returns a string with the description of the geometry as
indicated by the appropriate ports (geometry or width and height)"""
        # if complete geometry is available, ignore rest
        if self.hasInputFromPort("geometry"):
            return self.getInputFromPort("geometry")
        elif self.hasInputFromPort("width"):
            w = self.getInputFromPort("width")
            h = self.getInputFromPort("height")
            return "'%sx%s'" % (w, h)
        else:
            raise ModuleError(self, "Needs geometry or width/height")

    def run(self, *args):
        """run(*args), runs ImageMagick's 'convert' on a shell, passing all
arguments to the program."""
        cmd = ['convert'] + list(args)
        cmdline = list2cmdline(cmd)
        if not self.__quiet:
            print cmdline
        r = os.system(cmdline)
        if r != 0:
            raise ModuleError(self, "system call failed: '%s'" % cmdline)

    def compute(self):
        o = self.create_output_file()
        i = self.input_file_description()
        self.run(i, o.name)
        self.setResult("output", o)
        

class Negate(Convert):
    """Negate returns the two's complement negation of the image."""

    def compute(self):
        o = self.create_output_file()
        i = self.input_file_description()
        self.run(i,
                 "-negate",
                 o.name)
        self.setResult("output", o)


class Scale(Convert):
    """Scale rescales the input image to the given geometry description."""

    def compute(self):
        o = self.create_output_file()
        self.run(self.input_file_description(),
                 "-scale",
                 self.geometry_description(),
                 o.name)
        self.setResult("output", o)


class GaussianBlur(Convert):
    """GaussianBlur convolves the image with a Gaussian filter of given radius
and standard deviation."""

    def compute(self):
        (radius, sigma) = self.getInputFromPort('radiusSigma')
        o = self.create_output_file()
        self.run(self.input_file_description(),
                 "-blur %sx%s" % (radius, sigma),
                 o.name)
        self.setResult("output", o)


no_param_options = [("Negate", "-negate",
                     """Negate performs the two's complement negation of the image."""
                     ),
                    ("EqualizeHistogram", "-equalize", None),
                    ("Enhance", "-enhance", None),
                    ("VerticalFlip", "-flip", None),
                    ("HorizontalFlip", "-flop", None),
                    ("FloydSteinbergDither", "-dither", None),
                    ("IncreaseContrast", "-contrast", None),
                    ("Despeckle", "-despeckle", None),
                    ("Normalize", "-normalize", None)]


def no_param_options_method_dict(optionName):
    """Creates a method dictionary for a module that takes no extra
parameters. This dictionary will be used to dynamically create a
VisTrails module."""
   
    def compute(self):
        o = self.create_output_file()
        i = self.input_file_description()
        self.run(i, optionName, o.name)
        self.setResult("output", o)

    return {'compute': compute}


float_param_options = [("DetectEdges", "-edge", "radius", "filter radius"),
                       ("Emboss", "-emboss", "radius", "filter radius"),
                       ("GammaCorrect", "-gamma", "gamma", "gamma correction factor"),
                       ("MedianFilter", "-median", "radius", "filter radius")]

def float_param_options_method_dict(optionName, portName):
    """Creates a method dictionary for a module that has one port
taking a floating-point value. This dictionary will be used to
dynamically create a VisTrails module."""

    def compute(self):
        o = self.create_output_file()
        optionValue = self.getInputFromPort(portName)
        i = self.input_file_description()
        self.run(i, optionName, optionValue, o.name)
        self.setResult("output", o)

    return {'compute': compute}



################################################################################

def initialize():
    
    def parse_error_if_not_equal(s, expected):
        if s != expected:
            err = "Parse error on version line. Was expecting '%s', got '%s'"
            raise Exception(err % (s, expected))
    
    print "ImageMagick VisTrails package"
    print "-----------------------------"
    print "Will test ImageMagick presence..."

    

    if (not core.requirements.executable_file_exists('convert') and
        not core.bundles.install({'linux-ubuntu': 'imagemagick'})):
        raise core.requirements.MissingRequirement("ImageMagick suite")
    if core.system.systemType not in ['Windows', 'Microsoft']: 
        process = popen2.Popen4("convert -version")

        result = -1
        while result == -1:
            result = process.poll()
        conv_output = process.fromchild
    else:
        conv_output, input = popen2.popen4("convert -version")
        result = 0
        
    version_line = conv_output.readlines()[0][:-1].split(' ')
    if result != 0:
        raise Exception("ImageMagick does not seem to be present.")
    print "Ok, found ImageMagick"
    parse_error_if_not_equal(version_line[0], 'Version:')
    parse_error_if_not_equal(version_line[1], 'ImageMagick')
    print "Detected version %s" % version_line[2]
    global __version__
    __version__ = version_line[2]

    reg = core.modules.module_registry
    basic = core.modules.basic_modules
    reg.addModule(ImageMagick, abstract=True)
    reg.addInputPort(ImageMagick, "input", (basic.File, 'the input file'))
    reg.addInputPort(ImageMagick, "inputFormat", (basic.String, 'coerce interpretation of file to this format'))
    reg.addInputPort(ImageMagick, "outputFormat", (basic.String, 'Force output to be of this format'))

    reg.addModule(Convert)
    reg.addInputPort(Convert, "geometry", (basic.String, 'ImageMagick geometry'))
    reg.addInputPort(Convert, "width", (basic.String, 'width of the geometry for operation'))
    reg.addInputPort(Convert, "height", (basic.String, 'height of the geometry for operation'))
    reg.addOutputPort(Convert, "output", (basic.File, 'the output file'))

    for (name, opt, doc_string) in no_param_options:
        m = newModule(Convert, name, no_param_options_method_dict(opt),
                      docstring=doc_string)
        reg.addModule(m)

    for (name, opt, paramName, paramComment) in float_param_options:
        m = newModule(Convert, name, float_param_options_method_dict(opt, paramName))
        reg.addModule(m)
        reg.addInputPort(m, paramName, (basic.Float, paramComment))

    reg.addModule(GaussianBlur)
    reg.addInputPort(GaussianBlur, "radiusSigma", [(basic.Float, 'radius'), (basic.Float, 'sigma')])

    reg.addModule(Scale)

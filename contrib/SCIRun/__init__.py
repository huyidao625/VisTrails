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
## of VisTrails), please contact us at contact@vistrails.org.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################

# This file was generated using vistrail_converter.py

import core.modules
import core.modules.module_registry
from core.modules.vistrails_module import Module, ModuleError
from core.modules.basic_modules import Constant
import sr_py
import os
import time


version = "0.9.1"
identifier = "edu.utah.sci.vistrails.scirun"
name = "SCIRun"

class Time(Constant):
  def compute(self): 
    pass

class Converters(Constant):
  def compute(self): 
    pass

class Texture(Constant):
  def compute(self): 
    pass

class Visualization(Constant):
  def compute(self): 
    pass

class MiscField(Constant):
  def compute(self): 
    pass

class DataArrayMath(Constant):
  def compute(self): 
    pass

class Math(Constant):
  def compute(self): 
    pass

class ChangeMesh(Constant):
  def compute(self): 
    pass

class ChangeFieldData(Constant):
  def compute(self): 
    pass

class Geometry(Constant):
  def compute(self): 
    pass

class NewField(Constant):
  def compute(self): 
    pass

class ColorMap(Constant):
  def compute(self): 
    pass

class Field(Constant):
  def compute(self): 
    pass

class Nrrd(Constant):
  def compute(self): 
    pass

class Matrix(Constant):
  def compute(self): 
    pass

class ColorMap2(Constant):
  def compute(self): 
    pass

class Path(Constant):
  def compute(self): 
    pass

class String(Constant):
  def compute(self): 
    pass

class Bundle(Constant):
  def compute(self): 
    pass

class DataIO(Constant):
  def compute(self): 
    pass

class WriteBundle(DataIO) :
  def compute(self) :
    p = sr_py.WriteBundleAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(bundle, Filename)

class WritePath(DataIO) :
  def compute(self) :
    p = sr_py.WritePathAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    Input_Data = 0
    if self.has_input('Input Data') :
      Input_Data = self.get_input('Input Data')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Input_Data, Filename)

class WriteColorMap2D(DataIO) :
  def compute(self) :
    p = sr_py.WriteColorMap2DAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    if self.has_input('p_exporttype') :
      p.set_p_exporttype(self.get_input('p_exporttype'))
    Input_Data = 0
    if self.has_input('Input Data') :
      Input_Data = self.get_input('Input Data')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Input_Data, Filename)

class ReadHDF5File(DataIO) :
  def compute(self) :
    p = sr_py.ReadHDF5FileAlg()
    if self.has_input('p_have_HDF5') :
      p.set_p_have_HDF5(self.get_input('p_have_HDF5'))
    if self.has_input('p_power_app') :
      p.set_p_power_app(self.get_input('p_power_app'))
    if self.has_input('p_datasets') :
      p.set_p_datasets(self.get_input('p_datasets'))
    if self.has_input('p_dumpname') :
      p.set_p_dumpname(self.get_input('p_dumpname'))
    if self.has_input('p_ports') :
      p.set_p_ports(self.get_input('p_ports'))
    if self.has_input('p_ndims') :
      p.set_p_ndims(self.get_input('p_ndims'))
    if self.has_input('p_mergeData') :
      p.set_p_mergeData(self.get_input('p_mergeData'))
    if self.has_input('p_assumeSVT') :
      p.set_p_assumeSVT(self.get_input('p_assumeSVT'))
    if self.has_input('p_animate') :
      p.set_p_animate(self.get_input('p_animate'))
    if self.has_input('p_animate_tab') :
      p.set_p_animate_tab(self.get_input('p_animate_tab'))
    if self.has_input('p_basic_tab') :
      p.set_p_basic_tab(self.get_input('p_basic_tab'))
    if self.has_input('p_extended_tab') :
      p.set_p_extended_tab(self.get_input('p_extended_tab'))
    if self.has_input('p_playmode_tab') :
      p.set_p_playmode_tab(self.get_input('p_playmode_tab'))
    if self.has_input('p_selectable_min') :
      p.set_p_selectable_min(self.get_input('p_selectable_min'))
    if self.has_input('p_selectable_max') :
      p.set_p_selectable_max(self.get_input('p_selectable_max'))
    if self.has_input('p_selectable_inc') :
      p.set_p_selectable_inc(self.get_input('p_selectable_inc'))
    if self.has_input('p_range_min') :
      p.set_p_range_min(self.get_input('p_range_min'))
    if self.has_input('p_range_max') :
      p.set_p_range_max(self.get_input('p_range_max'))
    if self.has_input('p_playmode') :
      p.set_p_playmode(self.get_input('p_playmode'))
    if self.has_input('p_current') :
      p.set_p_current(self.get_input('p_current'))
    if self.has_input('p_execmode') :
      p.set_p_execmode(self.get_input('p_execmode'))
    if self.has_input('p_delay') :
      p.set_p_delay(self.get_input('p_delay'))
    if self.has_input('p_inc_amount') :
      p.set_p_inc_amount(self.get_input('p_inc_amount'))
    if self.has_input('p_update_type') :
      p.set_p_update_type(self.get_input('p_update_type'))
    if self.has_input('p_have_group') :
      p.set_p_have_group(self.get_input('p_have_group'))
    if self.has_input('p_have_attributes') :
      p.set_p_have_attributes(self.get_input('p_have_attributes'))
    if self.has_input('p_have_datasets') :
      p.set_p_have_datasets(self.get_input('p_have_datasets'))
    if self.has_input('p_continuous') :
      p.set_p_continuous(self.get_input('p_continuous'))
    if self.has_input('p_selectionString') :
      p.set_p_selectionString(self.get_input('p_selectionString'))
    if self.has_input('p_regexp') :
      p.set_p_regexp(self.get_input('p_regexp'))
    if self.has_input('p_allow_selection') :
      p.set_p_allow_selection(self.get_input('p_allow_selection'))
    if self.has_input('p_read_error') :
      p.set_p_read_error(self.get_input('p_read_error'))
    if self.has_input('p_max_dims') :
      p.set_p_max_dims(self.get_input('p_max_dims'))
    if self.has_input('p_0_dim') :
      p.set_p_0_dim(self.get_input('p_0_dim'))
    if self.has_input('p_0_start') :
      p.set_p_0_start(self.get_input('p_0_start'))
    if self.has_input('p_0_start2') :
      p.set_p_0_start2(self.get_input('p_0_start2'))
    if self.has_input('p_0_count') :
      p.set_p_0_count(self.get_input('p_0_count'))
    if self.has_input('p_0_count2') :
      p.set_p_0_count2(self.get_input('p_0_count2'))
    if self.has_input('p_0_stride') :
      p.set_p_0_stride(self.get_input('p_0_stride'))
    if self.has_input('p_0_stride2') :
      p.set_p_0_stride2(self.get_input('p_0_stride2'))
    if self.has_input('p_1_dim') :
      p.set_p_1_dim(self.get_input('p_1_dim'))
    if self.has_input('p_1_start') :
      p.set_p_1_start(self.get_input('p_1_start'))
    if self.has_input('p_1_start2') :
      p.set_p_1_start2(self.get_input('p_1_start2'))
    if self.has_input('p_1_count') :
      p.set_p_1_count(self.get_input('p_1_count'))
    if self.has_input('p_1_count2') :
      p.set_p_1_count2(self.get_input('p_1_count2'))
    if self.has_input('p_1_stride') :
      p.set_p_1_stride(self.get_input('p_1_stride'))
    if self.has_input('p_1_stride2') :
      p.set_p_1_stride2(self.get_input('p_1_stride2'))
    if self.has_input('p_2_dim') :
      p.set_p_2_dim(self.get_input('p_2_dim'))
    if self.has_input('p_2_start') :
      p.set_p_2_start(self.get_input('p_2_start'))
    if self.has_input('p_2_start2') :
      p.set_p_2_start2(self.get_input('p_2_start2'))
    if self.has_input('p_2_count') :
      p.set_p_2_count(self.get_input('p_2_count'))
    if self.has_input('p_2_count2') :
      p.set_p_2_count2(self.get_input('p_2_count2'))
    if self.has_input('p_2_stride') :
      p.set_p_2_stride(self.get_input('p_2_stride'))
    if self.has_input('p_2_stride2') :
      p.set_p_2_stride2(self.get_input('p_2_stride2'))
    if self.has_input('p_3_dim') :
      p.set_p_3_dim(self.get_input('p_3_dim'))
    if self.has_input('p_3_start') :
      p.set_p_3_start(self.get_input('p_3_start'))
    if self.has_input('p_3_start2') :
      p.set_p_3_start2(self.get_input('p_3_start2'))
    if self.has_input('p_3_count') :
      p.set_p_3_count(self.get_input('p_3_count'))
    if self.has_input('p_3_count2') :
      p.set_p_3_count2(self.get_input('p_3_count2'))
    if self.has_input('p_3_stride') :
      p.set_p_3_stride(self.get_input('p_3_stride'))
    if self.has_input('p_3_stride2') :
      p.set_p_3_stride2(self.get_input('p_3_stride2'))
    if self.has_input('p_4_dim') :
      p.set_p_4_dim(self.get_input('p_4_dim'))
    if self.has_input('p_4_start') :
      p.set_p_4_start(self.get_input('p_4_start'))
    if self.has_input('p_4_start2') :
      p.set_p_4_start2(self.get_input('p_4_start2'))
    if self.has_input('p_4_count') :
      p.set_p_4_count(self.get_input('p_4_count'))
    if self.has_input('p_4_count2') :
      p.set_p_4_count2(self.get_input('p_4_count2'))
    if self.has_input('p_4_stride') :
      p.set_p_4_stride(self.get_input('p_4_stride'))
    if self.has_input('p_4_stride2') :
      p.set_p_4_stride2(self.get_input('p_4_stride2'))
    if self.has_input('p_5_dim') :
      p.set_p_5_dim(self.get_input('p_5_dim'))
    if self.has_input('p_5_start') :
      p.set_p_5_start(self.get_input('p_5_start'))
    if self.has_input('p_5_start2') :
      p.set_p_5_start2(self.get_input('p_5_start2'))
    if self.has_input('p_5_count') :
      p.set_p_5_count(self.get_input('p_5_count'))
    if self.has_input('p_5_count2') :
      p.set_p_5_count2(self.get_input('p_5_count2'))
    if self.has_input('p_5_stride') :
      p.set_p_5_stride(self.get_input('p_5_stride'))
    if self.has_input('p_5_stride2') :
      p.set_p_5_stride2(self.get_input('p_5_stride2'))
    Full_filename = ''
    if self.has_input('Full filename') :
      Full_filename = self.get_input('Full filename')
    Current_Index = 0
    if self.has_input('Current Index') :
      Current_Index = self.get_input('Current Index')
    results = p.execute(Full_filename, Current_Index)
    self.set_output('Output 0 Nrrd', results[0])
    self.set_output('Output 1 Nrrd', results[1])
    self.set_output('Output 2 Nrrd', results[2])
    self.set_output('Output 3 Nrrd', results[3])
    self.set_output('Output 4 Nrrd', results[4])
    self.set_output('Output 5 Nrrd', results[5])
    self.set_output('Output 6 Nrrd', results[6])
    self.set_output('Output 7 Nrrd', results[7])
    self.set_output('Selected Index', results[8])

class ReadField(DataIO) :
  def compute(self) :
    p = sr_py.ReadFieldAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class WriteColorMap(DataIO) :
  def compute(self) :
    p = sr_py.WriteColorMapAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    if self.has_input('p_exporttype') :
      p.set_p_exporttype(self.get_input('p_exporttype'))
    Input_Data = 0
    if self.has_input('Input Data') :
      Input_Data = self.get_input('Input Data')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Input_Data, Filename)

class ReadColorMap2D(DataIO) :
  def compute(self) :
    p = sr_py.ReadColorMap2DAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class ReadString(DataIO) :
  def compute(self) :
    p = sr_py.ReadStringAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class ReadColorMap(DataIO) :
  def compute(self) :
    p = sr_py.ReadColorMapAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class ReadMatrix(DataIO) :
  def compute(self) :
    p = sr_py.ReadMatrixAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class WriteString(DataIO) :
  def compute(self) :
    p = sr_py.WriteStringAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    String = ''
    if self.has_input('String') :
      String = self.get_input('String')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(String, Filename)

class ReadPath(DataIO) :
  def compute(self) :
    p = sr_py.ReadPathAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class WriteField(DataIO) :
  def compute(self) :
    p = sr_py.WriteFieldAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    if self.has_input('p_exporttype') :
      p.set_p_exporttype(self.get_input('p_exporttype'))
    if self.has_input('p_increment') :
      p.set_p_increment(self.get_input('p_increment'))
    if self.has_input('p_current') :
      p.set_p_current(self.get_input('p_current'))
    Input_Data = 0
    if self.has_input('Input Data') :
      Input_Data = self.get_input('Input Data')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Input_Data, Filename)

class ReadBundle(DataIO) :
  def compute(self) :
    p = sr_py.ReadBundleAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    if self.has_input('p_types') :
      p.set_p_types(self.get_input('p_types'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('bundle', results[0])
    self.set_output('Filename', results[1])

class StreamMatrixFromDisk(DataIO) :
  def compute(self) :
    p = sr_py.StreamMatrixFromDiskAlg()
    if self.has_input('p_row_or_col') :
      p.set_p_row_or_col(self.get_input('p_row_or_col'))
    if self.has_input('p_slider_min') :
      p.set_p_slider_min(self.get_input('p_slider_min'))
    if self.has_input('p_slider_max') :
      p.set_p_slider_max(self.get_input('p_slider_max'))
    if self.has_input('p_range_min') :
      p.set_p_range_min(self.get_input('p_range_min'))
    if self.has_input('p_range_max') :
      p.set_p_range_max(self.get_input('p_range_max'))
    if self.has_input('p_playmode') :
      p.set_p_playmode(self.get_input('p_playmode'))
    if self.has_input('p_current') :
      p.set_p_current(self.get_input('p_current'))
    if self.has_input('p_execmode') :
      p.set_p_execmode(self.get_input('p_execmode'))
    if self.has_input('p_delay') :
      p.set_p_delay(self.get_input('p_delay'))
    if self.has_input('p_inc_amount') :
      p.set_p_inc_amount(self.get_input('p_inc_amount'))
    if self.has_input('p_send_amount') :
      p.set_p_send_amount(self.get_input('p_send_amount'))
    Indices = 0
    if self.has_input('Indices') :
      Indices = self.get_input('Indices')
    Weights = 0
    if self.has_input('Weights') :
      Weights = self.get_input('Weights')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Indices, Weights, Filename)
    self.set_output('DataVector', results[0])
    self.set_output('Index', results[1])
    self.set_output('Scaled Index', results[2])
    self.set_output('Filename', results[3])

class WriteMatrix(DataIO) :
  def compute(self) :
    p = sr_py.WriteMatrixAlg()
    if self.has_input('p_filetype') :
      p.set_p_filetype(self.get_input('p_filetype'))
    if self.has_input('p_confirm') :
      p.set_p_confirm(self.get_input('p_confirm'))
    if self.has_input('p_confirm_once') :
      p.set_p_confirm_once(self.get_input('p_confirm_once'))
    if self.has_input('p_exporttype') :
      p.set_p_exporttype(self.get_input('p_exporttype'))
    if self.has_input('p_split') :
      p.set_p_split(self.get_input('p_split'))
    Input_Data = 0
    if self.has_input('Input Data') :
      Input_Data = self.get_input('Input Data')
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Input_Data, Filename)

class ReadNrrd(DataIO) :
  def compute(self) :
    p = sr_py.ReadNrrdAlg()
    if self.has_input('p_from_env') :
      p.set_p_from_env(self.get_input('p_from_env'))
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Output Data', results[0])
    self.set_output('Filename', results[1])

class JoinFields(NewField) :
  def compute(self) :
    p = sr_py.JoinFieldsAlg()
    if self.has_input('p_tolerance') :
      p.set_p_tolerance(self.get_input('p_tolerance'))
    if self.has_input('p_force_nodemerge') :
      p.set_p_force_nodemerge(self.get_input('p_force_nodemerge'))
    if self.has_input('p_force_pointcloud') :
      p.set_p_force_pointcloud(self.get_input('p_force_pointcloud'))
    if self.has_input('p_matchval') :
      p.set_p_matchval(self.get_input('p_matchval'))
    if self.has_input('p_meshonly') :
      p.set_p_meshonly(self.get_input('p_meshonly'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Output Field', results)

class RefineMeshByIsovalue(NewField) :
  def compute(self) :
    p = sr_py.RefineMeshByIsovalueAlg()
    if self.has_input('p_isoval') :
      p.set_p_isoval(self.get_input('p_isoval'))
    if self.has_input('p_lte') :
      p.set_p_lte(self.get_input('p_lte'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    Optional_Isovalue = 0
    if self.has_input('Optional Isovalue') :
      Optional_Isovalue = self.get_input('Optional Isovalue')
    results = p.execute(Input, Optional_Isovalue)
    self.set_output('Refined', results[0])
    self.set_output('Mapping', results[1])

class FairMesh(NewField) :
  def compute(self) :
    p = sr_py.FairMeshAlg()
    if self.has_input('p_iterations') :
      p.set_p_iterations(self.get_input('p_iterations'))
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    Input_Mesh = 0
    if self.has_input('Input Mesh') :
      Input_Mesh = self.get_input('Input Mesh')
    results = p.execute(Input_Mesh)
    self.set_output('Faired Mesh', results)

class CreateStructHex(NewField) :
  def compute(self) :
    p = sr_py.CreateStructHexAlg()
    if self.has_input('p_sizex') :
      p.set_p_sizex(self.get_input('p_sizex'))
    if self.has_input('p_sizey') :
      p.set_p_sizey(self.get_input('p_sizey'))
    if self.has_input('p_sizez') :
      p.set_p_sizez(self.get_input('p_sizez'))
    if self.has_input('p_padpercent') :
      p.set_p_padpercent(self.get_input('p_padpercent'))
    if self.has_input('p_data_at') :
      p.set_p_data_at(self.get_input('p_data_at'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Sample Field', results)

class ClipLatVolByIndicesOrWidget(NewField) :
  def compute(self) :
    p = sr_py.ClipLatVolByIndicesOrWidgetAlg()
    if self.has_input('p_use_text_bbox') :
      p.set_p_use_text_bbox(self.get_input('p_use_text_bbox'))
    if self.has_input('p_text_min_x') :
      p.set_p_text_min_x(self.get_input('p_text_min_x'))
    if self.has_input('p_text_min_y') :
      p.set_p_text_min_y(self.get_input('p_text_min_y'))
    if self.has_input('p_text_min_z') :
      p.set_p_text_min_z(self.get_input('p_text_min_z'))
    if self.has_input('p_text_max_x') :
      p.set_p_text_max_x(self.get_input('p_text_max_x'))
    if self.has_input('p_text_max_y') :
      p.set_p_text_max_y(self.get_input('p_text_max_y'))
    if self.has_input('p_text_max_z') :
      p.set_p_text_max_z(self.get_input('p_text_max_z'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Selection Widget', results[0])
    self.set_output('Output Field', results[1])
    self.set_output('MaskVector', results[2])

class GetFieldBoundary(NewField) :
  def compute(self) :
    p = sr_py.GetFieldBoundaryAlg()
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('BoundaryField', results[0])
    self.set_output('Mapping', results[1])

class ConvertMatricesToMesh(NewField) :
  def compute(self) :
    p = sr_py.ConvertMatricesToMeshAlg()
    if self.has_input('p_fieldname') :
      p.set_p_fieldname(self.get_input('p_fieldname'))
    if self.has_input('p_meshname') :
      p.set_p_meshname(self.get_input('p_meshname'))
    if self.has_input('p_fieldbasetype') :
      p.set_p_fieldbasetype(self.get_input('p_fieldbasetype'))
    if self.has_input('p_datatype') :
      p.set_p_datatype(self.get_input('p_datatype'))
    Mesh_Elements = 0
    if self.has_input('Mesh Elements') :
      Mesh_Elements = self.get_input('Mesh Elements')
    Mesh_Positions = 0
    if self.has_input('Mesh Positions') :
      Mesh_Positions = self.get_input('Mesh Positions')
    Mesh_Normals = 0
    if self.has_input('Mesh Normals') :
      Mesh_Normals = self.get_input('Mesh Normals')
    results = p.execute(Mesh_Elements, Mesh_Positions, Mesh_Normals)
    self.set_output('Output Field', results)

class ClipFieldToFieldOrWidget(NewField) :
  def compute(self) :
    p = sr_py.ClipFieldToFieldOrWidgetAlg()
    if self.has_input('p_clip_location') :
      p.set_p_clip_location(self.get_input('p_clip_location'))
    if self.has_input('p_clipmode') :
      p.set_p_clipmode(self.get_input('p_clipmode'))
    if self.has_input('p_autoexecute') :
      p.set_p_autoexecute(self.get_input('p_autoexecute'))
    if self.has_input('p_autoinvert') :
      p.set_p_autoinvert(self.get_input('p_autoinvert'))
    if self.has_input('p_execmode') :
      p.set_p_execmode(self.get_input('p_execmode'))
    if self.has_input('p_center_x') :
      p.set_p_center_x(self.get_input('p_center_x'))
    if self.has_input('p_center_y') :
      p.set_p_center_y(self.get_input('p_center_y'))
    if self.has_input('p_center_z') :
      p.set_p_center_z(self.get_input('p_center_z'))
    if self.has_input('p_right_x') :
      p.set_p_right_x(self.get_input('p_right_x'))
    if self.has_input('p_right_y') :
      p.set_p_right_y(self.get_input('p_right_y'))
    if self.has_input('p_right_z') :
      p.set_p_right_z(self.get_input('p_right_z'))
    if self.has_input('p_down_x') :
      p.set_p_down_x(self.get_input('p_down_x'))
    if self.has_input('p_down_y') :
      p.set_p_down_y(self.get_input('p_down_y'))
    if self.has_input('p_down_z') :
      p.set_p_down_z(self.get_input('p_down_z'))
    if self.has_input('p_in_x') :
      p.set_p_in_x(self.get_input('p_in_x'))
    if self.has_input('p_in_y') :
      p.set_p_in_y(self.get_input('p_in_y'))
    if self.has_input('p_in_z') :
      p.set_p_in_z(self.get_input('p_in_z'))
    if self.has_input('p_scale') :
      p.set_p_scale(self.get_input('p_scale'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Clip_Field = 0
    if self.has_input('Clip Field') :
      Clip_Field = self.get_input('Clip Field')
    results = p.execute(Input_Field, Clip_Field)
    self.set_output('Selection Widget', results[0])
    self.set_output('Output Field', results[1])

class RefineMeshByIsovalue2(NewField) :
  def compute(self) :
    p = sr_py.RefineMeshByIsovalue2Alg()
    if self.has_input('p_isoval') :
      p.set_p_isoval(self.get_input('p_isoval'))
    if self.has_input('p_lte') :
      p.set_p_lte(self.get_input('p_lte'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    Optional_Isovalue = 0
    if self.has_input('Optional Isovalue') :
      Optional_Isovalue = self.get_input('Optional Isovalue')
    results = p.execute(Input, Optional_Isovalue)
    self.set_output('Refined', results[0])
    self.set_output('Mapping', results[1])

class CreateLatVol(NewField) :
  def compute(self) :
    p = sr_py.CreateLatVolAlg()
    if self.has_input('p_sizex') :
      p.set_p_sizex(self.get_input('p_sizex'))
    if self.has_input('p_sizey') :
      p.set_p_sizey(self.get_input('p_sizey'))
    if self.has_input('p_sizez') :
      p.set_p_sizez(self.get_input('p_sizez'))
    if self.has_input('p_padpercent') :
      p.set_p_padpercent(self.get_input('p_padpercent'))
    if self.has_input('p_data_at') :
      p.set_p_data_at(self.get_input('p_data_at'))
    if self.has_input('p_element_size') :
      p.set_p_element_size(self.get_input('p_element_size'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    LatVol_Size = 0
    if self.has_input('LatVol Size') :
      LatVol_Size = self.get_input('LatVol Size')
    results = p.execute(Input_Field, LatVol_Size)
    self.set_output('Output Sample Field', results)

class InterfaceWithCamal(NewField) :
  def compute(self) :
    p = sr_py.InterfaceWithCamalAlg()
    TriSurf = 0
    if self.has_input('TriSurf') :
      TriSurf = self.get_input('TriSurf')
    results = p.execute(TriSurf)
    self.set_output('TetVol', results)

class ClipVolumeByIsovalue(NewField) :
  def compute(self) :
    p = sr_py.ClipVolumeByIsovalueAlg()
    if self.has_input('p_isoval_min') :
      p.set_p_isoval_min(self.get_input('p_isoval_min'))
    if self.has_input('p_isoval_max') :
      p.set_p_isoval_max(self.get_input('p_isoval_max'))
    if self.has_input('p_isoval') :
      p.set_p_isoval(self.get_input('p_isoval'))
    if self.has_input('p_lte') :
      p.set_p_lte(self.get_input('p_lte'))
    if self.has_input('p_update_type') :
      p.set_p_update_type(self.get_input('p_update_type'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    Optional_Isovalue = 0
    if self.has_input('Optional Isovalue') :
      Optional_Isovalue = self.get_input('Optional Isovalue')
    results = p.execute(Input, Optional_Isovalue)
    self.set_output('Clipped', results[0])
    self.set_output('Mapping', results[1])

class RefineMesh(NewField) :
  def compute(self) :
    p = sr_py.RefineMeshAlg()
    if self.has_input('p_select') :
      p.set_p_select(self.get_input('p_select'))
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    if self.has_input('p_isoval') :
      p.set_p_isoval(self.get_input('p_isoval'))
    Mesh = 0
    if self.has_input('Mesh') :
      Mesh = self.get_input('Mesh')
    Isovalue = 0
    if self.has_input('Isovalue') :
      Isovalue = self.get_input('Isovalue')
    results = p.execute(Mesh, Isovalue)
    self.set_output('RefinedMesh', results[0])
    self.set_output('Mapping', results[1])

class MergeFields(NewField) :
  def compute(self) :
    p = sr_py.MergeFieldsAlg()
    Container_Mesh = 0
    if self.has_input('Container Mesh') :
      Container_Mesh = self.get_input('Container Mesh')
    Insert_Field = 0
    if self.has_input('Insert Field') :
      Insert_Field = self.get_input('Insert Field')
    results = p.execute(Container_Mesh, Insert_Field)
    self.set_output('Combined Field', results[0])
    self.set_output('Extended Insert Field', results[1])
    self.set_output('Combined To Extended Mapping', results[2])

class GetCentroidsFromMesh(NewField) :
  def compute(self) :
    p = sr_py.GetCentroidsFromMeshAlg()
    TetVolField = 0
    if self.has_input('TetVolField') :
      TetVolField = self.get_input('TetVolField')
    results = p.execute(TetVolField)
    self.set_output('PointCloudField', results)

class ExtractIsosurfaceByFunction(NewField) :
  def compute(self) :
    p = sr_py.ExtractIsosurfaceByFunctionAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_zero_checks') :
      p.set_p_zero_checks(self.get_input('p_zero_checks'))
    if self.has_input('p_slice_value_min') :
      p.set_p_slice_value_min(self.get_input('p_slice_value_min'))
    if self.has_input('p_slice_value_max') :
      p.set_p_slice_value_max(self.get_input('p_slice_value_max'))
    if self.has_input('p_slice_value') :
      p.set_p_slice_value(self.get_input('p_slice_value'))
    if self.has_input('p_slice_value_typed') :
      p.set_p_slice_value_typed(self.get_input('p_slice_value_typed'))
    if self.has_input('p_slice_value_quantity') :
      p.set_p_slice_value_quantity(self.get_input('p_slice_value_quantity'))
    if self.has_input('p_quantity_range') :
      p.set_p_quantity_range(self.get_input('p_quantity_range'))
    if self.has_input('p_quantity_clusive') :
      p.set_p_quantity_clusive(self.get_input('p_quantity_clusive'))
    if self.has_input('p_quantity_min') :
      p.set_p_quantity_min(self.get_input('p_quantity_min'))
    if self.has_input('p_quantity_max') :
      p.set_p_quantity_max(self.get_input('p_quantity_max'))
    if self.has_input('p_quantity_list') :
      p.set_p_quantity_list(self.get_input('p_quantity_list'))
    if self.has_input('p_slice_value_list') :
      p.set_p_slice_value_list(self.get_input('p_slice_value_list'))
    if self.has_input('p_matrix_list') :
      p.set_p_matrix_list(self.get_input('p_matrix_list'))
    if self.has_input('p_algorithm') :
      p.set_p_algorithm(self.get_input('p_algorithm'))
    if self.has_input('p_active_slice_value_selection_tab') :
      p.set_p_active_slice_value_selection_tab(self.get_input('p_active_slice_value_selection_tab'))
    if self.has_input('p_active_tab') :
      p.set_p_active_tab(self.get_input('p_active_tab'))
    if self.has_input('p_update_type') :
      p.set_p_update_type(self.get_input('p_update_type'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Optional_Slice_values = 0
    if self.has_input('Optional Slice values') :
      Optional_Slice_values = self.get_input('Optional Slice values')
    results = p.execute(Input_Field, Optional_Slice_values)
    self.set_output('Output Field', results)

class MergeTriSurfs(NewField) :
  def compute(self) :
    p = sr_py.MergeTriSurfsAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class InterfaceWithTetGen(NewField) :
  def compute(self) :
    p = sr_py.InterfaceWithTetGenAlg()
    if self.has_input('p_switch') :
      p.set_p_switch(self.get_input('p_switch'))
    Main = 0
    if self.has_input('Main') :
      Main = self.get_input('Main')
    Points = 0
    if self.has_input('Points') :
      Points = self.get_input('Points')
    Region_Attribs = 0
    if self.has_input('Region Attribs') :
      Region_Attribs = self.get_input('Region Attribs')
    Regions = 0
    if self.has_input('Regions') :
      Regions = self.get_input('Regions')
    results = p.execute(Main, Points, Region_Attribs, Regions)
    self.set_output('TetVol', results)

class CreateImage(NewField) :
  def compute(self) :
    p = sr_py.CreateImageAlg()
    if self.has_input('p_sizex') :
      p.set_p_sizex(self.get_input('p_sizex'))
    if self.has_input('p_sizey') :
      p.set_p_sizey(self.get_input('p_sizey'))
    if self.has_input('p_sizez') :
      p.set_p_sizez(self.get_input('p_sizez'))
    if self.has_input('p_z_value') :
      p.set_p_z_value(self.get_input('p_z_value'))
    if self.has_input('p_auto_size') :
      p.set_p_auto_size(self.get_input('p_auto_size'))
    if self.has_input('p_axis') :
      p.set_p_axis(self.get_input('p_axis'))
    if self.has_input('p_padpercent') :
      p.set_p_padpercent(self.get_input('p_padpercent'))
    if self.has_input('p_pos') :
      p.set_p_pos(self.get_input('p_pos'))
    if self.has_input('p_data_at') :
      p.set_p_data_at(self.get_input('p_data_at'))
    if self.has_input('p_update_type') :
      p.set_p_update_type(self.get_input('p_update_type'))
    if self.has_input('p_corigin_x') :
      p.set_p_corigin_x(self.get_input('p_corigin_x'))
    if self.has_input('p_corigin_y') :
      p.set_p_corigin_y(self.get_input('p_corigin_y'))
    if self.has_input('p_corigin_z') :
      p.set_p_corigin_z(self.get_input('p_corigin_z'))
    if self.has_input('p_cnormal_x') :
      p.set_p_cnormal_x(self.get_input('p_cnormal_x'))
    if self.has_input('p_cnormal_y') :
      p.set_p_cnormal_y(self.get_input('p_cnormal_y'))
    if self.has_input('p_cnormal_z') :
      p.set_p_cnormal_z(self.get_input('p_cnormal_z'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Sample Field', results)

class InsertHexVolSheetAlongSurface(NewField) :
  def compute(self) :
    p = sr_py.InsertHexVolSheetAlongSurfaceAlg()
    if self.has_input('p_side') :
      p.set_p_side(self.get_input('p_side'))
    if self.has_input('p_addlayer') :
      p.set_p_addlayer(self.get_input('p_addlayer'))
    HexField = 0
    if self.has_input('HexField') :
      HexField = self.get_input('HexField')
    TriField = 0
    if self.has_input('TriField') :
      TriField = self.get_input('TriField')
    results = p.execute(HexField, TriField)
    self.set_output('Side1Field', results[0])
    self.set_output('Side2Field', results[1])

class GenerateSinglePointProbeFromField(NewField) :
  def compute(self) :
    p = sr_py.GenerateSinglePointProbeFromFieldAlg()
    if self.has_input('p_main_frame') :
      p.set_p_main_frame(self.get_input('p_main_frame'))
    if self.has_input('p_locx') :
      p.set_p_locx(self.get_input('p_locx'))
    if self.has_input('p_locy') :
      p.set_p_locy(self.get_input('p_locy'))
    if self.has_input('p_locz') :
      p.set_p_locz(self.get_input('p_locz'))
    if self.has_input('p_value') :
      p.set_p_value(self.get_input('p_value'))
    if self.has_input('p_node') :
      p.set_p_node(self.get_input('p_node'))
    if self.has_input('p_edge') :
      p.set_p_edge(self.get_input('p_edge'))
    if self.has_input('p_face') :
      p.set_p_face(self.get_input('p_face'))
    if self.has_input('p_cell') :
      p.set_p_cell(self.get_input('p_cell'))
    if self.has_input('p_show_value') :
      p.set_p_show_value(self.get_input('p_show_value'))
    if self.has_input('p_show_node') :
      p.set_p_show_node(self.get_input('p_show_node'))
    if self.has_input('p_show_edge') :
      p.set_p_show_edge(self.get_input('p_show_edge'))
    if self.has_input('p_show_face') :
      p.set_p_show_face(self.get_input('p_show_face'))
    if self.has_input('p_show_cell') :
      p.set_p_show_cell(self.get_input('p_show_cell'))
    if self.has_input('p_probe_scale') :
      p.set_p_probe_scale(self.get_input('p_probe_scale'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('GenerateSinglePointProbeFromField Widget', results[0])
    self.set_output('GenerateSinglePointProbeFromField Point', results[1])
    self.set_output('Element Index', results[2])

class InterfaceWithCubit(NewField) :
  def compute(self) :
    p = sr_py.InterfaceWithCubitAlg()
    if self.has_input('p_cubitdir') :
      p.set_p_cubitdir(self.get_input('p_cubitdir'))
    if self.has_input('p_ncdump') :
      p.set_p_ncdump(self.get_input('p_ncdump'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    PointCloudField = 0
    if self.has_input('PointCloudField') :
      PointCloudField = self.get_input('PointCloudField')
    results = p.execute(Field, PointCloudField)
    self.set_output('Field', results)

class ClipFieldByFunction(NewField) :
  def compute(self) :
    p = sr_py.ClipFieldByFunctionAlg()
    if self.has_input('p_mode') :
      p.set_p_mode(self.get_input('p_mode'))
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Function, Input)
    self.set_output('Clipped', results[0])
    self.set_output('Mapping', results[1])
    self.set_output('MaskVector', results[2])

class GetDomainBoundary(NewField) :
  def compute(self) :
    p = sr_py.GetDomainBoundaryAlg()
    if self.has_input('p_userange') :
      p.set_p_userange(self.get_input('p_userange'))
    if self.has_input('p_minrange') :
      p.set_p_minrange(self.get_input('p_minrange'))
    if self.has_input('p_maxrange') :
      p.set_p_maxrange(self.get_input('p_maxrange'))
    if self.has_input('p_usevalue') :
      p.set_p_usevalue(self.get_input('p_usevalue'))
    if self.has_input('p_value') :
      p.set_p_value(self.get_input('p_value'))
    if self.has_input('p_includeouterboundary') :
      p.set_p_includeouterboundary(self.get_input('p_includeouterboundary'))
    if self.has_input('p_innerboundaryonly') :
      p.set_p_innerboundaryonly(self.get_input('p_innerboundaryonly'))
    if self.has_input('p_noinnerboundary') :
      p.set_p_noinnerboundary(self.get_input('p_noinnerboundary'))
    if self.has_input('p_disconnect') :
      p.set_p_disconnect(self.get_input('p_disconnect'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    MinValueValue = 0
    if self.has_input('MinValueValue') :
      MinValueValue = self.get_input('MinValueValue')
    MaxValue = 0
    if self.has_input('MaxValue') :
      MaxValue = self.get_input('MaxValue')
    results = p.execute(Field, MinValueValue, MaxValue)
    self.set_output('Field', results)

class CollectFields(NewField) :
  def compute(self) :
    p = sr_py.CollectFieldsAlg()
    if self.has_input('p_buffersize') :
      p.set_p_buffersize(self.get_input('p_buffersize'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    BufferSize = 0
    if self.has_input('BufferSize') :
      BufferSize = self.get_input('BufferSize')
    results = p.execute(Field, BufferSize)
    self.set_output('Fields', results)

class GeneratePointSamplesFromField(NewField) :
  def compute(self) :
    p = sr_py.GeneratePointSamplesFromFieldAlg()
    if self.has_input('p_num_seeds') :
      p.set_p_num_seeds(self.get_input('p_num_seeds'))
    if self.has_input('p_probe_scale') :
      p.set_p_probe_scale(self.get_input('p_probe_scale'))
    if self.has_input('p_send') :
      p.set_p_send(self.get_input('p_send'))
    if self.has_input('p_widget') :
      p.set_p_widget(self.get_input('p_widget'))
    if self.has_input('p_red') :
      p.set_p_red(self.get_input('p_red'))
    if self.has_input('p_green') :
      p.set_p_green(self.get_input('p_green'))
    if self.has_input('p_blue') :
      p.set_p_blue(self.get_input('p_blue'))
    if self.has_input('p_auto_execute') :
      p.set_p_auto_execute(self.get_input('p_auto_execute'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('GeneratePointSamplesFromField Widget', results[0])
    self.set_output('GeneratePointSamplesFromField Point', results[1])

class GeneratePointSamplesFromFieldOrWidget(NewField) :
  def compute(self) :
    p = sr_py.GeneratePointSamplesFromFieldOrWidgetAlg()
    if self.has_input('p_wtype') :
      p.set_p_wtype(self.get_input('p_wtype'))
    if self.has_input('p_endpoints') :
      p.set_p_endpoints(self.get_input('p_endpoints'))
    if self.has_input('p_maxseeds') :
      p.set_p_maxseeds(self.get_input('p_maxseeds'))
    if self.has_input('p_numseeds') :
      p.set_p_numseeds(self.get_input('p_numseeds'))
    if self.has_input('p_rngseed') :
      p.set_p_rngseed(self.get_input('p_rngseed'))
    if self.has_input('p_rnginc') :
      p.set_p_rnginc(self.get_input('p_rnginc'))
    if self.has_input('p_clamp') :
      p.set_p_clamp(self.get_input('p_clamp'))
    if self.has_input('p_autoexecute') :
      p.set_p_autoexecute(self.get_input('p_autoexecute'))
    if self.has_input('p_dist') :
      p.set_p_dist(self.get_input('p_dist'))
    if self.has_input('p_whichtab') :
      p.set_p_whichtab(self.get_input('p_whichtab'))
    Field_to_Sample = 0
    if self.has_input('Field to Sample') :
      Field_to_Sample = self.get_input('Field to Sample')
    results = p.execute(Field_to_Sample)
    self.set_output('Samples', results[0])
    self.set_output('Sampling Widget', results[1])

class DecimateTriSurf(NewField) :
  def compute(self) :
    p = sr_py.DecimateTriSurfAlg()
    TriSurf = 0
    if self.has_input('TriSurf') :
      TriSurf = self.get_input('TriSurf')
    results = p.execute(TriSurf)
    self.set_output('Decimated', results)

class GetSliceFromStructuredFieldByIndices(NewField) :
  def compute(self) :
    p = sr_py.GetSliceFromStructuredFieldByIndicesAlg()
    if self.has_input('p_axis') :
      p.set_p_axis(self.get_input('p_axis'))
    if self.has_input('p_dims') :
      p.set_p_dims(self.get_input('p_dims'))
    if self.has_input('p_dim_i') :
      p.set_p_dim_i(self.get_input('p_dim_i'))
    if self.has_input('p_dim_j') :
      p.set_p_dim_j(self.get_input('p_dim_j'))
    if self.has_input('p_dim_k') :
      p.set_p_dim_k(self.get_input('p_dim_k'))
    if self.has_input('p_index_i') :
      p.set_p_index_i(self.get_input('p_index_i'))
    if self.has_input('p_index_j') :
      p.set_p_index_j(self.get_input('p_index_j'))
    if self.has_input('p_index_k') :
      p.set_p_index_k(self.get_input('p_index_k'))
    if self.has_input('p_update_type') :
      p.set_p_update_type(self.get_input('p_update_type'))
    if self.has_input('p_continuous') :
      p.set_p_continuous(self.get_input('p_continuous'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Input_Matrix = 0
    if self.has_input('Input Matrix') :
      Input_Matrix = self.get_input('Input Matrix')
    results = p.execute(Input_Field, Input_Matrix)
    self.set_output('Output Field', results[0])
    self.set_output('Output Matrix', results[1])

class RemoveHexVolSheet(NewField) :
  def compute(self) :
    p = sr_py.RemoveHexVolSheetAlg()
    if self.has_input('p_edge_list') :
      p.set_p_edge_list(self.get_input('p_edge_list'))
    HexField = 0
    if self.has_input('HexField') :
      HexField = self.get_input('HexField')
    results = p.execute(HexField)
    self.set_output('NewHexField', results[0])
    self.set_output('ExtractedHexes', results[1])

class SubsampleStructuredFieldByIndices(NewField) :
  def compute(self) :
    p = sr_py.SubsampleStructuredFieldByIndicesAlg()
    if self.has_input('p_power_app') :
      p.set_p_power_app(self.get_input('p_power_app'))
    if self.has_input('p_wrap') :
      p.set_p_wrap(self.get_input('p_wrap'))
    if self.has_input('p_dims') :
      p.set_p_dims(self.get_input('p_dims'))
    if self.has_input('p_dim_i') :
      p.set_p_dim_i(self.get_input('p_dim_i'))
    if self.has_input('p_dim_j') :
      p.set_p_dim_j(self.get_input('p_dim_j'))
    if self.has_input('p_dim_k') :
      p.set_p_dim_k(self.get_input('p_dim_k'))
    if self.has_input('p_start_i') :
      p.set_p_start_i(self.get_input('p_start_i'))
    if self.has_input('p_start_j') :
      p.set_p_start_j(self.get_input('p_start_j'))
    if self.has_input('p_start_k') :
      p.set_p_start_k(self.get_input('p_start_k'))
    if self.has_input('p_stop_i') :
      p.set_p_stop_i(self.get_input('p_stop_i'))
    if self.has_input('p_stop_j') :
      p.set_p_stop_j(self.get_input('p_stop_j'))
    if self.has_input('p_stop_k') :
      p.set_p_stop_k(self.get_input('p_stop_k'))
    if self.has_input('p_stride_i') :
      p.set_p_stride_i(self.get_input('p_stride_i'))
    if self.has_input('p_stride_j') :
      p.set_p_stride_j(self.get_input('p_stride_j'))
    if self.has_input('p_stride_k') :
      p.set_p_stride_k(self.get_input('p_stride_k'))
    if self.has_input('p_wrap_i') :
      p.set_p_wrap_i(self.get_input('p_wrap_i'))
    if self.has_input('p_wrap_j') :
      p.set_p_wrap_j(self.get_input('p_wrap_j'))
    if self.has_input('p_wrap_k') :
      p.set_p_wrap_k(self.get_input('p_wrap_k'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Input_Matrix = 0
    if self.has_input('Input Matrix') :
      Input_Matrix = self.get_input('Input Matrix')
    results = p.execute(Input_Field, Input_Matrix)
    self.set_output('Output Field', results[0])
    self.set_output('Output Matrix', results[1])

class GetAllSegmentationBoundaries(NewField) :
  def compute(self) :
    p = sr_py.GetAllSegmentationBoundariesAlg()
    Segmentations = 0
    if self.has_input('Segmentations') :
      Segmentations = self.get_input('Segmentations')
    results = p.execute(Segmentations)
    self.set_output('Boundaries', results)

class ClipFieldWithSeed(NewField) :
  def compute(self) :
    p = sr_py.ClipFieldWithSeedAlg()
    if self.has_input('p_mode') :
      p.set_p_mode(self.get_input('p_mode'))
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    Seeds = 0
    if self.has_input('Seeds') :
      Seeds = self.get_input('Seeds')
    results = p.execute(Function, Input, Seeds)
    self.set_output('Clipped', results[0])
    self.set_output('Mapping', results[1])
    self.set_output('MaskVector', results[2])

class SplitNodesByDomain(NewField) :
  def compute(self) :
    p = sr_py.SplitNodesByDomainAlg()
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('SplitField', results)

class ApplyMappingMatrix(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ApplyMappingMatrixAlg()
    Source = 0
    if self.has_input('Source') :
      Source = self.get_input('Source')
    Destination = 0
    if self.has_input('Destination') :
      Destination = self.get_input('Destination')
    Mapping = 0
    if self.has_input('Mapping') :
      Mapping = self.get_input('Mapping')
    results = p.execute(Source, Destination, Mapping)
    self.set_output('Output', results)

class MaskLatVolWithTriSurf(ChangeFieldData) :
  def compute(self) :
    p = sr_py.MaskLatVolWithTriSurfAlg()
    LatVolField = 0
    if self.has_input('LatVolField') :
      LatVolField = self.get_input('LatVolField')
    TriSurfField = 0
    if self.has_input('TriSurfField') :
      TriSurfField = self.get_input('TriSurfField')
    results = p.execute(LatVolField, TriSurfField)
    self.set_output('LatVol Mask', results)

class ConvertFieldBasis(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ConvertFieldBasisAlg()
    if self.has_input('p_output_basis') :
      p.set_p_output_basis(self.get_input('p_output_basis'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('Output', results[0])
    self.set_output('Mapping', results[1])

class ReportMeshQualityMeasures(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ReportMeshQualityMeasuresAlg()
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('Checked', results)

class SelectAndSetFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.SelectAndSetFieldDataAlg()
    if self.has_input('p_selection1') :
      p.set_p_selection1(self.get_input('p_selection1'))
    if self.has_input('p_function1') :
      p.set_p_function1(self.get_input('p_function1'))
    if self.has_input('p_selection2') :
      p.set_p_selection2(self.get_input('p_selection2'))
    if self.has_input('p_function2') :
      p.set_p_function2(self.get_input('p_function2'))
    if self.has_input('p_selection3') :
      p.set_p_selection3(self.get_input('p_selection3'))
    if self.has_input('p_function3') :
      p.set_p_function3(self.get_input('p_function3'))
    if self.has_input('p_selection4') :
      p.set_p_selection4(self.get_input('p_selection4'))
    if self.has_input('p_function4') :
      p.set_p_function4(self.get_input('p_function4'))
    if self.has_input('p_functiondef') :
      p.set_p_functiondef(self.get_input('p_functiondef'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Field, Array)
    self.set_output('Field', results)

class CalculateFieldData3(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateFieldData3Alg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    Field1 = 0
    if self.has_input('Field1') :
      Field1 = self.get_input('Field1')
    Field2 = 0
    if self.has_input('Field2') :
      Field2 = self.get_input('Field2')
    Field3 = 0
    if self.has_input('Field3') :
      Field3 = self.get_input('Field3')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Field1, Field2, Field3, Function, Array)
    self.set_output('Field', results)

class SetFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.SetFieldDataAlg()
    if self.has_input('p_keepscalartype') :
      p.set_p_keepscalartype(self.get_input('p_keepscalartype'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Matrix_Data = 0
    if self.has_input('Matrix Data') :
      Matrix_Data = self.get_input('Matrix Data')
    Nrrd_Data = 0
    if self.has_input('Nrrd Data') :
      Nrrd_Data = self.get_input('Nrrd Data')
    results = p.execute(Field, Matrix_Data, Nrrd_Data)
    self.set_output('Field', results)

class SwapFieldDataWithMatrixEntries(ChangeFieldData) :
  def compute(self) :
    p = sr_py.SwapFieldDataWithMatrixEntriesAlg()
    if self.has_input('p_preserve_scalar_type') :
      p.set_p_preserve_scalar_type(self.get_input('p_preserve_scalar_type'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Input_Matrix = 0
    if self.has_input('Input Matrix') :
      Input_Matrix = self.get_input('Input Matrix')
    results = p.execute(Input_Field, Input_Matrix)
    self.set_output('Output Field', results[0])
    self.set_output('Output Matrix', results[1])

class ConvertLatVolDataFromElemToNode(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ConvertLatVolDataFromElemToNodeAlg()
    Elem_Field = 0
    if self.has_input('Elem Field') :
      Elem_Field = self.get_input('Elem Field')
    results = p.execute(Elem_Field)
    self.set_output('Node Field', results)

class CalculateNodeNormals(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateNodeNormalsAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Input_Point = 0
    if self.has_input('Input Point') :
      Input_Point = self.get_input('Input Point')
    results = p.execute(Input_Field, Input_Point)
    self.set_output('Output Field', results)

class CalculateVectorMagnitudes(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateVectorMagnitudesAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output CalculateVectorMagnitudes', results)

class ConvertIndicesToFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ConvertIndicesToFieldDataAlg()
    if self.has_input('p_outputtype') :
      p.set_p_outputtype(self.get_input('p_outputtype'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Data = 0
    if self.has_input('Data') :
      Data = self.get_input('Data')
    results = p.execute(Field, Data)
    self.set_output('Field', results)

class CalculateDistanceToFieldBoundary(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateDistanceToFieldBoundaryAlg()
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('DistanceField', results)

class MapFieldDataFromSourceToDestination(ChangeFieldData) :
  def compute(self) :
    p = sr_py.MapFieldDataFromSourceToDestinationAlg()
    if self.has_input('p_interpolation_basis') :
      p.set_p_interpolation_basis(self.get_input('p_interpolation_basis'))
    if self.has_input('p_map_source_to_single_dest') :
      p.set_p_map_source_to_single_dest(self.get_input('p_map_source_to_single_dest'))
    if self.has_input('p_exhaustive_search') :
      p.set_p_exhaustive_search(self.get_input('p_exhaustive_search'))
    if self.has_input('p_exhaustive_search_max_dist') :
      p.set_p_exhaustive_search_max_dist(self.get_input('p_exhaustive_search_max_dist'))
    if self.has_input('p_np') :
      p.set_p_np(self.get_input('p_np'))
    Source = 0
    if self.has_input('Source') :
      Source = self.get_input('Source')
    Destination = 0
    if self.has_input('Destination') :
      Destination = self.get_input('Destination')
    results = p.execute(Source, Destination)
    self.set_output('Remapped Destination', results)

class SelectAndSetFieldData3(ChangeFieldData) :
  def compute(self) :
    p = sr_py.SelectAndSetFieldData3Alg()
    if self.has_input('p_selection1') :
      p.set_p_selection1(self.get_input('p_selection1'))
    if self.has_input('p_function1') :
      p.set_p_function1(self.get_input('p_function1'))
    if self.has_input('p_selection2') :
      p.set_p_selection2(self.get_input('p_selection2'))
    if self.has_input('p_function2') :
      p.set_p_function2(self.get_input('p_function2'))
    if self.has_input('p_selection3') :
      p.set_p_selection3(self.get_input('p_selection3'))
    if self.has_input('p_function3') :
      p.set_p_function3(self.get_input('p_function3'))
    if self.has_input('p_selection4') :
      p.set_p_selection4(self.get_input('p_selection4'))
    if self.has_input('p_function4') :
      p.set_p_function4(self.get_input('p_function4'))
    if self.has_input('p_functiondef') :
      p.set_p_functiondef(self.get_input('p_functiondef'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    Field1 = 0
    if self.has_input('Field1') :
      Field1 = self.get_input('Field1')
    Field2 = 0
    if self.has_input('Field2') :
      Field2 = self.get_input('Field2')
    Field3 = 0
    if self.has_input('Field3') :
      Field3 = self.get_input('Field3')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Field1, Field2, Field3, Array)
    self.set_output('Field', results)

class CreateFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CreateFieldDataAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    if self.has_input('p_basis') :
      p.set_p_basis(self.get_input('p_basis'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    DataArray = 0
    if self.has_input('DataArray') :
      DataArray = self.get_input('DataArray')
    results = p.execute(Field, Function, DataArray)
    self.set_output('Field', results)

class ConvertLatVolDataFromNodeToElem(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ConvertLatVolDataFromNodeToElemAlg()
    Node_Field = 0
    if self.has_input('Node Field') :
      Node_Field = self.get_input('Node Field')
    results = p.execute(Node_Field)
    self.set_output('Elem Field', results)

class CalculateFieldDataCompiled(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateFieldDataCompiledAlg()
    if self.has_input('p_outputdatatype') :
      p.set_p_outputdatatype(self.get_input('p_outputdatatype'))
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_cache') :
      p.set_p_cache(self.get_input('p_cache'))
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Function, Input_Field)
    self.set_output('Output Field', results)

class MapFieldDataFromElemToNode(ChangeFieldData) :
  def compute(self) :
    p = sr_py.MapFieldDataFromElemToNodeAlg()
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Field', results)

class ApplyFilterToFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ApplyFilterToFieldDataAlg()
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    if self.has_input('p_ed_method') :
      p.set_p_ed_method(self.get_input('p_ed_method'))
    if self.has_input('p_ed_iterations') :
      p.set_p_ed_iterations(self.get_input('p_ed_iterations'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Field', results)

class GetFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.GetFieldDataAlg()
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Data', results)

class CalculateFieldData2(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateFieldData2Alg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    Field1 = 0
    if self.has_input('Field1') :
      Field1 = self.get_input('Field1')
    Field2 = 0
    if self.has_input('Field2') :
      Field2 = self.get_input('Field2')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Field1, Field2, Function, Array)
    self.set_output('Field', results)

class CalculateLatVolGradientsAtNodes(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateLatVolGradientsAtNodesAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Gradient', results)

class CalculateGradients(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateGradientsAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output CalculateGradients', results)

class CalculateSignedDistanceToField(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateSignedDistanceToFieldAlg()
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    ObjectField = 0
    if self.has_input('ObjectField') :
      ObjectField = self.get_input('ObjectField')
    results = p.execute(Field, ObjectField)
    self.set_output('SignedDistanceField', results)

class CalculateInsideWhichField(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateInsideWhichFieldAlg()
    if self.has_input('p_outputbasis') :
      p.set_p_outputbasis(self.get_input('p_outputbasis'))
    if self.has_input('p_outputtype') :
      p.set_p_outputtype(self.get_input('p_outputtype'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Object = 0
    if self.has_input('Object') :
      Object = self.get_input('Object')
    results = p.execute(Field, Object)
    self.set_output('Field', results)

class MapFieldDataFromNodeToElem(ChangeFieldData) :
  def compute(self) :
    p = sr_py.MapFieldDataFromNodeToElemAlg()
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Field', results)

class ConvertFieldDataType(ChangeFieldData) :
  def compute(self) :
    p = sr_py.ConvertFieldDataTypeAlg()
    if self.has_input('p_outputdatatype') :
      p.set_p_outputdatatype(self.get_input('p_outputdatatype'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class CalculateIsInsideField(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateIsInsideFieldAlg()
    if self.has_input('p_outputtype') :
      p.set_p_outputtype(self.get_input('p_outputtype'))
    if self.has_input('p_outval') :
      p.set_p_outval(self.get_input('p_outval'))
    if self.has_input('p_inval') :
      p.set_p_inval(self.get_input('p_inval'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    ObjectField = 0
    if self.has_input('ObjectField') :
      ObjectField = self.get_input('ObjectField')
    results = p.execute(Field, ObjectField)
    self.set_output('Field', results)

class CalculateFieldData(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateFieldDataAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Field, Function, Array)
    self.set_output('Field', results)

class CalculateDistanceToField(ChangeFieldData) :
  def compute(self) :
    p = sr_py.CalculateDistanceToFieldAlg()
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    ObjectField = 0
    if self.has_input('ObjectField') :
      ObjectField = self.get_input('ObjectField')
    results = p.execute(Field, ObjectField)
    self.set_output('DistanceField', results)

class TransformPlanarMesh(ChangeMesh) :
  def compute(self) :
    p = sr_py.TransformPlanarMeshAlg()
    if self.has_input('p_axis') :
      p.set_p_axis(self.get_input('p_axis'))
    if self.has_input('p_invert') :
      p.set_p_invert(self.get_input('p_invert'))
    if self.has_input('p_trans_x') :
      p.set_p_trans_x(self.get_input('p_trans_x'))
    if self.has_input('p_trans_y') :
      p.set_p_trans_y(self.get_input('p_trans_y'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Index_Matrix = 0
    if self.has_input('Index Matrix') :
      Index_Matrix = self.get_input('Index Matrix')
    results = p.execute(Input_Field, Index_Matrix)
    self.set_output('Transformed Field', results)

class ConvertMeshToUnstructuredMesh(ChangeMesh) :
  def compute(self) :
    p = sr_py.ConvertMeshToUnstructuredMeshAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class ConvertQuadSurfToTriSurf(ChangeMesh) :
  def compute(self) :
    p = sr_py.ConvertQuadSurfToTriSurfAlg()
    QuadSurf = 0
    if self.has_input('QuadSurf') :
      QuadSurf = self.get_input('QuadSurf')
    results = p.execute(QuadSurf)
    self.set_output('TriSurf', results)

class TransformMeshWithFunction(ChangeMesh) :
  def compute(self) :
    p = sr_py.TransformMeshWithFunctionAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class ConvertHexVolToTetVol(ChangeMesh) :
  def compute(self) :
    p = sr_py.ConvertHexVolToTetVolAlg()
    HexVol = 0
    if self.has_input('HexVol') :
      HexVol = self.get_input('HexVol')
    results = p.execute(HexVol)
    self.set_output('TetVol', results)

class ConvertMeshCoordinateSystem(ChangeMesh) :
  def compute(self) :
    p = sr_py.ConvertMeshCoordinateSystemAlg()
    if self.has_input('p_oldsystem') :
      p.set_p_oldsystem(self.get_input('p_oldsystem'))
    if self.has_input('p_newsystem') :
      p.set_p_newsystem(self.get_input('p_newsystem'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class ConvertMeshToPointCloud(ChangeMesh) :
  def compute(self) :
    p = sr_py.ConvertMeshToPointCloudAlg()
    if self.has_input('p_datalocation') :
      p.set_p_datalocation(self.get_input('p_datalocation'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Field', results)

class TransformMeshWithTransform(ChangeMesh) :
  def compute(self) :
    p = sr_py.TransformMeshWithTransformAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Transform_Matrix = 0
    if self.has_input('Transform Matrix') :
      Transform_Matrix = self.get_input('Transform Matrix')
    results = p.execute(Input_Field, Transform_Matrix)
    self.set_output('Transformed Field', results)

class ConvertRegularMeshToStructuredMesh(ChangeMesh) :
  def compute(self) :
    p = sr_py.ConvertRegularMeshToStructuredMeshAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class CalculateMeshNodes(ChangeMesh) :
  def compute(self) :
    p = sr_py.CalculateMeshNodesAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Field, Function, Array)
    self.set_output('Field', results)

class SmoothMesh(ChangeMesh) :
  def compute(self) :
    p = sr_py.SmoothMeshAlg()
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    IsoValue = 0
    if self.has_input('IsoValue') :
      IsoValue = self.get_input('IsoValue')
    results = p.execute(Input, IsoValue)
    self.set_output('Smoothed', results)

class EditMeshBoundingBox(ChangeMesh) :
  def compute(self) :
    p = sr_py.EditMeshBoundingBoxAlg()
    if self.has_input('p_outputcenterx') :
      p.set_p_outputcenterx(self.get_input('p_outputcenterx'))
    if self.has_input('p_outputcentery') :
      p.set_p_outputcentery(self.get_input('p_outputcentery'))
    if self.has_input('p_outputcenterz') :
      p.set_p_outputcenterz(self.get_input('p_outputcenterz'))
    if self.has_input('p_outputsizex') :
      p.set_p_outputsizex(self.get_input('p_outputsizex'))
    if self.has_input('p_outputsizey') :
      p.set_p_outputsizey(self.get_input('p_outputsizey'))
    if self.has_input('p_outputsizez') :
      p.set_p_outputsizez(self.get_input('p_outputsizez'))
    if self.has_input('p_useoutputcenter') :
      p.set_p_useoutputcenter(self.get_input('p_useoutputcenter'))
    if self.has_input('p_useoutputsize') :
      p.set_p_useoutputsize(self.get_input('p_useoutputsize'))
    if self.has_input('p_box_scale') :
      p.set_p_box_scale(self.get_input('p_box_scale'))
    if self.has_input('p_box_mode') :
      p.set_p_box_mode(self.get_input('p_box_mode'))
    if self.has_input('p_box_real_scale') :
      p.set_p_box_real_scale(self.get_input('p_box_real_scale'))
    if self.has_input('p_box_center_x') :
      p.set_p_box_center_x(self.get_input('p_box_center_x'))
    if self.has_input('p_box_center_y') :
      p.set_p_box_center_y(self.get_input('p_box_center_y'))
    if self.has_input('p_box_center_z') :
      p.set_p_box_center_z(self.get_input('p_box_center_z'))
    if self.has_input('p_box_right_x') :
      p.set_p_box_right_x(self.get_input('p_box_right_x'))
    if self.has_input('p_box_right_y') :
      p.set_p_box_right_y(self.get_input('p_box_right_y'))
    if self.has_input('p_box_right_z') :
      p.set_p_box_right_z(self.get_input('p_box_right_z'))
    if self.has_input('p_box_down_x') :
      p.set_p_box_down_x(self.get_input('p_box_down_x'))
    if self.has_input('p_box_down_y') :
      p.set_p_box_down_y(self.get_input('p_box_down_y'))
    if self.has_input('p_box_down_z') :
      p.set_p_box_down_z(self.get_input('p_box_down_z'))
    if self.has_input('p_box_in_x') :
      p.set_p_box_in_x(self.get_input('p_box_in_x'))
    if self.has_input('p_box_in_y') :
      p.set_p_box_in_y(self.get_input('p_box_in_y'))
    if self.has_input('p_box_in_z') :
      p.set_p_box_in_z(self.get_input('p_box_in_z'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results[0])
    self.set_output('Transformation Widget', results[1])
    self.set_output('Transformation Matrix', results[2])

class SwapNodeLocationsWithMatrixEntries(ChangeMesh) :
  def compute(self) :
    p = sr_py.SwapNodeLocationsWithMatrixEntriesAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    Input_Matrix = 0
    if self.has_input('Input Matrix') :
      Input_Matrix = self.get_input('Input Matrix')
    results = p.execute(Input_Field, Input_Matrix)
    self.set_output('Output Field', results[0])
    self.set_output('Output Matrix', results[1])

class MapFieldDataToNodeCoordinate(ChangeMesh) :
  def compute(self) :
    p = sr_py.MapFieldDataToNodeCoordinateAlg()
    if self.has_input('p_coord') :
      p.set_p_coord(self.get_input('p_coord'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Field', results)

class ScaleFieldMeshAndData(ChangeMesh) :
  def compute(self) :
    p = sr_py.ScaleFieldMeshAndDataAlg()
    if self.has_input('p_datascale') :
      p.set_p_datascale(self.get_input('p_datascale'))
    if self.has_input('p_geomscale') :
      p.set_p_geomscale(self.get_input('p_geomscale'))
    if self.has_input('p_usegeomcenter') :
      p.set_p_usegeomcenter(self.get_input('p_usegeomcenter'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    GeomScaleFactor = 0
    if self.has_input('GeomScaleFactor') :
      GeomScaleFactor = self.get_input('GeomScaleFactor')
    DataScaleFactor = 0
    if self.has_input('DataScaleFactor') :
      DataScaleFactor = self.get_input('DataScaleFactor')
    results = p.execute(Field, GeomScaleFactor, DataScaleFactor)
    self.set_output('Field', results)

class ReportColumnMatrixMisfit(Math) :
  def compute(self) :
    p = sr_py.ReportColumnMatrixMisfitAlg()
    if self.has_input('p_have_ui') :
      p.set_p_have_ui(self.get_input('p_have_ui'))
    if self.has_input('p_methodTCL') :
      p.set_p_methodTCL(self.get_input('p_methodTCL'))
    if self.has_input('p_pTCL') :
      p.set_p_pTCL(self.get_input('p_pTCL'))
    Vec1 = 0
    if self.has_input('Vec1') :
      Vec1 = self.get_input('Vec1')
    Vec2 = 0
    if self.has_input('Vec2') :
      Vec2 = self.get_input('Vec2')
    results = p.execute(Vec1, Vec2)
    self.set_output('Error Out', results)

class EvaluateLinAlgGeneral(Math) :
  def compute(self) :
    p = sr_py.EvaluateLinAlgGeneralAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    i1 = 0
    if self.has_input('i1') :
      i1 = self.get_input('i1')
    i2 = 0
    if self.has_input('i2') :
      i2 = self.get_input('i2')
    i3 = 0
    if self.has_input('i3') :
      i3 = self.get_input('i3')
    i4 = 0
    if self.has_input('i4') :
      i4 = self.get_input('i4')
    i5 = 0
    if self.has_input('i5') :
      i5 = self.get_input('i5')
    results = p.execute(i1, i2, i3, i4, i5)
    self.set_output('o1', results[0])
    self.set_output('o2', results[1])
    self.set_output('o3', results[2])
    self.set_output('o4', results[3])
    self.set_output('o5', results[4])

class AppendMatrix(Math) :
  def compute(self) :
    p = sr_py.AppendMatrixAlg()
    if self.has_input('p_row_or_column') :
      p.set_p_row_or_column(self.get_input('p_row_or_column'))
    BaseMatrix = 0
    if self.has_input('BaseMatrix') :
      BaseMatrix = self.get_input('BaseMatrix')
    AppendMatrix = 0
    if self.has_input('AppendMatrix') :
      AppendMatrix = self.get_input('AppendMatrix')
    results = p.execute(BaseMatrix, AppendMatrix)
    self.set_output('Matrix', results)

class EvaluateLinAlgBinary(Math) :
  def compute(self) :
    p = sr_py.EvaluateLinAlgBinaryAlg()
    if self.has_input('p_op') :
      p.set_p_op(self.get_input('p_op'))
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    A = 0
    if self.has_input('A') :
      A = self.get_input('A')
    B = 0
    if self.has_input('B') :
      B = self.get_input('B')
    results = p.execute(A, B)
    self.set_output('Output', results)

class ConvertMaskVectorToMappingMatrix(Math) :
  def compute(self) :
    p = sr_py.ConvertMaskVectorToMappingMatrixAlg()
    MaskVector = 0
    if self.has_input('MaskVector') :
      MaskVector = self.get_input('MaskVector')
    results = p.execute(MaskVector)
    self.set_output('MappingMatrix', results)

class SolveLinearSystem(Math) :
  def compute(self) :
    p = sr_py.SolveLinearSystemAlg()
    if self.has_input('p_target_error') :
      p.set_p_target_error(self.get_input('p_target_error'))
    if self.has_input('p_flops') :
      p.set_p_flops(self.get_input('p_flops'))
    if self.has_input('p_floprate') :
      p.set_p_floprate(self.get_input('p_floprate'))
    if self.has_input('p_memrefs') :
      p.set_p_memrefs(self.get_input('p_memrefs'))
    if self.has_input('p_memrate') :
      p.set_p_memrate(self.get_input('p_memrate'))
    if self.has_input('p_orig_error') :
      p.set_p_orig_error(self.get_input('p_orig_error'))
    if self.has_input('p_current_error') :
      p.set_p_current_error(self.get_input('p_current_error'))
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    if self.has_input('p_precond') :
      p.set_p_precond(self.get_input('p_precond'))
    if self.has_input('p_iteration') :
      p.set_p_iteration(self.get_input('p_iteration'))
    if self.has_input('p_maxiter') :
      p.set_p_maxiter(self.get_input('p_maxiter'))
    if self.has_input('p_use_previous_soln') :
      p.set_p_use_previous_soln(self.get_input('p_use_previous_soln'))
    if self.has_input('p_emit_partial') :
      p.set_p_emit_partial(self.get_input('p_emit_partial'))
    if self.has_input('p_emit_iter') :
      p.set_p_emit_iter(self.get_input('p_emit_iter'))
    if self.has_input('p_status') :
      p.set_p_status(self.get_input('p_status'))
    if self.has_input('p_np') :
      p.set_p_np(self.get_input('p_np'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    RHS = 0
    if self.has_input('RHS') :
      RHS = self.get_input('RHS')
    results = p.execute(Matrix, RHS)
    self.set_output('Solution', results)

class ReportMatrixColumnMeasure(Math) :
  def compute(self) :
    p = sr_py.ReportMatrixColumnMeasureAlg()
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Vector', results)

class SortMatrix(Math) :
  def compute(self) :
    p = sr_py.SortMatrixAlg()
    if self.has_input('p_row_or_col') :
      p.set_p_row_or_col(self.get_input('p_row_or_col'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Matrix', results)

class CreateGeometricTransform(Math) :
  def compute(self) :
    p = sr_py.CreateGeometricTransformAlg()
    if self.has_input('p_rotate_x') :
      p.set_p_rotate_x(self.get_input('p_rotate_x'))
    if self.has_input('p_rotate_y') :
      p.set_p_rotate_y(self.get_input('p_rotate_y'))
    if self.has_input('p_rotate_z') :
      p.set_p_rotate_z(self.get_input('p_rotate_z'))
    if self.has_input('p_rotate_theta') :
      p.set_p_rotate_theta(self.get_input('p_rotate_theta'))
    if self.has_input('p_translate_x') :
      p.set_p_translate_x(self.get_input('p_translate_x'))
    if self.has_input('p_translate_y') :
      p.set_p_translate_y(self.get_input('p_translate_y'))
    if self.has_input('p_translate_z') :
      p.set_p_translate_z(self.get_input('p_translate_z'))
    if self.has_input('p_scale_uniform') :
      p.set_p_scale_uniform(self.get_input('p_scale_uniform'))
    if self.has_input('p_scale_x') :
      p.set_p_scale_x(self.get_input('p_scale_x'))
    if self.has_input('p_scale_y') :
      p.set_p_scale_y(self.get_input('p_scale_y'))
    if self.has_input('p_scale_z') :
      p.set_p_scale_z(self.get_input('p_scale_z'))
    if self.has_input('p_shear_plane_a') :
      p.set_p_shear_plane_a(self.get_input('p_shear_plane_a'))
    if self.has_input('p_shear_plane_b') :
      p.set_p_shear_plane_b(self.get_input('p_shear_plane_b'))
    if self.has_input('p_shear_plane_c') :
      p.set_p_shear_plane_c(self.get_input('p_shear_plane_c'))
    if self.has_input('p_widget_resizable') :
      p.set_p_widget_resizable(self.get_input('p_widget_resizable'))
    if self.has_input('p_permute_x') :
      p.set_p_permute_x(self.get_input('p_permute_x'))
    if self.has_input('p_permute_y') :
      p.set_p_permute_y(self.get_input('p_permute_y'))
    if self.has_input('p_permute_z') :
      p.set_p_permute_z(self.get_input('p_permute_z'))
    if self.has_input('p_pre_transform') :
      p.set_p_pre_transform(self.get_input('p_pre_transform'))
    if self.has_input('p_which_transform') :
      p.set_p_which_transform(self.get_input('p_which_transform'))
    if self.has_input('p_widget_scale') :
      p.set_p_widget_scale(self.get_input('p_widget_scale'))
    if self.has_input('p_ignoring_widget_changes') :
      p.set_p_ignoring_widget_changes(self.get_input('p_ignoring_widget_changes'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Matrix', results[0])
    self.set_output('Geometry', results[1])

class ChooseMatrix(Math) :
  def compute(self) :
    p = sr_py.ChooseMatrixAlg()
    if self.has_input('p_use_first_valid') :
      p.set_p_use_first_valid(self.get_input('p_use_first_valid'))
    if self.has_input('p_port_valid_index') :
      p.set_p_port_valid_index(self.get_input('p_port_valid_index'))
    if self.has_input('p_port_selected_index') :
      p.set_p_port_selected_index(self.get_input('p_port_selected_index'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Matrix', results)

class ConvertMappingMatrixToMaskVector(Math) :
  def compute(self) :
    p = sr_py.ConvertMappingMatrixToMaskVectorAlg()
    MappingMatrix = 0
    if self.has_input('MappingMatrix') :
      MappingMatrix = self.get_input('MappingMatrix')
    results = p.execute(MappingMatrix)
    self.set_output('MaskVector', results)

class ResizeMatrix(Math) :
  def compute(self) :
    p = sr_py.ResizeMatrixAlg()
    if self.has_input('p_dim_m') :
      p.set_p_dim_m(self.get_input('p_dim_m'))
    if self.has_input('p_dim_n') :
      p.set_p_dim_n(self.get_input('p_dim_n'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    M = 0
    if self.has_input('M') :
      M = self.get_input('M')
    N = 0
    if self.has_input('N') :
      N = self.get_input('N')
    results = p.execute(Matrix, M, N)
    self.set_output('Matrix', results)

class CollectMatrices(Math) :
  def compute(self) :
    p = sr_py.CollectMatricesAlg()
    if self.has_input('p_append') :
      p.set_p_append(self.get_input('p_append'))
    if self.has_input('p_row') :
      p.set_p_row(self.get_input('p_row'))
    if self.has_input('p_front') :
      p.set_p_front(self.get_input('p_front'))
    Optional_BaseMatrix = 0
    if self.has_input('Optional BaseMatrix') :
      Optional_BaseMatrix = self.get_input('Optional BaseMatrix')
    SubMatrix = 0
    if self.has_input('SubMatrix') :
      SubMatrix = self.get_input('SubMatrix')
    results = p.execute(Optional_BaseMatrix, SubMatrix)
    self.set_output('CompositeMatrix', results)

class GetColumnOrRowFromMatrix(Math) :
  def compute(self) :
    p = sr_py.GetColumnOrRowFromMatrixAlg()
    if self.has_input('p_row_or_col') :
      p.set_p_row_or_col(self.get_input('p_row_or_col'))
    if self.has_input('p_selectable_min') :
      p.set_p_selectable_min(self.get_input('p_selectable_min'))
    if self.has_input('p_selectable_max') :
      p.set_p_selectable_max(self.get_input('p_selectable_max'))
    if self.has_input('p_selectable_inc') :
      p.set_p_selectable_inc(self.get_input('p_selectable_inc'))
    if self.has_input('p_selectable_units') :
      p.set_p_selectable_units(self.get_input('p_selectable_units'))
    if self.has_input('p_range_min') :
      p.set_p_range_min(self.get_input('p_range_min'))
    if self.has_input('p_range_max') :
      p.set_p_range_max(self.get_input('p_range_max'))
    if self.has_input('p_playmode') :
      p.set_p_playmode(self.get_input('p_playmode'))
    if self.has_input('p_current') :
      p.set_p_current(self.get_input('p_current'))
    if self.has_input('p_execmode') :
      p.set_p_execmode(self.get_input('p_execmode'))
    if self.has_input('p_delay') :
      p.set_p_delay(self.get_input('p_delay'))
    if self.has_input('p_inc_amount') :
      p.set_p_inc_amount(self.get_input('p_inc_amount'))
    if self.has_input('p_send_amount') :
      p.set_p_send_amount(self.get_input('p_send_amount'))
    if self.has_input('p_data_series_done') :
      p.set_p_data_series_done(self.get_input('p_data_series_done'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    Weight_Vector = 0
    if self.has_input('Weight Vector') :
      Weight_Vector = self.get_input('Weight Vector')
    Current_Index = 0
    if self.has_input('Current Index') :
      Current_Index = self.get_input('Current Index')
    results = p.execute(Matrix, Weight_Vector, Current_Index)
    self.set_output('Vector', results[0])
    self.set_output('Selected Index', results[1])

class BuildNoiseColumnMatrix(Math) :
  def compute(self) :
    p = sr_py.BuildNoiseColumnMatrixAlg()
    if self.has_input('p_snr') :
      p.set_p_snr(self.get_input('p_snr'))
    Signal = 0
    if self.has_input('Signal') :
      Signal = self.get_input('Signal')
    results = p.execute(Signal)
    self.set_output('Noise', results)

class EvaluateLinAlgUnary(Math) :
  def compute(self) :
    p = sr_py.EvaluateLinAlgUnaryAlg()
    if self.has_input('p_op') :
      p.set_p_op(self.get_input('p_op'))
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('Output', results)

class GetSubmatrix(Math) :
  def compute(self) :
    p = sr_py.GetSubmatrixAlg()
    if self.has_input('p_mincol') :
      p.set_p_mincol(self.get_input('p_mincol'))
    if self.has_input('p_maxcol') :
      p.set_p_maxcol(self.get_input('p_maxcol'))
    if self.has_input('p_minrow') :
      p.set_p_minrow(self.get_input('p_minrow'))
    if self.has_input('p_maxrow') :
      p.set_p_maxrow(self.get_input('p_maxrow'))
    if self.has_input('p_nrow') :
      p.set_p_nrow(self.get_input('p_nrow'))
    if self.has_input('p_ncol') :
      p.set_p_ncol(self.get_input('p_ncol'))
    Input_Matrix = 0
    if self.has_input('Input Matrix') :
      Input_Matrix = self.get_input('Input Matrix')
    Optional_Range_Bounds = 0
    if self.has_input('Optional Range Bounds') :
      Optional_Range_Bounds = self.get_input('Optional Range Bounds')
    results = p.execute(Input_Matrix, Optional_Range_Bounds)
    self.set_output('Output Matrix', results)

class ReorderMatrixByReverseCuthillMcKee(Math) :
  def compute(self) :
    p = sr_py.ReorderMatrixByReverseCuthillMcKeeAlg()
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Matrix', results[0])
    self.set_output('Mapping', results[1])
    self.set_output('InverseMapping', results[2])

class CreateMatrix(Math) :
  def compute(self) :
    p = sr_py.CreateMatrixAlg()
    if self.has_input('p_rows') :
      p.set_p_rows(self.get_input('p_rows'))
    if self.has_input('p_cols') :
      p.set_p_cols(self.get_input('p_cols'))
    if self.has_input('p_data') :
      p.set_p_data(self.get_input('p_data'))
    if self.has_input('p_clabel') :
      p.set_p_clabel(self.get_input('p_clabel'))
    if self.has_input('p_rlabel') :
      p.set_p_rlabel(self.get_input('p_rlabel'))
    results = p.execute()
    self.set_output('matrix', results)

class SolveMinNormLeastSqSystem(Math) :
  def compute(self) :
    p = sr_py.SolveMinNormLeastSqSystemAlg()
    BasisVec1 = 0
    if self.has_input('BasisVec1') :
      BasisVec1 = self.get_input('BasisVec1')
    BasisVec2 = 0
    if self.has_input('BasisVec2') :
      BasisVec2 = self.get_input('BasisVec2')
    BasisVec3 = 0
    if self.has_input('BasisVec3') :
      BasisVec3 = self.get_input('BasisVec3')
    TargetVec = 0
    if self.has_input('TargetVec') :
      TargetVec = self.get_input('TargetVec')
    results = p.execute(BasisVec1, BasisVec2, BasisVec3, TargetVec)
    self.set_output('WeightVec(Col)', results[0])
    self.set_output('ResultVec(Col)', results[1])

class ConvertMatrixType(Math) :
  def compute(self) :
    p = sr_py.ConvertMatrixTypeAlg()
    if self.has_input('p_oldtype') :
      p.set_p_oldtype(self.get_input('p_oldtype'))
    if self.has_input('p_newtype') :
      p.set_p_newtype(self.get_input('p_newtype'))
    if self.has_input('p_nrow') :
      p.set_p_nrow(self.get_input('p_nrow'))
    if self.has_input('p_ncol') :
      p.set_p_ncol(self.get_input('p_ncol'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('Output', results)

class ReportMatrixRowMeasure(Math) :
  def compute(self) :
    p = sr_py.ReportMatrixRowMeasureAlg()
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Vector', results)

class ReorderMatrixByCuthillMcKee(Math) :
  def compute(self) :
    p = sr_py.ReorderMatrixByCuthillMcKeeAlg()
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Matrix', results[0])
    self.set_output('Mapping', results[1])
    self.set_output('InverseMapping', results[2])

class ReportMatrixInfo(Math) :
  def compute(self) :
    p = sr_py.ReportMatrixInfoAlg()
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('NumRows', results[0])
    self.set_output('NumCols', results[1])
    self.set_output('NumElements', results[2])

class RemoveZerosFromMatrix(Math) :
  def compute(self) :
    p = sr_py.RemoveZerosFromMatrixAlg()
    if self.has_input('p_row_or_col') :
      p.set_p_row_or_col(self.get_input('p_row_or_col'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Matrix', results)

class RemoveZeroRowsAndColumns(Math) :
  def compute(self) :
    p = sr_py.RemoveZeroRowsAndColumnsAlg()
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('ReducedMatrix', results[0])
    self.set_output('LeftMapping', results[1])
    self.set_output('RightMapping', results[2])

class CreateDataArray(DataArrayMath) :
  def compute(self) :
    p = sr_py.CreateDataArrayAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    Size = 0
    if self.has_input('Size') :
      Size = self.get_input('Size')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Size, Function, Array)
    self.set_output('DataArray', results)

class CreateDataArrayFromIndices(DataArrayMath) :
  def compute(self) :
    p = sr_py.CreateDataArrayFromIndicesAlg()
    Indices = 0
    if self.has_input('Indices') :
      Indices = self.get_input('Indices')
    Template = 0
    if self.has_input('Template') :
      Template = self.get_input('Template')
    results = p.execute(Indices, Template)
    self.set_output('DataArray', results)

class ReportDataArrayInfo(DataArrayMath) :
  def compute(self) :
    p = sr_py.ReportDataArrayInfoAlg()
    DataArray = 0
    if self.has_input('DataArray') :
      DataArray = self.get_input('DataArray')
    results = p.execute(DataArray)
    self.set_output('NumElements', results)

class CreateVectorArray(DataArrayMath) :
  def compute(self) :
    p = sr_py.CreateVectorArrayAlg()
    X = 0
    if self.has_input('X') :
      X = self.get_input('X')
    Y = 0
    if self.has_input('Y') :
      Y = self.get_input('Y')
    Z = 0
    if self.has_input('Z') :
      Z = self.get_input('Z')
    results = p.execute(X, Y, Z)
    self.set_output('Vector', results)

class ReplicateDataArray(DataArrayMath) :
  def compute(self) :
    p = sr_py.ReplicateDataArrayAlg()
    if self.has_input('p_size') :
      p.set_p_size(self.get_input('p_size'))
    DataArray = 0
    if self.has_input('DataArray') :
      DataArray = self.get_input('DataArray')
    Size = 0
    if self.has_input('Size') :
      Size = self.get_input('Size')
    results = p.execute(DataArray, Size)
    self.set_output('DataArray', results)

class SplitVectorArrayInXYZ(DataArrayMath) :
  def compute(self) :
    p = sr_py.SplitVectorArrayInXYZAlg()
    VectorArray = 0
    if self.has_input('VectorArray') :
      VectorArray = self.get_input('VectorArray')
    results = p.execute(VectorArray)
    self.set_output('X', results[0])
    self.set_output('Y', results[1])
    self.set_output('Z', results[2])

class DecomposeTensorArrayIntoEigenVectors(DataArrayMath) :
  def compute(self) :
    p = sr_py.DecomposeTensorArrayIntoEigenVectorsAlg()
    TensorArray = 0
    if self.has_input('TensorArray') :
      TensorArray = self.get_input('TensorArray')
    results = p.execute(TensorArray)
    self.set_output('EigenVector1', results[0])
    self.set_output('EigenVector2', results[1])
    self.set_output('EigenVector3', results[2])
    self.set_output('EigenValue1', results[3])
    self.set_output('EigenValue2', results[4])
    self.set_output('EigenValue3', results[5])

class CalculateDataArray(DataArrayMath) :
  def compute(self) :
    p = sr_py.CalculateDataArrayAlg()
    if self.has_input('p_function') :
      p.set_p_function(self.get_input('p_function'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    DataArray = 0
    if self.has_input('DataArray') :
      DataArray = self.get_input('DataArray')
    Function = ''
    if self.has_input('Function') :
      Function = self.get_input('Function')
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(DataArray, Function, Array)
    self.set_output('DataArray', results)

class ReportDataArrayMeasure(DataArrayMath) :
  def compute(self) :
    p = sr_py.ReportDataArrayMeasureAlg()
    if self.has_input('p_measure') :
      p.set_p_measure(self.get_input('p_measure'))
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Array)
    self.set_output('Measure', results)

class AppendDataArrays(DataArrayMath) :
  def compute(self) :
    p = sr_py.AppendDataArraysAlg()
    Array = 0
    if self.has_input('Array') :
      Array = self.get_input('Array')
    results = p.execute(Array)
    self.set_output('Array', results)

class CreateTensorArray(DataArrayMath) :
  def compute(self) :
    p = sr_py.CreateTensorArrayAlg()
    EigenVector1 = 0
    if self.has_input('EigenVector1') :
      EigenVector1 = self.get_input('EigenVector1')
    EigenVector2 = 0
    if self.has_input('EigenVector2') :
      EigenVector2 = self.get_input('EigenVector2')
    EigenValue1 = 0
    if self.has_input('EigenValue1') :
      EigenValue1 = self.get_input('EigenValue1')
    EigenValue2 = 0
    if self.has_input('EigenValue2') :
      EigenValue2 = self.get_input('EigenValue2')
    EigenValue3 = 0
    if self.has_input('EigenValue3') :
      EigenValue3 = self.get_input('EigenValue3')
    results = p.execute(EigenVector1, EigenVector2, EigenValue1, EigenValue2, EigenValue3)
    self.set_output('TensorArray', results)

class PrintMatrixIntoString(String) :
  def compute(self) :
    p = sr_py.PrintMatrixIntoStringAlg()
    if self.has_input('p_formatstring') :
      p.set_p_formatstring(self.get_input('p_formatstring'))
    Format = ''
    if self.has_input('Format') :
      Format = self.get_input('Format')
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Format, Input)
    self.set_output('Output', results)

class GetFileName(String) :
  def compute(self) :
    p = sr_py.GetFileNameAlg()
    if self.has_input('p_filename_base') :
      p.set_p_filename_base(self.get_input('p_filename_base'))
    if self.has_input('p_delay') :
      p.set_p_delay(self.get_input('p_delay'))
    if self.has_input('p_pinned') :
      p.set_p_pinned(self.get_input('p_pinned'))
    results = p.execute()
    self.set_output('Full Filename', results)

class SplitFileName(String) :
  def compute(self) :
    p = sr_py.SplitFileNameAlg()
    Filename = ''
    if self.has_input('Filename') :
      Filename = self.get_input('Filename')
    results = p.execute(Filename)
    self.set_output('Pathname', results[0])
    self.set_output('Filename Base', results[1])
    self.set_output('Extension', results[2])
    self.set_output('Filename', results[3])

class PrintStringIntoString(String) :
  def compute(self) :
    p = sr_py.PrintStringIntoStringAlg()
    if self.has_input('p_formatstring') :
      p.set_p_formatstring(self.get_input('p_formatstring'))
    Format = ''
    if self.has_input('Format') :
      Format = self.get_input('Format')
    Input = ''
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Format, Input)
    self.set_output('Output', results)

class CreateString(String) :
  def compute(self) :
    p = sr_py.CreateStringAlg()
    if self.has_input('p_inputstring') :
      p.set_p_inputstring(self.get_input('p_inputstring'))
    results = p.execute()
    self.set_output('Output', results)

class ReportStringInfo(String) :
  def compute(self) :
    p = sr_py.ReportStringInfoAlg()
    if self.has_input('p_inputstring') :
      p.set_p_inputstring(self.get_input('p_inputstring'))
    Input = ''
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)

class JoinStrings(String) :
  def compute(self) :
    p = sr_py.JoinStringsAlg()
    input = ''
    if self.has_input('input') :
      input = self.get_input('input')
    results = p.execute(input)
    self.set_output('Output', results)

class GetNetworkFileName(String) :
  def compute(self) :
    p = sr_py.GetNetworkFileNameAlg()
    results = p.execute()
    self.set_output('String', results)

class SetFieldProperty(MiscField) :
  def compute(self) :
    p = sr_py.SetFieldPropertyAlg()
    if self.has_input('p_num_entries') :
      p.set_p_num_entries(self.get_input('p_num_entries'))
    if self.has_input('p_property') :
      p.set_p_property(self.get_input('p_property'))
    if self.has_input('p_type') :
      p.set_p_type(self.get_input('p_type'))
    if self.has_input('p_value') :
      p.set_p_value(self.get_input('p_value'))
    if self.has_input('p_readonly') :
      p.set_p_readonly(self.get_input('p_readonly'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Field', results)

class ReportScalarFieldStats(MiscField) :
  def compute(self) :
    p = sr_py.ReportScalarFieldStatsAlg()
    if self.has_input('p_min') :
      p.set_p_min(self.get_input('p_min'))
    if self.has_input('p_max') :
      p.set_p_max(self.get_input('p_max'))
    if self.has_input('p_mean') :
      p.set_p_mean(self.get_input('p_mean'))
    if self.has_input('p_median') :
      p.set_p_median(self.get_input('p_median'))
    if self.has_input('p_sigma') :
      p.set_p_sigma(self.get_input('p_sigma'))
    if self.has_input('p_is_fixed') :
      p.set_p_is_fixed(self.get_input('p_is_fixed'))
    if self.has_input('p_nbuckets') :
      p.set_p_nbuckets(self.get_input('p_nbuckets'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)

class SelectFieldROIWithBoxWidget(MiscField) :
  def compute(self) :
    p = sr_py.SelectFieldROIWithBoxWidgetAlg()
    if self.has_input('p_stampvalue') :
      p.set_p_stampvalue(self.get_input('p_stampvalue'))
    if self.has_input('p_runmode') :
      p.set_p_runmode(self.get_input('p_runmode'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Selection Widget', results[0])
    self.set_output('Output Field', results[1])

class BuildMatrixOfSurfaceNormals(MiscField) :
  def compute(self) :
    p = sr_py.BuildMatrixOfSurfaceNormalsAlg()
    Surface_Field = 0
    if self.has_input('Surface Field') :
      Surface_Field = self.get_input('Surface Field')
    results = p.execute(Surface_Field)
    self.set_output('Nodal Surface Normals', results)

class ReportFieldInfo(MiscField) :
  def compute(self) :
    p = sr_py.ReportFieldInfoAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('NumNodes', results[0])
    self.set_output('NumElements', results[1])
    self.set_output('NumData', results[2])
    self.set_output('DataMin', results[3])
    self.set_output('DataMax', results[4])
    self.set_output('FieldSize', results[5])
    self.set_output('FieldCenter', results[6])
    self.set_output('Dimensions', results[7])

class ReportFieldGeometryMeasures(MiscField) :
  def compute(self) :
    p = sr_py.ReportFieldGeometryMeasuresAlg()
    if self.has_input('p_simplexString') :
      p.set_p_simplexString(self.get_input('p_simplexString'))
    if self.has_input('p_xFlag') :
      p.set_p_xFlag(self.get_input('p_xFlag'))
    if self.has_input('p_yFlag') :
      p.set_p_yFlag(self.get_input('p_yFlag'))
    if self.has_input('p_zFlag') :
      p.set_p_zFlag(self.get_input('p_zFlag'))
    if self.has_input('p_idxFlag') :
      p.set_p_idxFlag(self.get_input('p_idxFlag'))
    if self.has_input('p_sizeFlag') :
      p.set_p_sizeFlag(self.get_input('p_sizeFlag'))
    if self.has_input('p_normalsFlag') :
      p.set_p_normalsFlag(self.get_input('p_normalsFlag'))
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Measures Matrix', results)

class SetFieldOrMeshStringProperty(MiscField) :
  def compute(self) :
    p = sr_py.SetFieldOrMeshStringPropertyAlg()
    if self.has_input('p_prop') :
      p.set_p_prop(self.get_input('p_prop'))
    if self.has_input('p_val') :
      p.set_p_val(self.get_input('p_val'))
    if self.has_input('p_meshprop') :
      p.set_p_meshprop(self.get_input('p_meshprop'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('Output', results)

class ManageFieldSeries(MiscField) :
  def compute(self) :
    p = sr_py.ManageFieldSeriesAlg()
    if self.has_input('p_num_ports') :
      p.set_p_num_ports(self.get_input('p_num_ports'))
    Input = 0
    if self.has_input('Input') :
      Input = self.get_input('Input')
    results = p.execute(Input)
    self.set_output('Output 0', results[0])
    self.set_output('Output 1', results[1])
    self.set_output('Output 2', results[2])
    self.set_output('Output 3', results[3])

class ReportSearchGridInfo(MiscField) :
  def compute(self) :
    p = sr_py.ReportSearchGridInfoAlg()
    Input_Field = 0
    if self.has_input('Input Field') :
      Input_Field = self.get_input('Input Field')
    results = p.execute(Input_Field)
    self.set_output('Output Sample Field', results)

class ChooseField(MiscField) :
  def compute(self) :
    p = sr_py.ChooseFieldAlg()
    if self.has_input('p_use_first_valid') :
      p.set_p_use_first_valid(self.get_input('p_use_first_valid'))
    if self.has_input('p_port_valid_index') :
      p.set_p_port_valid_index(self.get_input('p_port_valid_index'))
    if self.has_input('p_port_selected_index') :
      p.set_p_port_selected_index(self.get_input('p_port_selected_index'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Field', results)

class BuildPointCloudToLatVolMappingMatrix(MiscField) :
  def compute(self) :
    p = sr_py.BuildPointCloudToLatVolMappingMatrixAlg()
    if self.has_input('p_epsilon') :
      p.set_p_epsilon(self.get_input('p_epsilon'))
    PointCloudField = 0
    if self.has_input('PointCloudField') :
      PointCloudField = self.get_input('PointCloudField')
    LatVolField = 0
    if self.has_input('LatVolField') :
      LatVolField = self.get_input('LatVolField')
    results = p.execute(PointCloudField, LatVolField)
    self.set_output('MappingMatrix', results)

class BuildMappingMatrix(MiscField) :
  def compute(self) :
    p = sr_py.BuildMappingMatrixAlg()
    if self.has_input('p_interpolation_basis') :
      p.set_p_interpolation_basis(self.get_input('p_interpolation_basis'))
    if self.has_input('p_map_source_to_single_dest') :
      p.set_p_map_source_to_single_dest(self.get_input('p_map_source_to_single_dest'))
    if self.has_input('p_exhaustive_search') :
      p.set_p_exhaustive_search(self.get_input('p_exhaustive_search'))
    if self.has_input('p_exhaustive_search_max_dist') :
      p.set_p_exhaustive_search_max_dist(self.get_input('p_exhaustive_search_max_dist'))
    if self.has_input('p_np') :
      p.set_p_np(self.get_input('p_np'))
    Source = 0
    if self.has_input('Source') :
      Source = self.get_input('Source')
    Destination = 0
    if self.has_input('Destination') :
      Destination = self.get_input('Destination')
    results = p.execute(Source, Destination)
    self.set_output('Mapping', results)

class CoregisterPointClouds(MiscField) :
  def compute(self) :
    p = sr_py.CoregisterPointCloudsAlg()
    if self.has_input('p_allowScale') :
      p.set_p_allowScale(self.get_input('p_allowScale'))
    if self.has_input('p_allowRotate') :
      p.set_p_allowRotate(self.get_input('p_allowRotate'))
    if self.has_input('p_allowTranslate') :
      p.set_p_allowTranslate(self.get_input('p_allowTranslate'))
    if self.has_input('p_seed') :
      p.set_p_seed(self.get_input('p_seed'))
    if self.has_input('p_iters') :
      p.set_p_iters(self.get_input('p_iters'))
    if self.has_input('p_misfitTol') :
      p.set_p_misfitTol(self.get_input('p_misfitTol'))
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    Fixed_PointCloudField = 0
    if self.has_input('Fixed PointCloudField') :
      Fixed_PointCloudField = self.get_input('Fixed PointCloudField')
    Mobile_PointCloudField = 0
    if self.has_input('Mobile PointCloudField') :
      Mobile_PointCloudField = self.get_input('Mobile PointCloudField')
    DistanceField_From_Fixed = 0
    if self.has_input('DistanceField From Fixed') :
      DistanceField_From_Fixed = self.get_input('DistanceField From Fixed')
    results = p.execute(Fixed_PointCloudField, Mobile_PointCloudField, DistanceField_From_Fixed)
    self.set_output('Transform', results)

class CollectPointClouds(MiscField) :
  def compute(self) :
    p = sr_py.CollectPointCloudsAlg()
    if self.has_input('p_num_fields') :
      p.set_p_num_fields(self.get_input('p_num_fields'))
    Point_Cloud = 0
    if self.has_input('Point Cloud') :
      Point_Cloud = self.get_input('Point Cloud')
    results = p.execute(Point_Cloud)
    self.set_output('Curve', results)

class GetColorMapsFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetColorMapsFromBundleAlg()
    if self.has_input('p_colormap1_name') :
      p.set_p_colormap1_name(self.get_input('p_colormap1_name'))
    if self.has_input('p_colormap2_name') :
      p.set_p_colormap2_name(self.get_input('p_colormap2_name'))
    if self.has_input('p_colormap3_name') :
      p.set_p_colormap3_name(self.get_input('p_colormap3_name'))
    if self.has_input('p_colormap4_name') :
      p.set_p_colormap4_name(self.get_input('p_colormap4_name'))
    if self.has_input('p_colormap5_name') :
      p.set_p_colormap5_name(self.get_input('p_colormap5_name'))
    if self.has_input('p_colormap6_name') :
      p.set_p_colormap6_name(self.get_input('p_colormap6_name'))
    if self.has_input('p_colormap_selection') :
      p.set_p_colormap_selection(self.get_input('p_colormap_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('colormap1', results[1])
    self.set_output('colormap2', results[2])
    self.set_output('colormap3', results[3])
    self.set_output('colormap4', results[4])
    self.set_output('colormap5', results[5])
    self.set_output('colormap6', results[6])

class InsertFieldsIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertFieldsIntoBundleAlg()
    if self.has_input('p_field1_name') :
      p.set_p_field1_name(self.get_input('p_field1_name'))
    if self.has_input('p_field2_name') :
      p.set_p_field2_name(self.get_input('p_field2_name'))
    if self.has_input('p_field3_name') :
      p.set_p_field3_name(self.get_input('p_field3_name'))
    if self.has_input('p_field4_name') :
      p.set_p_field4_name(self.get_input('p_field4_name'))
    if self.has_input('p_field5_name') :
      p.set_p_field5_name(self.get_input('p_field5_name'))
    if self.has_input('p_field6_name') :
      p.set_p_field6_name(self.get_input('p_field6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    field1 = 0
    if self.has_input('field1') :
      field1 = self.get_input('field1')
    field2 = 0
    if self.has_input('field2') :
      field2 = self.get_input('field2')
    field3 = 0
    if self.has_input('field3') :
      field3 = self.get_input('field3')
    field4 = 0
    if self.has_input('field4') :
      field4 = self.get_input('field4')
    field5 = 0
    if self.has_input('field5') :
      field5 = self.get_input('field5')
    field6 = 0
    if self.has_input('field6') :
      field6 = self.get_input('field6')
    results = p.execute(bundle, field1, field2, field3, field4, field5, field6)
    self.set_output('bundle', results)

class GetFieldsFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetFieldsFromBundleAlg()
    if self.has_input('p_field1_name') :
      p.set_p_field1_name(self.get_input('p_field1_name'))
    if self.has_input('p_field2_name') :
      p.set_p_field2_name(self.get_input('p_field2_name'))
    if self.has_input('p_field3_name') :
      p.set_p_field3_name(self.get_input('p_field3_name'))
    if self.has_input('p_field4_name') :
      p.set_p_field4_name(self.get_input('p_field4_name'))
    if self.has_input('p_field5_name') :
      p.set_p_field5_name(self.get_input('p_field5_name'))
    if self.has_input('p_field6_name') :
      p.set_p_field6_name(self.get_input('p_field6_name'))
    if self.has_input('p_field_selection') :
      p.set_p_field_selection(self.get_input('p_field_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('field1', results[1])
    self.set_output('field2', results[2])
    self.set_output('field3', results[3])
    self.set_output('field4', results[4])
    self.set_output('field5', results[5])
    self.set_output('field6', results[6])

class InsertColorMap2sIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertColorMap2sIntoBundleAlg()
    if self.has_input('p_colormap21_name') :
      p.set_p_colormap21_name(self.get_input('p_colormap21_name'))
    if self.has_input('p_colormap22_name') :
      p.set_p_colormap22_name(self.get_input('p_colormap22_name'))
    if self.has_input('p_colormap23_name') :
      p.set_p_colormap23_name(self.get_input('p_colormap23_name'))
    if self.has_input('p_colormap24_name') :
      p.set_p_colormap24_name(self.get_input('p_colormap24_name'))
    if self.has_input('p_colormap25_name') :
      p.set_p_colormap25_name(self.get_input('p_colormap25_name'))
    if self.has_input('p_colormap26_name') :
      p.set_p_colormap26_name(self.get_input('p_colormap26_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    colormap21 = 0
    if self.has_input('colormap21') :
      colormap21 = self.get_input('colormap21')
    colormap22 = 0
    if self.has_input('colormap22') :
      colormap22 = self.get_input('colormap22')
    colormap23 = 0
    if self.has_input('colormap23') :
      colormap23 = self.get_input('colormap23')
    colormap24 = 0
    if self.has_input('colormap24') :
      colormap24 = self.get_input('colormap24')
    colormap25 = 0
    if self.has_input('colormap25') :
      colormap25 = self.get_input('colormap25')
    colormap26 = 0
    if self.has_input('colormap26') :
      colormap26 = self.get_input('colormap26')
    results = p.execute(bundle, colormap21, colormap22, colormap23, colormap24, colormap25, colormap26)
    self.set_output('bundle', results)

class GetBundlesFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetBundlesFromBundleAlg()
    if self.has_input('p_bundle1_name') :
      p.set_p_bundle1_name(self.get_input('p_bundle1_name'))
    if self.has_input('p_bundle2_name') :
      p.set_p_bundle2_name(self.get_input('p_bundle2_name'))
    if self.has_input('p_bundle3_name') :
      p.set_p_bundle3_name(self.get_input('p_bundle3_name'))
    if self.has_input('p_bundle4_name') :
      p.set_p_bundle4_name(self.get_input('p_bundle4_name'))
    if self.has_input('p_bundle5_name') :
      p.set_p_bundle5_name(self.get_input('p_bundle5_name'))
    if self.has_input('p_bundle6_name') :
      p.set_p_bundle6_name(self.get_input('p_bundle6_name'))
    if self.has_input('p_bundle_selection') :
      p.set_p_bundle_selection(self.get_input('p_bundle_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('bundle1', results[1])
    self.set_output('bundle2', results[2])
    self.set_output('bundle3', results[3])
    self.set_output('bundle4', results[4])
    self.set_output('bundle5', results[5])
    self.set_output('bundle6', results[6])

class GetPathsFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetPathsFromBundleAlg()
    if self.has_input('p_path1_name') :
      p.set_p_path1_name(self.get_input('p_path1_name'))
    if self.has_input('p_path2_name') :
      p.set_p_path2_name(self.get_input('p_path2_name'))
    if self.has_input('p_path3_name') :
      p.set_p_path3_name(self.get_input('p_path3_name'))
    if self.has_input('p_path4_name') :
      p.set_p_path4_name(self.get_input('p_path4_name'))
    if self.has_input('p_path5_name') :
      p.set_p_path5_name(self.get_input('p_path5_name'))
    if self.has_input('p_path6_name') :
      p.set_p_path6_name(self.get_input('p_path6_name'))
    if self.has_input('p_path_selection') :
      p.set_p_path_selection(self.get_input('p_path_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('path1', results[1])
    self.set_output('path2', results[2])
    self.set_output('path3', results[3])
    self.set_output('path4', results[4])
    self.set_output('path5', results[5])
    self.set_output('path6', results[6])

class InsertStringsIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertStringsIntoBundleAlg()
    if self.has_input('p_string1_name') :
      p.set_p_string1_name(self.get_input('p_string1_name'))
    if self.has_input('p_string2_name') :
      p.set_p_string2_name(self.get_input('p_string2_name'))
    if self.has_input('p_string3_name') :
      p.set_p_string3_name(self.get_input('p_string3_name'))
    if self.has_input('p_string4_name') :
      p.set_p_string4_name(self.get_input('p_string4_name'))
    if self.has_input('p_string5_name') :
      p.set_p_string5_name(self.get_input('p_string5_name'))
    if self.has_input('p_string6_name') :
      p.set_p_string6_name(self.get_input('p_string6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    string1 = ''
    if self.has_input('string1') :
      string1 = self.get_input('string1')
    string2 = ''
    if self.has_input('string2') :
      string2 = self.get_input('string2')
    string3 = ''
    if self.has_input('string3') :
      string3 = self.get_input('string3')
    string4 = ''
    if self.has_input('string4') :
      string4 = self.get_input('string4')
    string5 = ''
    if self.has_input('string5') :
      string5 = self.get_input('string5')
    string6 = ''
    if self.has_input('string6') :
      string6 = self.get_input('string6')
    results = p.execute(bundle, string1, string2, string3, string4, string5, string6)
    self.set_output('bundle', results)

class GetNrrdsFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetNrrdsFromBundleAlg()
    if self.has_input('p_nrrd1_name') :
      p.set_p_nrrd1_name(self.get_input('p_nrrd1_name'))
    if self.has_input('p_nrrd2_name') :
      p.set_p_nrrd2_name(self.get_input('p_nrrd2_name'))
    if self.has_input('p_nrrd3_name') :
      p.set_p_nrrd3_name(self.get_input('p_nrrd3_name'))
    if self.has_input('p_nrrd4_name') :
      p.set_p_nrrd4_name(self.get_input('p_nrrd4_name'))
    if self.has_input('p_nrrd5_name') :
      p.set_p_nrrd5_name(self.get_input('p_nrrd5_name'))
    if self.has_input('p_nrrd6_name') :
      p.set_p_nrrd6_name(self.get_input('p_nrrd6_name'))
    if self.has_input('p_transposenrrd1') :
      p.set_p_transposenrrd1(self.get_input('p_transposenrrd1'))
    if self.has_input('p_transposenrrd2') :
      p.set_p_transposenrrd2(self.get_input('p_transposenrrd2'))
    if self.has_input('p_transposenrrd3') :
      p.set_p_transposenrrd3(self.get_input('p_transposenrrd3'))
    if self.has_input('p_transposenrrd4') :
      p.set_p_transposenrrd4(self.get_input('p_transposenrrd4'))
    if self.has_input('p_transposenrrd5') :
      p.set_p_transposenrrd5(self.get_input('p_transposenrrd5'))
    if self.has_input('p_transposenrrd6') :
      p.set_p_transposenrrd6(self.get_input('p_transposenrrd6'))
    if self.has_input('p_nrrd_selection') :
      p.set_p_nrrd_selection(self.get_input('p_nrrd_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('nrrd1', results[1])
    self.set_output('nrrd2', results[2])
    self.set_output('nrrd3', results[3])
    self.set_output('nrrd4', results[4])
    self.set_output('nrrd5', results[5])
    self.set_output('nrrd6', results[6])

class GetMatricesFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetMatricesFromBundleAlg()
    if self.has_input('p_matrix1_name') :
      p.set_p_matrix1_name(self.get_input('p_matrix1_name'))
    if self.has_input('p_matrix2_name') :
      p.set_p_matrix2_name(self.get_input('p_matrix2_name'))
    if self.has_input('p_matrix3_name') :
      p.set_p_matrix3_name(self.get_input('p_matrix3_name'))
    if self.has_input('p_matrix4_name') :
      p.set_p_matrix4_name(self.get_input('p_matrix4_name'))
    if self.has_input('p_matrix5_name') :
      p.set_p_matrix5_name(self.get_input('p_matrix5_name'))
    if self.has_input('p_matrix6_name') :
      p.set_p_matrix6_name(self.get_input('p_matrix6_name'))
    if self.has_input('p_transposenrrd1') :
      p.set_p_transposenrrd1(self.get_input('p_transposenrrd1'))
    if self.has_input('p_transposenrrd2') :
      p.set_p_transposenrrd2(self.get_input('p_transposenrrd2'))
    if self.has_input('p_transposenrrd3') :
      p.set_p_transposenrrd3(self.get_input('p_transposenrrd3'))
    if self.has_input('p_transposenrrd4') :
      p.set_p_transposenrrd4(self.get_input('p_transposenrrd4'))
    if self.has_input('p_transposenrrd5') :
      p.set_p_transposenrrd5(self.get_input('p_transposenrrd5'))
    if self.has_input('p_transposenrrd6') :
      p.set_p_transposenrrd6(self.get_input('p_transposenrrd6'))
    if self.has_input('p_matrix_selection') :
      p.set_p_matrix_selection(self.get_input('p_matrix_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('matrix1', results[1])
    self.set_output('matrix2', results[2])
    self.set_output('matrix3', results[3])
    self.set_output('matrix4', results[4])
    self.set_output('matrix5', results[5])
    self.set_output('matrix6', results[6])

class JoinBundles(Bundle) :
  def compute(self) :
    p = sr_py.JoinBundlesAlg()
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results)

class ReportBundleInfo(Bundle) :
  def compute(self) :
    p = sr_py.ReportBundleInfoAlg()
    if self.has_input('p_tclinfostring') :
      p.set_p_tclinfostring(self.get_input('p_tclinfostring'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)

class InsertPathsIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertPathsIntoBundleAlg()
    if self.has_input('p_path1_name') :
      p.set_p_path1_name(self.get_input('p_path1_name'))
    if self.has_input('p_path2_name') :
      p.set_p_path2_name(self.get_input('p_path2_name'))
    if self.has_input('p_path3_name') :
      p.set_p_path3_name(self.get_input('p_path3_name'))
    if self.has_input('p_path4_name') :
      p.set_p_path4_name(self.get_input('p_path4_name'))
    if self.has_input('p_path5_name') :
      p.set_p_path5_name(self.get_input('p_path5_name'))
    if self.has_input('p_path6_name') :
      p.set_p_path6_name(self.get_input('p_path6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    path1 = 0
    if self.has_input('path1') :
      path1 = self.get_input('path1')
    path2 = 0
    if self.has_input('path2') :
      path2 = self.get_input('path2')
    path3 = 0
    if self.has_input('path3') :
      path3 = self.get_input('path3')
    path4 = 0
    if self.has_input('path4') :
      path4 = self.get_input('path4')
    path5 = 0
    if self.has_input('path5') :
      path5 = self.get_input('path5')
    path6 = 0
    if self.has_input('path6') :
      path6 = self.get_input('path6')
    results = p.execute(bundle, path1, path2, path3, path4, path5, path6)
    self.set_output('bundle', results)

class GetColorMap2sFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetColorMap2sFromBundleAlg()
    if self.has_input('p_colormap21_name') :
      p.set_p_colormap21_name(self.get_input('p_colormap21_name'))
    if self.has_input('p_colormap22_name') :
      p.set_p_colormap22_name(self.get_input('p_colormap22_name'))
    if self.has_input('p_colormap23_name') :
      p.set_p_colormap23_name(self.get_input('p_colormap23_name'))
    if self.has_input('p_colormap24_name') :
      p.set_p_colormap24_name(self.get_input('p_colormap24_name'))
    if self.has_input('p_colormap25_name') :
      p.set_p_colormap25_name(self.get_input('p_colormap25_name'))
    if self.has_input('p_colormap26_name') :
      p.set_p_colormap26_name(self.get_input('p_colormap26_name'))
    if self.has_input('p_colormap2_selection') :
      p.set_p_colormap2_selection(self.get_input('p_colormap2_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('colormap21', results[1])
    self.set_output('colormap22', results[2])
    self.set_output('colormap23', results[3])
    self.set_output('colormap24', results[4])
    self.set_output('colormap25', results[5])
    self.set_output('colormap26', results[6])

class InsertMatricesIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertMatricesIntoBundleAlg()
    if self.has_input('p_matrix1_name') :
      p.set_p_matrix1_name(self.get_input('p_matrix1_name'))
    if self.has_input('p_matrix2_name') :
      p.set_p_matrix2_name(self.get_input('p_matrix2_name'))
    if self.has_input('p_matrix3_name') :
      p.set_p_matrix3_name(self.get_input('p_matrix3_name'))
    if self.has_input('p_matrix4_name') :
      p.set_p_matrix4_name(self.get_input('p_matrix4_name'))
    if self.has_input('p_matrix5_name') :
      p.set_p_matrix5_name(self.get_input('p_matrix5_name'))
    if self.has_input('p_matrix6_name') :
      p.set_p_matrix6_name(self.get_input('p_matrix6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    matrix1 = 0
    if self.has_input('matrix1') :
      matrix1 = self.get_input('matrix1')
    matrix2 = 0
    if self.has_input('matrix2') :
      matrix2 = self.get_input('matrix2')
    matrix3 = 0
    if self.has_input('matrix3') :
      matrix3 = self.get_input('matrix3')
    matrix4 = 0
    if self.has_input('matrix4') :
      matrix4 = self.get_input('matrix4')
    matrix5 = 0
    if self.has_input('matrix5') :
      matrix5 = self.get_input('matrix5')
    matrix6 = 0
    if self.has_input('matrix6') :
      matrix6 = self.get_input('matrix6')
    results = p.execute(bundle, matrix1, matrix2, matrix3, matrix4, matrix5, matrix6)
    self.set_output('bundle', results)

class InsertNrrdsIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertNrrdsIntoBundleAlg()
    if self.has_input('p_nrrd1_name') :
      p.set_p_nrrd1_name(self.get_input('p_nrrd1_name'))
    if self.has_input('p_nrrd2_name') :
      p.set_p_nrrd2_name(self.get_input('p_nrrd2_name'))
    if self.has_input('p_nrrd3_name') :
      p.set_p_nrrd3_name(self.get_input('p_nrrd3_name'))
    if self.has_input('p_nrrd4_name') :
      p.set_p_nrrd4_name(self.get_input('p_nrrd4_name'))
    if self.has_input('p_nrrd5_name') :
      p.set_p_nrrd5_name(self.get_input('p_nrrd5_name'))
    if self.has_input('p_nrrd6_name') :
      p.set_p_nrrd6_name(self.get_input('p_nrrd6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    nrrd1 = 0
    if self.has_input('nrrd1') :
      nrrd1 = self.get_input('nrrd1')
    nrrd2 = 0
    if self.has_input('nrrd2') :
      nrrd2 = self.get_input('nrrd2')
    nrrd3 = 0
    if self.has_input('nrrd3') :
      nrrd3 = self.get_input('nrrd3')
    nrrd4 = 0
    if self.has_input('nrrd4') :
      nrrd4 = self.get_input('nrrd4')
    nrrd5 = 0
    if self.has_input('nrrd5') :
      nrrd5 = self.get_input('nrrd5')
    nrrd6 = 0
    if self.has_input('nrrd6') :
      nrrd6 = self.get_input('nrrd6')
    results = p.execute(bundle, nrrd1, nrrd2, nrrd3, nrrd4, nrrd5, nrrd6)
    self.set_output('bundle', results)

class InsertBundlesIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertBundlesIntoBundleAlg()
    if self.has_input('p_bundle1_name') :
      p.set_p_bundle1_name(self.get_input('p_bundle1_name'))
    if self.has_input('p_bundle2_name') :
      p.set_p_bundle2_name(self.get_input('p_bundle2_name'))
    if self.has_input('p_bundle3_name') :
      p.set_p_bundle3_name(self.get_input('p_bundle3_name'))
    if self.has_input('p_bundle4_name') :
      p.set_p_bundle4_name(self.get_input('p_bundle4_name'))
    if self.has_input('p_bundle5_name') :
      p.set_p_bundle5_name(self.get_input('p_bundle5_name'))
    if self.has_input('p_bundle6_name') :
      p.set_p_bundle6_name(self.get_input('p_bundle6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    bundle1 = 0
    if self.has_input('bundle1') :
      bundle1 = self.get_input('bundle1')
    bundle2 = 0
    if self.has_input('bundle2') :
      bundle2 = self.get_input('bundle2')
    bundle3 = 0
    if self.has_input('bundle3') :
      bundle3 = self.get_input('bundle3')
    bundle4 = 0
    if self.has_input('bundle4') :
      bundle4 = self.get_input('bundle4')
    bundle5 = 0
    if self.has_input('bundle5') :
      bundle5 = self.get_input('bundle5')
    bundle6 = 0
    if self.has_input('bundle6') :
      bundle6 = self.get_input('bundle6')
    results = p.execute(bundle, bundle1, bundle2, bundle3, bundle4, bundle5, bundle6)
    self.set_output('bundle', results)

class GetStringsFromBundle(Bundle) :
  def compute(self) :
    p = sr_py.GetStringsFromBundleAlg()
    if self.has_input('p_string1_name') :
      p.set_p_string1_name(self.get_input('p_string1_name'))
    if self.has_input('p_string2_name') :
      p.set_p_string2_name(self.get_input('p_string2_name'))
    if self.has_input('p_string3_name') :
      p.set_p_string3_name(self.get_input('p_string3_name'))
    if self.has_input('p_string4_name') :
      p.set_p_string4_name(self.get_input('p_string4_name'))
    if self.has_input('p_string5_name') :
      p.set_p_string5_name(self.get_input('p_string5_name'))
    if self.has_input('p_string6_name') :
      p.set_p_string6_name(self.get_input('p_string6_name'))
    if self.has_input('p_string_selection') :
      p.set_p_string_selection(self.get_input('p_string_selection'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    results = p.execute(bundle)
    self.set_output('bundle', results[0])
    self.set_output('string1', results[1])
    self.set_output('string2', results[2])
    self.set_output('string3', results[3])
    self.set_output('string4', results[4])
    self.set_output('string5', results[5])
    self.set_output('string6', results[6])

class InsertColorMapsIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertColorMapsIntoBundleAlg()
    if self.has_input('p_colormap1_name') :
      p.set_p_colormap1_name(self.get_input('p_colormap1_name'))
    if self.has_input('p_colormap2_name') :
      p.set_p_colormap2_name(self.get_input('p_colormap2_name'))
    if self.has_input('p_colormap3_name') :
      p.set_p_colormap3_name(self.get_input('p_colormap3_name'))
    if self.has_input('p_colormap4_name') :
      p.set_p_colormap4_name(self.get_input('p_colormap4_name'))
    if self.has_input('p_colormap5_name') :
      p.set_p_colormap5_name(self.get_input('p_colormap5_name'))
    if self.has_input('p_colormap6_name') :
      p.set_p_colormap6_name(self.get_input('p_colormap6_name'))
    if self.has_input('p_replace1') :
      p.set_p_replace1(self.get_input('p_replace1'))
    if self.has_input('p_replace2') :
      p.set_p_replace2(self.get_input('p_replace2'))
    if self.has_input('p_replace3') :
      p.set_p_replace3(self.get_input('p_replace3'))
    if self.has_input('p_replace4') :
      p.set_p_replace4(self.get_input('p_replace4'))
    if self.has_input('p_replace5') :
      p.set_p_replace5(self.get_input('p_replace5'))
    if self.has_input('p_replace6') :
      p.set_p_replace6(self.get_input('p_replace6'))
    if self.has_input('p_bundlename') :
      p.set_p_bundlename(self.get_input('p_bundlename'))
    bundle = 0
    if self.has_input('bundle') :
      bundle = self.get_input('bundle')
    colormap1 = 0
    if self.has_input('colormap1') :
      colormap1 = self.get_input('colormap1')
    colormap2 = 0
    if self.has_input('colormap2') :
      colormap2 = self.get_input('colormap2')
    colormap3 = 0
    if self.has_input('colormap3') :
      colormap3 = self.get_input('colormap3')
    colormap4 = 0
    if self.has_input('colormap4') :
      colormap4 = self.get_input('colormap4')
    colormap5 = 0
    if self.has_input('colormap5') :
      colormap5 = self.get_input('colormap5')
    colormap6 = 0
    if self.has_input('colormap6') :
      colormap6 = self.get_input('colormap6')
    results = p.execute(bundle, colormap1, colormap2, colormap3, colormap4, colormap5, colormap6)
    self.set_output('bundle', results)

class CreateParameterBundle(Bundle) :
  def compute(self) :
    p = sr_py.CreateParameterBundleAlg()
    if self.has_input('p_data') :
      p.set_p_data(self.get_input('p_data'))
    if self.has_input('p_new_field_count') :
      p.set_p_new_field_count(self.get_input('p_new_field_count'))
    if self.has_input('p_update_all') :
      p.set_p_update_all(self.get_input('p_update_all'))
    results = p.execute()
    self.set_output('ParameterList', results)

class InsertEnvironmentIntoBundle(Bundle) :
  def compute(self) :
    p = sr_py.InsertEnvironmentIntoBundleAlg()
    results = p.execute()
    self.set_output('Environment', results)

class ShowColorMap(Visualization) :
  def compute(self) :
    p = sr_py.ShowColorMapAlg()
    if self.has_input('p_length') :
      p.set_p_length(self.get_input('p_length'))
    if self.has_input('p_side') :
      p.set_p_side(self.get_input('p_side'))
    if self.has_input('p_numlabels') :
      p.set_p_numlabels(self.get_input('p_numlabels'))
    if self.has_input('p_scale') :
      p.set_p_scale(self.get_input('p_scale'))
    if self.has_input('p_numsigdigits') :
      p.set_p_numsigdigits(self.get_input('p_numsigdigits'))
    if self.has_input('p_units') :
      p.set_p_units(self.get_input('p_units'))
    if self.has_input('p_color_r') :
      p.set_p_color_r(self.get_input('p_color_r'))
    if self.has_input('p_color_g') :
      p.set_p_color_g(self.get_input('p_color_g'))
    if self.has_input('p_color_b') :
      p.set_p_color_b(self.get_input('p_color_b'))
    if self.has_input('p_text_fontsize') :
      p.set_p_text_fontsize(self.get_input('p_text_fontsize'))
    if self.has_input('p_extra_padding') :
      p.set_p_extra_padding(self.get_input('p_extra_padding'))
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    results = p.execute(ColorMap)
    self.set_output('Geometry', results)

class CreateAndEditColorMap2D(Visualization) :
  def compute(self) :
    p = sr_py.CreateAndEditColorMap2DAlg()
    if self.has_input('p_histo') :
      p.set_p_histo(self.get_input('p_histo'))
    if self.has_input('p_selected_widget') :
      p.set_p_selected_widget(self.get_input('p_selected_widget'))
    if self.has_input('p_selected_object') :
      p.set_p_selected_object(self.get_input('p_selected_object'))
    if self.has_input('p_num_entries') :
      p.set_p_num_entries(self.get_input('p_num_entries'))
    if self.has_input('p_marker') :
      p.set_p_marker(self.get_input('p_marker'))
    if self.has_input('p_cm2view_targ') :
      p.set_p_cm2view_targ(self.get_input('p_cm2view_targ'))
    if self.has_input('p_id') :
      p.set_p_id(self.get_input('p_id'))
    Input_Colormap = 0
    if self.has_input('Input Colormap') :
      Input_Colormap = self.get_input('Input Colormap')
    Histogram = 0
    if self.has_input('Histogram') :
      Histogram = self.get_input('Histogram')
    results = p.execute(Input_Colormap, Histogram)
    self.set_output('Output Colormap', results)

class ShowField(Visualization) :
  def compute(self) :
    p = sr_py.ShowFieldAlg()
    if self.has_input('p_nodes_on') :
      p.set_p_nodes_on(self.get_input('p_nodes_on'))
    if self.has_input('p_nodes_transparency') :
      p.set_p_nodes_transparency(self.get_input('p_nodes_transparency'))
    if self.has_input('p_nodes_color_type') :
      p.set_p_nodes_color_type(self.get_input('p_nodes_color_type'))
    if self.has_input('p_nodes_display_type') :
      p.set_p_nodes_display_type(self.get_input('p_nodes_display_type'))
    if self.has_input('p_edges_on') :
      p.set_p_edges_on(self.get_input('p_edges_on'))
    if self.has_input('p_edges_transparency') :
      p.set_p_edges_transparency(self.get_input('p_edges_transparency'))
    if self.has_input('p_edges_color_type') :
      p.set_p_edges_color_type(self.get_input('p_edges_color_type'))
    if self.has_input('p_edges_display_type') :
      p.set_p_edges_display_type(self.get_input('p_edges_display_type'))
    if self.has_input('p_faces_on') :
      p.set_p_faces_on(self.get_input('p_faces_on'))
    if self.has_input('p_faces_transparency') :
      p.set_p_faces_transparency(self.get_input('p_faces_transparency'))
    if self.has_input('p_faces_color_type') :
      p.set_p_faces_color_type(self.get_input('p_faces_color_type'))
    if self.has_input('p_faces_normals') :
      p.set_p_faces_normals(self.get_input('p_faces_normals'))
    if self.has_input('p_faces_usetexture') :
      p.set_p_faces_usetexture(self.get_input('p_faces_usetexture'))
    if self.has_input('p_text_on') :
      p.set_p_text_on(self.get_input('p_text_on'))
    if self.has_input('p_text_color_type') :
      p.set_p_text_color_type(self.get_input('p_text_color_type'))
    if self.has_input('p_text_color_r') :
      p.set_p_text_color_r(self.get_input('p_text_color_r'))
    if self.has_input('p_text_color_g') :
      p.set_p_text_color_g(self.get_input('p_text_color_g'))
    if self.has_input('p_text_color_b') :
      p.set_p_text_color_b(self.get_input('p_text_color_b'))
    if self.has_input('p_text_backface_cull') :
      p.set_p_text_backface_cull(self.get_input('p_text_backface_cull'))
    if self.has_input('p_text_always_visible') :
      p.set_p_text_always_visible(self.get_input('p_text_always_visible'))
    if self.has_input('p_text_fontsize') :
      p.set_p_text_fontsize(self.get_input('p_text_fontsize'))
    if self.has_input('p_text_precision') :
      p.set_p_text_precision(self.get_input('p_text_precision'))
    if self.has_input('p_text_render_locations') :
      p.set_p_text_render_locations(self.get_input('p_text_render_locations'))
    if self.has_input('p_text_show_data') :
      p.set_p_text_show_data(self.get_input('p_text_show_data'))
    if self.has_input('p_text_show_nodes') :
      p.set_p_text_show_nodes(self.get_input('p_text_show_nodes'))
    if self.has_input('p_text_show_edges') :
      p.set_p_text_show_edges(self.get_input('p_text_show_edges'))
    if self.has_input('p_text_show_faces') :
      p.set_p_text_show_faces(self.get_input('p_text_show_faces'))
    if self.has_input('p_text_show_cells') :
      p.set_p_text_show_cells(self.get_input('p_text_show_cells'))
    if self.has_input('p_def_color_r') :
      p.set_p_def_color_r(self.get_input('p_def_color_r'))
    if self.has_input('p_def_color_g') :
      p.set_p_def_color_g(self.get_input('p_def_color_g'))
    if self.has_input('p_def_color_b') :
      p.set_p_def_color_b(self.get_input('p_def_color_b'))
    if self.has_input('p_def_color_a') :
      p.set_p_def_color_a(self.get_input('p_def_color_a'))
    if self.has_input('p_nodes_scale') :
      p.set_p_nodes_scale(self.get_input('p_nodes_scale'))
    if self.has_input('p_nodes_scaleNV') :
      p.set_p_nodes_scaleNV(self.get_input('p_nodes_scaleNV'))
    if self.has_input('p_edges_scale') :
      p.set_p_edges_scale(self.get_input('p_edges_scale'))
    if self.has_input('p_edges_scaleNV') :
      p.set_p_edges_scaleNV(self.get_input('p_edges_scaleNV'))
    if self.has_input('p_active_tab') :
      p.set_p_active_tab(self.get_input('p_active_tab'))
    if self.has_input('p_interactive_mode') :
      p.set_p_interactive_mode(self.get_input('p_interactive_mode'))
    if self.has_input('p_show_progress') :
      p.set_p_show_progress(self.get_input('p_show_progress'))
    if self.has_input('p_field_name') :
      p.set_p_field_name(self.get_input('p_field_name'))
    if self.has_input('p_field_name_override') :
      p.set_p_field_name_override(self.get_input('p_field_name_override'))
    if self.has_input('p_nodes_resolution') :
      p.set_p_nodes_resolution(self.get_input('p_nodes_resolution'))
    if self.has_input('p_edges_resolution') :
      p.set_p_edges_resolution(self.get_input('p_edges_resolution'))
    if self.has_input('p_approx_div') :
      p.set_p_approx_div(self.get_input('p_approx_div'))
    if self.has_input('p_use_default_size') :
      p.set_p_use_default_size(self.get_input('p_use_default_size'))
    Mesh = 0
    if self.has_input('Mesh') :
      Mesh = self.get_input('Mesh')
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    results = p.execute(Mesh, ColorMap)
    self.set_output('Scene Graph', results)

class ExtractIsosurface(Visualization) :
  def compute(self) :
    p = sr_py.ExtractIsosurfaceAlg()
    if self.has_input('p_isoval_min') :
      p.set_p_isoval_min(self.get_input('p_isoval_min'))
    if self.has_input('p_isoval_max') :
      p.set_p_isoval_max(self.get_input('p_isoval_max'))
    if self.has_input('p_isoval') :
      p.set_p_isoval(self.get_input('p_isoval'))
    if self.has_input('p_isoval_typed') :
      p.set_p_isoval_typed(self.get_input('p_isoval_typed'))
    if self.has_input('p_isoval_quantity') :
      p.set_p_isoval_quantity(self.get_input('p_isoval_quantity'))
    if self.has_input('p_quantity_range') :
      p.set_p_quantity_range(self.get_input('p_quantity_range'))
    if self.has_input('p_quantity_clusive') :
      p.set_p_quantity_clusive(self.get_input('p_quantity_clusive'))
    if self.has_input('p_quantity_min') :
      p.set_p_quantity_min(self.get_input('p_quantity_min'))
    if self.has_input('p_quantity_max') :
      p.set_p_quantity_max(self.get_input('p_quantity_max'))
    if self.has_input('p_quantity_list') :
      p.set_p_quantity_list(self.get_input('p_quantity_list'))
    if self.has_input('p_isoval_list') :
      p.set_p_isoval_list(self.get_input('p_isoval_list'))
    if self.has_input('p_matrix_list') :
      p.set_p_matrix_list(self.get_input('p_matrix_list'))
    if self.has_input('p_algorithm') :
      p.set_p_algorithm(self.get_input('p_algorithm'))
    if self.has_input('p_build_trisurf') :
      p.set_p_build_trisurf(self.get_input('p_build_trisurf'))
    if self.has_input('p_build_geom') :
      p.set_p_build_geom(self.get_input('p_build_geom'))
    if self.has_input('p_transparency') :
      p.set_p_transparency(self.get_input('p_transparency'))
    if self.has_input('p_np') :
      p.set_p_np(self.get_input('p_np'))
    if self.has_input('p_active_isoval_selection_tab') :
      p.set_p_active_isoval_selection_tab(self.get_input('p_active_isoval_selection_tab'))
    if self.has_input('p_active_tab') :
      p.set_p_active_tab(self.get_input('p_active_tab'))
    if self.has_input('p_update_type') :
      p.set_p_update_type(self.get_input('p_update_type'))
    if self.has_input('p_color_r') :
      p.set_p_color_r(self.get_input('p_color_r'))
    if self.has_input('p_color_g') :
      p.set_p_color_g(self.get_input('p_color_g'))
    if self.has_input('p_color_b') :
      p.set_p_color_b(self.get_input('p_color_b'))
    if self.has_input('p_color_a') :
      p.set_p_color_a(self.get_input('p_color_a'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    Optional_Color_Map = 0
    if self.has_input('Optional Color Map') :
      Optional_Color_Map = self.get_input('Optional Color Map')
    Optional_Isovalues = 0
    if self.has_input('Optional Isovalues') :
      Optional_Isovalues = self.get_input('Optional Isovalues')
    results = p.execute(Field, Optional_Color_Map, Optional_Isovalues)
    self.set_output('Surface', results[0])
    self.set_output('Geometry', results[1])
    self.set_output('Mapping', results[2])

class CreateViewerAxes(Visualization) :
  def compute(self) :
    p = sr_py.CreateViewerAxesAlg()
    if self.has_input('p_precision') :
      p.set_p_precision(self.get_input('p_precision'))
    if self.has_input('p_squash') :
      p.set_p_squash(self.get_input('p_squash'))
    if self.has_input('p_valuerez') :
      p.set_p_valuerez(self.get_input('p_valuerez'))
    if self.has_input('p_labelrez') :
      p.set_p_labelrez(self.get_input('p_labelrez'))
    if self.has_input('p_Plane_01_0_Axis_absolute') :
      p.set_p_Plane_01_0_Axis_absolute(self.get_input('p_Plane_01_0_Axis_absolute'))
    if self.has_input('p_Plane_01_0_Axis_divisions') :
      p.set_p_Plane_01_0_Axis_divisions(self.get_input('p_Plane_01_0_Axis_divisions'))
    if self.has_input('p_Plane_01_0_Axis_offset') :
      p.set_p_Plane_01_0_Axis_offset(self.get_input('p_Plane_01_0_Axis_offset'))
    if self.has_input('p_Plane_01_0_Axis_range_first') :
      p.set_p_Plane_01_0_Axis_range_first(self.get_input('p_Plane_01_0_Axis_range_first'))
    if self.has_input('p_Plane_01_0_Axis_range_second') :
      p.set_p_Plane_01_0_Axis_range_second(self.get_input('p_Plane_01_0_Axis_range_second'))
    if self.has_input('p_Plane_01_0_Axis_min_absolute') :
      p.set_p_Plane_01_0_Axis_min_absolute(self.get_input('p_Plane_01_0_Axis_min_absolute'))
    if self.has_input('p_Plane_01_0_Axis_max_absolute') :
      p.set_p_Plane_01_0_Axis_max_absolute(self.get_input('p_Plane_01_0_Axis_max_absolute'))
    if self.has_input('p_Plane_01_0_Axis_minplane') :
      p.set_p_Plane_01_0_Axis_minplane(self.get_input('p_Plane_01_0_Axis_minplane'))
    if self.has_input('p_Plane_01_0_Axis_maxplane') :
      p.set_p_Plane_01_0_Axis_maxplane(self.get_input('p_Plane_01_0_Axis_maxplane'))
    if self.has_input('p_Plane_01_0_Axis_lines') :
      p.set_p_Plane_01_0_Axis_lines(self.get_input('p_Plane_01_0_Axis_lines'))
    if self.has_input('p_Plane_01_0_Axis_minticks') :
      p.set_p_Plane_01_0_Axis_minticks(self.get_input('p_Plane_01_0_Axis_minticks'))
    if self.has_input('p_Plane_01_0_Axis_maxticks') :
      p.set_p_Plane_01_0_Axis_maxticks(self.get_input('p_Plane_01_0_Axis_maxticks'))
    if self.has_input('p_Plane_01_0_Axis_minlabel') :
      p.set_p_Plane_01_0_Axis_minlabel(self.get_input('p_Plane_01_0_Axis_minlabel'))
    if self.has_input('p_Plane_01_0_Axis_maxlabel') :
      p.set_p_Plane_01_0_Axis_maxlabel(self.get_input('p_Plane_01_0_Axis_maxlabel'))
    if self.has_input('p_Plane_01_0_Axis_minvalue') :
      p.set_p_Plane_01_0_Axis_minvalue(self.get_input('p_Plane_01_0_Axis_minvalue'))
    if self.has_input('p_Plane_01_0_Axis_maxvalue') :
      p.set_p_Plane_01_0_Axis_maxvalue(self.get_input('p_Plane_01_0_Axis_maxvalue'))
    if self.has_input('p_Plane_01_0_Axis_width') :
      p.set_p_Plane_01_0_Axis_width(self.get_input('p_Plane_01_0_Axis_width'))
    if self.has_input('p_Plane_01_0_Axis_tickangle') :
      p.set_p_Plane_01_0_Axis_tickangle(self.get_input('p_Plane_01_0_Axis_tickangle'))
    if self.has_input('p_Plane_01_0_Axis_ticktilt') :
      p.set_p_Plane_01_0_Axis_ticktilt(self.get_input('p_Plane_01_0_Axis_ticktilt'))
    if self.has_input('p_Plane_01_0_Axis_ticksize') :
      p.set_p_Plane_01_0_Axis_ticksize(self.get_input('p_Plane_01_0_Axis_ticksize'))
    if self.has_input('p_Plane_01_0_Axis_labelangle') :
      p.set_p_Plane_01_0_Axis_labelangle(self.get_input('p_Plane_01_0_Axis_labelangle'))
    if self.has_input('p_Plane_01_0_Axis_labelheight') :
      p.set_p_Plane_01_0_Axis_labelheight(self.get_input('p_Plane_01_0_Axis_labelheight'))
    if self.has_input('p_Plane_01_0_Axis_valuesize') :
      p.set_p_Plane_01_0_Axis_valuesize(self.get_input('p_Plane_01_0_Axis_valuesize'))
    if self.has_input('p_Plane_01_0_Axis_valuesquash') :
      p.set_p_Plane_01_0_Axis_valuesquash(self.get_input('p_Plane_01_0_Axis_valuesquash'))
    if self.has_input('p_Plane_01_1_Axis_absolute') :
      p.set_p_Plane_01_1_Axis_absolute(self.get_input('p_Plane_01_1_Axis_absolute'))
    if self.has_input('p_Plane_01_1_Axis_divisions') :
      p.set_p_Plane_01_1_Axis_divisions(self.get_input('p_Plane_01_1_Axis_divisions'))
    if self.has_input('p_Plane_01_1_Axis_offset') :
      p.set_p_Plane_01_1_Axis_offset(self.get_input('p_Plane_01_1_Axis_offset'))
    if self.has_input('p_Plane_01_1_Axis_range_first') :
      p.set_p_Plane_01_1_Axis_range_first(self.get_input('p_Plane_01_1_Axis_range_first'))
    if self.has_input('p_Plane_01_1_Axis_range_second') :
      p.set_p_Plane_01_1_Axis_range_second(self.get_input('p_Plane_01_1_Axis_range_second'))
    if self.has_input('p_Plane_01_1_Axis_min_absolute') :
      p.set_p_Plane_01_1_Axis_min_absolute(self.get_input('p_Plane_01_1_Axis_min_absolute'))
    if self.has_input('p_Plane_01_1_Axis_max_absolute') :
      p.set_p_Plane_01_1_Axis_max_absolute(self.get_input('p_Plane_01_1_Axis_max_absolute'))
    if self.has_input('p_Plane_01_1_Axis_minplane') :
      p.set_p_Plane_01_1_Axis_minplane(self.get_input('p_Plane_01_1_Axis_minplane'))
    if self.has_input('p_Plane_01_1_Axis_maxplane') :
      p.set_p_Plane_01_1_Axis_maxplane(self.get_input('p_Plane_01_1_Axis_maxplane'))
    if self.has_input('p_Plane_01_1_Axis_lines') :
      p.set_p_Plane_01_1_Axis_lines(self.get_input('p_Plane_01_1_Axis_lines'))
    if self.has_input('p_Plane_01_1_Axis_minticks') :
      p.set_p_Plane_01_1_Axis_minticks(self.get_input('p_Plane_01_1_Axis_minticks'))
    if self.has_input('p_Plane_01_1_Axis_maxticks') :
      p.set_p_Plane_01_1_Axis_maxticks(self.get_input('p_Plane_01_1_Axis_maxticks'))
    if self.has_input('p_Plane_01_1_Axis_minlabel') :
      p.set_p_Plane_01_1_Axis_minlabel(self.get_input('p_Plane_01_1_Axis_minlabel'))
    if self.has_input('p_Plane_01_1_Axis_maxlabel') :
      p.set_p_Plane_01_1_Axis_maxlabel(self.get_input('p_Plane_01_1_Axis_maxlabel'))
    if self.has_input('p_Plane_01_1_Axis_minvalue') :
      p.set_p_Plane_01_1_Axis_minvalue(self.get_input('p_Plane_01_1_Axis_minvalue'))
    if self.has_input('p_Plane_01_1_Axis_maxvalue') :
      p.set_p_Plane_01_1_Axis_maxvalue(self.get_input('p_Plane_01_1_Axis_maxvalue'))
    if self.has_input('p_Plane_01_1_Axis_width') :
      p.set_p_Plane_01_1_Axis_width(self.get_input('p_Plane_01_1_Axis_width'))
    if self.has_input('p_Plane_01_1_Axis_tickangle') :
      p.set_p_Plane_01_1_Axis_tickangle(self.get_input('p_Plane_01_1_Axis_tickangle'))
    if self.has_input('p_Plane_01_1_Axis_ticktilt') :
      p.set_p_Plane_01_1_Axis_ticktilt(self.get_input('p_Plane_01_1_Axis_ticktilt'))
    if self.has_input('p_Plane_01_1_Axis_ticksize') :
      p.set_p_Plane_01_1_Axis_ticksize(self.get_input('p_Plane_01_1_Axis_ticksize'))
    if self.has_input('p_Plane_01_1_Axis_labelangle') :
      p.set_p_Plane_01_1_Axis_labelangle(self.get_input('p_Plane_01_1_Axis_labelangle'))
    if self.has_input('p_Plane_01_1_Axis_labelheight') :
      p.set_p_Plane_01_1_Axis_labelheight(self.get_input('p_Plane_01_1_Axis_labelheight'))
    if self.has_input('p_Plane_01_1_Axis_valuesize') :
      p.set_p_Plane_01_1_Axis_valuesize(self.get_input('p_Plane_01_1_Axis_valuesize'))
    if self.has_input('p_Plane_01_1_Axis_valuesquash') :
      p.set_p_Plane_01_1_Axis_valuesquash(self.get_input('p_Plane_01_1_Axis_valuesquash'))
    if self.has_input('p_Plane_02_0_Axis_absolute') :
      p.set_p_Plane_02_0_Axis_absolute(self.get_input('p_Plane_02_0_Axis_absolute'))
    if self.has_input('p_Plane_02_0_Axis_divisions') :
      p.set_p_Plane_02_0_Axis_divisions(self.get_input('p_Plane_02_0_Axis_divisions'))
    if self.has_input('p_Plane_02_0_Axis_offset') :
      p.set_p_Plane_02_0_Axis_offset(self.get_input('p_Plane_02_0_Axis_offset'))
    if self.has_input('p_Plane_02_0_Axis_range_first') :
      p.set_p_Plane_02_0_Axis_range_first(self.get_input('p_Plane_02_0_Axis_range_first'))
    if self.has_input('p_Plane_02_0_Axis_range_second') :
      p.set_p_Plane_02_0_Axis_range_second(self.get_input('p_Plane_02_0_Axis_range_second'))
    if self.has_input('p_Plane_02_0_Axis_min_absolute') :
      p.set_p_Plane_02_0_Axis_min_absolute(self.get_input('p_Plane_02_0_Axis_min_absolute'))
    if self.has_input('p_Plane_02_0_Axis_max_absolute') :
      p.set_p_Plane_02_0_Axis_max_absolute(self.get_input('p_Plane_02_0_Axis_max_absolute'))
    if self.has_input('p_Plane_02_0_Axis_minplane') :
      p.set_p_Plane_02_0_Axis_minplane(self.get_input('p_Plane_02_0_Axis_minplane'))
    if self.has_input('p_Plane_02_0_Axis_maxplane') :
      p.set_p_Plane_02_0_Axis_maxplane(self.get_input('p_Plane_02_0_Axis_maxplane'))
    if self.has_input('p_Plane_02_0_Axis_lines') :
      p.set_p_Plane_02_0_Axis_lines(self.get_input('p_Plane_02_0_Axis_lines'))
    if self.has_input('p_Plane_02_0_Axis_minticks') :
      p.set_p_Plane_02_0_Axis_minticks(self.get_input('p_Plane_02_0_Axis_minticks'))
    if self.has_input('p_Plane_02_0_Axis_maxticks') :
      p.set_p_Plane_02_0_Axis_maxticks(self.get_input('p_Plane_02_0_Axis_maxticks'))
    if self.has_input('p_Plane_02_0_Axis_minlabel') :
      p.set_p_Plane_02_0_Axis_minlabel(self.get_input('p_Plane_02_0_Axis_minlabel'))
    if self.has_input('p_Plane_02_0_Axis_maxlabel') :
      p.set_p_Plane_02_0_Axis_maxlabel(self.get_input('p_Plane_02_0_Axis_maxlabel'))
    if self.has_input('p_Plane_02_0_Axis_minvalue') :
      p.set_p_Plane_02_0_Axis_minvalue(self.get_input('p_Plane_02_0_Axis_minvalue'))
    if self.has_input('p_Plane_02_0_Axis_maxvalue') :
      p.set_p_Plane_02_0_Axis_maxvalue(self.get_input('p_Plane_02_0_Axis_maxvalue'))
    if self.has_input('p_Plane_02_0_Axis_width') :
      p.set_p_Plane_02_0_Axis_width(self.get_input('p_Plane_02_0_Axis_width'))
    if self.has_input('p_Plane_02_0_Axis_tickangle') :
      p.set_p_Plane_02_0_Axis_tickangle(self.get_input('p_Plane_02_0_Axis_tickangle'))
    if self.has_input('p_Plane_02_0_Axis_ticktilt') :
      p.set_p_Plane_02_0_Axis_ticktilt(self.get_input('p_Plane_02_0_Axis_ticktilt'))
    if self.has_input('p_Plane_02_0_Axis_ticksize') :
      p.set_p_Plane_02_0_Axis_ticksize(self.get_input('p_Plane_02_0_Axis_ticksize'))
    if self.has_input('p_Plane_02_0_Axis_labelangle') :
      p.set_p_Plane_02_0_Axis_labelangle(self.get_input('p_Plane_02_0_Axis_labelangle'))
    if self.has_input('p_Plane_02_0_Axis_labelheight') :
      p.set_p_Plane_02_0_Axis_labelheight(self.get_input('p_Plane_02_0_Axis_labelheight'))
    if self.has_input('p_Plane_02_0_Axis_valuesize') :
      p.set_p_Plane_02_0_Axis_valuesize(self.get_input('p_Plane_02_0_Axis_valuesize'))
    if self.has_input('p_Plane_02_0_Axis_valuesquash') :
      p.set_p_Plane_02_0_Axis_valuesquash(self.get_input('p_Plane_02_0_Axis_valuesquash'))
    if self.has_input('p_Plane_02_2_Axis_absolute') :
      p.set_p_Plane_02_2_Axis_absolute(self.get_input('p_Plane_02_2_Axis_absolute'))
    if self.has_input('p_Plane_02_2_Axis_divisions') :
      p.set_p_Plane_02_2_Axis_divisions(self.get_input('p_Plane_02_2_Axis_divisions'))
    if self.has_input('p_Plane_02_2_Axis_offset') :
      p.set_p_Plane_02_2_Axis_offset(self.get_input('p_Plane_02_2_Axis_offset'))
    if self.has_input('p_Plane_02_2_Axis_range_first') :
      p.set_p_Plane_02_2_Axis_range_first(self.get_input('p_Plane_02_2_Axis_range_first'))
    if self.has_input('p_Plane_02_2_Axis_range_second') :
      p.set_p_Plane_02_2_Axis_range_second(self.get_input('p_Plane_02_2_Axis_range_second'))
    if self.has_input('p_Plane_02_2_Axis_min_absolute') :
      p.set_p_Plane_02_2_Axis_min_absolute(self.get_input('p_Plane_02_2_Axis_min_absolute'))
    if self.has_input('p_Plane_02_2_Axis_max_absolute') :
      p.set_p_Plane_02_2_Axis_max_absolute(self.get_input('p_Plane_02_2_Axis_max_absolute'))
    if self.has_input('p_Plane_02_2_Axis_minplane') :
      p.set_p_Plane_02_2_Axis_minplane(self.get_input('p_Plane_02_2_Axis_minplane'))
    if self.has_input('p_Plane_02_2_Axis_maxplane') :
      p.set_p_Plane_02_2_Axis_maxplane(self.get_input('p_Plane_02_2_Axis_maxplane'))
    if self.has_input('p_Plane_02_2_Axis_lines') :
      p.set_p_Plane_02_2_Axis_lines(self.get_input('p_Plane_02_2_Axis_lines'))
    if self.has_input('p_Plane_02_2_Axis_minticks') :
      p.set_p_Plane_02_2_Axis_minticks(self.get_input('p_Plane_02_2_Axis_minticks'))
    if self.has_input('p_Plane_02_2_Axis_maxticks') :
      p.set_p_Plane_02_2_Axis_maxticks(self.get_input('p_Plane_02_2_Axis_maxticks'))
    if self.has_input('p_Plane_02_2_Axis_minlabel') :
      p.set_p_Plane_02_2_Axis_minlabel(self.get_input('p_Plane_02_2_Axis_minlabel'))
    if self.has_input('p_Plane_02_2_Axis_maxlabel') :
      p.set_p_Plane_02_2_Axis_maxlabel(self.get_input('p_Plane_02_2_Axis_maxlabel'))
    if self.has_input('p_Plane_02_2_Axis_minvalue') :
      p.set_p_Plane_02_2_Axis_minvalue(self.get_input('p_Plane_02_2_Axis_minvalue'))
    if self.has_input('p_Plane_02_2_Axis_maxvalue') :
      p.set_p_Plane_02_2_Axis_maxvalue(self.get_input('p_Plane_02_2_Axis_maxvalue'))
    if self.has_input('p_Plane_02_2_Axis_width') :
      p.set_p_Plane_02_2_Axis_width(self.get_input('p_Plane_02_2_Axis_width'))
    if self.has_input('p_Plane_02_2_Axis_tickangle') :
      p.set_p_Plane_02_2_Axis_tickangle(self.get_input('p_Plane_02_2_Axis_tickangle'))
    if self.has_input('p_Plane_02_2_Axis_ticktilt') :
      p.set_p_Plane_02_2_Axis_ticktilt(self.get_input('p_Plane_02_2_Axis_ticktilt'))
    if self.has_input('p_Plane_02_2_Axis_ticksize') :
      p.set_p_Plane_02_2_Axis_ticksize(self.get_input('p_Plane_02_2_Axis_ticksize'))
    if self.has_input('p_Plane_02_2_Axis_labelangle') :
      p.set_p_Plane_02_2_Axis_labelangle(self.get_input('p_Plane_02_2_Axis_labelangle'))
    if self.has_input('p_Plane_02_2_Axis_labelheight') :
      p.set_p_Plane_02_2_Axis_labelheight(self.get_input('p_Plane_02_2_Axis_labelheight'))
    if self.has_input('p_Plane_02_2_Axis_valuesize') :
      p.set_p_Plane_02_2_Axis_valuesize(self.get_input('p_Plane_02_2_Axis_valuesize'))
    if self.has_input('p_Plane_02_2_Axis_valuesquash') :
      p.set_p_Plane_02_2_Axis_valuesquash(self.get_input('p_Plane_02_2_Axis_valuesquash'))
    if self.has_input('p_Plane_12_1_Axis_absolute') :
      p.set_p_Plane_12_1_Axis_absolute(self.get_input('p_Plane_12_1_Axis_absolute'))
    if self.has_input('p_Plane_12_1_Axis_divisions') :
      p.set_p_Plane_12_1_Axis_divisions(self.get_input('p_Plane_12_1_Axis_divisions'))
    if self.has_input('p_Plane_12_1_Axis_offset') :
      p.set_p_Plane_12_1_Axis_offset(self.get_input('p_Plane_12_1_Axis_offset'))
    if self.has_input('p_Plane_12_1_Axis_range_first') :
      p.set_p_Plane_12_1_Axis_range_first(self.get_input('p_Plane_12_1_Axis_range_first'))
    if self.has_input('p_Plane_12_1_Axis_range_second') :
      p.set_p_Plane_12_1_Axis_range_second(self.get_input('p_Plane_12_1_Axis_range_second'))
    if self.has_input('p_Plane_12_1_Axis_min_absolute') :
      p.set_p_Plane_12_1_Axis_min_absolute(self.get_input('p_Plane_12_1_Axis_min_absolute'))
    if self.has_input('p_Plane_12_1_Axis_max_absolute') :
      p.set_p_Plane_12_1_Axis_max_absolute(self.get_input('p_Plane_12_1_Axis_max_absolute'))
    if self.has_input('p_Plane_12_1_Axis_minplane') :
      p.set_p_Plane_12_1_Axis_minplane(self.get_input('p_Plane_12_1_Axis_minplane'))
    if self.has_input('p_Plane_12_1_Axis_maxplane') :
      p.set_p_Plane_12_1_Axis_maxplane(self.get_input('p_Plane_12_1_Axis_maxplane'))
    if self.has_input('p_Plane_12_1_Axis_lines') :
      p.set_p_Plane_12_1_Axis_lines(self.get_input('p_Plane_12_1_Axis_lines'))
    if self.has_input('p_Plane_12_1_Axis_minticks') :
      p.set_p_Plane_12_1_Axis_minticks(self.get_input('p_Plane_12_1_Axis_minticks'))
    if self.has_input('p_Plane_12_1_Axis_maxticks') :
      p.set_p_Plane_12_1_Axis_maxticks(self.get_input('p_Plane_12_1_Axis_maxticks'))
    if self.has_input('p_Plane_12_1_Axis_minlabel') :
      p.set_p_Plane_12_1_Axis_minlabel(self.get_input('p_Plane_12_1_Axis_minlabel'))
    if self.has_input('p_Plane_12_1_Axis_maxlabel') :
      p.set_p_Plane_12_1_Axis_maxlabel(self.get_input('p_Plane_12_1_Axis_maxlabel'))
    if self.has_input('p_Plane_12_1_Axis_minvalue') :
      p.set_p_Plane_12_1_Axis_minvalue(self.get_input('p_Plane_12_1_Axis_minvalue'))
    if self.has_input('p_Plane_12_1_Axis_maxvalue') :
      p.set_p_Plane_12_1_Axis_maxvalue(self.get_input('p_Plane_12_1_Axis_maxvalue'))
    if self.has_input('p_Plane_12_1_Axis_width') :
      p.set_p_Plane_12_1_Axis_width(self.get_input('p_Plane_12_1_Axis_width'))
    if self.has_input('p_Plane_12_1_Axis_tickangle') :
      p.set_p_Plane_12_1_Axis_tickangle(self.get_input('p_Plane_12_1_Axis_tickangle'))
    if self.has_input('p_Plane_12_1_Axis_ticktilt') :
      p.set_p_Plane_12_1_Axis_ticktilt(self.get_input('p_Plane_12_1_Axis_ticktilt'))
    if self.has_input('p_Plane_12_1_Axis_ticksize') :
      p.set_p_Plane_12_1_Axis_ticksize(self.get_input('p_Plane_12_1_Axis_ticksize'))
    if self.has_input('p_Plane_12_1_Axis_labelangle') :
      p.set_p_Plane_12_1_Axis_labelangle(self.get_input('p_Plane_12_1_Axis_labelangle'))
    if self.has_input('p_Plane_12_1_Axis_labelheight') :
      p.set_p_Plane_12_1_Axis_labelheight(self.get_input('p_Plane_12_1_Axis_labelheight'))
    if self.has_input('p_Plane_12_1_Axis_valuesize') :
      p.set_p_Plane_12_1_Axis_valuesize(self.get_input('p_Plane_12_1_Axis_valuesize'))
    if self.has_input('p_Plane_12_1_Axis_valuesquash') :
      p.set_p_Plane_12_1_Axis_valuesquash(self.get_input('p_Plane_12_1_Axis_valuesquash'))
    if self.has_input('p_Plane_12_2_Axis_absolute') :
      p.set_p_Plane_12_2_Axis_absolute(self.get_input('p_Plane_12_2_Axis_absolute'))
    if self.has_input('p_Plane_12_2_Axis_divisions') :
      p.set_p_Plane_12_2_Axis_divisions(self.get_input('p_Plane_12_2_Axis_divisions'))
    if self.has_input('p_Plane_12_2_Axis_offset') :
      p.set_p_Plane_12_2_Axis_offset(self.get_input('p_Plane_12_2_Axis_offset'))
    if self.has_input('p_Plane_12_2_Axis_range_first') :
      p.set_p_Plane_12_2_Axis_range_first(self.get_input('p_Plane_12_2_Axis_range_first'))
    if self.has_input('p_Plane_12_2_Axis_range_second') :
      p.set_p_Plane_12_2_Axis_range_second(self.get_input('p_Plane_12_2_Axis_range_second'))
    if self.has_input('p_Plane_12_2_Axis_min_absolute') :
      p.set_p_Plane_12_2_Axis_min_absolute(self.get_input('p_Plane_12_2_Axis_min_absolute'))
    if self.has_input('p_Plane_12_2_Axis_max_absolute') :
      p.set_p_Plane_12_2_Axis_max_absolute(self.get_input('p_Plane_12_2_Axis_max_absolute'))
    if self.has_input('p_Plane_12_2_Axis_minplane') :
      p.set_p_Plane_12_2_Axis_minplane(self.get_input('p_Plane_12_2_Axis_minplane'))
    if self.has_input('p_Plane_12_2_Axis_maxplane') :
      p.set_p_Plane_12_2_Axis_maxplane(self.get_input('p_Plane_12_2_Axis_maxplane'))
    if self.has_input('p_Plane_12_2_Axis_lines') :
      p.set_p_Plane_12_2_Axis_lines(self.get_input('p_Plane_12_2_Axis_lines'))
    if self.has_input('p_Plane_12_2_Axis_minticks') :
      p.set_p_Plane_12_2_Axis_minticks(self.get_input('p_Plane_12_2_Axis_minticks'))
    if self.has_input('p_Plane_12_2_Axis_maxticks') :
      p.set_p_Plane_12_2_Axis_maxticks(self.get_input('p_Plane_12_2_Axis_maxticks'))
    if self.has_input('p_Plane_12_2_Axis_minlabel') :
      p.set_p_Plane_12_2_Axis_minlabel(self.get_input('p_Plane_12_2_Axis_minlabel'))
    if self.has_input('p_Plane_12_2_Axis_maxlabel') :
      p.set_p_Plane_12_2_Axis_maxlabel(self.get_input('p_Plane_12_2_Axis_maxlabel'))
    if self.has_input('p_Plane_12_2_Axis_minvalue') :
      p.set_p_Plane_12_2_Axis_minvalue(self.get_input('p_Plane_12_2_Axis_minvalue'))
    if self.has_input('p_Plane_12_2_Axis_maxvalue') :
      p.set_p_Plane_12_2_Axis_maxvalue(self.get_input('p_Plane_12_2_Axis_maxvalue'))
    if self.has_input('p_Plane_12_2_Axis_width') :
      p.set_p_Plane_12_2_Axis_width(self.get_input('p_Plane_12_2_Axis_width'))
    if self.has_input('p_Plane_12_2_Axis_tickangle') :
      p.set_p_Plane_12_2_Axis_tickangle(self.get_input('p_Plane_12_2_Axis_tickangle'))
    if self.has_input('p_Plane_12_2_Axis_ticktilt') :
      p.set_p_Plane_12_2_Axis_ticktilt(self.get_input('p_Plane_12_2_Axis_ticktilt'))
    if self.has_input('p_Plane_12_2_Axis_ticksize') :
      p.set_p_Plane_12_2_Axis_ticksize(self.get_input('p_Plane_12_2_Axis_ticksize'))
    if self.has_input('p_Plane_12_2_Axis_labelangle') :
      p.set_p_Plane_12_2_Axis_labelangle(self.get_input('p_Plane_12_2_Axis_labelangle'))
    if self.has_input('p_Plane_12_2_Axis_labelheight') :
      p.set_p_Plane_12_2_Axis_labelheight(self.get_input('p_Plane_12_2_Axis_labelheight'))
    if self.has_input('p_Plane_12_2_Axis_valuesize') :
      p.set_p_Plane_12_2_Axis_valuesize(self.get_input('p_Plane_12_2_Axis_valuesize'))
    if self.has_input('p_Plane_12_2_Axis_valuesquash') :
      p.set_p_Plane_12_2_Axis_valuesquash(self.get_input('p_Plane_12_2_Axis_valuesquash'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Axes', results)

class RescaleColorMap(Visualization) :
  def compute(self) :
    p = sr_py.RescaleColorMapAlg()
    if self.has_input('p_main_frame') :
      p.set_p_main_frame(self.get_input('p_main_frame'))
    if self.has_input('p_isFixed') :
      p.set_p_isFixed(self.get_input('p_isFixed'))
    if self.has_input('p_min') :
      p.set_p_min(self.get_input('p_min'))
    if self.has_input('p_max') :
      p.set_p_max(self.get_input('p_max'))
    if self.has_input('p_makeSymmetric') :
      p.set_p_makeSymmetric(self.get_input('p_makeSymmetric'))
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(ColorMap, Field)
    self.set_output('ColorMap', results)

class ConvertNrrdsToTexture(Visualization) :
  def compute(self) :
    p = sr_py.ConvertNrrdsToTextureAlg()
    if self.has_input('p_vmin') :
      p.set_p_vmin(self.get_input('p_vmin'))
    if self.has_input('p_vmax') :
      p.set_p_vmax(self.get_input('p_vmax'))
    if self.has_input('p_gmin') :
      p.set_p_gmin(self.get_input('p_gmin'))
    if self.has_input('p_gmax') :
      p.set_p_gmax(self.get_input('p_gmax'))
    if self.has_input('p_mmin') :
      p.set_p_mmin(self.get_input('p_mmin'))
    if self.has_input('p_mmax') :
      p.set_p_mmax(self.get_input('p_mmax'))
    if self.has_input('p_is_fixed') :
      p.set_p_is_fixed(self.get_input('p_is_fixed'))
    if self.has_input('p_card_mem') :
      p.set_p_card_mem(self.get_input('p_card_mem'))
    if self.has_input('p_card_mem_auto') :
      p.set_p_card_mem_auto(self.get_input('p_card_mem_auto'))
    if self.has_input('p_is_uchar') :
      p.set_p_is_uchar(self.get_input('p_is_uchar'))
    if self.has_input('p_histogram') :
      p.set_p_histogram(self.get_input('p_histogram'))
    if self.has_input('p_gamma') :
      p.set_p_gamma(self.get_input('p_gamma'))
    Value_Nrrd = 0
    if self.has_input('Value Nrrd') :
      Value_Nrrd = self.get_input('Value Nrrd')
    Gradient_Magnitude_Nrrd = 0
    if self.has_input('Gradient Magnitude Nrrd') :
      Gradient_Magnitude_Nrrd = self.get_input('Gradient Magnitude Nrrd')
    results = p.execute(Value_Nrrd, Gradient_Magnitude_Nrrd)
    self.set_output('Texture', results[0])
    self.set_output('JointHistoGram', results[1])

class ChooseColorMap(Visualization) :
  def compute(self) :
    p = sr_py.ChooseColorMapAlg()
    if self.has_input('p_use_first_valid') :
      p.set_p_use_first_valid(self.get_input('p_use_first_valid'))
    if self.has_input('p_port_valid_index') :
      p.set_p_port_valid_index(self.get_input('p_port_valid_index'))
    if self.has_input('p_port_selected_index') :
      p.set_p_port_selected_index(self.get_input('p_port_selected_index'))
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    results = p.execute(ColorMap)
    self.set_output('ColorMap', results)

class CreateLightForViewer(Visualization) :
  def compute(self) :
    p = sr_py.CreateLightForViewerAlg()
    if self.has_input('p_control_pos_saved') :
      p.set_p_control_pos_saved(self.get_input('p_control_pos_saved'))
    if self.has_input('p_control_x') :
      p.set_p_control_x(self.get_input('p_control_x'))
    if self.has_input('p_control_y') :
      p.set_p_control_y(self.get_input('p_control_y'))
    if self.has_input('p_control_z') :
      p.set_p_control_z(self.get_input('p_control_z'))
    if self.has_input('p_at_x') :
      p.set_p_at_x(self.get_input('p_at_x'))
    if self.has_input('p_at_y') :
      p.set_p_at_y(self.get_input('p_at_y'))
    if self.has_input('p_at_z') :
      p.set_p_at_z(self.get_input('p_at_z'))
    if self.has_input('p_type') :
      p.set_p_type(self.get_input('p_type'))
    if self.has_input('p_on') :
      p.set_p_on(self.get_input('p_on'))
    results = p.execute()
    self.set_output('Geometry', results)

class ShowTextureVolume(Visualization) :
  def compute(self) :
    p = sr_py.ShowTextureVolumeAlg()
    if self.has_input('p_sampling_rate_hi') :
      p.set_p_sampling_rate_hi(self.get_input('p_sampling_rate_hi'))
    if self.has_input('p_sampling_rate_lo') :
      p.set_p_sampling_rate_lo(self.get_input('p_sampling_rate_lo'))
    if self.has_input('p_gradient_min') :
      p.set_p_gradient_min(self.get_input('p_gradient_min'))
    if self.has_input('p_gradient_max') :
      p.set_p_gradient_max(self.get_input('p_gradient_max'))
    if self.has_input('p_adaptive') :
      p.set_p_adaptive(self.get_input('p_adaptive'))
    if self.has_input('p_cmap_size') :
      p.set_p_cmap_size(self.get_input('p_cmap_size'))
    if self.has_input('p_sw_raster') :
      p.set_p_sw_raster(self.get_input('p_sw_raster'))
    if self.has_input('p_render_style') :
      p.set_p_render_style(self.get_input('p_render_style'))
    if self.has_input('p_alpha_scale') :
      p.set_p_alpha_scale(self.get_input('p_alpha_scale'))
    if self.has_input('p_interp_mode') :
      p.set_p_interp_mode(self.get_input('p_interp_mode'))
    if self.has_input('p_shading') :
      p.set_p_shading(self.get_input('p_shading'))
    if self.has_input('p_ambient') :
      p.set_p_ambient(self.get_input('p_ambient'))
    if self.has_input('p_diffuse') :
      p.set_p_diffuse(self.get_input('p_diffuse'))
    if self.has_input('p_specular') :
      p.set_p_specular(self.get_input('p_specular'))
    if self.has_input('p_shine') :
      p.set_p_shine(self.get_input('p_shine'))
    if self.has_input('p_light') :
      p.set_p_light(self.get_input('p_light'))
    if self.has_input('p_blend_res') :
      p.set_p_blend_res(self.get_input('p_blend_res'))
    if self.has_input('p_multi_level') :
      p.set_p_multi_level(self.get_input('p_multi_level'))
    if self.has_input('p_use_stencil') :
      p.set_p_use_stencil(self.get_input('p_use_stencil'))
    if self.has_input('p_invert_opacity') :
      p.set_p_invert_opacity(self.get_input('p_invert_opacity'))
    if self.has_input('p_num_clipping_planes') :
      p.set_p_num_clipping_planes(self.get_input('p_num_clipping_planes'))
    if self.has_input('p_show_clipping_widgets') :
      p.set_p_show_clipping_widgets(self.get_input('p_show_clipping_widgets'))
    if self.has_input('p_level_on') :
      p.set_p_level_on(self.get_input('p_level_on'))
    if self.has_input('p_level_vals') :
      p.set_p_level_vals(self.get_input('p_level_vals'))
    if self.has_input('p_id') :
      p.set_p_id(self.get_input('p_id'))
    Texture = 0
    if self.has_input('Texture') :
      Texture = self.get_input('Texture')
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    ColorMap2 = 0
    if self.has_input('ColorMap2') :
      ColorMap2 = self.get_input('ColorMap2')
    results = p.execute(Texture, ColorMap, ColorMap2)
    self.set_output('Geometry', results[0])
    self.set_output('ColorMap', results[1])

class ShowFieldGlyphs(Visualization) :
  def compute(self) :
    p = sr_py.ShowFieldGlyphsAlg()
    if self.has_input('p_scalars_has_data') :
      p.set_p_scalars_has_data(self.get_input('p_scalars_has_data'))
    if self.has_input('p_scalars_on') :
      p.set_p_scalars_on(self.get_input('p_scalars_on'))
    if self.has_input('p_scalars_display_type') :
      p.set_p_scalars_display_type(self.get_input('p_scalars_display_type'))
    if self.has_input('p_scalars_transparency') :
      p.set_p_scalars_transparency(self.get_input('p_scalars_transparency'))
    if self.has_input('p_scalars_normalize') :
      p.set_p_scalars_normalize(self.get_input('p_scalars_normalize'))
    if self.has_input('p_scalars_color_type') :
      p.set_p_scalars_color_type(self.get_input('p_scalars_color_type'))
    if self.has_input('p_scalars_resolution') :
      p.set_p_scalars_resolution(self.get_input('p_scalars_resolution'))
    if self.has_input('p_vectors_has_data') :
      p.set_p_vectors_has_data(self.get_input('p_vectors_has_data'))
    if self.has_input('p_vectors_on') :
      p.set_p_vectors_on(self.get_input('p_vectors_on'))
    if self.has_input('p_vectors_display_type') :
      p.set_p_vectors_display_type(self.get_input('p_vectors_display_type'))
    if self.has_input('p_vectors_transparency') :
      p.set_p_vectors_transparency(self.get_input('p_vectors_transparency'))
    if self.has_input('p_vectors_normalize') :
      p.set_p_vectors_normalize(self.get_input('p_vectors_normalize'))
    if self.has_input('p_vectors_bidirectional') :
      p.set_p_vectors_bidirectional(self.get_input('p_vectors_bidirectional'))
    if self.has_input('p_vectors_color_type') :
      p.set_p_vectors_color_type(self.get_input('p_vectors_color_type'))
    if self.has_input('p_vectors_resolution') :
      p.set_p_vectors_resolution(self.get_input('p_vectors_resolution'))
    if self.has_input('p_tensors_has_data') :
      p.set_p_tensors_has_data(self.get_input('p_tensors_has_data'))
    if self.has_input('p_tensors_on') :
      p.set_p_tensors_on(self.get_input('p_tensors_on'))
    if self.has_input('p_tensors_display_type') :
      p.set_p_tensors_display_type(self.get_input('p_tensors_display_type'))
    if self.has_input('p_tensors_transparency') :
      p.set_p_tensors_transparency(self.get_input('p_tensors_transparency'))
    if self.has_input('p_tensors_normalize') :
      p.set_p_tensors_normalize(self.get_input('p_tensors_normalize'))
    if self.has_input('p_tensors_color_type') :
      p.set_p_tensors_color_type(self.get_input('p_tensors_color_type'))
    if self.has_input('p_tensors_resolution') :
      p.set_p_tensors_resolution(self.get_input('p_tensors_resolution'))
    if self.has_input('p_tensors_emphasis') :
      p.set_p_tensors_emphasis(self.get_input('p_tensors_emphasis'))
    if self.has_input('p_secondary_has_data') :
      p.set_p_secondary_has_data(self.get_input('p_secondary_has_data'))
    if self.has_input('p_secondary_on') :
      p.set_p_secondary_on(self.get_input('p_secondary_on'))
    if self.has_input('p_secondary_display_type') :
      p.set_p_secondary_display_type(self.get_input('p_secondary_display_type'))
    if self.has_input('p_secondary_color_type') :
      p.set_p_secondary_color_type(self.get_input('p_secondary_color_type'))
    if self.has_input('p_secondary_alpha') :
      p.set_p_secondary_alpha(self.get_input('p_secondary_alpha'))
    if self.has_input('p_secondary_value') :
      p.set_p_secondary_value(self.get_input('p_secondary_value'))
    if self.has_input('p_tertiary_has_data') :
      p.set_p_tertiary_has_data(self.get_input('p_tertiary_has_data'))
    if self.has_input('p_tertiary_on') :
      p.set_p_tertiary_on(self.get_input('p_tertiary_on'))
    if self.has_input('p_tertiary_display_type') :
      p.set_p_tertiary_display_type(self.get_input('p_tertiary_display_type'))
    if self.has_input('p_tertiary_color_type') :
      p.set_p_tertiary_color_type(self.get_input('p_tertiary_color_type'))
    if self.has_input('p_tertiary_alpha') :
      p.set_p_tertiary_alpha(self.get_input('p_tertiary_alpha'))
    if self.has_input('p_tertiary_value') :
      p.set_p_tertiary_value(self.get_input('p_tertiary_value'))
    if self.has_input('p_text_on') :
      p.set_p_text_on(self.get_input('p_text_on'))
    if self.has_input('p_text_color_type') :
      p.set_p_text_color_type(self.get_input('p_text_color_type'))
    if self.has_input('p_text_color_r') :
      p.set_p_text_color_r(self.get_input('p_text_color_r'))
    if self.has_input('p_text_color_g') :
      p.set_p_text_color_g(self.get_input('p_text_color_g'))
    if self.has_input('p_text_color_b') :
      p.set_p_text_color_b(self.get_input('p_text_color_b'))
    if self.has_input('p_text_backface_cull') :
      p.set_p_text_backface_cull(self.get_input('p_text_backface_cull'))
    if self.has_input('p_text_always_visible') :
      p.set_p_text_always_visible(self.get_input('p_text_always_visible'))
    if self.has_input('p_text_fontsize') :
      p.set_p_text_fontsize(self.get_input('p_text_fontsize'))
    if self.has_input('p_text_precision') :
      p.set_p_text_precision(self.get_input('p_text_precision'))
    if self.has_input('p_text_render_locations') :
      p.set_p_text_render_locations(self.get_input('p_text_render_locations'))
    if self.has_input('p_text_show_data') :
      p.set_p_text_show_data(self.get_input('p_text_show_data'))
    if self.has_input('p_text_show_nodes') :
      p.set_p_text_show_nodes(self.get_input('p_text_show_nodes'))
    if self.has_input('p_text_show_edges') :
      p.set_p_text_show_edges(self.get_input('p_text_show_edges'))
    if self.has_input('p_text_show_faces') :
      p.set_p_text_show_faces(self.get_input('p_text_show_faces'))
    if self.has_input('p_text_show_cells') :
      p.set_p_text_show_cells(self.get_input('p_text_show_cells'))
    if self.has_input('p_def_color_r') :
      p.set_p_def_color_r(self.get_input('p_def_color_r'))
    if self.has_input('p_def_color_g') :
      p.set_p_def_color_g(self.get_input('p_def_color_g'))
    if self.has_input('p_def_color_b') :
      p.set_p_def_color_b(self.get_input('p_def_color_b'))
    if self.has_input('p_def_color_a') :
      p.set_p_def_color_a(self.get_input('p_def_color_a'))
    if self.has_input('p_active_tab') :
      p.set_p_active_tab(self.get_input('p_active_tab'))
    if self.has_input('p_interactive_mode') :
      p.set_p_interactive_mode(self.get_input('p_interactive_mode'))
    if self.has_input('p_show_progress') :
      p.set_p_show_progress(self.get_input('p_show_progress'))
    if self.has_input('p_field_name') :
      p.set_p_field_name(self.get_input('p_field_name'))
    if self.has_input('p_field_name_override') :
      p.set_p_field_name_override(self.get_input('p_field_name_override'))
    if self.has_input('p_approx_div') :
      p.set_p_approx_div(self.get_input('p_approx_div'))
    if self.has_input('p_use_default_size') :
      p.set_p_use_default_size(self.get_input('p_use_default_size'))
    Primary_Data = 0
    if self.has_input('Primary Data') :
      Primary_Data = self.get_input('Primary Data')
    Primary_ColorMap = 0
    if self.has_input('Primary ColorMap') :
      Primary_ColorMap = self.get_input('Primary ColorMap')
    Secondary_Data = 0
    if self.has_input('Secondary Data') :
      Secondary_Data = self.get_input('Secondary Data')
    Secondary_ColorMap = 0
    if self.has_input('Secondary ColorMap') :
      Secondary_ColorMap = self.get_input('Secondary ColorMap')
    Tertiary_Data = 0
    if self.has_input('Tertiary Data') :
      Tertiary_Data = self.get_input('Tertiary Data')
    Tertiary_ColorMap = 0
    if self.has_input('Tertiary ColorMap') :
      Tertiary_ColorMap = self.get_input('Tertiary ColorMap')
    results = p.execute(Primary_Data, Primary_ColorMap, Secondary_Data, Secondary_ColorMap, Tertiary_Data, Tertiary_ColorMap)
    self.set_output('Scene Graph', results)

class GenerateStreamLines(Visualization) :
  def compute(self) :
    p = sr_py.GenerateStreamLinesAlg()
    if self.has_input('p_stepsize') :
      p.set_p_stepsize(self.get_input('p_stepsize'))
    if self.has_input('p_tolerance') :
      p.set_p_tolerance(self.get_input('p_tolerance'))
    if self.has_input('p_maxsteps') :
      p.set_p_maxsteps(self.get_input('p_maxsteps'))
    if self.has_input('p_direction') :
      p.set_p_direction(self.get_input('p_direction'))
    if self.has_input('p_value') :
      p.set_p_value(self.get_input('p_value'))
    if self.has_input('p_remove_colinear_pts') :
      p.set_p_remove_colinear_pts(self.get_input('p_remove_colinear_pts'))
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    if self.has_input('p_nthreads') :
      p.set_p_nthreads(self.get_input('p_nthreads'))
    if self.has_input('p_auto_parameterize') :
      p.set_p_auto_parameterize(self.get_input('p_auto_parameterize'))
    Vector_Field = 0
    if self.has_input('Vector Field') :
      Vector_Field = self.get_input('Vector Field')
    Seed_Points = 0
    if self.has_input('Seed Points') :
      Seed_Points = self.get_input('Seed Points')
    results = p.execute(Vector_Field, Seed_Points)
    self.set_output('Streamlines', results)

class GenerateStreamLinesWithPlacementHeuristic(Visualization) :
  def compute(self) :
    p = sr_py.GenerateStreamLinesWithPlacementHeuristicAlg()
    if self.has_input('p_numsl') :
      p.set_p_numsl(self.get_input('p_numsl'))
    if self.has_input('p_numpts') :
      p.set_p_numpts(self.get_input('p_numpts'))
    if self.has_input('p_minper') :
      p.set_p_minper(self.get_input('p_minper'))
    if self.has_input('p_maxper') :
      p.set_p_maxper(self.get_input('p_maxper'))
    if self.has_input('p_ming') :
      p.set_p_ming(self.get_input('p_ming'))
    if self.has_input('p_maxg') :
      p.set_p_maxg(self.get_input('p_maxg'))
    if self.has_input('p_numsamples') :
      p.set_p_numsamples(self.get_input('p_numsamples'))
    if self.has_input('p_method') :
      p.set_p_method(self.get_input('p_method'))
    if self.has_input('p_stepsize') :
      p.set_p_stepsize(self.get_input('p_stepsize'))
    if self.has_input('p_stepout') :
      p.set_p_stepout(self.get_input('p_stepout'))
    if self.has_input('p_maxsteps') :
      p.set_p_maxsteps(self.get_input('p_maxsteps'))
    if self.has_input('p_minmag') :
      p.set_p_minmag(self.get_input('p_minmag'))
    if self.has_input('p_direction') :
      p.set_p_direction(self.get_input('p_direction'))
    Source = 0
    if self.has_input('Source') :
      Source = self.get_input('Source')
    Weighting = 0
    if self.has_input('Weighting') :
      Weighting = self.get_input('Weighting')
    Flow = 0
    if self.has_input('Flow') :
      Flow = self.get_input('Flow')
    Compare = 0
    if self.has_input('Compare') :
      Compare = self.get_input('Compare')
    Seed_points = 0
    if self.has_input('Seed points') :
      Seed_points = self.get_input('Seed points')
    results = p.execute(Source, Weighting, Flow, Compare, Seed_points)
    self.set_output('Streamlines', results[0])
    self.set_output('Render', results[1])

class ShowString(Visualization) :
  def compute(self) :
    p = sr_py.ShowStringAlg()
    if self.has_input('p_bbox') :
      p.set_p_bbox(self.get_input('p_bbox'))
    if self.has_input('p_size') :
      p.set_p_size(self.get_input('p_size'))
    if self.has_input('p_location_x') :
      p.set_p_location_x(self.get_input('p_location_x'))
    if self.has_input('p_location_y') :
      p.set_p_location_y(self.get_input('p_location_y'))
    if self.has_input('p_color_r') :
      p.set_p_color_r(self.get_input('p_color_r'))
    if self.has_input('p_color_g') :
      p.set_p_color_g(self.get_input('p_color_g'))
    if self.has_input('p_color_b') :
      p.set_p_color_b(self.get_input('p_color_b'))
    Format_String = ''
    if self.has_input('Format String') :
      Format_String = self.get_input('Format String')
    results = p.execute(Format_String)
    self.set_output('Title', results)

class CreateAndEditColorMap(Visualization) :
  def compute(self) :
    p = sr_py.CreateAndEditColorMapAlg()
    if self.has_input('p_rgbhsv') :
      p.set_p_rgbhsv(self.get_input('p_rgbhsv'))
    if self.has_input('p_rgb_points') :
      p.set_p_rgb_points(self.get_input('p_rgb_points'))
    if self.has_input('p_alpha_points') :
      p.set_p_alpha_points(self.get_input('p_alpha_points'))
    if self.has_input('p_resolution') :
      p.set_p_resolution(self.get_input('p_resolution'))
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    results = p.execute(ColorMap)
    self.set_output('ColorMap', results[0])
    self.set_output('Geometry', results[1])

class ShowMeshBoundingBox(Visualization) :
  def compute(self) :
    p = sr_py.ShowMeshBoundingBoxAlg()
    if self.has_input('p_sizex') :
      p.set_p_sizex(self.get_input('p_sizex'))
    if self.has_input('p_sizey') :
      p.set_p_sizey(self.get_input('p_sizey'))
    if self.has_input('p_sizez') :
      p.set_p_sizez(self.get_input('p_sizez'))
    Field = 0
    if self.has_input('Field') :
      Field = self.get_input('Field')
    results = p.execute(Field)
    self.set_output('Scene Graph', results)

class CreateStandardColorMaps(Visualization) :
  def compute(self) :
    p = sr_py.CreateStandardColorMapsAlg()
    if self.has_input('p_mapName') :
      p.set_p_mapName(self.get_input('p_mapName'))
    if self.has_input('p_gamma') :
      p.set_p_gamma(self.get_input('p_gamma'))
    if self.has_input('p_resolution') :
      p.set_p_resolution(self.get_input('p_resolution'))
    if self.has_input('p_reverse') :
      p.set_p_reverse(self.get_input('p_reverse'))
    if self.has_input('p_faux') :
      p.set_p_faux(self.get_input('p_faux'))
    if self.has_input('p_positionList') :
      p.set_p_positionList(self.get_input('p_positionList'))
    if self.has_input('p_nodeList') :
      p.set_p_nodeList(self.get_input('p_nodeList'))
    if self.has_input('p_width') :
      p.set_p_width(self.get_input('p_width'))
    if self.has_input('p_height') :
      p.set_p_height(self.get_input('p_height'))
    results = p.execute()
    self.set_output('ColorMap', results)

class ShowTextureSlices(Visualization) :
  def compute(self) :
    p = sr_py.ShowTextureSlicesAlg()
    if self.has_input('p_control_pos_saved') :
      p.set_p_control_pos_saved(self.get_input('p_control_pos_saved'))
    if self.has_input('p_drawX') :
      p.set_p_drawX(self.get_input('p_drawX'))
    if self.has_input('p_drawY') :
      p.set_p_drawY(self.get_input('p_drawY'))
    if self.has_input('p_drawZ') :
      p.set_p_drawZ(self.get_input('p_drawZ'))
    if self.has_input('p_drawView') :
      p.set_p_drawView(self.get_input('p_drawView'))
    if self.has_input('p_interp_mode') :
      p.set_p_interp_mode(self.get_input('p_interp_mode'))
    if self.has_input('p_draw_phi_0') :
      p.set_p_draw_phi_0(self.get_input('p_draw_phi_0'))
    if self.has_input('p_draw_phi_1') :
      p.set_p_draw_phi_1(self.get_input('p_draw_phi_1'))
    if self.has_input('p_phi_0') :
      p.set_p_phi_0(self.get_input('p_phi_0'))
    if self.has_input('p_phi_1') :
      p.set_p_phi_1(self.get_input('p_phi_1'))
    if self.has_input('p_multi_level') :
      p.set_p_multi_level(self.get_input('p_multi_level'))
    if self.has_input('p_color_changed') :
      p.set_p_color_changed(self.get_input('p_color_changed'))
    if self.has_input('p_colors') :
      p.set_p_colors(self.get_input('p_colors'))
    if self.has_input('p_level_on') :
      p.set_p_level_on(self.get_input('p_level_on'))
    if self.has_input('p_outline_levels') :
      p.set_p_outline_levels(self.get_input('p_outline_levels'))
    if self.has_input('p_use_stencil') :
      p.set_p_use_stencil(self.get_input('p_use_stencil'))
    Texture = 0
    if self.has_input('Texture') :
      Texture = self.get_input('Texture')
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    ColorMap2 = 0
    if self.has_input('ColorMap2') :
      ColorMap2 = self.get_input('ColorMap2')
    results = p.execute(Texture, ColorMap, ColorMap2)
    self.set_output('Geometry', results[0])
    self.set_output('ColorMap', results[1])

class ShowMatrix(Visualization) :
  def compute(self) :
    p = sr_py.ShowMatrixAlg()
    if self.has_input('p_xpos') :
      p.set_p_xpos(self.get_input('p_xpos'))
    if self.has_input('p_ypos') :
      p.set_p_ypos(self.get_input('p_ypos'))
    if self.has_input('p_xscale') :
      p.set_p_xscale(self.get_input('p_xscale'))
    if self.has_input('p_yscale') :
      p.set_p_yscale(self.get_input('p_yscale'))
    if self.has_input('p_3d_mode') :
      p.set_p_3d_mode(self.get_input('p_3d_mode'))
    if self.has_input('p_gmode') :
      p.set_p_gmode(self.get_input('p_gmode'))
    if self.has_input('p_showtext') :
      p.set_p_showtext(self.get_input('p_showtext'))
    if self.has_input('p_row_begin') :
      p.set_p_row_begin(self.get_input('p_row_begin'))
    if self.has_input('p_rows') :
      p.set_p_rows(self.get_input('p_rows'))
    if self.has_input('p_col_begin') :
      p.set_p_col_begin(self.get_input('p_col_begin'))
    if self.has_input('p_cols') :
      p.set_p_cols(self.get_input('p_cols'))
    if self.has_input('p_colormapmode') :
      p.set_p_colormapmode(self.get_input('p_colormapmode'))
    ColorMap = 0
    if self.has_input('ColorMap') :
      ColorMap = self.get_input('ColorMap')
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(ColorMap, Matrix)
    self.set_output('Geometry', results)

class CreateViewerClockIcon(Visualization) :
  def compute(self) :
    p = sr_py.CreateViewerClockIconAlg()
    if self.has_input('p_type') :
      p.set_p_type(self.get_input('p_type'))
    if self.has_input('p_bbox') :
      p.set_p_bbox(self.get_input('p_bbox'))
    if self.has_input('p_format') :
      p.set_p_format(self.get_input('p_format'))
    if self.has_input('p_min') :
      p.set_p_min(self.get_input('p_min'))
    if self.has_input('p_max') :
      p.set_p_max(self.get_input('p_max'))
    if self.has_input('p_current') :
      p.set_p_current(self.get_input('p_current'))
    if self.has_input('p_size') :
      p.set_p_size(self.get_input('p_size'))
    if self.has_input('p_location_x') :
      p.set_p_location_x(self.get_input('p_location_x'))
    if self.has_input('p_location_y') :
      p.set_p_location_y(self.get_input('p_location_y'))
    if self.has_input('p_color_r') :
      p.set_p_color_r(self.get_input('p_color_r'))
    if self.has_input('p_color_g') :
      p.set_p_color_g(self.get_input('p_color_g'))
    if self.has_input('p_color_b') :
      p.set_p_color_b(self.get_input('p_color_b'))
    Time_Matrix = 0
    if self.has_input('Time Matrix') :
      Time_Matrix = self.get_input('Time Matrix')
    Time_Nrrd = 0
    if self.has_input('Time Nrrd') :
      Time_Nrrd = self.get_input('Time Nrrd')
    results = p.execute(Time_Matrix, Time_Nrrd)
    self.set_output('Clock', results)

class ConvertFieldsToTexture(Visualization) :
  def compute(self) :
    p = sr_py.ConvertFieldsToTextureAlg()
    if self.has_input('p_vmin') :
      p.set_p_vmin(self.get_input('p_vmin'))
    if self.has_input('p_vmax') :
      p.set_p_vmax(self.get_input('p_vmax'))
    if self.has_input('p_gmin') :
      p.set_p_gmin(self.get_input('p_gmin'))
    if self.has_input('p_gmax') :
      p.set_p_gmax(self.get_input('p_gmax'))
    if self.has_input('p_is_fixed') :
      p.set_p_is_fixed(self.get_input('p_is_fixed'))
    if self.has_input('p_card_mem') :
      p.set_p_card_mem(self.get_input('p_card_mem'))
    if self.has_input('p_card_mem_auto') :
      p.set_p_card_mem_auto(self.get_input('p_card_mem_auto'))
    if self.has_input('p_histogram') :
      p.set_p_histogram(self.get_input('p_histogram'))
    if self.has_input('p_gamma') :
      p.set_p_gamma(self.get_input('p_gamma'))
    Value_Field = 0
    if self.has_input('Value Field') :
      Value_Field = self.get_input('Value Field')
    Gradient_Magnitude_Field = 0
    if self.has_input('Gradient Magnitude Field') :
      Gradient_Magnitude_Field = self.get_input('Gradient Magnitude Field')
    results = p.execute(Value_Field, Gradient_Magnitude_Field)
    self.set_output('Texture', results[0])
    self.set_output('JointHistoGram', results[1])

class ColorMap2DSemantics(Visualization) :
  def compute(self) :
    p = sr_py.ColorMap2DSemanticsAlg()
    Input_Colormap = 0
    if self.has_input('Input Colormap') :
      Input_Colormap = self.get_input('Input Colormap')
    results = p.execute(Input_Colormap)
    self.set_output('Output Colormap', results)

class ConvertMatrixToString(Converters) :
  def compute(self) :
    p = sr_py.ConvertMatrixToStringAlg()
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('String', results)

class ConvertMatrixToField(Converters) :
  def compute(self) :
    p = sr_py.ConvertMatrixToFieldAlg()
    if self.has_input('p_datalocation') :
      p.set_p_datalocation(self.get_input('p_datalocation'))
    Matrix = 0
    if self.has_input('Matrix') :
      Matrix = self.get_input('Matrix')
    results = p.execute(Matrix)
    self.set_output('Field', results)

class TimeControls(Time) :
  def compute(self) :
    p = sr_py.TimeControlsAlg()
    if self.has_input('p_execmode') :
      p.set_p_execmode(self.get_input('p_execmode'))
    if self.has_input('p_scale_factor') :
      p.set_p_scale_factor(self.get_input('p_scale_factor'))
    results = p.execute()
    self.set_output('time', results)


def initialize(*args, **keywords):

  env = []
  for k in os.environ.keys() :
    estr = "%s=%s" % (k, os.environ[k])
    env.append(estr)
  sr_py.init_sr_py(env)

  reg = core.modules.module_registry

  reg.add_module(Time, abstract=True)
  reg.add_module(Converters, abstract=True)
  reg.add_module(Texture, abstract=True)
  reg.add_module(Visualization, abstract=True)
  reg.add_module(MiscField, abstract=True)
  reg.add_module(DataArrayMath, abstract=True)
  reg.add_module(Math, abstract=True)
  reg.add_module(ChangeMesh, abstract=True)
  reg.add_module(ChangeFieldData, abstract=True)
  reg.add_module(Geometry, abstract=True)
  reg.add_module(NewField, abstract=True)
  reg.add_module(ColorMap, abstract=True)
  reg.add_module(Field, abstract=True)
  reg.add_module(Nrrd, abstract=True)
  reg.add_module(Matrix, abstract=True)
  reg.add_module(ColorMap2, abstract=True)
  reg.add_module(Path, abstract=True)
  reg.add_module(String, abstract=True)
  reg.add_module(Bundle, abstract=True)
  reg.add_module(DataIO, abstract=True)
  reg.add_module(WriteBundle)
  reg.add_input_port(WriteBundle, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteBundle, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteBundle, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(WriteBundle, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(WritePath)
  reg.add_input_port(WritePath, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WritePath, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WritePath, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WritePath, 'Input Data',
                   (Path, "Path"))
  reg.add_input_port(WritePath, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(WriteColorMap2D)
  reg.add_input_port(WriteColorMap2D, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap2D, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap2D, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap2D, 'p_exporttype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap2D, 'Input Data',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(WriteColorMap2D, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadHDF5File)
  reg.add_input_port(ReadHDF5File, 'p_have_HDF5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_power_app',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_datasets',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_dumpname',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_ports',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_ndims',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_mergeData',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_assumeSVT',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_animate',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_animate_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_basic_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_extended_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_playmode_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_selectable_min',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_selectable_max',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_selectable_inc',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_range_min',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_range_max',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_playmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_current',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_execmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_delay',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_inc_amount',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_update_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_have_group',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_have_attributes',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_have_datasets',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_continuous',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_selectionString',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_regexp',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_allow_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_read_error',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_max_dims',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_dim',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_start',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_start2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_count',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_count2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_stride',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_0_stride2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_dim',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_start',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_start2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_count',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_count2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_stride',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_1_stride2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_dim',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_start',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_start2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_count',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_count2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_stride',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_2_stride2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_dim',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_start',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_start2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_count',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_count2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_stride',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_3_stride2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_dim',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_start',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_start2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_count',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_count2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_stride',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_4_stride2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_dim',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_start',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_start2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_count',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_count2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_stride',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'p_5_stride2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadHDF5File, 'Full filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(ReadHDF5File, 'Current Index',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReadHDF5File, 'Output 0 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 1 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 2 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 3 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 4 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 5 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 6 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Output 7 Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ReadHDF5File, 'Selected Index',
                   (Matrix, "Matrix"))

  reg.add_module(ReadField)
  reg.add_input_port(ReadField, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadField, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadField, 'Output Data',
                   (Field, "Field"))
  reg.add_output_port(ReadField, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(WriteColorMap)
  reg.add_input_port(WriteColorMap, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap, 'p_exporttype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteColorMap, 'Input Data',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(WriteColorMap, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadColorMap2D)
  reg.add_input_port(ReadColorMap2D, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadColorMap2D, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadColorMap2D, 'Output Data',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(ReadColorMap2D, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadString)
  reg.add_input_port(ReadString, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadString, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadString, 'Output Data',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadString, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadColorMap)
  reg.add_input_port(ReadColorMap, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadColorMap, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadColorMap, 'Output Data',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(ReadColorMap, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadMatrix)
  reg.add_input_port(ReadMatrix, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadMatrix, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadMatrix, 'Output Data',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReadMatrix, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(WriteString)
  reg.add_input_port(WriteString, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteString, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteString, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteString, 'String',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(WriteString, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadPath)
  reg.add_input_port(ReadPath, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadPath, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadPath, 'Output Data',
                   (Path, "Path"))
  reg.add_output_port(ReadPath, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(WriteField)
  reg.add_input_port(WriteField, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteField, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteField, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteField, 'p_exporttype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteField, 'p_increment',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(WriteField, 'p_current',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(WriteField, 'Input Data',
                   (Field, "Field"))
  reg.add_input_port(WriteField, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadBundle)
  reg.add_input_port(ReadBundle, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadBundle, 'p_types',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadBundle, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(ReadBundle, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(StreamMatrixFromDisk)
  reg.add_input_port(StreamMatrixFromDisk, 'p_row_or_col',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_slider_min',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_slider_max',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_range_min',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_range_max',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_playmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_current',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_execmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_delay',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_inc_amount',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'p_send_amount',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(StreamMatrixFromDisk, 'Indices',
                   (Matrix, "Matrix"))
  reg.add_input_port(StreamMatrixFromDisk, 'Weights',
                   (Matrix, "Matrix"))
  reg.add_input_port(StreamMatrixFromDisk, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(StreamMatrixFromDisk, 'DataVector',
                   (Matrix, "Matrix"))
  reg.add_output_port(StreamMatrixFromDisk, 'Index',
                   (Matrix, "Matrix"))
  reg.add_output_port(StreamMatrixFromDisk, 'Scaled Index',
                   (Matrix, "Matrix"))
  reg.add_output_port(StreamMatrixFromDisk, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(WriteMatrix)
  reg.add_input_port(WriteMatrix, 'p_filetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteMatrix, 'p_confirm',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteMatrix, 'p_confirm_once',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteMatrix, 'p_exporttype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(WriteMatrix, 'p_split',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(WriteMatrix, 'Input Data',
                   (Matrix, "Matrix"))
  reg.add_input_port(WriteMatrix, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReadNrrd)
  reg.add_input_port(ReadNrrd, 'p_from_env',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReadNrrd, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ReadNrrd, 'Output Data',
                   (Field, "Field"))
  reg.add_output_port(ReadNrrd, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(JoinFields)
  reg.add_input_port(JoinFields, 'p_tolerance',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(JoinFields, 'p_force_nodemerge',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(JoinFields, 'p_force_pointcloud',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(JoinFields, 'p_matchval',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(JoinFields, 'p_meshonly',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(JoinFields, 'Field',
                   (Field, "Field"))
  reg.add_output_port(JoinFields, 'Output Field',
                   (Field, "Field"))

  reg.add_module(RefineMeshByIsovalue)
  reg.add_input_port(RefineMeshByIsovalue, 'p_isoval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(RefineMeshByIsovalue, 'p_lte',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(RefineMeshByIsovalue, 'Input',
                   (Field, "Field"))
  reg.add_input_port(RefineMeshByIsovalue, 'Optional Isovalue',
                   (Matrix, "Matrix"))
  reg.add_output_port(RefineMeshByIsovalue, 'Refined',
                   (Field, "Field"))
  reg.add_output_port(RefineMeshByIsovalue, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(FairMesh)
  reg.add_input_port(FairMesh, 'p_iterations',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(FairMesh, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(FairMesh, 'Input Mesh',
                   (Field, "Field"))
  reg.add_output_port(FairMesh, 'Faired Mesh',
                   (Field, "Field"))

  reg.add_module(CreateStructHex)
  reg.add_input_port(CreateStructHex, 'p_sizex',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStructHex, 'p_sizey',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStructHex, 'p_sizez',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStructHex, 'p_padpercent',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateStructHex, 'p_data_at',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateStructHex, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(CreateStructHex, 'Output Sample Field',
                   (Field, "Field"))

  reg.add_module(ClipLatVolByIndicesOrWidget)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_use_text_bbox',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_text_min_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_text_min_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_text_min_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_text_max_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_text_max_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'p_text_max_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipLatVolByIndicesOrWidget, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ClipLatVolByIndicesOrWidget, 'Selection Widget',
                   (Geometry, "Geometry"))
  reg.add_output_port(ClipLatVolByIndicesOrWidget, 'Output Field',
                   (Field, "Field"))
  reg.add_output_port(ClipLatVolByIndicesOrWidget, 'MaskVector',
                   (Nrrd, "Nrrd"))

  reg.add_module(GetFieldBoundary)
  reg.add_input_port(GetFieldBoundary, 'Field',
                   (Field, "Field"))
  reg.add_output_port(GetFieldBoundary, 'BoundaryField',
                   (Field, "Field"))
  reg.add_output_port(GetFieldBoundary, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(ConvertMatricesToMesh)
  reg.add_input_port(ConvertMatricesToMesh, 'p_fieldname',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatricesToMesh, 'p_meshname',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatricesToMesh, 'p_fieldbasetype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatricesToMesh, 'p_datatype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatricesToMesh, 'Mesh Elements',
                   (Matrix, "Matrix"))
  reg.add_input_port(ConvertMatricesToMesh, 'Mesh Positions',
                   (Matrix, "Matrix"))
  reg.add_input_port(ConvertMatricesToMesh, 'Mesh Normals',
                   (Matrix, "Matrix"))
  reg.add_output_port(ConvertMatricesToMesh, 'Output Field',
                   (Field, "Field"))

  reg.add_module(ClipFieldToFieldOrWidget)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_clip_location',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_clipmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_autoexecute',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_autoinvert',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_execmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_center_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_center_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_center_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_right_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_right_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_right_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_down_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_down_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_down_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_in_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_in_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_in_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'p_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipFieldToFieldOrWidget, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(ClipFieldToFieldOrWidget, 'Clip Field',
                   (Field, "Field"))
  reg.add_output_port(ClipFieldToFieldOrWidget, 'Selection Widget',
                   (Geometry, "Geometry"))
  reg.add_output_port(ClipFieldToFieldOrWidget, 'Output Field',
                   (Field, "Field"))

  reg.add_module(RefineMeshByIsovalue2)
  reg.add_input_port(RefineMeshByIsovalue2, 'p_isoval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(RefineMeshByIsovalue2, 'p_lte',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(RefineMeshByIsovalue2, 'Input',
                   (Field, "Field"))
  reg.add_input_port(RefineMeshByIsovalue2, 'Optional Isovalue',
                   (Matrix, "Matrix"))
  reg.add_output_port(RefineMeshByIsovalue2, 'Refined',
                   (Field, "Field"))
  reg.add_output_port(RefineMeshByIsovalue2, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(CreateLatVol)
  reg.add_input_port(CreateLatVol, 'p_sizex',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateLatVol, 'p_sizey',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateLatVol, 'p_sizez',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateLatVol, 'p_padpercent',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLatVol, 'p_data_at',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateLatVol, 'p_element_size',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateLatVol, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(CreateLatVol, 'LatVol Size',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateLatVol, 'Output Sample Field',
                   (Field, "Field"))

  reg.add_module(InterfaceWithCamal)
  reg.add_input_port(InterfaceWithCamal, 'TriSurf',
                   (Field, "Field"))
  reg.add_output_port(InterfaceWithCamal, 'TetVol',
                   (Field, "Field"))

  reg.add_module(ClipVolumeByIsovalue)
  reg.add_input_port(ClipVolumeByIsovalue, 'p_isoval_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipVolumeByIsovalue, 'p_isoval_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipVolumeByIsovalue, 'p_isoval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ClipVolumeByIsovalue, 'p_lte',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ClipVolumeByIsovalue, 'p_update_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipVolumeByIsovalue, 'Input',
                   (Field, "Field"))
  reg.add_input_port(ClipVolumeByIsovalue, 'Optional Isovalue',
                   (Matrix, "Matrix"))
  reg.add_output_port(ClipVolumeByIsovalue, 'Clipped',
                   (Field, "Field"))
  reg.add_output_port(ClipVolumeByIsovalue, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(RefineMesh)
  reg.add_input_port(RefineMesh, 'p_select',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(RefineMesh, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(RefineMesh, 'p_isoval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(RefineMesh, 'Mesh',
                   (Field, "Field"))
  reg.add_input_port(RefineMesh, 'Isovalue',
                   (Matrix, "Matrix"))
  reg.add_output_port(RefineMesh, 'RefinedMesh',
                   (Field, "Field"))
  reg.add_output_port(RefineMesh, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(MergeFields)
  reg.add_input_port(MergeFields, 'Container Mesh',
                   (Field, "Field"))
  reg.add_input_port(MergeFields, 'Insert Field',
                   (Field, "Field"))
  reg.add_output_port(MergeFields, 'Combined Field',
                   (Field, "Field"))
  reg.add_output_port(MergeFields, 'Extended Insert Field',
                   (Field, "Field"))
  reg.add_output_port(MergeFields, 'Combined To Extended Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(GetCentroidsFromMesh)
  reg.add_input_port(GetCentroidsFromMesh, 'TetVolField',
                   (Field, "Field"))
  reg.add_output_port(GetCentroidsFromMesh, 'PointCloudField',
                   (Field, "Field"))

  reg.add_module(ExtractIsosurfaceByFunction)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_zero_checks',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_slice_value_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_slice_value_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_slice_value',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_slice_value_typed',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_slice_value_quantity',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_quantity_range',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_quantity_clusive',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_quantity_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_quantity_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_quantity_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_slice_value_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_matrix_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_algorithm',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_active_slice_value_selection_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_active_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'p_update_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurfaceByFunction, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(ExtractIsosurfaceByFunction, 'Optional Slice values',
                   (Matrix, "Matrix"))
  reg.add_output_port(ExtractIsosurfaceByFunction, 'Output Field',
                   (Field, "Field"))

  reg.add_module(MergeTriSurfs)
  reg.add_input_port(MergeTriSurfs, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(MergeTriSurfs, 'Output Field',
                   (Field, "Field"))

  reg.add_module(InterfaceWithTetGen)
  reg.add_input_port(InterfaceWithTetGen, 'p_switch',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InterfaceWithTetGen, 'Main',
                   (Field, "Field"))
  reg.add_input_port(InterfaceWithTetGen, 'Points',
                   (Field, "Field"))
  reg.add_input_port(InterfaceWithTetGen, 'Region Attribs',
                   (Field, "Field"))
  reg.add_input_port(InterfaceWithTetGen, 'Regions',
                   (Field, "Field"))
  reg.add_output_port(InterfaceWithTetGen, 'TetVol',
                   (Field, "Field"))

  reg.add_module(CreateImage)
  reg.add_input_port(CreateImage, 'p_sizex',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_sizey',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_sizez',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_z_value',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_auto_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_axis',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_padpercent',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_pos',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_data_at',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_update_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_corigin_x',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_corigin_y',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_corigin_z',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_cnormal_x',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_cnormal_y',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'p_cnormal_z',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateImage, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(CreateImage, 'Output Sample Field',
                   (Field, "Field"))

  reg.add_module(InsertHexVolSheetAlongSurface)
  reg.add_input_port(InsertHexVolSheetAlongSurface, 'p_side',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertHexVolSheetAlongSurface, 'p_addlayer',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertHexVolSheetAlongSurface, 'HexField',
                   (Field, "Field"))
  reg.add_input_port(InsertHexVolSheetAlongSurface, 'TriField',
                   (Field, "Field"))
  reg.add_output_port(InsertHexVolSheetAlongSurface, 'Side1Field',
                   (Field, "Field"))
  reg.add_output_port(InsertHexVolSheetAlongSurface, 'Side2Field',
                   (Field, "Field"))

  reg.add_module(GenerateSinglePointProbeFromField)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_main_frame',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_locx',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_locy',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_locz',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_value',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_node',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_edge',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_face',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_cell',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_show_value',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_show_node',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_show_edge',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_show_face',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_show_cell',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'p_probe_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateSinglePointProbeFromField, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(GenerateSinglePointProbeFromField, 'GenerateSinglePointProbeFromField Widget',
                   (Geometry, "Geometry"))
  reg.add_output_port(GenerateSinglePointProbeFromField, 'GenerateSinglePointProbeFromField Point',
                   (Field, "Field"))
  reg.add_output_port(GenerateSinglePointProbeFromField, 'Element Index',
                   (Matrix, "Matrix"))

  reg.add_module(InterfaceWithCubit)
  reg.add_input_port(InterfaceWithCubit, 'p_cubitdir',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InterfaceWithCubit, 'p_ncdump',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InterfaceWithCubit, 'Field',
                   (Field, "Field"))
  reg.add_input_port(InterfaceWithCubit, 'PointCloudField',
                   (Field, "Field"))
  reg.add_output_port(InterfaceWithCubit, 'Field',
                   (Field, "Field"))

  reg.add_module(ClipFieldByFunction)
  reg.add_input_port(ClipFieldByFunction, 'p_mode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldByFunction, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldByFunction, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(ClipFieldByFunction, 'Input',
                   (Field, "Field"))
  reg.add_output_port(ClipFieldByFunction, 'Clipped',
                   (Field, "Field"))
  reg.add_output_port(ClipFieldByFunction, 'Mapping',
                   (Matrix, "Matrix"))
  reg.add_output_port(ClipFieldByFunction, 'MaskVector',
                   (Nrrd, "Nrrd"))

  reg.add_module(GetDomainBoundary)
  reg.add_input_port(GetDomainBoundary, 'p_userange',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_minrange',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_maxrange',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_usevalue',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_value',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_includeouterboundary',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_innerboundaryonly',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_noinnerboundary',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'p_disconnect',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetDomainBoundary, 'Field',
                   (Field, "Field"))
  reg.add_input_port(GetDomainBoundary, 'MinValueValue',
                   (Matrix, "Matrix"))
  reg.add_input_port(GetDomainBoundary, 'MaxValue',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetDomainBoundary, 'Field',
                   (Field, "Field"))

  reg.add_module(CollectFields)
  reg.add_input_port(CollectFields, 'p_buffersize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CollectFields, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CollectFields, 'BufferSize',
                   (Matrix, "Matrix"))
  reg.add_output_port(CollectFields, 'Fields',
                   (Field, "Field"))

  reg.add_module(GeneratePointSamplesFromField)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_num_seeds',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_probe_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_send',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_widget',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_red',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_green',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_blue',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'p_auto_execute',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromField, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(GeneratePointSamplesFromField, 'GeneratePointSamplesFromField Widget',
                   (Geometry, "Geometry"))
  reg.add_output_port(GeneratePointSamplesFromField, 'GeneratePointSamplesFromField Point',
                   (Field, "Field"))

  reg.add_module(GeneratePointSamplesFromFieldOrWidget)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_wtype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_endpoints',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_maxseeds',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_numseeds',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_rngseed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_rnginc',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_clamp',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_autoexecute',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_dist',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'p_whichtab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GeneratePointSamplesFromFieldOrWidget, 'Field to Sample',
                   (Field, "Field"))
  reg.add_output_port(GeneratePointSamplesFromFieldOrWidget, 'Samples',
                   (Field, "Field"))
  reg.add_output_port(GeneratePointSamplesFromFieldOrWidget, 'Sampling Widget',
                   (Geometry, "Geometry"))

  reg.add_module(DecimateTriSurf)
  reg.add_input_port(DecimateTriSurf, 'TriSurf',
                   (Field, "Field"))
  reg.add_output_port(DecimateTriSurf, 'Decimated',
                   (Field, "Field"))

  reg.add_module(GetSliceFromStructuredFieldByIndices)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_axis',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_dims',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_dim_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_dim_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_dim_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_index_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_index_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_index_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_update_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'p_continuous',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(GetSliceFromStructuredFieldByIndices, 'Input Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetSliceFromStructuredFieldByIndices, 'Output Field',
                   (Field, "Field"))
  reg.add_output_port(GetSliceFromStructuredFieldByIndices, 'Output Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(RemoveHexVolSheet)
  reg.add_input_port(RemoveHexVolSheet, 'p_edge_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(RemoveHexVolSheet, 'HexField',
                   (Field, "Field"))
  reg.add_output_port(RemoveHexVolSheet, 'NewHexField',
                   (Field, "Field"))
  reg.add_output_port(RemoveHexVolSheet, 'ExtractedHexes',
                   (Field, "Field"))

  reg.add_module(SubsampleStructuredFieldByIndices)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_power_app',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_wrap',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_dims',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_dim_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_dim_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_dim_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_start_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_start_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_start_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_stop_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_stop_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_stop_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_stride_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_stride_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_stride_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_wrap_i',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_wrap_j',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'p_wrap_k',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(SubsampleStructuredFieldByIndices, 'Input Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(SubsampleStructuredFieldByIndices, 'Output Field',
                   (Field, "Field"))
  reg.add_output_port(SubsampleStructuredFieldByIndices, 'Output Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(GetAllSegmentationBoundaries)
  reg.add_input_port(GetAllSegmentationBoundaries, 'Segmentations',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(GetAllSegmentationBoundaries, 'Boundaries',
                   (Field, "Field"))

  reg.add_module(ClipFieldWithSeed)
  reg.add_input_port(ClipFieldWithSeed, 'p_mode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldWithSeed, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ClipFieldWithSeed, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(ClipFieldWithSeed, 'Input',
                   (Field, "Field"))
  reg.add_input_port(ClipFieldWithSeed, 'Seeds',
                   (Field, "Field"))
  reg.add_output_port(ClipFieldWithSeed, 'Clipped',
                   (Field, "Field"))
  reg.add_output_port(ClipFieldWithSeed, 'Mapping',
                   (Matrix, "Matrix"))
  reg.add_output_port(ClipFieldWithSeed, 'MaskVector',
                   (Nrrd, "Nrrd"))

  reg.add_module(SplitNodesByDomain)
  reg.add_input_port(SplitNodesByDomain, 'Field',
                   (Field, "Field"))
  reg.add_output_port(SplitNodesByDomain, 'SplitField',
                   (Field, "Field"))

  reg.add_module(ApplyMappingMatrix)
  reg.add_input_port(ApplyMappingMatrix, 'Source',
                   (Field, "Field"))
  reg.add_input_port(ApplyMappingMatrix, 'Destination',
                   (Field, "Field"))
  reg.add_input_port(ApplyMappingMatrix, 'Mapping',
                   (Matrix, "Matrix"))
  reg.add_output_port(ApplyMappingMatrix, 'Output',
                   (Field, "Field"))

  reg.add_module(MaskLatVolWithTriSurf)
  reg.add_input_port(MaskLatVolWithTriSurf, 'LatVolField',
                   (Field, "Field"))
  reg.add_input_port(MaskLatVolWithTriSurf, 'TriSurfField',
                   (Field, "Field"))
  reg.add_output_port(MaskLatVolWithTriSurf, 'LatVol Mask',
                   (Field, "Field"))

  reg.add_module(ConvertFieldBasis)
  reg.add_input_port(ConvertFieldBasis, 'p_output_basis',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertFieldBasis, 'Input',
                   (Field, "Field"))
  reg.add_output_port(ConvertFieldBasis, 'Output',
                   (Field, "Field"))
  reg.add_output_port(ConvertFieldBasis, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(ReportMeshQualityMeasures)
  reg.add_input_port(ReportMeshQualityMeasures, 'Input',
                   (Field, "Field"))
  reg.add_output_port(ReportMeshQualityMeasures, 'Checked',
                   (Nrrd, "Nrrd"))

  reg.add_module(SelectAndSetFieldData)
  reg.add_input_port(SelectAndSetFieldData, 'p_selection1',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_function1',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_selection2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_function2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_selection3',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_function3',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_selection4',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_function4',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_functiondef',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData, 'Field',
                   (Field, "Field"))
  reg.add_input_port(SelectAndSetFieldData, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(SelectAndSetFieldData, 'Field',
                   (Field, "Field"))

  reg.add_module(CalculateFieldData3)
  reg.add_input_port(CalculateFieldData3, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldData3, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldData3, 'Field1',
                   (Field, "Field"))
  reg.add_input_port(CalculateFieldData3, 'Field2',
                   (Field, "Field"))
  reg.add_input_port(CalculateFieldData3, 'Field3',
                   (Field, "Field"))
  reg.add_input_port(CalculateFieldData3, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CalculateFieldData3, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(CalculateFieldData3, 'Field',
                   (Field, "Field"))

  reg.add_module(SetFieldData)
  reg.add_input_port(SetFieldData, 'p_keepscalartype',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SetFieldData, 'Field',
                   (Field, "Field"))
  reg.add_input_port(SetFieldData, 'Matrix Data',
                   (Matrix, "Matrix"))
  reg.add_input_port(SetFieldData, 'Nrrd Data',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(SetFieldData, 'Field',
                   (Field, "Field"))

  reg.add_module(SwapFieldDataWithMatrixEntries)
  reg.add_input_port(SwapFieldDataWithMatrixEntries, 'p_preserve_scalar_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SwapFieldDataWithMatrixEntries, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(SwapFieldDataWithMatrixEntries, 'Input Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(SwapFieldDataWithMatrixEntries, 'Output Field',
                   (Field, "Field"))
  reg.add_output_port(SwapFieldDataWithMatrixEntries, 'Output Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(ConvertLatVolDataFromElemToNode)
  reg.add_input_port(ConvertLatVolDataFromElemToNode, 'Elem Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertLatVolDataFromElemToNode, 'Node Field',
                   (Field, "Field"))

  reg.add_module(CalculateNodeNormals)
  reg.add_input_port(CalculateNodeNormals, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateNodeNormals, 'Input Point',
                   (Field, "Field"))
  reg.add_output_port(CalculateNodeNormals, 'Output Field',
                   (Field, "Field"))

  reg.add_module(CalculateVectorMagnitudes)
  reg.add_input_port(CalculateVectorMagnitudes, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(CalculateVectorMagnitudes, 'Output CalculateVectorMagnitudes',
                   (Field, "Field"))

  reg.add_module(ConvertIndicesToFieldData)
  reg.add_input_port(ConvertIndicesToFieldData, 'p_outputtype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertIndicesToFieldData, 'Field',
                   (Field, "Field"))
  reg.add_input_port(ConvertIndicesToFieldData, 'Data',
                   (Matrix, "Matrix"))
  reg.add_output_port(ConvertIndicesToFieldData, 'Field',
                   (Field, "Field"))

  reg.add_module(CalculateDistanceToFieldBoundary)
  reg.add_input_port(CalculateDistanceToFieldBoundary, 'Field',
                   (Field, "Field"))
  reg.add_output_port(CalculateDistanceToFieldBoundary, 'DistanceField',
                   (Field, "Field"))

  reg.add_module(MapFieldDataFromSourceToDestination)
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'p_interpolation_basis',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'p_map_source_to_single_dest',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'p_exhaustive_search',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'p_exhaustive_search_max_dist',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'p_np',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'Source',
                   (Field, "Field"))
  reg.add_input_port(MapFieldDataFromSourceToDestination, 'Destination',
                   (Field, "Field"))
  reg.add_output_port(MapFieldDataFromSourceToDestination, 'Remapped Destination',
                   (Field, "Field"))

  reg.add_module(SelectAndSetFieldData3)
  reg.add_input_port(SelectAndSetFieldData3, 'p_selection1',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_function1',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_selection2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_function2',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_selection3',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_function3',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_selection4',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_function4',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_functiondef',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SelectAndSetFieldData3, 'Field1',
                   (Field, "Field"))
  reg.add_input_port(SelectAndSetFieldData3, 'Field2',
                   (Field, "Field"))
  reg.add_input_port(SelectAndSetFieldData3, 'Field3',
                   (Field, "Field"))
  reg.add_input_port(SelectAndSetFieldData3, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(SelectAndSetFieldData3, 'Field',
                   (Field, "Field"))

  reg.add_module(CreateFieldData)
  reg.add_input_port(CreateFieldData, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateFieldData, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateFieldData, 'p_basis',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateFieldData, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CreateFieldData, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CreateFieldData, 'DataArray',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateFieldData, 'Field',
                   (Field, "Field"))

  reg.add_module(ConvertLatVolDataFromNodeToElem)
  reg.add_input_port(ConvertLatVolDataFromNodeToElem, 'Node Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertLatVolDataFromNodeToElem, 'Elem Field',
                   (Field, "Field"))

  reg.add_module(CalculateFieldDataCompiled)
  reg.add_input_port(CalculateFieldDataCompiled, 'p_outputdatatype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldDataCompiled, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldDataCompiled, 'p_cache',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CalculateFieldDataCompiled, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CalculateFieldDataCompiled, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(CalculateFieldDataCompiled, 'Output Field',
                   (Field, "Field"))

  reg.add_module(MapFieldDataFromElemToNode)
  reg.add_input_port(MapFieldDataFromElemToNode, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(MapFieldDataFromElemToNode, 'Field',
                   (Field, "Field"))
  reg.add_output_port(MapFieldDataFromElemToNode, 'Field',
                   (Field, "Field"))

  reg.add_module(ApplyFilterToFieldData)
  reg.add_input_port(ApplyFilterToFieldData, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ApplyFilterToFieldData, 'p_ed_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ApplyFilterToFieldData, 'p_ed_iterations',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ApplyFilterToFieldData, 'Field',
                   (Field, "Field"))
  reg.add_output_port(ApplyFilterToFieldData, 'Field',
                   (Field, "Field"))

  reg.add_module(GetFieldData)
  reg.add_input_port(GetFieldData, 'Field',
                   (Field, "Field"))
  reg.add_output_port(GetFieldData, 'Data',
                   (Matrix, "Matrix"))

  reg.add_module(CalculateFieldData2)
  reg.add_input_port(CalculateFieldData2, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldData2, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldData2, 'Field1',
                   (Field, "Field"))
  reg.add_input_port(CalculateFieldData2, 'Field2',
                   (Field, "Field"))
  reg.add_input_port(CalculateFieldData2, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CalculateFieldData2, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(CalculateFieldData2, 'Field',
                   (Field, "Field"))

  reg.add_module(CalculateLatVolGradientsAtNodes)
  reg.add_input_port(CalculateLatVolGradientsAtNodes, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(CalculateLatVolGradientsAtNodes, 'Output Gradient',
                   (Field, "Field"))

  reg.add_module(CalculateGradients)
  reg.add_input_port(CalculateGradients, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(CalculateGradients, 'Output CalculateGradients',
                   (Field, "Field"))

  reg.add_module(CalculateSignedDistanceToField)
  reg.add_input_port(CalculateSignedDistanceToField, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateSignedDistanceToField, 'ObjectField',
                   (Field, "Field"))
  reg.add_output_port(CalculateSignedDistanceToField, 'SignedDistanceField',
                   (Field, "Field"))

  reg.add_module(CalculateInsideWhichField)
  reg.add_input_port(CalculateInsideWhichField, 'p_outputbasis',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateInsideWhichField, 'p_outputtype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateInsideWhichField, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateInsideWhichField, 'Object',
                   (Field, "Field"))
  reg.add_output_port(CalculateInsideWhichField, 'Field',
                   (Field, "Field"))

  reg.add_module(MapFieldDataFromNodeToElem)
  reg.add_input_port(MapFieldDataFromNodeToElem, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(MapFieldDataFromNodeToElem, 'Field',
                   (Field, "Field"))
  reg.add_output_port(MapFieldDataFromNodeToElem, 'Field',
                   (Field, "Field"))

  reg.add_module(ConvertFieldDataType)
  reg.add_input_port(ConvertFieldDataType, 'p_outputdatatype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertFieldDataType, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertFieldDataType, 'Output Field',
                   (Field, "Field"))

  reg.add_module(CalculateIsInsideField)
  reg.add_input_port(CalculateIsInsideField, 'p_outputtype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateIsInsideField, 'p_outval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CalculateIsInsideField, 'p_inval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CalculateIsInsideField, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateIsInsideField, 'ObjectField',
                   (Field, "Field"))
  reg.add_output_port(CalculateIsInsideField, 'Field',
                   (Field, "Field"))

  reg.add_module(CalculateFieldData)
  reg.add_input_port(CalculateFieldData, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldData, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateFieldData, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateFieldData, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CalculateFieldData, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(CalculateFieldData, 'Field',
                   (Field, "Field"))

  reg.add_module(CalculateDistanceToField)
  reg.add_input_port(CalculateDistanceToField, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateDistanceToField, 'ObjectField',
                   (Field, "Field"))
  reg.add_output_port(CalculateDistanceToField, 'DistanceField',
                   (Field, "Field"))

  reg.add_module(TransformPlanarMesh)
  reg.add_input_port(TransformPlanarMesh, 'p_axis',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(TransformPlanarMesh, 'p_invert',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(TransformPlanarMesh, 'p_trans_x',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(TransformPlanarMesh, 'p_trans_y',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(TransformPlanarMesh, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(TransformPlanarMesh, 'Index Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(TransformPlanarMesh, 'Transformed Field',
                   (Field, "Field"))

  reg.add_module(ConvertMeshToUnstructuredMesh)
  reg.add_input_port(ConvertMeshToUnstructuredMesh, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertMeshToUnstructuredMesh, 'Output Field',
                   (Field, "Field"))

  reg.add_module(ConvertQuadSurfToTriSurf)
  reg.add_input_port(ConvertQuadSurfToTriSurf, 'QuadSurf',
                   (Field, "Field"))
  reg.add_output_port(ConvertQuadSurfToTriSurf, 'TriSurf',
                   (Field, "Field"))

  reg.add_module(TransformMeshWithFunction)
  reg.add_input_port(TransformMeshWithFunction, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(TransformMeshWithFunction, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(TransformMeshWithFunction, 'Output Field',
                   (Field, "Field"))

  reg.add_module(ConvertHexVolToTetVol)
  reg.add_input_port(ConvertHexVolToTetVol, 'HexVol',
                   (Field, "Field"))
  reg.add_output_port(ConvertHexVolToTetVol, 'TetVol',
                   (Field, "Field"))

  reg.add_module(ConvertMeshCoordinateSystem)
  reg.add_input_port(ConvertMeshCoordinateSystem, 'p_oldsystem',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMeshCoordinateSystem, 'p_newsystem',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMeshCoordinateSystem, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertMeshCoordinateSystem, 'Output Field',
                   (Field, "Field"))

  reg.add_module(ConvertMeshToPointCloud)
  reg.add_input_port(ConvertMeshToPointCloud, 'p_datalocation',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertMeshToPointCloud, 'Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertMeshToPointCloud, 'Field',
                   (Field, "Field"))

  reg.add_module(TransformMeshWithTransform)
  reg.add_input_port(TransformMeshWithTransform, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(TransformMeshWithTransform, 'Transform Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(TransformMeshWithTransform, 'Transformed Field',
                   (Field, "Field"))

  reg.add_module(ConvertRegularMeshToStructuredMesh)
  reg.add_input_port(ConvertRegularMeshToStructuredMesh, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertRegularMeshToStructuredMesh, 'Output Field',
                   (Field, "Field"))

  reg.add_module(CalculateMeshNodes)
  reg.add_input_port(CalculateMeshNodes, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateMeshNodes, 'Field',
                   (Field, "Field"))
  reg.add_input_port(CalculateMeshNodes, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CalculateMeshNodes, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(CalculateMeshNodes, 'Field',
                   (Field, "Field"))

  reg.add_module(SmoothMesh)
  reg.add_input_port(SmoothMesh, 'Input',
                   (Field, "Field"))
  reg.add_input_port(SmoothMesh, 'IsoValue',
                   (Matrix, "Matrix"))
  reg.add_output_port(SmoothMesh, 'Smoothed',
                   (Field, "Field"))

  reg.add_module(EditMeshBoundingBox)
  reg.add_input_port(EditMeshBoundingBox, 'p_outputcenterx',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_outputcentery',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_outputcenterz',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_outputsizex',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_outputsizey',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_outputsizez',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_useoutputcenter',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_useoutputsize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_mode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_real_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_center_x',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_center_y',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_center_z',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_right_x',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_right_y',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_right_z',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_down_x',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_down_y',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_down_z',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_in_x',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_in_y',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'p_box_in_z',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EditMeshBoundingBox, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(EditMeshBoundingBox, 'Output Field',
                   (Field, "Field"))
  reg.add_output_port(EditMeshBoundingBox, 'Transformation Widget',
                   (Geometry, "Geometry"))
  reg.add_output_port(EditMeshBoundingBox, 'Transformation Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(SwapNodeLocationsWithMatrixEntries)
  reg.add_input_port(SwapNodeLocationsWithMatrixEntries, 'Input Field',
                   (Field, "Field"))
  reg.add_input_port(SwapNodeLocationsWithMatrixEntries, 'Input Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(SwapNodeLocationsWithMatrixEntries, 'Output Field',
                   (Field, "Field"))
  reg.add_output_port(SwapNodeLocationsWithMatrixEntries, 'Output Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(MapFieldDataToNodeCoordinate)
  reg.add_input_port(MapFieldDataToNodeCoordinate, 'p_coord',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(MapFieldDataToNodeCoordinate, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(MapFieldDataToNodeCoordinate, 'Output Field',
                   (Field, "Field"))

  reg.add_module(ScaleFieldMeshAndData)
  reg.add_input_port(ScaleFieldMeshAndData, 'p_datascale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ScaleFieldMeshAndData, 'p_geomscale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ScaleFieldMeshAndData, 'p_usegeomcenter',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ScaleFieldMeshAndData, 'Field',
                   (Field, "Field"))
  reg.add_input_port(ScaleFieldMeshAndData, 'GeomScaleFactor',
                   (Matrix, "Matrix"))
  reg.add_input_port(ScaleFieldMeshAndData, 'DataScaleFactor',
                   (Matrix, "Matrix"))
  reg.add_output_port(ScaleFieldMeshAndData, 'Field',
                   (Field, "Field"))

  reg.add_module(ReportColumnMatrixMisfit)
  reg.add_input_port(ReportColumnMatrixMisfit, 'p_have_ui',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportColumnMatrixMisfit, 'p_methodTCL',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportColumnMatrixMisfit, 'p_pTCL',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportColumnMatrixMisfit, 'Vec1',
                   (Matrix, "Matrix"))
  reg.add_input_port(ReportColumnMatrixMisfit, 'Vec2',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportColumnMatrixMisfit, 'Error Out',
                   (Matrix, "Matrix"))

  reg.add_module(EvaluateLinAlgGeneral)
  reg.add_input_port(EvaluateLinAlgGeneral, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EvaluateLinAlgGeneral, 'i1',
                   (Matrix, "Matrix"))
  reg.add_input_port(EvaluateLinAlgGeneral, 'i2',
                   (Matrix, "Matrix"))
  reg.add_input_port(EvaluateLinAlgGeneral, 'i3',
                   (Matrix, "Matrix"))
  reg.add_input_port(EvaluateLinAlgGeneral, 'i4',
                   (Matrix, "Matrix"))
  reg.add_input_port(EvaluateLinAlgGeneral, 'i5',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgGeneral, 'o1',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgGeneral, 'o2',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgGeneral, 'o3',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgGeneral, 'o4',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgGeneral, 'o5',
                   (Matrix, "Matrix"))

  reg.add_module(AppendMatrix)
  reg.add_input_port(AppendMatrix, 'p_row_or_column',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(AppendMatrix, 'BaseMatrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(AppendMatrix, 'AppendMatrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(AppendMatrix, 'Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(EvaluateLinAlgBinary)
  reg.add_input_port(EvaluateLinAlgBinary, 'p_op',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EvaluateLinAlgBinary, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EvaluateLinAlgBinary, 'A',
                   (Matrix, "Matrix"))
  reg.add_input_port(EvaluateLinAlgBinary, 'B',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgBinary, 'Output',
                   (Matrix, "Matrix"))

  reg.add_module(ConvertMaskVectorToMappingMatrix)
  reg.add_input_port(ConvertMaskVectorToMappingMatrix, 'MaskVector',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ConvertMaskVectorToMappingMatrix, 'MappingMatrix',
                   (Matrix, "Matrix"))

  reg.add_module(SolveLinearSystem)
  reg.add_input_port(SolveLinearSystem, 'p_target_error',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_flops',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_floprate',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_memrefs',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_memrate',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_orig_error',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_current_error',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_precond',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_iteration',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_maxiter',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_use_previous_soln',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_emit_partial',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_emit_iter',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_status',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'p_np',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SolveLinearSystem, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(SolveLinearSystem, 'RHS',
                   (Matrix, "Matrix"))
  reg.add_output_port(SolveLinearSystem, 'Solution',
                   (Matrix, "Matrix"))

  reg.add_module(ReportMatrixColumnMeasure)
  reg.add_input_port(ReportMatrixColumnMeasure, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportMatrixColumnMeasure, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportMatrixColumnMeasure, 'Vector',
                   (Matrix, "Matrix"))

  reg.add_module(SortMatrix)
  reg.add_input_port(SortMatrix, 'p_row_or_col',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SortMatrix, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(SortMatrix, 'Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(CreateGeometricTransform)
  reg.add_input_port(CreateGeometricTransform, 'p_rotate_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_rotate_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_rotate_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_rotate_theta',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_translate_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_translate_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_translate_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_scale_uniform',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_scale_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_scale_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_scale_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_shear_plane_a',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_shear_plane_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_shear_plane_c',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_widget_resizable',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_permute_x',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_permute_y',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_permute_z',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_pre_transform',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_which_transform',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_widget_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'p_ignoring_widget_changes',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateGeometricTransform, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateGeometricTransform, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateGeometricTransform, 'Geometry',
                   (Geometry, "Geometry"))

  reg.add_module(ChooseMatrix)
  reg.add_input_port(ChooseMatrix, 'p_use_first_valid',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseMatrix, 'p_port_valid_index',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseMatrix, 'p_port_selected_index',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseMatrix, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ChooseMatrix, 'Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(ConvertMappingMatrixToMaskVector)
  reg.add_input_port(ConvertMappingMatrixToMaskVector, 'MappingMatrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ConvertMappingMatrixToMaskVector, 'MaskVector',
                   (Nrrd, "Nrrd"))

  reg.add_module(ResizeMatrix)
  reg.add_input_port(ResizeMatrix, 'p_dim_m',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ResizeMatrix, 'p_dim_n',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ResizeMatrix, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(ResizeMatrix, 'M',
                   (Matrix, "Matrix"))
  reg.add_input_port(ResizeMatrix, 'N',
                   (Matrix, "Matrix"))
  reg.add_output_port(ResizeMatrix, 'Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(CollectMatrices)
  reg.add_input_port(CollectMatrices, 'p_append',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CollectMatrices, 'p_row',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CollectMatrices, 'p_front',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CollectMatrices, 'Optional BaseMatrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(CollectMatrices, 'SubMatrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(CollectMatrices, 'CompositeMatrix',
                   (Matrix, "Matrix"))

  reg.add_module(GetColumnOrRowFromMatrix)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_row_or_col',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_selectable_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_selectable_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_selectable_inc',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_selectable_units',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_range_min',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_range_max',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_playmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_current',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_execmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_delay',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_inc_amount',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_send_amount',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'p_data_series_done',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetColumnOrRowFromMatrix, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(GetColumnOrRowFromMatrix, 'Weight Vector',
                   (Matrix, "Matrix"))
  reg.add_input_port(GetColumnOrRowFromMatrix, 'Current Index',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetColumnOrRowFromMatrix, 'Vector',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetColumnOrRowFromMatrix, 'Selected Index',
                   (Matrix, "Matrix"))

  reg.add_module(BuildNoiseColumnMatrix)
  reg.add_input_port(BuildNoiseColumnMatrix, 'p_snr',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(BuildNoiseColumnMatrix, 'Signal',
                   (Matrix, "Matrix"))
  reg.add_output_port(BuildNoiseColumnMatrix, 'Noise',
                   (Matrix, "Matrix"))

  reg.add_module(EvaluateLinAlgUnary)
  reg.add_input_port(EvaluateLinAlgUnary, 'p_op',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EvaluateLinAlgUnary, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(EvaluateLinAlgUnary, 'Input',
                   (Matrix, "Matrix"))
  reg.add_output_port(EvaluateLinAlgUnary, 'Output',
                   (Matrix, "Matrix"))

  reg.add_module(GetSubmatrix)
  reg.add_input_port(GetSubmatrix, 'p_mincol',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSubmatrix, 'p_maxcol',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSubmatrix, 'p_minrow',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSubmatrix, 'p_maxrow',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSubmatrix, 'p_nrow',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSubmatrix, 'p_ncol',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetSubmatrix, 'Input Matrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(GetSubmatrix, 'Optional Range Bounds',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetSubmatrix, 'Output Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(ReorderMatrixByReverseCuthillMcKee)
  reg.add_input_port(ReorderMatrixByReverseCuthillMcKee, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReorderMatrixByReverseCuthillMcKee, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReorderMatrixByReverseCuthillMcKee, 'Mapping',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReorderMatrixByReverseCuthillMcKee, 'InverseMapping',
                   (Matrix, "Matrix"))

  reg.add_module(CreateMatrix)
  reg.add_input_port(CreateMatrix, 'p_rows',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateMatrix, 'p_cols',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateMatrix, 'p_data',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateMatrix, 'p_clabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateMatrix, 'p_rlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_output_port(CreateMatrix, 'matrix',
                   (Matrix, "Matrix"))

  reg.add_module(SolveMinNormLeastSqSystem)
  reg.add_input_port(SolveMinNormLeastSqSystem, 'BasisVec1',
                   (Matrix, "Matrix"))
  reg.add_input_port(SolveMinNormLeastSqSystem, 'BasisVec2',
                   (Matrix, "Matrix"))
  reg.add_input_port(SolveMinNormLeastSqSystem, 'BasisVec3',
                   (Matrix, "Matrix"))
  reg.add_input_port(SolveMinNormLeastSqSystem, 'TargetVec',
                   (Matrix, "Matrix"))
  reg.add_output_port(SolveMinNormLeastSqSystem, 'WeightVec(Col)',
                   (Matrix, "Matrix"))
  reg.add_output_port(SolveMinNormLeastSqSystem, 'ResultVec(Col)',
                   (Matrix, "Matrix"))

  reg.add_module(ConvertMatrixType)
  reg.add_input_port(ConvertMatrixType, 'p_oldtype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatrixType, 'p_newtype',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatrixType, 'p_nrow',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatrixType, 'p_ncol',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatrixType, 'Input',
                   (Matrix, "Matrix"))
  reg.add_output_port(ConvertMatrixType, 'Output',
                   (Matrix, "Matrix"))

  reg.add_module(ReportMatrixRowMeasure)
  reg.add_input_port(ReportMatrixRowMeasure, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportMatrixRowMeasure, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportMatrixRowMeasure, 'Vector',
                   (Matrix, "Matrix"))

  reg.add_module(ReorderMatrixByCuthillMcKee)
  reg.add_input_port(ReorderMatrixByCuthillMcKee, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReorderMatrixByCuthillMcKee, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReorderMatrixByCuthillMcKee, 'Mapping',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReorderMatrixByCuthillMcKee, 'InverseMapping',
                   (Matrix, "Matrix"))

  reg.add_module(ReportMatrixInfo)
  reg.add_input_port(ReportMatrixInfo, 'Input',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportMatrixInfo, 'NumRows',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportMatrixInfo, 'NumCols',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportMatrixInfo, 'NumElements',
                   (Matrix, "Matrix"))

  reg.add_module(RemoveZerosFromMatrix)
  reg.add_input_port(RemoveZerosFromMatrix, 'p_row_or_col',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(RemoveZerosFromMatrix, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(RemoveZerosFromMatrix, 'Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(RemoveZeroRowsAndColumns)
  reg.add_input_port(RemoveZeroRowsAndColumns, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(RemoveZeroRowsAndColumns, 'ReducedMatrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(RemoveZeroRowsAndColumns, 'LeftMapping',
                   (Matrix, "Matrix"))
  reg.add_output_port(RemoveZeroRowsAndColumns, 'RightMapping',
                   (Matrix, "Matrix"))

  reg.add_module(CreateDataArray)
  reg.add_input_port(CreateDataArray, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateDataArray, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateDataArray, 'Size',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateDataArray, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CreateDataArray, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateDataArray, 'DataArray',
                   (Matrix, "Matrix"))

  reg.add_module(CreateDataArrayFromIndices)
  reg.add_input_port(CreateDataArrayFromIndices, 'Indices',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateDataArrayFromIndices, 'Template',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateDataArrayFromIndices, 'DataArray',
                   (Matrix, "Matrix"))

  reg.add_module(ReportDataArrayInfo)
  reg.add_input_port(ReportDataArrayInfo, 'DataArray',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportDataArrayInfo, 'NumElements',
                   (Matrix, "Matrix"))

  reg.add_module(CreateVectorArray)
  reg.add_input_port(CreateVectorArray, 'X',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateVectorArray, 'Y',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateVectorArray, 'Z',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateVectorArray, 'Vector',
                   (Matrix, "Matrix"))

  reg.add_module(ReplicateDataArray)
  reg.add_input_port(ReplicateDataArray, 'p_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReplicateDataArray, 'DataArray',
                   (Matrix, "Matrix"))
  reg.add_input_port(ReplicateDataArray, 'Size',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReplicateDataArray, 'DataArray',
                   (Matrix, "Matrix"))

  reg.add_module(SplitVectorArrayInXYZ)
  reg.add_input_port(SplitVectorArrayInXYZ, 'VectorArray',
                   (Matrix, "Matrix"))
  reg.add_output_port(SplitVectorArrayInXYZ, 'X',
                   (Matrix, "Matrix"))
  reg.add_output_port(SplitVectorArrayInXYZ, 'Y',
                   (Matrix, "Matrix"))
  reg.add_output_port(SplitVectorArrayInXYZ, 'Z',
                   (Matrix, "Matrix"))

  reg.add_module(DecomposeTensorArrayIntoEigenVectors)
  reg.add_input_port(DecomposeTensorArrayIntoEigenVectors, 'TensorArray',
                   (Matrix, "Matrix"))
  reg.add_output_port(DecomposeTensorArrayIntoEigenVectors, 'EigenVector1',
                   (Matrix, "Matrix"))
  reg.add_output_port(DecomposeTensorArrayIntoEigenVectors, 'EigenVector2',
                   (Matrix, "Matrix"))
  reg.add_output_port(DecomposeTensorArrayIntoEigenVectors, 'EigenVector3',
                   (Matrix, "Matrix"))
  reg.add_output_port(DecomposeTensorArrayIntoEigenVectors, 'EigenValue1',
                   (Matrix, "Matrix"))
  reg.add_output_port(DecomposeTensorArrayIntoEigenVectors, 'EigenValue2',
                   (Matrix, "Matrix"))
  reg.add_output_port(DecomposeTensorArrayIntoEigenVectors, 'EigenValue3',
                   (Matrix, "Matrix"))

  reg.add_module(CalculateDataArray)
  reg.add_input_port(CalculateDataArray, 'p_function',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateDataArray, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CalculateDataArray, 'DataArray',
                   (Matrix, "Matrix"))
  reg.add_input_port(CalculateDataArray, 'Function',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(CalculateDataArray, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(CalculateDataArray, 'DataArray',
                   (Matrix, "Matrix"))

  reg.add_module(ReportDataArrayMeasure)
  reg.add_input_port(ReportDataArrayMeasure, 'p_measure',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportDataArrayMeasure, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportDataArrayMeasure, 'Measure',
                   (Matrix, "Matrix"))

  reg.add_module(AppendDataArrays)
  reg.add_input_port(AppendDataArrays, 'Array',
                   (Matrix, "Matrix"))
  reg.add_output_port(AppendDataArrays, 'Array',
                   (Matrix, "Matrix"))

  reg.add_module(CreateTensorArray)
  reg.add_input_port(CreateTensorArray, 'EigenVector1',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateTensorArray, 'EigenVector2',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateTensorArray, 'EigenValue1',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateTensorArray, 'EigenValue2',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateTensorArray, 'EigenValue3',
                   (Matrix, "Matrix"))
  reg.add_output_port(CreateTensorArray, 'TensorArray',
                   (Matrix, "Matrix"))

  reg.add_module(PrintMatrixIntoString)
  reg.add_input_port(PrintMatrixIntoString, 'p_formatstring',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(PrintMatrixIntoString, 'Format',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(PrintMatrixIntoString, 'Input',
                   (Matrix, "Matrix"))
  reg.add_output_port(PrintMatrixIntoString, 'Output',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(GetFileName)
  reg.add_input_port(GetFileName, 'p_filename_base',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFileName, 'p_delay',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetFileName, 'p_pinned',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_output_port(GetFileName, 'Full Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(SplitFileName)
  reg.add_input_port(SplitFileName, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(SplitFileName, 'Pathname',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(SplitFileName, 'Filename Base',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(SplitFileName, 'Extension',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(SplitFileName, 'Filename',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(PrintStringIntoString)
  reg.add_input_port(PrintStringIntoString, 'p_formatstring',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(PrintStringIntoString, 'Format',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(PrintStringIntoString, 'Input',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(PrintStringIntoString, 'Output',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(CreateString)
  reg.add_input_port(CreateString, 'p_inputstring',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_output_port(CreateString, 'Output',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ReportStringInfo)
  reg.add_input_port(ReportStringInfo, 'p_inputstring',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportStringInfo, 'Input',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(JoinStrings)
  reg.add_input_port(JoinStrings, 'input',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(JoinStrings, 'Output',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(GetNetworkFileName)
  reg.add_output_port(GetNetworkFileName, 'String',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(SetFieldProperty)
  reg.add_input_port(SetFieldProperty, 'p_num_entries',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldProperty, 'p_property',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldProperty, 'p_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldProperty, 'p_value',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldProperty, 'p_readonly',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldProperty, 'Field',
                   (Field, "Field"))
  reg.add_output_port(SetFieldProperty, 'Field',
                   (Field, "Field"))

  reg.add_module(ReportScalarFieldStats)
  reg.add_input_port(ReportScalarFieldStats, 'p_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'p_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'p_mean',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'p_median',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'p_sigma',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'p_is_fixed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'p_nbuckets',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportScalarFieldStats, 'Input Field',
                   (Field, "Field"))

  reg.add_module(SelectFieldROIWithBoxWidget)
  reg.add_input_port(SelectFieldROIWithBoxWidget, 'p_stampvalue',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SelectFieldROIWithBoxWidget, 'p_runmode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SelectFieldROIWithBoxWidget, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(SelectFieldROIWithBoxWidget, 'Selection Widget',
                   (Geometry, "Geometry"))
  reg.add_output_port(SelectFieldROIWithBoxWidget, 'Output Field',
                   (Field, "Field"))

  reg.add_module(BuildMatrixOfSurfaceNormals)
  reg.add_input_port(BuildMatrixOfSurfaceNormals, 'Surface Field',
                   (Field, "Field"))
  reg.add_output_port(BuildMatrixOfSurfaceNormals, 'Nodal Surface Normals',
                   (Matrix, "Matrix"))

  reg.add_module(ReportFieldInfo)
  reg.add_input_port(ReportFieldInfo, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ReportFieldInfo, 'NumNodes',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'NumElements',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'NumData',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'DataMin',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'DataMax',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'FieldSize',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'FieldCenter',
                   (Matrix, "Matrix"))
  reg.add_output_port(ReportFieldInfo, 'Dimensions',
                   (Matrix, "Matrix"))

  reg.add_module(ReportFieldGeometryMeasures)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_simplexString',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_xFlag',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_yFlag',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_zFlag',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_idxFlag',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_sizeFlag',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'p_normalsFlag',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ReportFieldGeometryMeasures, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ReportFieldGeometryMeasures, 'Output Measures Matrix',
                   (Matrix, "Matrix"))

  reg.add_module(SetFieldOrMeshStringProperty)
  reg.add_input_port(SetFieldOrMeshStringProperty, 'p_prop',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldOrMeshStringProperty, 'p_val',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(SetFieldOrMeshStringProperty, 'p_meshprop',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(SetFieldOrMeshStringProperty, 'Input',
                   (Field, "Field"))
  reg.add_output_port(SetFieldOrMeshStringProperty, 'Output',
                   (Field, "Field"))

  reg.add_module(ManageFieldSeries)
  reg.add_input_port(ManageFieldSeries, 'p_num_ports',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ManageFieldSeries, 'Input',
                   (Field, "Field"))
  reg.add_output_port(ManageFieldSeries, 'Output 0',
                   (Field, "Field"))
  reg.add_output_port(ManageFieldSeries, 'Output 1',
                   (Field, "Field"))
  reg.add_output_port(ManageFieldSeries, 'Output 2',
                   (Field, "Field"))
  reg.add_output_port(ManageFieldSeries, 'Output 3',
                   (Field, "Field"))

  reg.add_module(ReportSearchGridInfo)
  reg.add_input_port(ReportSearchGridInfo, 'Input Field',
                   (Field, "Field"))
  reg.add_output_port(ReportSearchGridInfo, 'Output Sample Field',
                   (Field, "Field"))

  reg.add_module(ChooseField)
  reg.add_input_port(ChooseField, 'p_use_first_valid',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseField, 'p_port_valid_index',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseField, 'p_port_selected_index',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseField, 'Field',
                   (Field, "Field"))
  reg.add_output_port(ChooseField, 'Field',
                   (Field, "Field"))

  reg.add_module(BuildPointCloudToLatVolMappingMatrix)
  reg.add_input_port(BuildPointCloudToLatVolMappingMatrix, 'p_epsilon',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(BuildPointCloudToLatVolMappingMatrix, 'PointCloudField',
                   (Field, "Field"))
  reg.add_input_port(BuildPointCloudToLatVolMappingMatrix, 'LatVolField',
                   (Field, "Field"))
  reg.add_output_port(BuildPointCloudToLatVolMappingMatrix, 'MappingMatrix',
                   (Matrix, "Matrix"))

  reg.add_module(BuildMappingMatrix)
  reg.add_input_port(BuildMappingMatrix, 'p_interpolation_basis',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(BuildMappingMatrix, 'p_map_source_to_single_dest',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(BuildMappingMatrix, 'p_exhaustive_search',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(BuildMappingMatrix, 'p_exhaustive_search_max_dist',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(BuildMappingMatrix, 'p_np',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(BuildMappingMatrix, 'Source',
                   (Field, "Field"))
  reg.add_input_port(BuildMappingMatrix, 'Destination',
                   (Field, "Field"))
  reg.add_output_port(BuildMappingMatrix, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(CoregisterPointClouds)
  reg.add_input_port(CoregisterPointClouds, 'p_allowScale',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'p_allowRotate',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'p_allowTranslate',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'p_seed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'p_iters',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'p_misfitTol',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'p_method',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CoregisterPointClouds, 'Fixed PointCloudField',
                   (Field, "Field"))
  reg.add_input_port(CoregisterPointClouds, 'Mobile PointCloudField',
                   (Field, "Field"))
  reg.add_input_port(CoregisterPointClouds, 'DistanceField From Fixed',
                   (Field, "Field"))
  reg.add_output_port(CoregisterPointClouds, 'Transform',
                   (Matrix, "Matrix"))

  reg.add_module(CollectPointClouds)
  reg.add_input_port(CollectPointClouds, 'p_num_fields',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CollectPointClouds, 'Point Cloud',
                   (Field, "Field"))
  reg.add_output_port(CollectPointClouds, 'Curve',
                   (Field, "Field"))

  reg.add_module(GetColorMapsFromBundle)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'p_colormap_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMapsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetColorMapsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetColorMapsFromBundle, 'colormap1',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(GetColorMapsFromBundle, 'colormap2',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(GetColorMapsFromBundle, 'colormap3',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(GetColorMapsFromBundle, 'colormap4',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(GetColorMapsFromBundle, 'colormap5',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(GetColorMapsFromBundle, 'colormap6',
                   (ColorMap, "ColorMap"))

  reg.add_module(InsertFieldsIntoBundle)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_field1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_field2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_field3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_field4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_field5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_field6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertFieldsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertFieldsIntoBundle, 'field1',
                   (Field, "Field"))
  reg.add_input_port(InsertFieldsIntoBundle, 'field2',
                   (Field, "Field"))
  reg.add_input_port(InsertFieldsIntoBundle, 'field3',
                   (Field, "Field"))
  reg.add_input_port(InsertFieldsIntoBundle, 'field4',
                   (Field, "Field"))
  reg.add_input_port(InsertFieldsIntoBundle, 'field5',
                   (Field, "Field"))
  reg.add_input_port(InsertFieldsIntoBundle, 'field6',
                   (Field, "Field"))
  reg.add_output_port(InsertFieldsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(GetFieldsFromBundle)
  reg.add_input_port(GetFieldsFromBundle, 'p_field1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'p_field2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'p_field3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'p_field4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'p_field5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'p_field6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'p_field_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetFieldsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetFieldsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetFieldsFromBundle, 'field1',
                   (Field, "Field"))
  reg.add_output_port(GetFieldsFromBundle, 'field2',
                   (Field, "Field"))
  reg.add_output_port(GetFieldsFromBundle, 'field3',
                   (Field, "Field"))
  reg.add_output_port(GetFieldsFromBundle, 'field4',
                   (Field, "Field"))
  reg.add_output_port(GetFieldsFromBundle, 'field5',
                   (Field, "Field"))
  reg.add_output_port(GetFieldsFromBundle, 'field6',
                   (Field, "Field"))

  reg.add_module(InsertColorMap2sIntoBundle)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_colormap21_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_colormap22_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_colormap23_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_colormap24_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_colormap25_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_colormap26_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMap2sIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertColorMap2sIntoBundle, 'colormap21',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(InsertColorMap2sIntoBundle, 'colormap22',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(InsertColorMap2sIntoBundle, 'colormap23',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(InsertColorMap2sIntoBundle, 'colormap24',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(InsertColorMap2sIntoBundle, 'colormap25',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(InsertColorMap2sIntoBundle, 'colormap26',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(InsertColorMap2sIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(GetBundlesFromBundle)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'p_bundle_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetBundlesFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle1',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle2',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle3',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle4',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle5',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetBundlesFromBundle, 'bundle6',
                   (Bundle, "Bundle"))

  reg.add_module(GetPathsFromBundle)
  reg.add_input_port(GetPathsFromBundle, 'p_path1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'p_path2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'p_path3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'p_path4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'p_path5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'p_path6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'p_path_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetPathsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetPathsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetPathsFromBundle, 'path1',
                   (Path, "Path"))
  reg.add_output_port(GetPathsFromBundle, 'path2',
                   (Path, "Path"))
  reg.add_output_port(GetPathsFromBundle, 'path3',
                   (Path, "Path"))
  reg.add_output_port(GetPathsFromBundle, 'path4',
                   (Path, "Path"))
  reg.add_output_port(GetPathsFromBundle, 'path5',
                   (Path, "Path"))
  reg.add_output_port(GetPathsFromBundle, 'path6',
                   (Path, "Path"))

  reg.add_module(InsertStringsIntoBundle)
  reg.add_input_port(InsertStringsIntoBundle, 'p_string1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_string2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_string3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_string4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_string5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_string6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertStringsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertStringsIntoBundle, 'string1',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(InsertStringsIntoBundle, 'string2',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(InsertStringsIntoBundle, 'string3',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(InsertStringsIntoBundle, 'string4',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(InsertStringsIntoBundle, 'string5',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_input_port(InsertStringsIntoBundle, 'string6',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(InsertStringsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(GetNrrdsFromBundle)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_transposenrrd1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_transposenrrd2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_transposenrrd3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_transposenrrd4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_transposenrrd5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_transposenrrd6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'p_nrrd_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetNrrdsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetNrrdsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetNrrdsFromBundle, 'nrrd1',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(GetNrrdsFromBundle, 'nrrd2',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(GetNrrdsFromBundle, 'nrrd3',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(GetNrrdsFromBundle, 'nrrd4',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(GetNrrdsFromBundle, 'nrrd5',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(GetNrrdsFromBundle, 'nrrd6',
                   (Nrrd, "Nrrd"))

  reg.add_module(GetMatricesFromBundle)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_transposenrrd1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_transposenrrd2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_transposenrrd3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_transposenrrd4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_transposenrrd5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_transposenrrd6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'p_matrix_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetMatricesFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetMatricesFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetMatricesFromBundle, 'matrix1',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetMatricesFromBundle, 'matrix2',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetMatricesFromBundle, 'matrix3',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetMatricesFromBundle, 'matrix4',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetMatricesFromBundle, 'matrix5',
                   (Matrix, "Matrix"))
  reg.add_output_port(GetMatricesFromBundle, 'matrix6',
                   (Matrix, "Matrix"))

  reg.add_module(JoinBundles)
  reg.add_input_port(JoinBundles, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(JoinBundles, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(ReportBundleInfo)
  reg.add_input_port(ReportBundleInfo, 'p_tclinfostring',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ReportBundleInfo, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(InsertPathsIntoBundle)
  reg.add_input_port(InsertPathsIntoBundle, 'p_path1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_path2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_path3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_path4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_path5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_path6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertPathsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertPathsIntoBundle, 'path1',
                   (Path, "Path"))
  reg.add_input_port(InsertPathsIntoBundle, 'path2',
                   (Path, "Path"))
  reg.add_input_port(InsertPathsIntoBundle, 'path3',
                   (Path, "Path"))
  reg.add_input_port(InsertPathsIntoBundle, 'path4',
                   (Path, "Path"))
  reg.add_input_port(InsertPathsIntoBundle, 'path5',
                   (Path, "Path"))
  reg.add_input_port(InsertPathsIntoBundle, 'path6',
                   (Path, "Path"))
  reg.add_output_port(InsertPathsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(GetColorMap2sFromBundle)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap21_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap22_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap23_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap24_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap25_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap26_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'p_colormap2_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetColorMap2sFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetColorMap2sFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetColorMap2sFromBundle, 'colormap21',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(GetColorMap2sFromBundle, 'colormap22',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(GetColorMap2sFromBundle, 'colormap23',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(GetColorMap2sFromBundle, 'colormap24',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(GetColorMap2sFromBundle, 'colormap25',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(GetColorMap2sFromBundle, 'colormap26',
                   (ColorMap2, "ColorMap2"))

  reg.add_module(InsertMatricesIntoBundle)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_matrix1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_matrix2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_matrix3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_matrix4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_matrix5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_matrix6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertMatricesIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertMatricesIntoBundle, 'matrix1',
                   (Matrix, "Matrix"))
  reg.add_input_port(InsertMatricesIntoBundle, 'matrix2',
                   (Matrix, "Matrix"))
  reg.add_input_port(InsertMatricesIntoBundle, 'matrix3',
                   (Matrix, "Matrix"))
  reg.add_input_port(InsertMatricesIntoBundle, 'matrix4',
                   (Matrix, "Matrix"))
  reg.add_input_port(InsertMatricesIntoBundle, 'matrix5',
                   (Matrix, "Matrix"))
  reg.add_input_port(InsertMatricesIntoBundle, 'matrix6',
                   (Matrix, "Matrix"))
  reg.add_output_port(InsertMatricesIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(InsertNrrdsIntoBundle)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_nrrd1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_nrrd2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_nrrd3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_nrrd4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_nrrd5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_nrrd6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertNrrdsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertNrrdsIntoBundle, 'nrrd1',
                   (Nrrd, "Nrrd"))
  reg.add_input_port(InsertNrrdsIntoBundle, 'nrrd2',
                   (Nrrd, "Nrrd"))
  reg.add_input_port(InsertNrrdsIntoBundle, 'nrrd3',
                   (Nrrd, "Nrrd"))
  reg.add_input_port(InsertNrrdsIntoBundle, 'nrrd4',
                   (Nrrd, "Nrrd"))
  reg.add_input_port(InsertNrrdsIntoBundle, 'nrrd5',
                   (Nrrd, "Nrrd"))
  reg.add_input_port(InsertNrrdsIntoBundle, 'nrrd6',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(InsertNrrdsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(InsertBundlesIntoBundle)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundle1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundle2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundle3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundle4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundle5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundle6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle1',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle2',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle3',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle4',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle5',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertBundlesIntoBundle, 'bundle6',
                   (Bundle, "Bundle"))
  reg.add_output_port(InsertBundlesIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(GetStringsFromBundle)
  reg.add_input_port(GetStringsFromBundle, 'p_string1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'p_string2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'p_string3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'p_string4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'p_string5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'p_string6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'p_string_selection',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(GetStringsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetStringsFromBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_output_port(GetStringsFromBundle, 'string1',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(GetStringsFromBundle, 'string2',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(GetStringsFromBundle, 'string3',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(GetStringsFromBundle, 'string4',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(GetStringsFromBundle, 'string5',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(GetStringsFromBundle, 'string6',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(InsertColorMapsIntoBundle)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_colormap1_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_colormap2_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_colormap3_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_colormap4_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_colormap5_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_colormap6_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_replace1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_replace2',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_replace3',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_replace4',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_replace5',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_replace6',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'p_bundlename',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(InsertColorMapsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))
  reg.add_input_port(InsertColorMapsIntoBundle, 'colormap1',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(InsertColorMapsIntoBundle, 'colormap2',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(InsertColorMapsIntoBundle, 'colormap3',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(InsertColorMapsIntoBundle, 'colormap4',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(InsertColorMapsIntoBundle, 'colormap5',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(InsertColorMapsIntoBundle, 'colormap6',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(InsertColorMapsIntoBundle, 'bundle',
                   (Bundle, "Bundle"))

  reg.add_module(CreateParameterBundle)
  reg.add_input_port(CreateParameterBundle, 'p_data',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateParameterBundle, 'p_new_field_count',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateParameterBundle, 'p_update_all',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_output_port(CreateParameterBundle, 'ParameterList',
                   (Bundle, "Bundle"))

  reg.add_module(InsertEnvironmentIntoBundle)
  reg.add_output_port(InsertEnvironmentIntoBundle, 'Environment',
                   (Bundle, "Bundle"))

  reg.add_module(ShowColorMap)
  reg.add_input_port(ShowColorMap, 'p_length',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_side',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_numlabels',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_numsigdigits',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_units',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_text_fontsize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'p_extra_padding',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(ShowColorMap, 'Geometry',
                   (Geometry, "Geometry"))

  reg.add_module(CreateAndEditColorMap2D)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_histo',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_selected_widget',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_selected_object',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_num_entries',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_marker',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_cm2view_targ',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'p_id',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap2D, 'Input Colormap',
                   (ColorMap2, "ColorMap2"))
  reg.add_input_port(CreateAndEditColorMap2D, 'Histogram',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(CreateAndEditColorMap2D, 'Output Colormap',
                   (ColorMap2, "ColorMap2"))

  reg.add_module(ShowField)
  reg.add_input_port(ShowField, 'p_nodes_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_nodes_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_nodes_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_nodes_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowField, 'p_faces_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_faces_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_faces_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_faces_normals',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_faces_usetexture',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_backface_cull',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_always_visible',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_fontsize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_precision',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_render_locations',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_show_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_show_nodes',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_show_edges',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_show_faces',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_text_show_cells',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_def_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_def_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_def_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_def_color_a',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_nodes_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_nodes_scaleNV',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_scaleNV',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowField, 'p_active_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowField, 'p_interactive_mode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowField, 'p_show_progress',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_field_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowField, 'p_field_name_override',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_nodes_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_edges_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_approx_div',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'p_use_default_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowField, 'Mesh',
                   (Field, "Field"))
  reg.add_input_port(ShowField, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(ShowField, 'Scene Graph',
                   (Geometry, "Geometry"))

  reg.add_module(ExtractIsosurface)
  reg.add_input_port(ExtractIsosurface, 'p_isoval_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_isoval_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_isoval',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_isoval_typed',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_isoval_quantity',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_quantity_range',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_quantity_clusive',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_quantity_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_quantity_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_quantity_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_isoval_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_matrix_list',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_algorithm',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_build_trisurf',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_build_geom',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_np',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_active_isoval_selection_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_active_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_update_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'p_color_a',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ExtractIsosurface, 'Field',
                   (Field, "Field"))
  reg.add_input_port(ExtractIsosurface, 'Optional Color Map',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(ExtractIsosurface, 'Optional Isovalues',
                   (Matrix, "Matrix"))
  reg.add_output_port(ExtractIsosurface, 'Surface',
                   (Field, "Field"))
  reg.add_output_port(ExtractIsosurface, 'Geometry',
                   (Geometry, "Geometry"))
  reg.add_output_port(ExtractIsosurface, 'Mapping',
                   (Matrix, "Matrix"))

  reg.add_module(CreateViewerAxes)
  reg.add_input_port(CreateViewerAxes, 'p_precision',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_squash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_valuerez',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_labelrez',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_divisions',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_offset',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_range_first',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_range_second',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_min_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_max_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_minplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_maxplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_lines',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_minticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_maxticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_minlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_maxlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_minvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_maxvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_width',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_tickangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_ticktilt',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_ticksize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_labelangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_labelheight',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_valuesize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_0_Axis_valuesquash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_divisions',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_offset',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_range_first',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_range_second',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_min_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_max_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_minplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_maxplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_lines',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_minticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_maxticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_minlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_maxlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_minvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_maxvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_width',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_tickangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_ticktilt',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_ticksize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_labelangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_labelheight',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_valuesize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_01_1_Axis_valuesquash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_divisions',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_offset',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_range_first',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_range_second',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_min_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_max_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_minplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_maxplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_lines',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_minticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_maxticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_minlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_maxlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_minvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_maxvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_width',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_tickangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_ticktilt',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_ticksize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_labelangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_labelheight',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_valuesize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_0_Axis_valuesquash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_divisions',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_offset',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_range_first',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_range_second',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_min_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_max_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_minplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_maxplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_lines',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_minticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_maxticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_minlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_maxlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_minvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_maxvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_width',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_tickangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_ticktilt',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_ticksize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_labelangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_labelheight',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_valuesize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_02_2_Axis_valuesquash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_divisions',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_offset',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_range_first',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_range_second',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_min_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_max_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_minplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_maxplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_lines',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_minticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_maxticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_minlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_maxlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_minvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_maxvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_width',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_tickangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_ticktilt',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_ticksize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_labelangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_labelheight',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_valuesize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_1_Axis_valuesquash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_divisions',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_offset',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_range_first',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_range_second',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_min_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_max_absolute',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_minplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_maxplane',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_lines',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_minticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_maxticks',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_minlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_maxlabel',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_minvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_maxvalue',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_width',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_tickangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_ticktilt',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_ticksize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_labelangle',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_labelheight',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_valuesize',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'p_Plane_12_2_Axis_valuesquash',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerAxes, 'Field',
                   (Field, "Field"))
  reg.add_output_port(CreateViewerAxes, 'Axes',
                   (Geometry, "Geometry"))

  reg.add_module(RescaleColorMap)
  reg.add_input_port(RescaleColorMap, 'p_main_frame',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(RescaleColorMap, 'p_isFixed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(RescaleColorMap, 'p_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(RescaleColorMap, 'p_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(RescaleColorMap, 'p_makeSymmetric',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(RescaleColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(RescaleColorMap, 'Field',
                   (Field, "Field"))
  reg.add_output_port(RescaleColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))

  reg.add_module(ConvertNrrdsToTexture)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_vmin',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_vmax',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_gmin',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_gmax',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_mmin',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_mmax',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_is_fixed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_card_mem',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_card_mem_auto',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_is_uchar',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_histogram',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'p_gamma',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertNrrdsToTexture, 'Value Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_input_port(ConvertNrrdsToTexture, 'Gradient Magnitude Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(ConvertNrrdsToTexture, 'Texture',
                   (Texture, "Texture"))
  reg.add_output_port(ConvertNrrdsToTexture, 'JointHistoGram',
                   (Nrrd, "Nrrd"))

  reg.add_module(ChooseColorMap)
  reg.add_input_port(ChooseColorMap, 'p_use_first_valid',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseColorMap, 'p_port_valid_index',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseColorMap, 'p_port_selected_index',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ChooseColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(ChooseColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))

  reg.add_module(CreateLightForViewer)
  reg.add_input_port(CreateLightForViewer, 'p_control_pos_saved',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_control_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_control_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_control_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_at_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_at_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_at_z',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateLightForViewer, 'p_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_output_port(CreateLightForViewer, 'Geometry',
                   (Geometry, "Geometry"))

  reg.add_module(ShowTextureVolume)
  reg.add_input_port(ShowTextureVolume, 'p_sampling_rate_hi',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_sampling_rate_lo',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_gradient_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_gradient_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_adaptive',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_cmap_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_sw_raster',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_render_style',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_alpha_scale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_interp_mode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_shading',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_ambient',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_diffuse',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_specular',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_shine',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_light',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_blend_res',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_multi_level',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_use_stencil',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_invert_opacity',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_num_clipping_planes',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_show_clipping_widgets',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_level_on',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_level_vals',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'p_id',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowTextureVolume, 'Texture',
                   (Texture, "Texture"))
  reg.add_input_port(ShowTextureVolume, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(ShowTextureVolume, 'ColorMap2',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(ShowTextureVolume, 'Geometry',
                   (Geometry, "Geometry"))
  reg.add_output_port(ShowTextureVolume, 'ColorMap',
                   (ColorMap, "ColorMap"))

  reg.add_module(ShowFieldGlyphs)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_has_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_normalize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_scalars_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_has_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_normalize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_bidirectional',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_vectors_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_has_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_transparency',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_normalize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tensors_emphasis',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_secondary_has_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_secondary_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_secondary_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_secondary_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_secondary_alpha',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_secondary_value',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tertiary_has_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tertiary_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tertiary_display_type',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tertiary_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tertiary_alpha',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_tertiary_value',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_on',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_color_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_backface_cull',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_always_visible',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_fontsize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_precision',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_render_locations',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_show_data',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_show_nodes',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_show_edges',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_show_faces',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_text_show_cells',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_def_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_def_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_def_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_def_color_a',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_active_tab',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_interactive_mode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_show_progress',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_field_name',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_field_name_override',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_approx_div',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'p_use_default_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowFieldGlyphs, 'Primary Data',
                   (Field, "Field"))
  reg.add_input_port(ShowFieldGlyphs, 'Primary ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(ShowFieldGlyphs, 'Secondary Data',
                   (Field, "Field"))
  reg.add_input_port(ShowFieldGlyphs, 'Secondary ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(ShowFieldGlyphs, 'Tertiary Data',
                   (Field, "Field"))
  reg.add_input_port(ShowFieldGlyphs, 'Tertiary ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(ShowFieldGlyphs, 'Scene Graph',
                   (Geometry, "Geometry"))

  reg.add_module(GenerateStreamLines)
  reg.add_input_port(GenerateStreamLines, 'p_stepsize',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_tolerance',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_maxsteps',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_direction',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_value',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_remove_colinear_pts',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_method',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_nthreads',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'p_auto_parameterize',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLines, 'Vector Field',
                   (Field, "Field"))
  reg.add_input_port(GenerateStreamLines, 'Seed Points',
                   (Field, "Field"))
  reg.add_output_port(GenerateStreamLines, 'Streamlines',
                   (Field, "Field"))

  reg.add_module(GenerateStreamLinesWithPlacementHeuristic)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_numsl',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_numpts',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_minper',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_maxper',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_ming',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_maxg',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_numsamples',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_method',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_stepsize',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_stepout',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_maxsteps',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_minmag',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'p_direction',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'Source',
                   (Field, "Field"))
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'Weighting',
                   (Field, "Field"))
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'Flow',
                   (Field, "Field"))
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'Compare',
                   (Field, "Field"))
  reg.add_input_port(GenerateStreamLinesWithPlacementHeuristic, 'Seed points',
                   (Field, "Field"))
  reg.add_output_port(GenerateStreamLinesWithPlacementHeuristic, 'Streamlines',
                   (Field, "Field"))
  reg.add_output_port(GenerateStreamLinesWithPlacementHeuristic, 'Render',
                   (Field, "Field"))

  reg.add_module(ShowString)
  reg.add_input_port(ShowString, 'p_bbox',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowString, 'p_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowString, 'p_location_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowString, 'p_location_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowString, 'p_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowString, 'p_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowString, 'p_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowString, 'Format String',
                   (core.modules.basic_modules.String, 'tip'))
  reg.add_output_port(ShowString, 'Title',
                   (Geometry, "Geometry"))

  reg.add_module(CreateAndEditColorMap)
  reg.add_input_port(CreateAndEditColorMap, 'p_rgbhsv',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap, 'p_rgb_points',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap, 'p_alpha_points',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap, 'p_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateAndEditColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(CreateAndEditColorMap, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_output_port(CreateAndEditColorMap, 'Geometry',
                   (Geometry, "Geometry"))

  reg.add_module(ShowMeshBoundingBox)
  reg.add_input_port(ShowMeshBoundingBox, 'p_sizex',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMeshBoundingBox, 'p_sizey',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMeshBoundingBox, 'p_sizez',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMeshBoundingBox, 'Field',
                   (Field, "Field"))
  reg.add_output_port(ShowMeshBoundingBox, 'Scene Graph',
                   (Geometry, "Geometry"))

  reg.add_module(CreateStandardColorMaps)
  reg.add_input_port(CreateStandardColorMaps, 'p_mapName',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_gamma',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_resolution',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_reverse',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_faux',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_positionList',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_nodeList',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_width',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateStandardColorMaps, 'p_height',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_output_port(CreateStandardColorMaps, 'ColorMap',
                   (ColorMap, "ColorMap"))

  reg.add_module(ShowTextureSlices)
  reg.add_input_port(ShowTextureSlices, 'p_control_pos_saved',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_drawX',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_drawY',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_drawZ',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_drawView',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_interp_mode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_draw_phi_0',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_draw_phi_1',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_phi_0',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_phi_1',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_multi_level',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_color_changed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_colors',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_level_on',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_outline_levels',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'p_use_stencil',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowTextureSlices, 'Texture',
                   (Texture, "Texture"))
  reg.add_input_port(ShowTextureSlices, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(ShowTextureSlices, 'ColorMap2',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(ShowTextureSlices, 'Geometry',
                   (Geometry, "Geometry"))
  reg.add_output_port(ShowTextureSlices, 'ColorMap',
                   (ColorMap, "ColorMap"))

  reg.add_module(ShowMatrix)
  reg.add_input_port(ShowMatrix, 'p_xpos',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_ypos',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_xscale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_yscale',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_3d_mode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_gmode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_showtext',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_row_begin',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_rows',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_col_begin',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_cols',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'p_colormapmode',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ShowMatrix, 'ColorMap',
                   (ColorMap, "ColorMap"))
  reg.add_input_port(ShowMatrix, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ShowMatrix, 'Geometry',
                   (Geometry, "Geometry"))

  reg.add_module(CreateViewerClockIcon)
  reg.add_input_port(CreateViewerClockIcon, 'p_type',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_bbox',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_format',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_min',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_max',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_current',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_size',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_location_x',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_location_y',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_color_r',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_color_g',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'p_color_b',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(CreateViewerClockIcon, 'Time Matrix',
                   (Matrix, "Matrix"))
  reg.add_input_port(CreateViewerClockIcon, 'Time Nrrd',
                   (Nrrd, "Nrrd"))
  reg.add_output_port(CreateViewerClockIcon, 'Clock',
                   (Geometry, "Geometry"))

  reg.add_module(ConvertFieldsToTexture)
  reg.add_input_port(ConvertFieldsToTexture, 'p_vmin',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_vmax',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_gmin',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_gmax',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_is_fixed',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_card_mem',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_card_mem_auto',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_histogram',
                   (core.modules.basic_modules.Integer, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'p_gamma',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_input_port(ConvertFieldsToTexture, 'Value Field',
                   (Field, "Field"))
  reg.add_input_port(ConvertFieldsToTexture, 'Gradient Magnitude Field',
                   (Field, "Field"))
  reg.add_output_port(ConvertFieldsToTexture, 'Texture',
                   (Texture, "Texture"))
  reg.add_output_port(ConvertFieldsToTexture, 'JointHistoGram',
                   (Nrrd, "Nrrd"))

  reg.add_module(ColorMap2DSemantics)
  reg.add_input_port(ColorMap2DSemantics, 'Input Colormap',
                   (ColorMap2, "ColorMap2"))
  reg.add_output_port(ColorMap2DSemantics, 'Output Colormap',
                   (ColorMap2, "ColorMap2"))

  reg.add_module(ConvertMatrixToString)
  reg.add_input_port(ConvertMatrixToString, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ConvertMatrixToString, 'String',
                   (core.modules.basic_modules.String, 'tip'))

  reg.add_module(ConvertMatrixToField)
  reg.add_input_port(ConvertMatrixToField, 'p_datalocation',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(ConvertMatrixToField, 'Matrix',
                   (Matrix, "Matrix"))
  reg.add_output_port(ConvertMatrixToField, 'Field',
                   (Field, "Field"))

  reg.add_module(TimeControls)
  reg.add_input_port(TimeControls, 'p_execmode',
                   (core.modules.basic_modules.String, 'tip'), True)
  reg.add_input_port(TimeControls, 'p_scale_factor',
                   (core.modules.basic_modules.Float, 'tip'), True)
  reg.add_output_port(TimeControls, 'time',
                   (Time, "Time"))



  import viewercell
  viewercell.registerSelf()
  import cm2viewcell
  cm2viewcell.registerSelf()


def package_dependencies():
  return ['edu.utah.sci.vistrails.spreadsheet']


def finalize():
  sr_py.terminate()
  time.sleep(.5)

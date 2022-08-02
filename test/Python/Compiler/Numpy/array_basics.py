# RUN: %PYTHON %s | npcomp-opt -split-input-file | FileCheck %s --dump-input=fail

import numpy as np
from npcomp.compiler.numpy import test_config

import_global = test_config.create_import_dump_decorator()

global_data = (np.zeros((2, 3)) + [1.0, 2.0, 3.0] * np.reshape([1.0, 2.0],
                                                               (2, 1)))


# CHECK-LABEL: func @global_array_to_const
@import_global
def global_array_to_const():
  return global_data

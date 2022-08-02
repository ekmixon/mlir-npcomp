# RUN: %PYTHON %s | npcomp-opt -split-input-file | FileCheck %s --dump-input=fail

# Subset of constant tests which verify against a GenericTarget32.

from npcomp.compiler.numpy import test_config
from npcomp.compiler.numpy.target import *

import_global = test_config.create_import_dump_decorator(
    target_factory=GenericTarget32)


# CHECK-LABEL: func @integer_constants
@import_global
def integer_constants():
  return 100


# CHECK-LABEL: func @float_constants
@import_global
def float_constants():
  return 2.2

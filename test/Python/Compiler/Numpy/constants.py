# RUN: %PYTHON %s | npcomp-opt -split-input-file | FileCheck %s --dump-input=fail

from npcomp.compiler.numpy import test_config

import_global = test_config.create_import_dump_decorator()


# CHECK-LABEL: func @integer_constants
@import_global
def integer_constants():
  # CHECK: %[[A_CAST:.*]] = basicpy.unknown_cast %[[A]] : i64 -> !basicpy.UnknownType
  # CHECK: return %[[A_CAST]]
  return 100


# CHECK-LABEL: func @float_constants
@import_global
def float_constants():
  # CHECK: %[[A_CAST:.*]] = basicpy.unknown_cast %[[A]] : f64 -> !basicpy.UnknownType
  # CHECK: return %[[A_CAST]]
  return 2.2


# CHECK-LABEL: func @bool_true_constant
@import_global
def bool_true_constant():
  return True


# CHECK-LABEL: func @bool_false_constant
@import_global
def bool_false_constant():
  return False


# CHECK-LABEL: func @string_constant
@import_global
def string_constant():
  return "foobar"


# CHECK-LABEL: func @joined_string_constant
@import_global
def joined_string_constant():
  return "I am" " still here"


# CHECK-LABEL: func @bytes_constant
@import_global
def bytes_constant():
  return b"foobar"


# CHECK-LABEL: func @ellipsis
@import_global
def ellipsis():
  return ...


# CHECK-LABEL: func @none_constant
@import_global
def none_constant():
  return None

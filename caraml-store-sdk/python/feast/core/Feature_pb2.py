# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Feature.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x66\x65\x61st/core/Feature.proto\x12\nfeast.core\x1a\x17\x66\x65\x61st/types/Value.proto\"\xd5\x01\n\x0b\x46\x65\x61tureSpec\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12:\n\nvalue_type\x18\x02 \x01(\x0e\x32\x1b.feast.types.ValueType.EnumR\tvalueType\x12;\n\x06labels\x18\x03 \x03(\x0b\x32#.feast.core.FeatureSpec.LabelsEntryR\x06labels\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42x\n\x1e\x64\x65v.caraml.store.protobuf.coreB\x0c\x46\x65\x61tureProtoZHgithub.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast/coreb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.Feature_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036dev.caraml.store.protobuf.coreB\014FeatureProtoZHgithub.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast/core'
  _FEATURESPEC_LABELSENTRY._options = None
  _FEATURESPEC_LABELSENTRY._serialized_options = b'8\001'
  _FEATURESPEC._serialized_start=66
  _FEATURESPEC._serialized_end=279
  _FEATURESPEC_LABELSENTRY._serialized_start=222
  _FEATURESPEC_LABELSENTRY._serialized_end=279
# @@protoc_insertion_point(module_scope)

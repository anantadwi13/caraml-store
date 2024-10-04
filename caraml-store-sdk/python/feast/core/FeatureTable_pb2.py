# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/FeatureTable.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2
from feast.core import Feature_pb2 as feast_dot_core_dot_Feature__pb2
from feast.core import OnlineStore_pb2 as feast_dot_core_dot_OnlineStore__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x66\x65\x61st/core/FeatureTable.proto\x12\nfeast.core\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1b\x66\x65\x61st/core/DataSource.proto\x1a\x18\x66\x65\x61st/core/Feature.proto\x1a\x1c\x66\x65\x61st/core/OnlineStore.proto\"f\n\x0c\x46\x65\x61tureTable\x12*\n\x04spec\x18\x01 \x01(\x0b\x32\x1c.feast.core.FeatureTableSpec\x12*\n\x04meta\x18\x02 \x01(\x0b\x32\x1c.feast.core.FeatureTableMeta\"\xb6\x03\n\x10\x46\x65\x61tureTableSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x65ntities\x18\x03 \x03(\t\x12)\n\x08\x66\x65\x61tures\x18\x04 \x03(\x0b\x32\x17.feast.core.FeatureSpec\x12\x38\n\x06labels\x18\x05 \x03(\x0b\x32(.feast.core.FeatureTableSpec.LabelsEntry\x12*\n\x07max_age\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12,\n\x0c\x62\x61tch_source\x18\x07 \x01(\x0b\x32\x16.feast.core.DataSource\x12-\n\rstream_source\x18\x08 \x01(\x0b\x32\x16.feast.core.DataSource\x12\x36\n\x13staleness_threshold\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\x0conline_store\x18\n \x01(\x0b\x32\x17.feast.core.OnlineStore\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa5\x01\n\x10\x46\x65\x61tureTableMeta\x12\x35\n\x11\x63reated_timestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\x16last_updated_timestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08revision\x18\x03 \x01(\x03\x12\x0c\n\x04hash\x18\x04 \x01(\tB}\n\x1e\x64\x65v.caraml.store.protobuf.coreB\x11\x46\x65\x61tureTableProtoZHgithub.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast/coreb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.core.FeatureTable_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036dev.caraml.store.protobuf.coreB\021FeatureTableProtoZHgithub.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast/core'
  _FEATURETABLESPEC_LABELSENTRY._options = None
  _FEATURETABLESPEC_LABELSENTRY._serialized_options = b'8\001'
  _FEATURETABLE._serialized_start=195
  _FEATURETABLE._serialized_end=297
  _FEATURETABLESPEC._serialized_start=300
  _FEATURETABLESPEC._serialized_end=738
  _FEATURETABLESPEC_LABELSENTRY._serialized_start=693
  _FEATURETABLESPEC_LABELSENTRY._serialized_end=738
  _FEATURETABLEMETA._serialized_start=741
  _FEATURETABLEMETA._serialized_end=906
# @@protoc_insertion_point(module_scope)

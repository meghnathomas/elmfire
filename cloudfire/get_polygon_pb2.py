# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: get_polygon.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'get_polygon.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11get_polygon.proto\"E\n\x07Request\x12\x10\n\x08\x66irename\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t\x12\x15\n\rtransfer_mode\x18\x03 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07\x66ileloc\x18\x01 \x01(\t21\n\nGetPolygon\x12#\n\rGetDomainData\x12\x08.Request\x1a\x06.Reply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_polygon_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST']._serialized_start=21
  _globals['_REQUEST']._serialized_end=90
  _globals['_REPLY']._serialized_start=92
  _globals['_REPLY']._serialized_end=116
  _globals['_GETPOLYGON']._serialized_start=118
  _globals['_GETPOLYGON']._serialized_end=167
# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/common/protocol/headers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/common/protocol/headers.proto',
  package='v2ray.core.common.protocol',
  syntax='proto3',
  serialized_options=_b('\n\036com.v2ray.core.common.protocolP\001Z\010protocol\252\002\032V2Ray.Core.Common.Protocol'),
  serialized_pb=_b('\n,v2ray.com/core/common/protocol/headers.proto\x12\x1av2ray.core.common.protocol\"H\n\x0eSecurityConfig\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.v2ray.core.common.protocol.SecurityType*b\n\x0cSecurityType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06LEGACY\x10\x01\x12\x08\n\x04\x41UTO\x10\x02\x12\x0e\n\nAES128_GCM\x10\x03\x12\x15\n\x11\x43HACHA20_POLY1305\x10\x04\x12\x08\n\x04NONE\x10\x05\x42I\n\x1e\x63om.v2ray.core.common.protocolP\x01Z\x08protocol\xaa\x02\x1aV2Ray.Core.Common.Protocolb\x06proto3')
)

_SECURITYTYPE = _descriptor.EnumDescriptor(
  name='SecurityType',
  full_name='v2ray.core.common.protocol.SecurityType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEGACY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AES128_GCM', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHACHA20_POLY1305', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=150,
  serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_SECURITYTYPE)

SecurityType = enum_type_wrapper.EnumTypeWrapper(_SECURITYTYPE)
UNKNOWN = 0
LEGACY = 1
AUTO = 2
AES128_GCM = 3
CHACHA20_POLY1305 = 4
NONE = 5



_SECURITYCONFIG = _descriptor.Descriptor(
  name='SecurityConfig',
  full_name='v2ray.core.common.protocol.SecurityConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='v2ray.core.common.protocol.SecurityConfig.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=148,
)

_SECURITYCONFIG.fields_by_name['type'].enum_type = _SECURITYTYPE
DESCRIPTOR.message_types_by_name['SecurityConfig'] = _SECURITYCONFIG
DESCRIPTOR.enum_types_by_name['SecurityType'] = _SECURITYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecurityConfig = _reflection.GeneratedProtocolMessageType('SecurityConfig', (_message.Message,), dict(
  DESCRIPTOR = _SECURITYCONFIG,
  __module__ = 'v2ray.com.core.common.protocol.headers_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.common.protocol.SecurityConfig)
  ))
_sym_db.RegisterMessage(SecurityConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

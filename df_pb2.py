# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: df.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='df.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x08\x64\x66.proto\"\x15\n\x04Path\x12\r\n\x05value\x18\x01 \x01(\t2#\n\x04\x64\x61ta\x12\x1b\n\tread_data\x12\x05.Path\x1a\x05.Path\"\x00\x62\x06proto3')
)




_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Path.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=33,
)

DESCRIPTOR.message_types_by_name['Path'] = _PATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'df_pb2'
  # @@protoc_insertion_point(class_scope:Path)
  ))
_sym_db.RegisterMessage(Path)



_DATA = _descriptor.ServiceDescriptor(
  name='data',
  full_name='data',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=35,
  serialized_end=70,
  methods=[
  _descriptor.MethodDescriptor(
    name='read_data',
    full_name='data.read_data',
    index=0,
    containing_service=None,
    input_type=_PATH,
    output_type=_PATH,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATA)

DESCRIPTOR.services_by_name['data'] = _DATA

# @@protoc_insertion_point(module_scope)

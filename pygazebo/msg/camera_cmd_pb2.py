# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera_cmd.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='camera_cmd.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63\x61mera_cmd.proto\x12\x0bgazebo.msgs\"!\n\tCameraCmd\x12\x14\n\x0c\x66ollow_model\x18\x01 \x01(\t')
)




_CAMERACMD = _descriptor.Descriptor(
  name='CameraCmd',
  full_name='gazebo.msgs.CameraCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='follow_model', full_name='gazebo.msgs.CameraCmd.follow_model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=66,
)

DESCRIPTOR.message_types_by_name['CameraCmd'] = _CAMERACMD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraCmd = _reflection.GeneratedProtocolMessageType('CameraCmd', (_message.Message,), dict(
  DESCRIPTOR = _CAMERACMD,
  __module__ = 'camera_cmd_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.CameraCmd)
  ))
_sym_db.RegisterMessage(CameraCmd)


# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: users.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0busers.proto\x12\x04user\"w\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t\x12\x12\n\ncreated_at\x18\x06 \x01(\t\x12\x12\n\nupdated_at\x18\x07 \x01(\t\"\x11\n\x0fGetUsersRequest\"-\n\x10GetUsersResponse\x12\x19\n\x05users\x18\x01 \x03(\x0b\x32\n.user.User\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\t\"/\n\x13GetUserByIdResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"-\n\x11\x43reateUserRequest\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\".\n\x12\x43reateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"-\n\x11UpdateUserRequest\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\".\n\x12UpdateUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\".\n\x12\x44\x65leteUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User2\xd9\x02\n\x0bUserService\x12;\n\x08GetUsers\x12\x15.user.GetUsersRequest\x1a\x16.user.GetUsersResponse\"\x00\x12\x44\n\x0bGetUserById\x12\x18.user.GetUserByIdRequest\x1a\x19.user.GetUserByIdResponse\"\x00\x12\x41\n\nCreateUser\x12\x17.user.CreateUserRequest\x1a\x18.user.CreateUserResponse\"\x00\x12\x41\n\nUpdateUser\x12\x17.user.UpdateUserRequest\x1a\x18.user.UpdateUserResponse\"\x00\x12\x41\n\nDeleteUser\x12\x17.user.DeleteUserRequest\x1a\x18.user.DeleteUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=21
  _globals['_USER']._serialized_end=140
  _globals['_GETUSERSREQUEST']._serialized_start=142
  _globals['_GETUSERSREQUEST']._serialized_end=159
  _globals['_GETUSERSRESPONSE']._serialized_start=161
  _globals['_GETUSERSRESPONSE']._serialized_end=206
  _globals['_GETUSERBYIDREQUEST']._serialized_start=208
  _globals['_GETUSERBYIDREQUEST']._serialized_end=240
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=242
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=289
  _globals['_CREATEUSERREQUEST']._serialized_start=291
  _globals['_CREATEUSERREQUEST']._serialized_end=336
  _globals['_CREATEUSERRESPONSE']._serialized_start=338
  _globals['_CREATEUSERRESPONSE']._serialized_end=384
  _globals['_UPDATEUSERREQUEST']._serialized_start=386
  _globals['_UPDATEUSERREQUEST']._serialized_end=431
  _globals['_UPDATEUSERRESPONSE']._serialized_start=433
  _globals['_UPDATEUSERRESPONSE']._serialized_end=479
  _globals['_DELETEUSERREQUEST']._serialized_start=481
  _globals['_DELETEUSERREQUEST']._serialized_end=512
  _globals['_DELETEUSERRESPONSE']._serialized_start=514
  _globals['_DELETEUSERRESPONSE']._serialized_end=560
  _globals['_USERSERVICE']._serialized_start=563
  _globals['_USERSERVICE']._serialized_end=908
# @@protoc_insertion_point(module_scope)

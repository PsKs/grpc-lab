# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x04todo\"I\n\x11\x43reateTaskRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08\x64ue_date\x18\x03 \x01(\t\"U\n\x11UpdateTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x64ue_date\x18\x04 \x01(\t\"!\n\x13MarkTaskDoneRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1f\n\x11\x44\x65leteTaskRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"^\n\x0cTaskResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x10\n\x08\x64ue_date\x18\x04 \x01(\t\x12\x0c\n\x04\x64one\x18\x05 \x01(\x08\"2\n\rTasksResponse\x12!\n\x05tasks\x18\x01 \x03(\x0b\x32\x12.todo.TaskResponse\"\x07\n\x05\x45mpty2\xdc\x02\n\x0bTodoService\x12\x39\n\nCreateTask\x12\x17.todo.CreateTaskRequest\x1a\x12.todo.TaskResponse\x12\x30\n\x0cReadAllTasks\x12\x0b.todo.Empty\x1a\x13.todo.TasksResponse\x12\x32\n\x0eReadTodayTasks\x12\x0b.todo.Empty\x1a\x13.todo.TasksResponse\x12\x39\n\nUpdateTask\x12\x17.todo.UpdateTaskRequest\x1a\x12.todo.TaskResponse\x12=\n\x0cMarkTaskDone\x12\x19.todo.MarkTaskDoneRequest\x1a\x12.todo.TaskResponse\x12\x32\n\nDeleteTask\x12\x17.todo.DeleteTaskRequest\x1a\x0b.todo.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CREATETASKREQUEST']._serialized_start=20
  _globals['_CREATETASKREQUEST']._serialized_end=93
  _globals['_UPDATETASKREQUEST']._serialized_start=95
  _globals['_UPDATETASKREQUEST']._serialized_end=180
  _globals['_MARKTASKDONEREQUEST']._serialized_start=182
  _globals['_MARKTASKDONEREQUEST']._serialized_end=215
  _globals['_DELETETASKREQUEST']._serialized_start=217
  _globals['_DELETETASKREQUEST']._serialized_end=248
  _globals['_TASKRESPONSE']._serialized_start=250
  _globals['_TASKRESPONSE']._serialized_end=344
  _globals['_TASKSRESPONSE']._serialized_start=346
  _globals['_TASKSRESPONSE']._serialized_end=396
  _globals['_EMPTY']._serialized_start=398
  _globals['_EMPTY']._serialized_end=405
  _globals['_TODOSERVICE']._serialized_start=408
  _globals['_TODOSERVICE']._serialized_end=756
# @@protoc_insertion_point(module_scope)

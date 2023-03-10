# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

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
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\"Z\n\rClient2Server\x12!\n\x03\x63md\x18\x01 \x01(\x0e\x32\x14.Client2ServerReqCmd\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0b\n\x03seq\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\x0c\"\x88\x01\n\rServer2Client\x12!\n\x03\x63md\x18\x01 \x01(\x0e\x32\x14.Client2ServerReqCmd\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0b\n\x03seq\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x0c\n\x04\x62ody\x18\x05 \x01(\x0c\x12\x0c\n\x04\x63ode\x18\x06 \x01(\x05\x12\x0b\n\x03msg\x18\x07 \x01(\t\"\x1b\n\x0cHeartBeatReq\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1b\n\x0cHeartBeatRsp\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1f\n\x0c\x45nterRoomReq\x12\x0f\n\x07\x66rom_id\x18\x01 \x01(\t\",\n\x0c\x45nterRoomRsp\x12\x1c\n\troom_info\x18\x01 \x01(\x0b\x32\t.RoomInfo\"\x1e\n\x0cLeaveRoomReq\x12\x0e\n\x06reason\x18\x01 \x01(\t\"\x1b\n\x0cLeaveRoomRsp\x12\x0b\n\x03msg\x18\x01 \x01(\t\"3\n\x0e\x43reateTableReq\x12\x0f\n\x07game_id\x18\x01 \x01(\x05\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x0e\x43reateTableRsp\x12\x10\n\x08table_id\x18\x01 \x01(\x05\" \n\x0cJoinTableReq\x12\x10\n\x08table_id\x18\x01 \x01(\x05\".\n\x0cJoinTableRsp\x12\x1e\n\ntable_info\x18\x01 \x01(\x0b\x32\n.TableInfo\"!\n\rLeaveTableReq\x12\x10\n\x08table_id\x18\x01 \x01(\x05\"\x0f\n\rLeaveTableRsp\"_\n\x08RoomInfo\x12\x0f\n\x07room_id\x18\x01 \x01(\x05\x12\x1f\n\x0btables_info\x18\x02 \x03(\x0b\x32\n.TableInfo\x12!\n\x0cplayers_info\x18\x03 \x03(\x0b\x32\x0b.PlayerInfo\"\x1d\n\tTableInfo\x12\x10\n\x08table_id\x18\x01 \x01(\x05\"\x19\n\nPlayerInfo\x12\x0b\n\x03uid\x18\x01 \x01(\t\"L\n\x0fTableMessageReq\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x18\n\x02op\x18\x02 \x01(\x0e\x32\x0c.TableOpType\x12\r\n\x05\x63\x61rds\x18\x03 \x03(\x05\"3\n\x0fTableMessageRsp\x12\x10\n\x08table_id\x18\x01 \x01(\x05\x12\x0e\n\x06result\x18\x02 \x01(\x05\"p\n\x0c\x42roadCastMsg\x12 \n\x08\x62st_type\x18\x01 \x01(\x0e\x32\x0e.BroadCastType\x12\x10\n\x08\x66rom_uid\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\t*\xaa\x02\n\x13\x43lient2ServerReqCmd\x12\x11\n\rE_CMD_INVALID\x10\x00\x12\x14\n\x10\x45_CMD_HEART_BEAT\x10\n\x12\x14\n\x10\x45_CMD_BROAD_CAST\x10\x14\x12\x15\n\x10\x45_CMD_ROOM_ENTER\x10\x90N\x12\x15\n\x10\x45_CMD_ROOM_LEAVE\x10\x91N\x12\x15\n\x0f\x45_CMD_HALL_CHAT\x10\xa0\x9c\x01\x12\x19\n\x13\x45_CMD_HALL_ACTIVITY\x10\xa1\x9c\x01\x12\x18\n\x12\x45_CMD_TABLE_CREATE\x10\xb0\xea\x01\x12\x16\n\x10\x45_CMD_TABLE_JOIN\x10\xb1\xea\x01\x12\x17\n\x11\x45_CMD_TABLE_LEAVE\x10\xb2\xea\x01\x12\x19\n\x13\x45_CMD_TABLE_MESSAGE\x10\xb3\xea\x01\x12\x0e\n\tE_CMD_RPC\x10\xd0\x0f*\x9f\x01\n\x0bTableOpType\x12\x18\n\x14\x45_CMD_TABLE_OP_VALID\x10\x00\x12\x14\n\x10\x45_CMD_TABLE_CHAT\x10\x01\x12\x18\n\x14\x45_CMD_TABLE_OP_READY\x10\x02\x12\x14\n\x10\x45_CMD_TABLE_INIT\x10\x03\x12\x17\n\x13\x45_CMD_TABLE_OP_PASS\x10\x04\x12\x17\n\x13\x45_CMD_TABLE_OP_DROP\x10\x05*9\n\rBroadCastType\x12\x14\n\x10\x45_BS_TYPE_SYSTEM\x10\x00\x12\x12\n\x0e\x45_BS_TYPE_CHAT\x10\x01\x62\x06proto3')
)

_CLIENT2SERVERREQCMD = _descriptor.EnumDescriptor(
  name='Client2ServerReqCmd',
  full_name='Client2ServerReqCmd',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='E_CMD_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_HEART_BEAT', index=1, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_BROAD_CAST', index=2, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_ROOM_ENTER', index=3, number=10000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_ROOM_LEAVE', index=4, number=10001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_HALL_CHAT', index=5, number=20000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_HALL_ACTIVITY', index=6, number=20001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_CREATE', index=7, number=30000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_JOIN', index=8, number=30001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_LEAVE', index=9, number=30002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_MESSAGE', index=10, number=30003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_RPC', index=11, number=2000,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1070,
  serialized_end=1368,
)
_sym_db.RegisterEnumDescriptor(_CLIENT2SERVERREQCMD)

Client2ServerReqCmd = enum_type_wrapper.EnumTypeWrapper(_CLIENT2SERVERREQCMD)
_TABLEOPTYPE = _descriptor.EnumDescriptor(
  name='TableOpType',
  full_name='TableOpType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_OP_VALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_CHAT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_OP_READY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_INIT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_OP_PASS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_CMD_TABLE_OP_DROP', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1371,
  serialized_end=1530,
)
_sym_db.RegisterEnumDescriptor(_TABLEOPTYPE)

TableOpType = enum_type_wrapper.EnumTypeWrapper(_TABLEOPTYPE)
_BROADCASTTYPE = _descriptor.EnumDescriptor(
  name='BroadCastType',
  full_name='BroadCastType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='E_BS_TYPE_SYSTEM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='E_BS_TYPE_CHAT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1532,
  serialized_end=1589,
)
_sym_db.RegisterEnumDescriptor(_BROADCASTTYPE)

BroadCastType = enum_type_wrapper.EnumTypeWrapper(_BROADCASTTYPE)
E_CMD_INVALID = 0
E_CMD_HEART_BEAT = 10
E_CMD_BROAD_CAST = 20
E_CMD_ROOM_ENTER = 10000
E_CMD_ROOM_LEAVE = 10001
E_CMD_HALL_CHAT = 20000
E_CMD_HALL_ACTIVITY = 20001
E_CMD_TABLE_CREATE = 30000
E_CMD_TABLE_JOIN = 30001
E_CMD_TABLE_LEAVE = 30002
E_CMD_TABLE_MESSAGE = 30003
E_CMD_RPC = 2000
E_CMD_TABLE_OP_VALID = 0
E_CMD_TABLE_CHAT = 1
E_CMD_TABLE_OP_READY = 2
E_CMD_TABLE_INIT = 3
E_CMD_TABLE_OP_PASS = 4
E_CMD_TABLE_OP_DROP = 5
E_BS_TYPE_SYSTEM = 0
E_BS_TYPE_CHAT = 1



_CLIENT2SERVER = _descriptor.Descriptor(
  name='Client2Server',
  full_name='Client2Server',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='Client2Server.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='Client2Server.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='Client2Server.seq', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Client2Server.body', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=17,
  serialized_end=107,
)


_SERVER2CLIENT = _descriptor.Descriptor(
  name='Server2Client',
  full_name='Server2Client',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd', full_name='Server2Client.cmd', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='Server2Client.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='Server2Client.seq', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Server2Client.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Server2Client.body', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='Server2Client.code', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='Server2Client.msg', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=246,
)


_HEARTBEATREQ = _descriptor.Descriptor(
  name='HeartBeatReq',
  full_name='HeartBeatReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='HeartBeatReq.msg', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=275,
)


_HEARTBEATRSP = _descriptor.Descriptor(
  name='HeartBeatRsp',
  full_name='HeartBeatRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='HeartBeatRsp.msg', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=304,
)


_ENTERROOMREQ = _descriptor.Descriptor(
  name='EnterRoomReq',
  full_name='EnterRoomReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_id', full_name='EnterRoomReq.from_id', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=337,
)


_ENTERROOMRSP = _descriptor.Descriptor(
  name='EnterRoomRsp',
  full_name='EnterRoomRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_info', full_name='EnterRoomRsp.room_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=339,
  serialized_end=383,
)


_LEAVEROOMREQ = _descriptor.Descriptor(
  name='LeaveRoomReq',
  full_name='LeaveRoomReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='LeaveRoomReq.reason', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=415,
)


_LEAVEROOMRSP = _descriptor.Descriptor(
  name='LeaveRoomRsp',
  full_name='LeaveRoomRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='LeaveRoomRsp.msg', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=444,
)


_CREATETABLEREQ = _descriptor.Descriptor(
  name='CreateTableReq',
  full_name='CreateTableReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_id', full_name='CreateTableReq.game_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='CreateTableReq.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=497,
)


_CREATETABLERSP = _descriptor.Descriptor(
  name='CreateTableRsp',
  full_name='CreateTableRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='CreateTableRsp.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=499,
  serialized_end=533,
)


_JOINTABLEREQ = _descriptor.Descriptor(
  name='JoinTableReq',
  full_name='JoinTableReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='JoinTableReq.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=535,
  serialized_end=567,
)


_JOINTABLERSP = _descriptor.Descriptor(
  name='JoinTableRsp',
  full_name='JoinTableRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_info', full_name='JoinTableRsp.table_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=569,
  serialized_end=615,
)


_LEAVETABLEREQ = _descriptor.Descriptor(
  name='LeaveTableReq',
  full_name='LeaveTableReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='LeaveTableReq.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=617,
  serialized_end=650,
)


_LEAVETABLERSP = _descriptor.Descriptor(
  name='LeaveTableRsp',
  full_name='LeaveTableRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=652,
  serialized_end=667,
)


_ROOMINFO = _descriptor.Descriptor(
  name='RoomInfo',
  full_name='RoomInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_id', full_name='RoomInfo.room_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tables_info', full_name='RoomInfo.tables_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='players_info', full_name='RoomInfo.players_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=669,
  serialized_end=764,
)


_TABLEINFO = _descriptor.Descriptor(
  name='TableInfo',
  full_name='TableInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='TableInfo.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=766,
  serialized_end=795,
)


_PLAYERINFO = _descriptor.Descriptor(
  name='PlayerInfo',
  full_name='PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='PlayerInfo.uid', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=797,
  serialized_end=822,
)


_TABLEMESSAGEREQ = _descriptor.Descriptor(
  name='TableMessageReq',
  full_name='TableMessageReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='TableMessageReq.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='op', full_name='TableMessageReq.op', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cards', full_name='TableMessageReq.cards', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=824,
  serialized_end=900,
)


_TABLEMESSAGERSP = _descriptor.Descriptor(
  name='TableMessageRsp',
  full_name='TableMessageRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_id', full_name='TableMessageRsp.table_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='TableMessageRsp.result', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=902,
  serialized_end=953,
)


_BROADCASTMSG = _descriptor.Descriptor(
  name='BroadCastMsg',
  full_name='BroadCastMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bst_type', full_name='BroadCastMsg.bst_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_uid', full_name='BroadCastMsg.from_uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='BroadCastMsg.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='BroadCastMsg.message', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='BroadCastMsg.time', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=955,
  serialized_end=1067,
)

_CLIENT2SERVER.fields_by_name['cmd'].enum_type = _CLIENT2SERVERREQCMD
_SERVER2CLIENT.fields_by_name['cmd'].enum_type = _CLIENT2SERVERREQCMD
_ENTERROOMRSP.fields_by_name['room_info'].message_type = _ROOMINFO
_JOINTABLERSP.fields_by_name['table_info'].message_type = _TABLEINFO
_ROOMINFO.fields_by_name['tables_info'].message_type = _TABLEINFO
_ROOMINFO.fields_by_name['players_info'].message_type = _PLAYERINFO
_TABLEMESSAGEREQ.fields_by_name['op'].enum_type = _TABLEOPTYPE
_BROADCASTMSG.fields_by_name['bst_type'].enum_type = _BROADCASTTYPE
DESCRIPTOR.message_types_by_name['Client2Server'] = _CLIENT2SERVER
DESCRIPTOR.message_types_by_name['Server2Client'] = _SERVER2CLIENT
DESCRIPTOR.message_types_by_name['HeartBeatReq'] = _HEARTBEATREQ
DESCRIPTOR.message_types_by_name['HeartBeatRsp'] = _HEARTBEATRSP
DESCRIPTOR.message_types_by_name['EnterRoomReq'] = _ENTERROOMREQ
DESCRIPTOR.message_types_by_name['EnterRoomRsp'] = _ENTERROOMRSP
DESCRIPTOR.message_types_by_name['LeaveRoomReq'] = _LEAVEROOMREQ
DESCRIPTOR.message_types_by_name['LeaveRoomRsp'] = _LEAVEROOMRSP
DESCRIPTOR.message_types_by_name['CreateTableReq'] = _CREATETABLEREQ
DESCRIPTOR.message_types_by_name['CreateTableRsp'] = _CREATETABLERSP
DESCRIPTOR.message_types_by_name['JoinTableReq'] = _JOINTABLEREQ
DESCRIPTOR.message_types_by_name['JoinTableRsp'] = _JOINTABLERSP
DESCRIPTOR.message_types_by_name['LeaveTableReq'] = _LEAVETABLEREQ
DESCRIPTOR.message_types_by_name['LeaveTableRsp'] = _LEAVETABLERSP
DESCRIPTOR.message_types_by_name['RoomInfo'] = _ROOMINFO
DESCRIPTOR.message_types_by_name['TableInfo'] = _TABLEINFO
DESCRIPTOR.message_types_by_name['PlayerInfo'] = _PLAYERINFO
DESCRIPTOR.message_types_by_name['TableMessageReq'] = _TABLEMESSAGEREQ
DESCRIPTOR.message_types_by_name['TableMessageRsp'] = _TABLEMESSAGERSP
DESCRIPTOR.message_types_by_name['BroadCastMsg'] = _BROADCASTMSG
DESCRIPTOR.enum_types_by_name['Client2ServerReqCmd'] = _CLIENT2SERVERREQCMD
DESCRIPTOR.enum_types_by_name['TableOpType'] = _TABLEOPTYPE
DESCRIPTOR.enum_types_by_name['BroadCastType'] = _BROADCASTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Client2Server = _reflection.GeneratedProtocolMessageType('Client2Server', (_message.Message,), dict(
  DESCRIPTOR = _CLIENT2SERVER,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Client2Server)
  ))
_sym_db.RegisterMessage(Client2Server)

Server2Client = _reflection.GeneratedProtocolMessageType('Server2Client', (_message.Message,), dict(
  DESCRIPTOR = _SERVER2CLIENT,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Server2Client)
  ))
_sym_db.RegisterMessage(Server2Client)

HeartBeatReq = _reflection.GeneratedProtocolMessageType('HeartBeatReq', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:HeartBeatReq)
  ))
_sym_db.RegisterMessage(HeartBeatReq)

HeartBeatRsp = _reflection.GeneratedProtocolMessageType('HeartBeatRsp', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEATRSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:HeartBeatRsp)
  ))
_sym_db.RegisterMessage(HeartBeatRsp)

EnterRoomReq = _reflection.GeneratedProtocolMessageType('EnterRoomReq', (_message.Message,), dict(
  DESCRIPTOR = _ENTERROOMREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:EnterRoomReq)
  ))
_sym_db.RegisterMessage(EnterRoomReq)

EnterRoomRsp = _reflection.GeneratedProtocolMessageType('EnterRoomRsp', (_message.Message,), dict(
  DESCRIPTOR = _ENTERROOMRSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:EnterRoomRsp)
  ))
_sym_db.RegisterMessage(EnterRoomRsp)

LeaveRoomReq = _reflection.GeneratedProtocolMessageType('LeaveRoomReq', (_message.Message,), dict(
  DESCRIPTOR = _LEAVEROOMREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:LeaveRoomReq)
  ))
_sym_db.RegisterMessage(LeaveRoomReq)

LeaveRoomRsp = _reflection.GeneratedProtocolMessageType('LeaveRoomRsp', (_message.Message,), dict(
  DESCRIPTOR = _LEAVEROOMRSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:LeaveRoomRsp)
  ))
_sym_db.RegisterMessage(LeaveRoomRsp)

CreateTableReq = _reflection.GeneratedProtocolMessageType('CreateTableReq', (_message.Message,), dict(
  DESCRIPTOR = _CREATETABLEREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:CreateTableReq)
  ))
_sym_db.RegisterMessage(CreateTableReq)

CreateTableRsp = _reflection.GeneratedProtocolMessageType('CreateTableRsp', (_message.Message,), dict(
  DESCRIPTOR = _CREATETABLERSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:CreateTableRsp)
  ))
_sym_db.RegisterMessage(CreateTableRsp)

JoinTableReq = _reflection.GeneratedProtocolMessageType('JoinTableReq', (_message.Message,), dict(
  DESCRIPTOR = _JOINTABLEREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:JoinTableReq)
  ))
_sym_db.RegisterMessage(JoinTableReq)

JoinTableRsp = _reflection.GeneratedProtocolMessageType('JoinTableRsp', (_message.Message,), dict(
  DESCRIPTOR = _JOINTABLERSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:JoinTableRsp)
  ))
_sym_db.RegisterMessage(JoinTableRsp)

LeaveTableReq = _reflection.GeneratedProtocolMessageType('LeaveTableReq', (_message.Message,), dict(
  DESCRIPTOR = _LEAVETABLEREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:LeaveTableReq)
  ))
_sym_db.RegisterMessage(LeaveTableReq)

LeaveTableRsp = _reflection.GeneratedProtocolMessageType('LeaveTableRsp', (_message.Message,), dict(
  DESCRIPTOR = _LEAVETABLERSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:LeaveTableRsp)
  ))
_sym_db.RegisterMessage(LeaveTableRsp)

RoomInfo = _reflection.GeneratedProtocolMessageType('RoomInfo', (_message.Message,), dict(
  DESCRIPTOR = _ROOMINFO,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:RoomInfo)
  ))
_sym_db.RegisterMessage(RoomInfo)

TableInfo = _reflection.GeneratedProtocolMessageType('TableInfo', (_message.Message,), dict(
  DESCRIPTOR = _TABLEINFO,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:TableInfo)
  ))
_sym_db.RegisterMessage(TableInfo)

PlayerInfo = _reflection.GeneratedProtocolMessageType('PlayerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERINFO,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:PlayerInfo)
  ))
_sym_db.RegisterMessage(PlayerInfo)

TableMessageReq = _reflection.GeneratedProtocolMessageType('TableMessageReq', (_message.Message,), dict(
  DESCRIPTOR = _TABLEMESSAGEREQ,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:TableMessageReq)
  ))
_sym_db.RegisterMessage(TableMessageReq)

TableMessageRsp = _reflection.GeneratedProtocolMessageType('TableMessageRsp', (_message.Message,), dict(
  DESCRIPTOR = _TABLEMESSAGERSP,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:TableMessageRsp)
  ))
_sym_db.RegisterMessage(TableMessageRsp)

BroadCastMsg = _reflection.GeneratedProtocolMessageType('BroadCastMsg', (_message.Message,), dict(
  DESCRIPTOR = _BROADCASTMSG,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:BroadCastMsg)
  ))
_sym_db.RegisterMessage(BroadCastMsg)


# @@protoc_insertion_point(module_scope)

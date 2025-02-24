# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/exec.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2
from flwr.proto import recordset_pb2 as flwr_dot_proto_dot_recordset__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66lwr/proto/exec.proto\x12\nflwr.proto\x1a\x14\x66lwr/proto/fab.proto\x1a\x1a\x66lwr/proto/transport.proto\x1a\x1a\x66lwr/proto/recordset.proto\x1a\x14\x66lwr/proto/run.proto\"\xfb\x01\n\x0fStartRunRequest\x12\x1c\n\x03\x66\x61\x62\x18\x01 \x01(\x0b\x32\x0f.flwr.proto.Fab\x12H\n\x0foverride_config\x18\x02 \x03(\x0b\x32/.flwr.proto.StartRunRequest.OverrideConfigEntry\x12\x35\n\x12\x66\x65\x64\x65ration_options\x18\x03 \x01(\x0b\x32\x19.flwr.proto.ConfigsRecord\x1aI\n\x13OverrideConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.flwr.proto.Scalar:\x02\x38\x01\"2\n\x10StartRunResponse\x12\x13\n\x06run_id\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\t\n\x07_run_id\"<\n\x11StreamLogsRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12\x17\n\x0f\x61\x66ter_timestamp\x18\x02 \x01(\x01\"B\n\x12StreamLogsResponse\x12\x12\n\nlog_output\x18\x01 \x01(\t\x12\x18\n\x10latest_timestamp\x18\x02 \x01(\x01\"1\n\x0fListRunsRequest\x12\x13\n\x06run_id\x18\x01 \x01(\x04H\x00\x88\x01\x01\x42\t\n\x07_run_id\"\x9d\x01\n\x10ListRunsResponse\x12;\n\x08run_dict\x18\x01 \x03(\x0b\x32).flwr.proto.ListRunsResponse.RunDictEntry\x12\x0b\n\x03now\x18\x02 \x01(\t\x1a?\n\x0cRunDictEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.flwr.proto.Run:\x02\x38\x01\"\x18\n\x16GetLoginDetailsRequest\"\x8a\x01\n\x17GetLoginDetailsResponse\x12\x11\n\tauth_type\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65vice_code\x18\x02 \x01(\t\x12!\n\x19verification_uri_complete\x18\x03 \x01(\t\x12\x12\n\nexpires_in\x18\x04 \x01(\x03\x12\x10\n\x08interval\x18\x05 \x01(\x03\"+\n\x14GetAuthTokensRequest\x12\x13\n\x0b\x64\x65vice_code\x18\x01 \x01(\t\"D\n\x15GetAuthTokensResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\" \n\x0eStopRunRequest\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\"\"\n\x0fStopRunResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xe5\x03\n\x04\x45xec\x12G\n\x08StartRun\x12\x1b.flwr.proto.StartRunRequest\x1a\x1c.flwr.proto.StartRunResponse\"\x00\x12\x44\n\x07StopRun\x12\x1a.flwr.proto.StopRunRequest\x1a\x1b.flwr.proto.StopRunResponse\"\x00\x12O\n\nStreamLogs\x12\x1d.flwr.proto.StreamLogsRequest\x1a\x1e.flwr.proto.StreamLogsResponse\"\x00\x30\x01\x12G\n\x08ListRuns\x12\x1b.flwr.proto.ListRunsRequest\x1a\x1c.flwr.proto.ListRunsResponse\"\x00\x12\\\n\x0fGetLoginDetails\x12\".flwr.proto.GetLoginDetailsRequest\x1a#.flwr.proto.GetLoginDetailsResponse\"\x00\x12V\n\rGetAuthTokens\x12 .flwr.proto.GetAuthTokensRequest\x1a!.flwr.proto.GetAuthTokensResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.exec_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STARTRUNREQUEST_OVERRIDECONFIGENTRY']._options = None
  _globals['_STARTRUNREQUEST_OVERRIDECONFIGENTRY']._serialized_options = b'8\001'
  _globals['_LISTRUNSRESPONSE_RUNDICTENTRY']._options = None
  _globals['_LISTRUNSRESPONSE_RUNDICTENTRY']._serialized_options = b'8\001'
  _globals['_STARTRUNREQUEST']._serialized_start=138
  _globals['_STARTRUNREQUEST']._serialized_end=389
  _globals['_STARTRUNREQUEST_OVERRIDECONFIGENTRY']._serialized_start=316
  _globals['_STARTRUNREQUEST_OVERRIDECONFIGENTRY']._serialized_end=389
  _globals['_STARTRUNRESPONSE']._serialized_start=391
  _globals['_STARTRUNRESPONSE']._serialized_end=441
  _globals['_STREAMLOGSREQUEST']._serialized_start=443
  _globals['_STREAMLOGSREQUEST']._serialized_end=503
  _globals['_STREAMLOGSRESPONSE']._serialized_start=505
  _globals['_STREAMLOGSRESPONSE']._serialized_end=571
  _globals['_LISTRUNSREQUEST']._serialized_start=573
  _globals['_LISTRUNSREQUEST']._serialized_end=622
  _globals['_LISTRUNSRESPONSE']._serialized_start=625
  _globals['_LISTRUNSRESPONSE']._serialized_end=782
  _globals['_LISTRUNSRESPONSE_RUNDICTENTRY']._serialized_start=719
  _globals['_LISTRUNSRESPONSE_RUNDICTENTRY']._serialized_end=782
  _globals['_GETLOGINDETAILSREQUEST']._serialized_start=784
  _globals['_GETLOGINDETAILSREQUEST']._serialized_end=808
  _globals['_GETLOGINDETAILSRESPONSE']._serialized_start=811
  _globals['_GETLOGINDETAILSRESPONSE']._serialized_end=949
  _globals['_GETAUTHTOKENSREQUEST']._serialized_start=951
  _globals['_GETAUTHTOKENSREQUEST']._serialized_end=994
  _globals['_GETAUTHTOKENSRESPONSE']._serialized_start=996
  _globals['_GETAUTHTOKENSRESPONSE']._serialized_end=1064
  _globals['_STOPRUNREQUEST']._serialized_start=1066
  _globals['_STOPRUNREQUEST']._serialized_end=1098
  _globals['_STOPRUNRESPONSE']._serialized_start=1100
  _globals['_STOPRUNRESPONSE']._serialized_end=1134
  _globals['_EXEC']._serialized_start=1137
  _globals['_EXEC']._serialized_end=1622
# @@protoc_insertion_point(module_scope)

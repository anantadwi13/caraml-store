# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast_spark/api/JobService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.core import DataSource_pb2 as feast_dot_core_dot_DataSource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n feast_spark/api/JobService.proto\x12\x0f\x66\x65\x61st_spark.api\x1a\x1b\x66\x65\x61st/core/DataSource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"r\n\x0cScheduledJob\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x1a\n\x12ingestion_timespan\x18\x04 \x01(\x05\x12\x15\n\rcron_schedule\x18\x05 \x01(\t\"\xac\x04\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12&\n\x04type\x18\x02 \x01(\x0e\x32\x18.feast_spark.api.JobType\x12*\n\x06status\x18\x03 \x01(\x0e\x32\x1a.feast_spark.api.JobStatus\x12\x0c\n\x04hash\x18\x04 \x01(\t\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12:\n\tretrieval\x18\x06 \x01(\x0b\x32%.feast_spark.api.Job.RetrievalJobMetaH\x00\x12\x43\n\x0f\x62\x61tch_ingestion\x18\x07 \x01(\x0b\x32(.feast_spark.api.Job.OfflineToOnlineMetaH\x00\x12\x43\n\x10stream_ingestion\x18\x08 \x01(\x0b\x32\'.feast_spark.api.Job.StreamToOnlineMetaH\x00\x12\x0f\n\x07log_uri\x18\t \x01(\t\x12\x15\n\rerror_message\x18\n \x01(\t\x12\x0f\n\x07project\x18\x0b \x01(\t\x1a+\n\x10RetrievalJobMeta\x12\x17\n\x0foutput_location\x18\x01 \x01(\t\x1a)\n\x13OfflineToOnlineMeta\x12\x12\n\ntable_name\x18\x01 \x01(\t\x1a(\n\x12StreamToOnlineMeta\x12\x12\n\ntable_name\x18\x01 \x01(\tB\x06\n\x04meta\"\xc5\x01\n\'StartOfflineToOnlineIngestionJobRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12.\n\nstart_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x17\n\x0f\x64\x65lta_ingestion\x18\x05 \x01(\x08\"\x8f\x01\n(StartOfflineToOnlineIngestionJobResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x32\n\x0ejob_start_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x0f\n\x07log_uri\x18\x04 \x01(\t\"E\n\x1eStartStreamIngestionJobRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\"-\n\x1fStartStreamIngestionJobResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x84\x01\n*ScheduleOfflineToOnlineIngestionJobRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x1a\n\x12ingestion_timespan\x18\x03 \x01(\x05\x12\x15\n\rcron_schedule\x18\x04 \x01(\t\"-\n+ScheduleOfflineToOnlineIngestionJobResponse\"S\n,UnscheduleOfflineToOnlineIngestionJobRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\"/\n-UnscheduleOfflineToOnlineIngestionJobResponse\"\xa4\x01\n\x1cGetHistoricalFeaturesRequest\x12\x14\n\x0c\x66\x65\x61ture_refs\x18\x01 \x03(\t\x12-\n\rentity_source\x18\x02 \x01(\x0b\x32\x16.feast.core.DataSource\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x17\n\x0foutput_location\x18\x04 \x01(\t\x12\x15\n\routput_format\x18\x05 \x01(\t\"\x89\x01\n\x1dGetHistoricalFeaturesResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0foutput_file_uri\x18\x02 \x01(\t\x12\x32\n\x0ejob_start_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07log_uri\x18\x04 \x01(\t\"z\n\x0fListJobsRequest\x12\x1a\n\x12include_terminated\x18\x01 \x01(\x08\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12&\n\x04type\x18\x04 \x01(\x0e\x32\x18.feast_spark.api.JobType\"?\n\x18ListScheduledJobsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\"6\n\x10ListJobsResponse\x12\"\n\x04jobs\x18\x01 \x03(\x0b\x32\x14.feast_spark.api.Job\"H\n\x19ListScheduledJobsResponse\x12+\n\x04jobs\x18\x01 \x03(\x0b\x32\x1d.feast_spark.api.ScheduledJob\"\x1f\n\rGetJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"3\n\x0eGetJobResponse\x12!\n\x03job\x18\x01 \x01(\x0b\x32\x14.feast_spark.api.Job\"\"\n\x10\x43\x61ncelJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\x13\n\x11\x43\x61ncelJobResponse\"&\n\x14UnscheduleJobRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"\x17\n\x15UnscheduleJobResponse\"?\n\x17GetHealthMetricsRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x13\n\x0btable_names\x18\x02 \x03(\t\":\n\x18GetHealthMetricsResponse\x12\x0e\n\x06passed\x18\x01 \x03(\t\x12\x0e\n\x06\x66\x61iled\x18\x02 \x03(\t*`\n\x07JobType\x12\x0f\n\x0bINVALID_JOB\x10\x00\x12\x17\n\x13\x42\x41TCH_INGESTION_JOB\x10\x01\x12\x18\n\x14STREAM_INGESTION_JOB\x10\x02\x12\x11\n\rRETRIEVAL_JOB\x10\x04*~\n\tJobStatus\x12\x16\n\x12JOB_STATUS_INVALID\x10\x00\x12\x16\n\x12JOB_STATUS_PENDING\x10\x01\x12\x16\n\x12JOB_STATUS_RUNNING\x10\x02\x12\x13\n\x0fJOB_STATUS_DONE\x10\x03\x12\x14\n\x10JOB_STATUS_ERROR\x10\x04\x32\x8d\n\n\nJobService\x12\x97\x01\n StartOfflineToOnlineIngestionJob\x12\x38.feast_spark.api.StartOfflineToOnlineIngestionJobRequest\x1a\x39.feast_spark.api.StartOfflineToOnlineIngestionJobResponse\x12|\n\x17StartStreamIngestionJob\x12/.feast_spark.api.StartStreamIngestionJobRequest\x1a\x30.feast_spark.api.StartStreamIngestionJobResponse\x12\xa0\x01\n#ScheduleOfflineToOnlineIngestionJob\x12;.feast_spark.api.ScheduleOfflineToOnlineIngestionJobRequest\x1a<.feast_spark.api.ScheduleOfflineToOnlineIngestionJobResponse\x12\xa6\x01\n%UnscheduleOfflineToOnlineIngestionJob\x12=.feast_spark.api.UnscheduleOfflineToOnlineIngestionJobRequest\x1a>.feast_spark.api.UnscheduleOfflineToOnlineIngestionJobResponse\x12v\n\x15GetHistoricalFeatures\x12-.feast_spark.api.GetHistoricalFeaturesRequest\x1a..feast_spark.api.GetHistoricalFeaturesResponse\x12O\n\x08ListJobs\x12 .feast_spark.api.ListJobsRequest\x1a!.feast_spark.api.ListJobsResponse\x12j\n\x11ListScheduledJobs\x12).feast_spark.api.ListScheduledJobsRequest\x1a*.feast_spark.api.ListScheduledJobsResponse\x12R\n\tCancelJob\x12!.feast_spark.api.CancelJobRequest\x1a\".feast_spark.api.CancelJobResponse\x12^\n\rUnscheduleJob\x12%.feast_spark.api.UnscheduleJobRequest\x1a&.feast_spark.api.UnscheduleJobResponse\x12I\n\x06GetJob\x12\x1e.feast_spark.api.GetJobRequest\x1a\x1f.feast_spark.api.GetJobResponse\x12g\n\x10GetHealthMetrics\x12(.feast_spark.api.GetHealthMetricsRequest\x1a).feast_spark.api.GetHealthMetricsResponseB\x86\x01\n$dev.caraml.store.protobuf.jobserviceB\x0fJobServiceProtoZMgithub.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast_spark/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast_spark.api.JobService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$dev.caraml.store.protobuf.jobserviceB\017JobServiceProtoZMgithub.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast_spark/api'
  _JOBTYPE._serialized_start=2529
  _JOBTYPE._serialized_end=2625
  _JOBSTATUS._serialized_start=2627
  _JOBSTATUS._serialized_end=2753
  _SCHEDULEDJOB._serialized_start=115
  _SCHEDULEDJOB._serialized_end=229
  _JOB._serialized_start=232
  _JOB._serialized_end=788
  _JOB_RETRIEVALJOBMETA._serialized_start=652
  _JOB_RETRIEVALJOBMETA._serialized_end=695
  _JOB_OFFLINETOONLINEMETA._serialized_start=697
  _JOB_OFFLINETOONLINEMETA._serialized_end=738
  _JOB_STREAMTOONLINEMETA._serialized_start=740
  _JOB_STREAMTOONLINEMETA._serialized_end=780
  _STARTOFFLINETOONLINEINGESTIONJOBREQUEST._serialized_start=791
  _STARTOFFLINETOONLINEINGESTIONJOBREQUEST._serialized_end=988
  _STARTOFFLINETOONLINEINGESTIONJOBRESPONSE._serialized_start=991
  _STARTOFFLINETOONLINEINGESTIONJOBRESPONSE._serialized_end=1134
  _STARTSTREAMINGESTIONJOBREQUEST._serialized_start=1136
  _STARTSTREAMINGESTIONJOBREQUEST._serialized_end=1205
  _STARTSTREAMINGESTIONJOBRESPONSE._serialized_start=1207
  _STARTSTREAMINGESTIONJOBRESPONSE._serialized_end=1252
  _SCHEDULEOFFLINETOONLINEINGESTIONJOBREQUEST._serialized_start=1255
  _SCHEDULEOFFLINETOONLINEINGESTIONJOBREQUEST._serialized_end=1387
  _SCHEDULEOFFLINETOONLINEINGESTIONJOBRESPONSE._serialized_start=1389
  _SCHEDULEOFFLINETOONLINEINGESTIONJOBRESPONSE._serialized_end=1434
  _UNSCHEDULEOFFLINETOONLINEINGESTIONJOBREQUEST._serialized_start=1436
  _UNSCHEDULEOFFLINETOONLINEINGESTIONJOBREQUEST._serialized_end=1519
  _UNSCHEDULEOFFLINETOONLINEINGESTIONJOBRESPONSE._serialized_start=1521
  _UNSCHEDULEOFFLINETOONLINEINGESTIONJOBRESPONSE._serialized_end=1568
  _GETHISTORICALFEATURESREQUEST._serialized_start=1571
  _GETHISTORICALFEATURESREQUEST._serialized_end=1735
  _GETHISTORICALFEATURESRESPONSE._serialized_start=1738
  _GETHISTORICALFEATURESRESPONSE._serialized_end=1875
  _LISTJOBSREQUEST._serialized_start=1877
  _LISTJOBSREQUEST._serialized_end=1999
  _LISTSCHEDULEDJOBSREQUEST._serialized_start=2001
  _LISTSCHEDULEDJOBSREQUEST._serialized_end=2064
  _LISTJOBSRESPONSE._serialized_start=2066
  _LISTJOBSRESPONSE._serialized_end=2120
  _LISTSCHEDULEDJOBSRESPONSE._serialized_start=2122
  _LISTSCHEDULEDJOBSRESPONSE._serialized_end=2194
  _GETJOBREQUEST._serialized_start=2196
  _GETJOBREQUEST._serialized_end=2227
  _GETJOBRESPONSE._serialized_start=2229
  _GETJOBRESPONSE._serialized_end=2280
  _CANCELJOBREQUEST._serialized_start=2282
  _CANCELJOBREQUEST._serialized_end=2316
  _CANCELJOBRESPONSE._serialized_start=2318
  _CANCELJOBRESPONSE._serialized_end=2337
  _UNSCHEDULEJOBREQUEST._serialized_start=2339
  _UNSCHEDULEJOBREQUEST._serialized_end=2377
  _UNSCHEDULEJOBRESPONSE._serialized_start=2379
  _UNSCHEDULEJOBRESPONSE._serialized_end=2402
  _GETHEALTHMETRICSREQUEST._serialized_start=2404
  _GETHEALTHMETRICSREQUEST._serialized_end=2467
  _GETHEALTHMETRICSRESPONSE._serialized_start=2469
  _GETHEALTHMETRICSRESPONSE._serialized_end=2527
  _JOBSERVICE._serialized_start=2756
  _JOBSERVICE._serialized_end=4049
# @@protoc_insertion_point(module_scope)

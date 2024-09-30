"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import feast.core.DataSource_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _JobType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JobTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INVALID_JOB: _JobType.ValueType  # 0
    BATCH_INGESTION_JOB: _JobType.ValueType  # 1
    STREAM_INGESTION_JOB: _JobType.ValueType  # 2
    RETRIEVAL_JOB: _JobType.ValueType  # 4

class JobType(_JobType, metaclass=_JobTypeEnumTypeWrapper): ...

INVALID_JOB: JobType.ValueType  # 0
BATCH_INGESTION_JOB: JobType.ValueType  # 1
STREAM_INGESTION_JOB: JobType.ValueType  # 2
RETRIEVAL_JOB: JobType.ValueType  # 4
global___JobType = JobType

class _JobStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _JobStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_JobStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    JOB_STATUS_INVALID: _JobStatus.ValueType  # 0
    JOB_STATUS_PENDING: _JobStatus.ValueType  # 1
    """The Job has be registered and waiting to get scheduled to run"""
    JOB_STATUS_RUNNING: _JobStatus.ValueType  # 2
    """The Job is currently processing its task"""
    JOB_STATUS_DONE: _JobStatus.ValueType  # 3
    """The Job has successfully completed its task"""
    JOB_STATUS_ERROR: _JobStatus.ValueType  # 4
    """The Job has encountered an error while processing its task"""

class JobStatus(_JobStatus, metaclass=_JobStatusEnumTypeWrapper): ...

JOB_STATUS_INVALID: JobStatus.ValueType  # 0
JOB_STATUS_PENDING: JobStatus.ValueType  # 1
"""The Job has be registered and waiting to get scheduled to run"""
JOB_STATUS_RUNNING: JobStatus.ValueType  # 2
"""The Job is currently processing its task"""
JOB_STATUS_DONE: JobStatus.ValueType  # 3
"""The Job has successfully completed its task"""
JOB_STATUS_ERROR: JobStatus.ValueType  # 4
"""The Job has encountered an error while processing its task"""
global___JobStatus = JobStatus

@typing_extensions.final
class ScheduledJob(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    INGESTION_TIMESPAN_FIELD_NUMBER: builtins.int
    CRON_SCHEDULE_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Identifier of the Job"""
    table_name: builtins.str
    project: builtins.str
    ingestion_timespan: builtins.int
    """Timespan of the ingested data per job, in days. The data from  end of the day - timespan till end of the day will be ingested. Eg. if the job execution date is 10/4/2021, and ingestion timespan is 2, then data from 9/4/2021 00:00 to 10/4/2021 23:59 (inclusive) will be ingested."""
    cron_schedule: builtins.str
    """Crontab string. Eg. 0 13 * * *"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        table_name: builtins.str = ...,
        project: builtins.str = ...,
        ingestion_timespan: builtins.int = ...,
        cron_schedule: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cron_schedule", b"cron_schedule", "id", b"id", "ingestion_timespan", b"ingestion_timespan", "project", b"project", "table_name", b"table_name"]) -> None: ...

global___ScheduledJob = ScheduledJob

@typing_extensions.final
class Job(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class RetrievalJobMeta(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        OUTPUT_LOCATION_FIELD_NUMBER: builtins.int
        output_location: builtins.str
        def __init__(
            self,
            *,
            output_location: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["output_location", b"output_location"]) -> None: ...

    @typing_extensions.final
    class OfflineToOnlineMeta(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TABLE_NAME_FIELD_NUMBER: builtins.int
        table_name: builtins.str
        def __init__(
            self,
            *,
            table_name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["table_name", b"table_name"]) -> None: ...

    @typing_extensions.final
    class StreamToOnlineMeta(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TABLE_NAME_FIELD_NUMBER: builtins.int
        table_name: builtins.str
        def __init__(
            self,
            *,
            table_name: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["table_name", b"table_name"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    START_TIME_FIELD_NUMBER: builtins.int
    RETRIEVAL_FIELD_NUMBER: builtins.int
    BATCH_INGESTION_FIELD_NUMBER: builtins.int
    STREAM_INGESTION_FIELD_NUMBER: builtins.int
    LOG_URI_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Identifier of the Job"""
    type: global___JobType.ValueType
    """Type of the Job"""
    status: global___JobStatus.ValueType
    """Current job status"""
    hash: builtins.str
    """Deterministic hash of the Job"""
    @property
    def start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start time of the Job"""
    @property
    def retrieval(self) -> global___Job.RetrievalJobMeta: ...
    @property
    def batch_ingestion(self) -> global___Job.OfflineToOnlineMeta: ...
    @property
    def stream_ingestion(self) -> global___Job.StreamToOnlineMeta: ...
    log_uri: builtins.str
    """Path to Spark job logs, if available"""
    error_message: builtins.str
    """Spark job error message, if available"""
    project: builtins.str
    """Project"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        type: global___JobType.ValueType = ...,
        status: global___JobStatus.ValueType = ...,
        hash: builtins.str = ...,
        start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        retrieval: global___Job.RetrievalJobMeta | None = ...,
        batch_ingestion: global___Job.OfflineToOnlineMeta | None = ...,
        stream_ingestion: global___Job.StreamToOnlineMeta | None = ...,
        log_uri: builtins.str = ...,
        error_message: builtins.str = ...,
        project: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["batch_ingestion", b"batch_ingestion", "meta", b"meta", "retrieval", b"retrieval", "start_time", b"start_time", "stream_ingestion", b"stream_ingestion"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["batch_ingestion", b"batch_ingestion", "error_message", b"error_message", "hash", b"hash", "id", b"id", "log_uri", b"log_uri", "meta", b"meta", "project", b"project", "retrieval", b"retrieval", "start_time", b"start_time", "status", b"status", "stream_ingestion", b"stream_ingestion", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["meta", b"meta"]) -> typing_extensions.Literal["retrieval", "batch_ingestion", "stream_ingestion"] | None: ...

global___Job = Job

@typing_extensions.final
class StartOfflineToOnlineIngestionJobRequest(google.protobuf.message.Message):
    """Ingest data from offline store into online store"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    START_DATE_FIELD_NUMBER: builtins.int
    END_DATE_FIELD_NUMBER: builtins.int
    DELTA_INGESTION_FIELD_NUMBER: builtins.int
    project: builtins.str
    """Feature table to ingest"""
    table_name: builtins.str
    @property
    def start_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Start of time range for source data from offline store"""
    @property
    def end_date(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """End of time range for source data from offline store"""
    delta_ingestion: builtins.bool
    """optional setting for delta ingestion"""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        table_name: builtins.str = ...,
        start_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        end_date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        delta_ingestion: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["end_date", b"end_date", "start_date", b"start_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["delta_ingestion", b"delta_ingestion", "end_date", b"end_date", "project", b"project", "start_date", b"start_date", "table_name", b"table_name"]) -> None: ...

global___StartOfflineToOnlineIngestionJobRequest = StartOfflineToOnlineIngestionJobRequest

@typing_extensions.final
class StartOfflineToOnlineIngestionJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    JOB_START_TIME_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    LOG_URI_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Job ID assigned by Feast"""
    @property
    def job_start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Job start time"""
    table_name: builtins.str
    """Feature table associated with the job"""
    log_uri: builtins.str
    """Path to Spark job logs, if available"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        job_start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        table_name: builtins.str = ...,
        log_uri: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job_start_time", b"job_start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "job_start_time", b"job_start_time", "log_uri", b"log_uri", "table_name", b"table_name"]) -> None: ...

global___StartOfflineToOnlineIngestionJobResponse = StartOfflineToOnlineIngestionJobResponse

@typing_extensions.final
class StartStreamIngestionJobRequest(google.protobuf.message.Message):
    """Ingest data from streaming source into online store"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    project: builtins.str
    """Feature table to ingest"""
    table_name: builtins.str
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["project", b"project", "table_name", b"table_name"]) -> None: ...

global___StartStreamIngestionJobRequest = StartStreamIngestionJobRequest

@typing_extensions.final
class StartStreamIngestionJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Job ID assigned by Feast"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id"]) -> None: ...

global___StartStreamIngestionJobResponse = StartStreamIngestionJobResponse

@typing_extensions.final
class ScheduleOfflineToOnlineIngestionJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    INGESTION_TIMESPAN_FIELD_NUMBER: builtins.int
    CRON_SCHEDULE_FIELD_NUMBER: builtins.int
    project: builtins.str
    """Feature table to ingest"""
    table_name: builtins.str
    ingestion_timespan: builtins.int
    """Timespan of the ingested data per job, in days. The data from  end of the day - timespan till end of the day will be ingested. Eg. if the job execution date is 10/4/2021, and ingestion timespan is 2, then data from 9/4/2021 00:00 to 10/4/2021 23:59 (inclusive) will be ingested."""
    cron_schedule: builtins.str
    """Crontab string. Eg. 0 13 * * *"""
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        table_name: builtins.str = ...,
        ingestion_timespan: builtins.int = ...,
        cron_schedule: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cron_schedule", b"cron_schedule", "ingestion_timespan", b"ingestion_timespan", "project", b"project", "table_name", b"table_name"]) -> None: ...

global___ScheduleOfflineToOnlineIngestionJobRequest = ScheduleOfflineToOnlineIngestionJobRequest

@typing_extensions.final
class ScheduleOfflineToOnlineIngestionJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ScheduleOfflineToOnlineIngestionJobResponse = ScheduleOfflineToOnlineIngestionJobResponse

@typing_extensions.final
class UnscheduleOfflineToOnlineIngestionJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    project: builtins.str
    table_name: builtins.str
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["project", b"project", "table_name", b"table_name"]) -> None: ...

global___UnscheduleOfflineToOnlineIngestionJobRequest = UnscheduleOfflineToOnlineIngestionJobRequest

@typing_extensions.final
class UnscheduleOfflineToOnlineIngestionJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnscheduleOfflineToOnlineIngestionJobResponse = UnscheduleOfflineToOnlineIngestionJobResponse

@typing_extensions.final
class GetHistoricalFeaturesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURE_REFS_FIELD_NUMBER: builtins.int
    ENTITY_SOURCE_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    OUTPUT_LOCATION_FIELD_NUMBER: builtins.int
    OUTPUT_FORMAT_FIELD_NUMBER: builtins.int
    @property
    def feature_refs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of feature references that are being retrieved"""
    @property
    def entity_source(self) -> feast.core.DataSource_pb2.DataSource:
        """Batch DataSource that can be used to obtain entity values for historical retrieval.
        For each entity value, a feature value will be retrieved for that value/timestamp
        Only 'BATCH_*' source types are supported.
        Currently only BATCH_FILE source type is supported.
        """
    project: builtins.str
    """Optional field to specify project name override. If specified, uses the
    given project for retrieval. Overrides the projects specified in
    Feature References if both are specified.
    """
    output_location: builtins.str
    """Specifies the path in a bucket to write the exported feature data files
    Export to AWS S3 - s3://path/to/features
    Export to GCP GCS -  gs://path/to/features
    """
    output_format: builtins.str
    """Specify format name for output, eg. parquet"""
    def __init__(
        self,
        *,
        feature_refs: collections.abc.Iterable[builtins.str] | None = ...,
        entity_source: feast.core.DataSource_pb2.DataSource | None = ...,
        project: builtins.str = ...,
        output_location: builtins.str = ...,
        output_format: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["entity_source", b"entity_source"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["entity_source", b"entity_source", "feature_refs", b"feature_refs", "output_format", b"output_format", "output_location", b"output_location", "project", b"project"]) -> None: ...

global___GetHistoricalFeaturesRequest = GetHistoricalFeaturesRequest

@typing_extensions.final
class GetHistoricalFeaturesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    OUTPUT_FILE_URI_FIELD_NUMBER: builtins.int
    JOB_START_TIME_FIELD_NUMBER: builtins.int
    LOG_URI_FIELD_NUMBER: builtins.int
    id: builtins.str
    """Export Job with ID assigned by Feast"""
    output_file_uri: builtins.str
    """Uri to the join result output file"""
    @property
    def job_start_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Job start time"""
    log_uri: builtins.str
    """Path to Spark job logs, if available"""
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        output_file_uri: builtins.str = ...,
        job_start_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        log_uri: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job_start_time", b"job_start_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "job_start_time", b"job_start_time", "log_uri", b"log_uri", "output_file_uri", b"output_file_uri"]) -> None: ...

global___GetHistoricalFeaturesResponse = GetHistoricalFeaturesResponse

@typing_extensions.final
class ListJobsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INCLUDE_TERMINATED_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    PROJECT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    include_terminated: builtins.bool
    table_name: builtins.str
    project: builtins.str
    type: global___JobType.ValueType
    def __init__(
        self,
        *,
        include_terminated: builtins.bool = ...,
        table_name: builtins.str = ...,
        project: builtins.str = ...,
        type: global___JobType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["include_terminated", b"include_terminated", "project", b"project", "table_name", b"table_name", "type", b"type"]) -> None: ...

global___ListJobsRequest = ListJobsRequest

@typing_extensions.final
class ListScheduledJobsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_NAME_FIELD_NUMBER: builtins.int
    project: builtins.str
    table_name: builtins.str
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        table_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["project", b"project", "table_name", b"table_name"]) -> None: ...

global___ListScheduledJobsRequest = ListScheduledJobsRequest

@typing_extensions.final
class ListJobsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOBS_FIELD_NUMBER: builtins.int
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Job]: ...
    def __init__(
        self,
        *,
        jobs: collections.abc.Iterable[global___Job] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jobs", b"jobs"]) -> None: ...

global___ListJobsResponse = ListJobsResponse

@typing_extensions.final
class ListScheduledJobsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOBS_FIELD_NUMBER: builtins.int
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ScheduledJob]: ...
    def __init__(
        self,
        *,
        jobs: collections.abc.Iterable[global___ScheduledJob] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["jobs", b"jobs"]) -> None: ...

global___ListScheduledJobsResponse = ListScheduledJobsResponse

@typing_extensions.final
class GetJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_id", b"job_id"]) -> None: ...

global___GetJobRequest = GetJobRequest

@typing_extensions.final
class GetJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_FIELD_NUMBER: builtins.int
    @property
    def job(self) -> global___Job: ...
    def __init__(
        self,
        *,
        job: global___Job | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["job", b"job"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["job", b"job"]) -> None: ...

global___GetJobResponse = GetJobResponse

@typing_extensions.final
class CancelJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_id", b"job_id"]) -> None: ...

global___CancelJobRequest = CancelJobRequest

@typing_extensions.final
class CancelJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CancelJobResponse = CancelJobResponse

@typing_extensions.final
class UnscheduleJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["job_id", b"job_id"]) -> None: ...

global___UnscheduleJobRequest = UnscheduleJobRequest

@typing_extensions.final
class UnscheduleJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___UnscheduleJobResponse = UnscheduleJobResponse

@typing_extensions.final
class GetHealthMetricsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_FIELD_NUMBER: builtins.int
    TABLE_NAMES_FIELD_NUMBER: builtins.int
    project: builtins.str
    @property
    def table_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        project: builtins.str = ...,
        table_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["project", b"project", "table_names", b"table_names"]) -> None: ...

global___GetHealthMetricsRequest = GetHealthMetricsRequest

@typing_extensions.final
class GetHealthMetricsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PASSED_FIELD_NUMBER: builtins.int
    FAILED_FIELD_NUMBER: builtins.int
    @property
    def passed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def failed(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        passed: collections.abc.Iterable[builtins.str] | None = ...,
        failed: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["failed", b"failed", "passed", b"passed"]) -> None: ...

global___GetHealthMetricsResponse = GetHealthMetricsResponse

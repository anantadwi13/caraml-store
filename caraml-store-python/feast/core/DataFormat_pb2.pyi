"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class FileFormat(google.protobuf.message.Message):
    """Defines the file format encoding the features/entity data in files"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ParquetFormat(google.protobuf.message.Message):
        """Defines options for the Parquet data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(
            self,
        ) -> None: ...

    PARQUET_FORMAT_FIELD_NUMBER: builtins.int
    @property
    def parquet_format(self) -> global___FileFormat.ParquetFormat: ...
    def __init__(
        self,
        *,
        parquet_format: global___FileFormat.ParquetFormat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["format", b"format", "parquet_format", b"parquet_format"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["format", b"format", "parquet_format", b"parquet_format"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["format", b"format"]) -> typing_extensions.Literal["parquet_format"] | None: ...

global___FileFormat = FileFormat

@typing_extensions.final
class StreamFormat(google.protobuf.message.Message):
    """Defines the data format encoding features/entity data in data streams"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ProtoFormat(google.protobuf.message.Message):
        """Defines options for the protobuf data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CLASS_PATH_FIELD_NUMBER: builtins.int
        class_path: builtins.str
        """Classpath to the generated Java Protobuf class that can be used to decode
        Feature data from the obtained stream message
        """
        def __init__(
            self,
            *,
            class_path: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["class_path", b"class_path"]) -> None: ...

    @typing_extensions.final
    class AvroFormat(google.protobuf.message.Message):
        """Defines options for the avro data format"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SCHEMA_JSON_FIELD_NUMBER: builtins.int
        schema_json: builtins.str
        """Optional if used in a File DataSource as schema is embedded in avro file.
        Specifies the schema of the Avro message as JSON string.
        """
        def __init__(
            self,
            *,
            schema_json: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["schema_json", b"schema_json"]) -> None: ...

    AVRO_FORMAT_FIELD_NUMBER: builtins.int
    PROTO_FORMAT_FIELD_NUMBER: builtins.int
    @property
    def avro_format(self) -> global___StreamFormat.AvroFormat: ...
    @property
    def proto_format(self) -> global___StreamFormat.ProtoFormat: ...
    def __init__(
        self,
        *,
        avro_format: global___StreamFormat.AvroFormat | None = ...,
        proto_format: global___StreamFormat.ProtoFormat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["avro_format", b"avro_format", "format", b"format", "proto_format", b"proto_format"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["avro_format", b"avro_format", "format", b"format", "proto_format", b"proto_format"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["format", b"format"]) -> typing_extensions.Literal["avro_format", "proto_format"] | None: ...

global___StreamFormat = StreamFormat

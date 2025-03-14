"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import inspect_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# OutputInfo records output info from the tools.
class OutputInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCES_SIZE_GB_FIELD_NUMBER: builtins.int
    TARGETS_SIZE_GB_FIELD_NUMBER: builtins.int
    FAILURE_MESSAGE_FIELD_NUMBER: builtins.int
    FAILURE_MESSAGE_WITHOUT_PRIVACY_INFO_FIELD_NUMBER: builtins.int
    SERIAL_OUTPUTS_FIELD_NUMBER: builtins.int
    IMPORT_FILE_FORMAT_FIELD_NUMBER: builtins.int
    DETECTED_SOURCES_SIZE_GB_FIELD_NUMBER: builtins.int
    INFLATION_TYPE_FIELD_NUMBER: builtins.int
    INFLATION_TIME_MS_FIELD_NUMBER: builtins.int
    SHADOW_INFLATION_TIME_MS_FIELD_NUMBER: builtins.int
    SHADOW_DISK_MATCH_RESULT_FIELD_NUMBER: builtins.int
    IS_UEFI_COMPATIBLE_IMAGE_FIELD_NUMBER: builtins.int
    IS_UEFI_DETECTED_FIELD_NUMBER: builtins.int
    INSPECTION_RESULTS_FIELD_NUMBER: builtins.int
    # Size of import/export sources (image/disk/file)
    @property
    def sources_size_gb(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Size of import/export targets (image/disk/file)
    @property
    def targets_size_gb(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Failure message of the command
    failure_message: typing.Text = ...
    # Failure message of the command without privacy info
    failure_message_without_privacy_info: typing.Text = ...
    # Each element is the serial output log of a worker instance.
    # This is only populated if the workflow fails.
    @property
    def serial_outputs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    # Import file format
    import_file_format: typing.Text = ...
    # Size of import/export sources (image/disk/file) that was detected.
    # sources_size_gb, in contrast, contains the actual value. Ideally
    # these values will match; a mismatch indicates an error in our
    # detection.
    @property
    def detected_sources_size_gb(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Inflation type, which can be qemu or API.
    inflation_type: typing.Text = ...
    # Inflation time
    @property
    def inflation_time_ms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Inflation time of the shadow disk.  It's for new API validation.
    @property
    def shadow_inflation_time_ms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    # Shadow disk match result for shadow disk inflater. It's for new API
    # validation.
    shadow_disk_match_result: typing.Text = ...
    # Indicates whether the image is imported and marked as UEFI_COMPATIBLE.
    is_uefi_compatible_image: builtins.bool = ...
    # Indicates whether the image is auto-detected to be UEFI compatible.
    is_uefi_detected: builtins.bool = ...
    # Inspection results. Ref to the def of 'InspectionResults' to see details.
    @property
    def inspection_results(self) -> inspect_pb2.InspectionResults: ...
    def __init__(self,
        *,
        sources_size_gb : typing.Optional[typing.Iterable[builtins.int]] = ...,
        targets_size_gb : typing.Optional[typing.Iterable[builtins.int]] = ...,
        failure_message : typing.Text = ...,
        failure_message_without_privacy_info : typing.Text = ...,
        serial_outputs : typing.Optional[typing.Iterable[typing.Text]] = ...,
        import_file_format : typing.Text = ...,
        detected_sources_size_gb : typing.Optional[typing.Iterable[builtins.int]] = ...,
        inflation_type : typing.Text = ...,
        inflation_time_ms : typing.Optional[typing.Iterable[builtins.int]] = ...,
        shadow_inflation_time_ms : typing.Optional[typing.Iterable[builtins.int]] = ...,
        shadow_disk_match_result : typing.Text = ...,
        is_uefi_compatible_image : builtins.bool = ...,
        is_uefi_detected : builtins.bool = ...,
        inspection_results : typing.Optional[inspect_pb2.InspectionResults] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"inspection_results",b"inspection_results"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"detected_sources_size_gb",b"detected_sources_size_gb",u"failure_message",b"failure_message",u"failure_message_without_privacy_info",b"failure_message_without_privacy_info",u"import_file_format",b"import_file_format",u"inflation_time_ms",b"inflation_time_ms",u"inflation_type",b"inflation_type",u"inspection_results",b"inspection_results",u"is_uefi_compatible_image",b"is_uefi_compatible_image",u"is_uefi_detected",b"is_uefi_detected",u"serial_outputs",b"serial_outputs",u"shadow_disk_match_result",b"shadow_disk_match_result",u"shadow_inflation_time_ms",b"shadow_inflation_time_ms",u"sources_size_gb",b"sources_size_gb",u"targets_size_gb",b"targets_size_gb"]) -> None: ...
global___OutputInfo = OutputInfo

"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# Distro denotes a product line of operating systems, using the following
# test:
#   If two operating systems at the same version and CPU architecture can be
#   imported using the same logic, then they have the same Distro. For example,
#   if Ubuntu 20.04 and xubuntu 20.04 are importable using
#   the same logic, then they'd both be categorized as Distro.UBUNTU.
#
# When adding new members, keep in mind:
#  - Group distros by family, using buckets of size 1000.
#  - The following properties are orthogonal and should not be encoded here:
#      - CPU architecture
#      - Major or minor versions
#      - GCE licensing (such as BYOL)
class Distro(_Distro, metaclass=_DistroEnumTypeWrapper):
    pass
class _Distro:
    V = typing.NewType('V', builtins.int)
class _DistroEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Distro.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    DISTRO_UNKNOWN = Distro.V(0)
    WINDOWS = Distro.V(1000)
    DEBIAN = Distro.V(2000)
    UBUNTU = Distro.V(2001)
    KALI = Distro.V(2002)
    OPENSUSE = Distro.V(3000)
    SLES = Distro.V(3001)
    SLES_SAP = Distro.V(3002)
    FEDORA = Distro.V(4000)
    RHEL = Distro.V(4001)
    CENTOS = Distro.V(4002)
    AMAZON = Distro.V(4003)
    ORACLE = Distro.V(4004)
    ROCKY = Distro.V(4005)

DISTRO_UNKNOWN = Distro.V(0)
WINDOWS = Distro.V(1000)
DEBIAN = Distro.V(2000)
UBUNTU = Distro.V(2001)
KALI = Distro.V(2002)
OPENSUSE = Distro.V(3000)
SLES = Distro.V(3001)
SLES_SAP = Distro.V(3002)
FEDORA = Distro.V(4000)
RHEL = Distro.V(4001)
CENTOS = Distro.V(4002)
AMAZON = Distro.V(4003)
ORACLE = Distro.V(4004)
ROCKY = Distro.V(4005)
global___Distro = Distro


class Architecture(_Architecture, metaclass=_ArchitectureEnumTypeWrapper):
    pass
class _Architecture:
    V = typing.NewType('V', builtins.int)
class _ArchitectureEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Architecture.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ARCHITECTURE_UNKNOWN = Architecture.V(0)
    X86 = Architecture.V(1)
    X64 = Architecture.V(2)

ARCHITECTURE_UNKNOWN = Architecture.V(0)
X86 = Architecture.V(1)
X64 = Architecture.V(2)
global___Architecture = Architecture


# OsRelease records the name and version of an operating system.
class OsRelease(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLI_FORMATTED_FIELD_NUMBER: builtins.int
    DISTRO_FIELD_NUMBER: builtins.int
    MAJOR_VERSION_FIELD_NUMBER: builtins.int
    MINOR_VERSION_FIELD_NUMBER: builtins.int
    ARCHITECTURE_FIELD_NUMBER: builtins.int
    DISTRO_ID_FIELD_NUMBER: builtins.int
    # cli_formatted is a concatenation of distro, major_version, and
    # minor_version using the format expected by the `--os` flag.
    # For examples, see:
    #  https://cloud.google.com/sdk/gcloud/reference/compute/images/import#--os
    cli_formatted: typing.Text = ...
    # distro is the lowercase name of the distribution. Examples:
    # [centos, debian, opensuse, rhel, sles, sles-sap, ubuntu, windows]
    distro: typing.Text = ...
    # major_version of the OS, as represented by the vendor.
    # Examples:
    #   - Windows 2008r2: 2008
    #   - Ubuntu 18.04:  18
    #   - OpenSUSE Tumbleweed: tumbleweed
    major_version: typing.Text = ...
    # minor_version of the OS, as formatted by the vendor.
    # Examples:
    #   - Windows 2008r2: r2
    #   - Ubuntu 18.04:  04
    #   - OpenSUSE Tumbleweed: <empty>
    minor_version: typing.Text = ...
    architecture: global___Architecture.V = ...
    # Enumerated representation of the distro. Prefer this for
    # programmatic usage.
    distro_id: global___Distro.V = ...
    def __init__(self,
        *,
        cli_formatted : typing.Text = ...,
        distro : typing.Text = ...,
        major_version : typing.Text = ...,
        minor_version : typing.Text = ...,
        architecture : global___Architecture.V = ...,
        distro_id : global___Distro.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"architecture",b"architecture",u"cli_formatted",b"cli_formatted",u"distro",b"distro",u"distro_id",b"distro_id",u"major_version",b"major_version",u"minor_version",b"minor_version"]) -> None: ...
global___OsRelease = OsRelease

# InspectionResults contains metadata determined using automated inspection
# of the guest image.
class InspectionResults(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class ErrorWhen(_ErrorWhen, metaclass=_ErrorWhenEnumTypeWrapper):
        pass
    class _ErrorWhen:
        V = typing.NewType('V', builtins.int)
    class _ErrorWhenEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ErrorWhen.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        NO_ERROR = InspectionResults.ErrorWhen.V(0)
        STARTING_WORKER = InspectionResults.ErrorWhen.V(100)
        RUNNING_WORKER = InspectionResults.ErrorWhen.V(101)
        MOUNTING_GUEST = InspectionResults.ErrorWhen.V(200)
        INSPECTING_OS = InspectionResults.ErrorWhen.V(201)
        INSPECTING_BOOTLOADER = InspectionResults.ErrorWhen.V(202)
        DECODING_WORKER_RESPONSE = InspectionResults.ErrorWhen.V(300)
        INTERPRETING_INSPECTION_RESULTS = InspectionResults.ErrorWhen.V(301)

    NO_ERROR = InspectionResults.ErrorWhen.V(0)
    STARTING_WORKER = InspectionResults.ErrorWhen.V(100)
    RUNNING_WORKER = InspectionResults.ErrorWhen.V(101)
    MOUNTING_GUEST = InspectionResults.ErrorWhen.V(200)
    INSPECTING_OS = InspectionResults.ErrorWhen.V(201)
    INSPECTING_BOOTLOADER = InspectionResults.ErrorWhen.V(202)
    DECODING_WORKER_RESPONSE = InspectionResults.ErrorWhen.V(300)
    INTERPRETING_INSPECTION_RESULTS = InspectionResults.ErrorWhen.V(301)

    OS_RELEASE_FIELD_NUMBER: builtins.int
    BIOS_BOOTABLE_FIELD_NUMBER: builtins.int
    UEFI_BOOTABLE_FIELD_NUMBER: builtins.int
    ROOT_FS_FIELD_NUMBER: builtins.int
    ERROR_WHEN_FIELD_NUMBER: builtins.int
    ELAPSED_TIME_MS_FIELD_NUMBER: builtins.int
    OS_COUNT_FIELD_NUMBER: builtins.int
    # The OS and version detected. Populated when a single OS is
    # detected. Empty when none or multiple are found.
    @property
    def os_release(self) -> global___OsRelease: ...
    # bios_bootable indicates whether `os_release` is bootable using bios.
    bios_bootable: builtins.bool = ...
    # uefi_bootable indicates whether `os_release` is bootable with UEFI.
    uefi_bootable: builtins.bool = ...
    # root_fs indicates the file system type of the partition containing
    # the root directory ("/") of `os_release`.
    root_fs: typing.Text = ...
    # If inspection is not successful, when the error occurred.
    #
    # Success is independent of whether results were found. For example,
    # inspection of an empty disk will have empty results,
    # and error_when will be 'NO_ERROR'.
    error_when: global___InspectionResults.ErrorWhen.V = ...
    # Total time spent inspecting. This includes prep, running the worker,
    # and tearing down the worker.
    elapsed_time_ms: builtins.int = ...
    # Number of operating systems detected on the disk.
    os_count: builtins.int = ...
    def __init__(self,
        *,
        os_release : typing.Optional[global___OsRelease] = ...,
        bios_bootable : builtins.bool = ...,
        uefi_bootable : builtins.bool = ...,
        root_fs : typing.Text = ...,
        error_when : global___InspectionResults.ErrorWhen.V = ...,
        elapsed_time_ms : builtins.int = ...,
        os_count : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"os_release",b"os_release"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bios_bootable",b"bios_bootable",u"elapsed_time_ms",b"elapsed_time_ms",u"error_when",b"error_when",u"os_count",b"os_count",u"os_release",b"os_release",u"root_fs",b"root_fs",u"uefi_bootable",b"uefi_bootable"]) -> None: ...
global___InspectionResults = InspectionResults

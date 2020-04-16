# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/resource.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/resource.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\rResourceProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\370\001\001\242\002\004GAPI",
    serialized_pb=b'\n\x19google/api/resource.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"\xff\x01\n\x12ResourceDescriptor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07pattern\x18\x02 \x03(\t\x12\x12\n\nname_field\x18\x03 \x01(\t\x12\x37\n\x07history\x18\x04 \x01(\x0e\x32&.google.api.ResourceDescriptor.History\x12\x0e\n\x06plural\x18\x05 \x01(\t\x12\x10\n\x08singular\x18\x06 \x01(\t"[\n\x07History\x12\x17\n\x13HISTORY_UNSPECIFIED\x10\x00\x12\x1d\n\x19ORIGINALLY_SINGLE_PATTERN\x10\x01\x12\x18\n\x14\x46UTURE_MULTI_PATTERN\x10\x02"5\n\x11ResourceReference\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x12\n\nchild_type\x18\x02 \x01(\t:Y\n\x12resource_reference\x12\x1d.google.protobuf.FieldOptions\x18\x9f\x08 \x01(\x0b\x32\x1d.google.api.ResourceReference:Z\n\x13resource_definition\x12\x1c.google.protobuf.FileOptions\x18\x9d\x08 \x03(\x0b\x32\x1e.google.api.ResourceDescriptor:R\n\x08resource\x12\x1f.google.protobuf.MessageOptions\x18\x9d\x08 \x01(\x0b\x32\x1e.google.api.ResourceDescriptorBn\n\x0e\x63om.google.apiB\rResourceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xf8\x01\x01\xa2\x02\x04GAPIb\x06proto3',
    dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR],
)


RESOURCE_REFERENCE_FIELD_NUMBER = 1055
resource_reference = _descriptor.FieldDescriptor(
    name="resource_reference",
    full_name="google.api.resource_reference",
    index=0,
    number=1055,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
)
RESOURCE_DEFINITION_FIELD_NUMBER = 1053
resource_definition = _descriptor.FieldDescriptor(
    name="resource_definition",
    full_name="google.api.resource_definition",
    index=1,
    number=1053,
    type=11,
    cpp_type=10,
    label=3,
    has_default_value=False,
    default_value=[],
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
)
RESOURCE_FIELD_NUMBER = 1053
resource = _descriptor.FieldDescriptor(
    name="resource",
    full_name="google.api.resource",
    index=2,
    number=1053,
    type=11,
    cpp_type=10,
    label=1,
    has_default_value=False,
    default_value=None,
    message_type=None,
    enum_type=None,
    containing_type=None,
    is_extension=True,
    extension_scope=None,
    serialized_options=None,
    file=DESCRIPTOR,
)

_RESOURCEDESCRIPTOR_HISTORY = _descriptor.EnumDescriptor(
    name="History",
    full_name="google.api.ResourceDescriptor.History",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="HISTORY_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ORIGINALLY_SINGLE_PATTERN",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FUTURE_MULTI_PATTERN",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=240,
    serialized_end=331,
)
_sym_db.RegisterEnumDescriptor(_RESOURCEDESCRIPTOR_HISTORY)


_RESOURCEDESCRIPTOR = _descriptor.Descriptor(
    name="ResourceDescriptor",
    full_name="google.api.ResourceDescriptor",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.api.ResourceDescriptor.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="pattern",
            full_name="google.api.ResourceDescriptor.pattern",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="name_field",
            full_name="google.api.ResourceDescriptor.name_field",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="history",
            full_name="google.api.ResourceDescriptor.history",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="plural",
            full_name="google.api.ResourceDescriptor.plural",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="singular",
            full_name="google.api.ResourceDescriptor.singular",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_RESOURCEDESCRIPTOR_HISTORY],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=76,
    serialized_end=331,
)


_RESOURCEREFERENCE = _descriptor.Descriptor(
    name="ResourceReference",
    full_name="google.api.ResourceReference",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.api.ResourceReference.type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="child_type",
            full_name="google.api.ResourceReference.child_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=333,
    serialized_end=386,
)

_RESOURCEDESCRIPTOR.fields_by_name["history"].enum_type = _RESOURCEDESCRIPTOR_HISTORY
_RESOURCEDESCRIPTOR_HISTORY.containing_type = _RESOURCEDESCRIPTOR
DESCRIPTOR.message_types_by_name["ResourceDescriptor"] = _RESOURCEDESCRIPTOR
DESCRIPTOR.message_types_by_name["ResourceReference"] = _RESOURCEREFERENCE
DESCRIPTOR.extensions_by_name["resource_reference"] = resource_reference
DESCRIPTOR.extensions_by_name["resource_definition"] = resource_definition
DESCRIPTOR.extensions_by_name["resource"] = resource
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceDescriptor = _reflection.GeneratedProtocolMessageType(
    "ResourceDescriptor",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCEDESCRIPTOR,
        "__module__": "google.api.resource_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ResourceDescriptor)
    },
)
_sym_db.RegisterMessage(ResourceDescriptor)

ResourceReference = _reflection.GeneratedProtocolMessageType(
    "ResourceReference",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESOURCEREFERENCE,
        "__module__": "google.api.resource_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ResourceReference)
    },
)
_sym_db.RegisterMessage(ResourceReference)

resource_reference.message_type = _RESOURCEREFERENCE
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(
    resource_reference
)
resource_definition.message_type = _RESOURCEDESCRIPTOR
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(
    resource_definition
)
resource.message_type = _RESOURCEDESCRIPTOR
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(resource)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

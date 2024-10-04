// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.30.0
// 	protoc        v5.27.1
// source: feast/core/Entity.proto

package core

import (
	types "github.com/caraml-dev/caraml-store/caraml-store-sdk/go/protos/feast/types"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Entity struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// User-specified specifications of this entity.
	Spec *EntitySpec `protobuf:"bytes,1,opt,name=spec,proto3" json:"spec,omitempty"`
	// System-populated metadata for this entity.
	Meta *EntityMeta `protobuf:"bytes,2,opt,name=meta,proto3" json:"meta,omitempty"`
}

func (x *Entity) Reset() {
	*x = Entity{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_Entity_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Entity) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Entity) ProtoMessage() {}

func (x *Entity) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_Entity_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Entity.ProtoReflect.Descriptor instead.
func (*Entity) Descriptor() ([]byte, []int) {
	return file_feast_core_Entity_proto_rawDescGZIP(), []int{0}
}

func (x *Entity) GetSpec() *EntitySpec {
	if x != nil {
		return x.Spec
	}
	return nil
}

func (x *Entity) GetMeta() *EntityMeta {
	if x != nil {
		return x.Meta
	}
	return nil
}

type EntitySpec struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// Name of the entity.
	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// Type of the entity.
	ValueType types.ValueType_Enum `protobuf:"varint,2,opt,name=value_type,json=valueType,proto3,enum=feast.types.ValueType_Enum" json:"value_type,omitempty"`
	// Description of the entity.
	Description string `protobuf:"bytes,3,opt,name=description,proto3" json:"description,omitempty"`
	// User defined metadata
	Labels map[string]string `protobuf:"bytes,8,rep,name=labels,proto3" json:"labels,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
}

func (x *EntitySpec) Reset() {
	*x = EntitySpec{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_Entity_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EntitySpec) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EntitySpec) ProtoMessage() {}

func (x *EntitySpec) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_Entity_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EntitySpec.ProtoReflect.Descriptor instead.
func (*EntitySpec) Descriptor() ([]byte, []int) {
	return file_feast_core_Entity_proto_rawDescGZIP(), []int{1}
}

func (x *EntitySpec) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *EntitySpec) GetValueType() types.ValueType_Enum {
	if x != nil {
		return x.ValueType
	}
	return types.ValueType_Enum(0)
}

func (x *EntitySpec) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *EntitySpec) GetLabels() map[string]string {
	if x != nil {
		return x.Labels
	}
	return nil
}

type EntityMeta struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	CreatedTimestamp     *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=created_timestamp,json=createdTimestamp,proto3" json:"created_timestamp,omitempty"`
	LastUpdatedTimestamp *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=last_updated_timestamp,json=lastUpdatedTimestamp,proto3" json:"last_updated_timestamp,omitempty"`
}

func (x *EntityMeta) Reset() {
	*x = EntityMeta{}
	if protoimpl.UnsafeEnabled {
		mi := &file_feast_core_Entity_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *EntityMeta) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*EntityMeta) ProtoMessage() {}

func (x *EntityMeta) ProtoReflect() protoreflect.Message {
	mi := &file_feast_core_Entity_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use EntityMeta.ProtoReflect.Descriptor instead.
func (*EntityMeta) Descriptor() ([]byte, []int) {
	return file_feast_core_Entity_proto_rawDescGZIP(), []int{2}
}

func (x *EntityMeta) GetCreatedTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedTimestamp
	}
	return nil
}

func (x *EntityMeta) GetLastUpdatedTimestamp() *timestamppb.Timestamp {
	if x != nil {
		return x.LastUpdatedTimestamp
	}
	return nil
}

var File_feast_core_Entity_proto protoreflect.FileDescriptor

var file_feast_core_Entity_proto_rawDesc = []byte{
	0x0a, 0x17, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x45, 0x6e, 0x74,
	0x69, 0x74, 0x79, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x0a, 0x66, 0x65, 0x61, 0x73, 0x74,
	0x2e, 0x63, 0x6f, 0x72, 0x65, 0x1a, 0x17, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x74, 0x79, 0x70,
	0x65, 0x73, 0x2f, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f,
	0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22,
	0x60, 0x0a, 0x06, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x12, 0x2a, 0x0a, 0x04, 0x73, 0x70, 0x65,
	0x63, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e,
	0x63, 0x6f, 0x72, 0x65, 0x2e, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x53, 0x70, 0x65, 0x63, 0x52,
	0x04, 0x73, 0x70, 0x65, 0x63, 0x12, 0x2a, 0x0a, 0x04, 0x6d, 0x65, 0x74, 0x61, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x16, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65,
	0x2e, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x4d, 0x65, 0x74, 0x61, 0x52, 0x04, 0x6d, 0x65, 0x74,
	0x61, 0x22, 0xf5, 0x01, 0x0a, 0x0a, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x53, 0x70, 0x65, 0x63,
	0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04,
	0x6e, 0x61, 0x6d, 0x65, 0x12, 0x3a, 0x0a, 0x0a, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x5f, 0x74, 0x79,
	0x70, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x1b, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74,
	0x2e, 0x74, 0x79, 0x70, 0x65, 0x73, 0x2e, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x54, 0x79, 0x70, 0x65,
	0x2e, 0x45, 0x6e, 0x75, 0x6d, 0x52, 0x09, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x54, 0x79, 0x70, 0x65,
	0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x18,
	0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69,
	0x6f, 0x6e, 0x12, 0x3a, 0x0a, 0x06, 0x6c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x18, 0x08, 0x20, 0x03,
	0x28, 0x0b, 0x32, 0x22, 0x2e, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2e, 0x63, 0x6f, 0x72, 0x65, 0x2e,
	0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x53, 0x70, 0x65, 0x63, 0x2e, 0x4c, 0x61, 0x62, 0x65, 0x6c,
	0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x06, 0x6c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x1a, 0x39,
	0x0a, 0x0b, 0x4c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a,
	0x03, 0x6b, 0x65, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12,
	0x14, 0x0a, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0xa7, 0x01, 0x0a, 0x0a, 0x45, 0x6e,
	0x74, 0x69, 0x74, 0x79, 0x4d, 0x65, 0x74, 0x61, 0x12, 0x47, 0x0a, 0x11, 0x63, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x64, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52,
	0x10, 0x63, 0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x12, 0x50, 0x0a, 0x16, 0x6c, 0x61, 0x73, 0x74, 0x5f, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65,
	0x64, 0x5f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x14, 0x6c,
	0x61, 0x73, 0x74, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74,
	0x61, 0x6d, 0x70, 0x42, 0x77, 0x0a, 0x1e, 0x64, 0x65, 0x76, 0x2e, 0x63, 0x61, 0x72, 0x61, 0x6d,
	0x6c, 0x2e, 0x73, 0x74, 0x6f, 0x72, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x63, 0x6f, 0x72, 0x65, 0x42, 0x0b, 0x45, 0x6e, 0x74, 0x69, 0x74, 0x79, 0x50, 0x72, 0x6f,
	0x74, 0x6f, 0x5a, 0x48, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x63,
	0x61, 0x72, 0x61, 0x6d, 0x6c, 0x2d, 0x64, 0x65, 0x76, 0x2f, 0x63, 0x61, 0x72, 0x61, 0x6d, 0x6c,
	0x2d, 0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x63, 0x61, 0x72, 0x61, 0x6d, 0x6c, 0x2d, 0x73, 0x74,
	0x6f, 0x72, 0x65, 0x2d, 0x73, 0x64, 0x6b, 0x2f, 0x67, 0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x73, 0x2f, 0x66, 0x65, 0x61, 0x73, 0x74, 0x2f, 0x63, 0x6f, 0x72, 0x65, 0x62, 0x06, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_feast_core_Entity_proto_rawDescOnce sync.Once
	file_feast_core_Entity_proto_rawDescData = file_feast_core_Entity_proto_rawDesc
)

func file_feast_core_Entity_proto_rawDescGZIP() []byte {
	file_feast_core_Entity_proto_rawDescOnce.Do(func() {
		file_feast_core_Entity_proto_rawDescData = protoimpl.X.CompressGZIP(file_feast_core_Entity_proto_rawDescData)
	})
	return file_feast_core_Entity_proto_rawDescData
}

var file_feast_core_Entity_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_feast_core_Entity_proto_goTypes = []interface{}{
	(*Entity)(nil),                // 0: feast.core.Entity
	(*EntitySpec)(nil),            // 1: feast.core.EntitySpec
	(*EntityMeta)(nil),            // 2: feast.core.EntityMeta
	nil,                           // 3: feast.core.EntitySpec.LabelsEntry
	(types.ValueType_Enum)(0),     // 4: feast.types.ValueType.Enum
	(*timestamppb.Timestamp)(nil), // 5: google.protobuf.Timestamp
}
var file_feast_core_Entity_proto_depIdxs = []int32{
	1, // 0: feast.core.Entity.spec:type_name -> feast.core.EntitySpec
	2, // 1: feast.core.Entity.meta:type_name -> feast.core.EntityMeta
	4, // 2: feast.core.EntitySpec.value_type:type_name -> feast.types.ValueType.Enum
	3, // 3: feast.core.EntitySpec.labels:type_name -> feast.core.EntitySpec.LabelsEntry
	5, // 4: feast.core.EntityMeta.created_timestamp:type_name -> google.protobuf.Timestamp
	5, // 5: feast.core.EntityMeta.last_updated_timestamp:type_name -> google.protobuf.Timestamp
	6, // [6:6] is the sub-list for method output_type
	6, // [6:6] is the sub-list for method input_type
	6, // [6:6] is the sub-list for extension type_name
	6, // [6:6] is the sub-list for extension extendee
	0, // [0:6] is the sub-list for field type_name
}

func init() { file_feast_core_Entity_proto_init() }
func file_feast_core_Entity_proto_init() {
	if File_feast_core_Entity_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_feast_core_Entity_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Entity); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_feast_core_Entity_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EntitySpec); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_feast_core_Entity_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*EntityMeta); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_feast_core_Entity_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_feast_core_Entity_proto_goTypes,
		DependencyIndexes: file_feast_core_Entity_proto_depIdxs,
		MessageInfos:      file_feast_core_Entity_proto_msgTypes,
	}.Build()
	File_feast_core_Entity_proto = out.File
	file_feast_core_Entity_proto_rawDesc = nil
	file_feast_core_Entity_proto_goTypes = nil
	file_feast_core_Entity_proto_depIdxs = nil
}

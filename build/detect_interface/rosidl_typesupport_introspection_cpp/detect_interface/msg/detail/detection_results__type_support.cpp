// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "detect_interface/msg/detail/detection_results__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace detect_interface
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void DetectionResults_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) detect_interface::msg::DetectionResults(_init);
}

void DetectionResults_fini_function(void * message_memory)
{
  auto typed_message = static_cast<detect_interface::msg::DetectionResults *>(message_memory);
  typed_message->~DetectionResults();
}

size_t size_function__DetectionResults__labels(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectionResults__labels(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectionResults__labels(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<std::string> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectionResults__labels(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const std::string *>(
    get_const_function__DetectionResults__labels(untyped_member, index));
  auto & value = *reinterpret_cast<std::string *>(untyped_value);
  value = item;
}

void assign_function__DetectionResults__labels(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<std::string *>(
    get_function__DetectionResults__labels(untyped_member, index));
  const auto & value = *reinterpret_cast<const std::string *>(untyped_value);
  item = value;
}

void resize_function__DetectionResults__labels(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<std::string> *>(untyped_member);
  member->resize(size);
}

size_t size_function__DetectionResults__scores(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<float> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectionResults__scores(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<float> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectionResults__scores(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<float> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectionResults__scores(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const float *>(
    get_const_function__DetectionResults__scores(untyped_member, index));
  auto & value = *reinterpret_cast<float *>(untyped_value);
  value = item;
}

void assign_function__DetectionResults__scores(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<float *>(
    get_function__DetectionResults__scores(untyped_member, index));
  const auto & value = *reinterpret_cast<const float *>(untyped_value);
  item = value;
}

void resize_function__DetectionResults__scores(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<float> *>(untyped_member);
  member->resize(size);
}

size_t size_function__DetectionResults__bounding_boxes(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<detect_interface::msg::BoundingBox> *>(untyped_member);
  return member->size();
}

const void * get_const_function__DetectionResults__bounding_boxes(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<detect_interface::msg::BoundingBox> *>(untyped_member);
  return &member[index];
}

void * get_function__DetectionResults__bounding_boxes(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<detect_interface::msg::BoundingBox> *>(untyped_member);
  return &member[index];
}

void fetch_function__DetectionResults__bounding_boxes(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const detect_interface::msg::BoundingBox *>(
    get_const_function__DetectionResults__bounding_boxes(untyped_member, index));
  auto & value = *reinterpret_cast<detect_interface::msg::BoundingBox *>(untyped_value);
  value = item;
}

void assign_function__DetectionResults__bounding_boxes(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<detect_interface::msg::BoundingBox *>(
    get_function__DetectionResults__bounding_boxes(untyped_member, index));
  const auto & value = *reinterpret_cast<const detect_interface::msg::BoundingBox *>(untyped_value);
  item = value;
}

void resize_function__DetectionResults__bounding_boxes(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<detect_interface::msg::BoundingBox> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember DetectionResults_message_member_array[3] = {
  {
    "labels",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(detect_interface::msg::DetectionResults, labels),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectionResults__labels,  // size() function pointer
    get_const_function__DetectionResults__labels,  // get_const(index) function pointer
    get_function__DetectionResults__labels,  // get(index) function pointer
    fetch_function__DetectionResults__labels,  // fetch(index, &value) function pointer
    assign_function__DetectionResults__labels,  // assign(index, value) function pointer
    resize_function__DetectionResults__labels  // resize(index) function pointer
  },
  {
    "scores",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(detect_interface::msg::DetectionResults, scores),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectionResults__scores,  // size() function pointer
    get_const_function__DetectionResults__scores,  // get_const(index) function pointer
    get_function__DetectionResults__scores,  // get(index) function pointer
    fetch_function__DetectionResults__scores,  // fetch(index, &value) function pointer
    assign_function__DetectionResults__scores,  // assign(index, value) function pointer
    resize_function__DetectionResults__scores  // resize(index) function pointer
  },
  {
    "bounding_boxes",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<detect_interface::msg::BoundingBox>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(detect_interface::msg::DetectionResults, bounding_boxes),  // bytes offset in struct
    nullptr,  // default value
    size_function__DetectionResults__bounding_boxes,  // size() function pointer
    get_const_function__DetectionResults__bounding_boxes,  // get_const(index) function pointer
    get_function__DetectionResults__bounding_boxes,  // get(index) function pointer
    fetch_function__DetectionResults__bounding_boxes,  // fetch(index, &value) function pointer
    assign_function__DetectionResults__bounding_boxes,  // assign(index, value) function pointer
    resize_function__DetectionResults__bounding_boxes  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers DetectionResults_message_members = {
  "detect_interface::msg",  // message namespace
  "DetectionResults",  // message name
  3,  // number of fields
  sizeof(detect_interface::msg::DetectionResults),
  DetectionResults_message_member_array,  // message members
  DetectionResults_init_function,  // function to initialize message memory (memory has to be allocated)
  DetectionResults_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t DetectionResults_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &DetectionResults_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace detect_interface


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<detect_interface::msg::DetectionResults>()
{
  return &::detect_interface::msg::rosidl_typesupport_introspection_cpp::DetectionResults_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, detect_interface, msg, DetectionResults)() {
  return &::detect_interface::msg::rosidl_typesupport_introspection_cpp::DetectionResults_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "detect_interface/msg/detail/detection_results__rosidl_typesupport_introspection_c.h"
#include "detect_interface/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "detect_interface/msg/detail/detection_results__functions.h"
#include "detect_interface/msg/detail/detection_results__struct.h"


// Include directives for member types
// Member `labels`
#include "rosidl_runtime_c/string_functions.h"
// Member `scores`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `bounding_boxes`
#include "detect_interface/msg/bounding_box.h"
// Member `bounding_boxes`
#include "detect_interface/msg/detail/bounding_box__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  detect_interface__msg__DetectionResults__init(message_memory);
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_fini_function(void * message_memory)
{
  detect_interface__msg__DetectionResults__fini(message_memory);
}

size_t detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__size_function__DetectionResults__labels(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__labels(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__labels(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__fetch_function__DetectionResults__labels(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__labels(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__assign_function__DetectionResults__labels(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__labels(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__resize_function__DetectionResults__labels(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

size_t detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__size_function__DetectionResults__scores(
  const void * untyped_member)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return member->size;
}

const void * detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__scores(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__float__Sequence * member =
    (const rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void * detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__scores(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  return &member->data[index];
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__fetch_function__DetectionResults__scores(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__scores(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__assign_function__DetectionResults__scores(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__scores(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

bool detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__resize_function__DetectionResults__scores(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__float__Sequence * member =
    (rosidl_runtime_c__float__Sequence *)(untyped_member);
  rosidl_runtime_c__float__Sequence__fini(member);
  return rosidl_runtime_c__float__Sequence__init(member, size);
}

size_t detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__size_function__DetectionResults__bounding_boxes(
  const void * untyped_member)
{
  const detect_interface__msg__BoundingBox__Sequence * member =
    (const detect_interface__msg__BoundingBox__Sequence *)(untyped_member);
  return member->size;
}

const void * detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__bounding_boxes(
  const void * untyped_member, size_t index)
{
  const detect_interface__msg__BoundingBox__Sequence * member =
    (const detect_interface__msg__BoundingBox__Sequence *)(untyped_member);
  return &member->data[index];
}

void * detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__bounding_boxes(
  void * untyped_member, size_t index)
{
  detect_interface__msg__BoundingBox__Sequence * member =
    (detect_interface__msg__BoundingBox__Sequence *)(untyped_member);
  return &member->data[index];
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__fetch_function__DetectionResults__bounding_boxes(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const detect_interface__msg__BoundingBox * item =
    ((const detect_interface__msg__BoundingBox *)
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__bounding_boxes(untyped_member, index));
  detect_interface__msg__BoundingBox * value =
    (detect_interface__msg__BoundingBox *)(untyped_value);
  *value = *item;
}

void detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__assign_function__DetectionResults__bounding_boxes(
  void * untyped_member, size_t index, const void * untyped_value)
{
  detect_interface__msg__BoundingBox * item =
    ((detect_interface__msg__BoundingBox *)
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__bounding_boxes(untyped_member, index));
  const detect_interface__msg__BoundingBox * value =
    (const detect_interface__msg__BoundingBox *)(untyped_value);
  *item = *value;
}

bool detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__resize_function__DetectionResults__bounding_boxes(
  void * untyped_member, size_t size)
{
  detect_interface__msg__BoundingBox__Sequence * member =
    (detect_interface__msg__BoundingBox__Sequence *)(untyped_member);
  detect_interface__msg__BoundingBox__Sequence__fini(member);
  return detect_interface__msg__BoundingBox__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_member_array[3] = {
  {
    "labels",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(detect_interface__msg__DetectionResults, labels),  // bytes offset in struct
    NULL,  // default value
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__size_function__DetectionResults__labels,  // size() function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__labels,  // get_const(index) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__labels,  // get(index) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__fetch_function__DetectionResults__labels,  // fetch(index, &value) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__assign_function__DetectionResults__labels,  // assign(index, value) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__resize_function__DetectionResults__labels  // resize(index) function pointer
  },
  {
    "scores",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(detect_interface__msg__DetectionResults, scores),  // bytes offset in struct
    NULL,  // default value
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__size_function__DetectionResults__scores,  // size() function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__scores,  // get_const(index) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__scores,  // get(index) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__fetch_function__DetectionResults__scores,  // fetch(index, &value) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__assign_function__DetectionResults__scores,  // assign(index, value) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__resize_function__DetectionResults__scores  // resize(index) function pointer
  },
  {
    "bounding_boxes",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(detect_interface__msg__DetectionResults, bounding_boxes),  // bytes offset in struct
    NULL,  // default value
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__size_function__DetectionResults__bounding_boxes,  // size() function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_const_function__DetectionResults__bounding_boxes,  // get_const(index) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__get_function__DetectionResults__bounding_boxes,  // get(index) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__fetch_function__DetectionResults__bounding_boxes,  // fetch(index, &value) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__assign_function__DetectionResults__bounding_boxes,  // assign(index, value) function pointer
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__resize_function__DetectionResults__bounding_boxes  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_members = {
  "detect_interface__msg",  // message namespace
  "DetectionResults",  // message name
  3,  // number of fields
  sizeof(detect_interface__msg__DetectionResults),
  detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_member_array,  // message members
  detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_init_function,  // function to initialize message memory (memory has to be allocated)
  detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_type_support_handle = {
  0,
  &detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_detect_interface
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, detect_interface, msg, DetectionResults)() {
  detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, detect_interface, msg, BoundingBox)();
  if (!detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_type_support_handle.typesupport_identifier) {
    detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &detect_interface__msg__DetectionResults__rosidl_typesupport_introspection_c__DetectionResults_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

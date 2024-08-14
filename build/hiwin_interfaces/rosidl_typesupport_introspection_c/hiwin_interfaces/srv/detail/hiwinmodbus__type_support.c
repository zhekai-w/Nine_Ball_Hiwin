// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "hiwin_interfaces/srv/detail/hiwinmodbus__rosidl_typesupport_introspection_c.h"
#include "hiwin_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "hiwin_interfaces/srv/detail/hiwinmodbus__functions.h"
#include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.h"


// Include directives for member types
// Member `mode`
#include "rosidl_runtime_c/string_functions.h"
// Member `pose`
// Member `circ_s`
// Member `circ_end`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  hiwin_interfaces__srv__Hiwinmodbus_Request__init(message_memory);
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_fini_function(void * message_memory)
{
  hiwin_interfaces__srv__Hiwinmodbus_Request__fini(message_memory);
}

size_t hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__size_function__Hiwinmodbus_Request__pose(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__pose(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__pose(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__fetch_function__Hiwinmodbus_Request__pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__pose(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__assign_function__Hiwinmodbus_Request__pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__pose(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__resize_function__Hiwinmodbus_Request__pose(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__size_function__Hiwinmodbus_Request__circ_s(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__circ_s(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__circ_s(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__fetch_function__Hiwinmodbus_Request__circ_s(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__circ_s(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__assign_function__Hiwinmodbus_Request__circ_s(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__circ_s(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__resize_function__Hiwinmodbus_Request__circ_s(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__size_function__Hiwinmodbus_Request__circ_end(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__circ_end(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__circ_end(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__fetch_function__Hiwinmodbus_Request__circ_end(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__circ_end(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__assign_function__Hiwinmodbus_Request__circ_end(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__circ_end(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__resize_function__Hiwinmodbus_Request__circ_end(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_member_array[12] = {
  {
    "mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "holding",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, holding),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "vel",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, vel),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "acc",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, acc),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "digital_output",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, digital_output),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "onoff",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, onoff),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "pose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, pose),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__size_function__Hiwinmodbus_Request__pose,  // size() function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__pose,  // get_const(index) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__pose,  // get(index) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__fetch_function__Hiwinmodbus_Request__pose,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__assign_function__Hiwinmodbus_Request__pose,  // assign(index, value) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__resize_function__Hiwinmodbus_Request__pose  // resize(index) function pointer
  },
  {
    "circ_s",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, circ_s),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__size_function__Hiwinmodbus_Request__circ_s,  // size() function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__circ_s,  // get_const(index) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__circ_s,  // get(index) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__fetch_function__Hiwinmodbus_Request__circ_s,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__assign_function__Hiwinmodbus_Request__circ_s,  // assign(index, value) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__resize_function__Hiwinmodbus_Request__circ_s  // resize(index) function pointer
  },
  {
    "circ_end",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, circ_end),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__size_function__Hiwinmodbus_Request__circ_end,  // size() function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_const_function__Hiwinmodbus_Request__circ_end,  // get_const(index) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__get_function__Hiwinmodbus_Request__circ_end,  // get(index) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__fetch_function__Hiwinmodbus_Request__circ_end,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__assign_function__Hiwinmodbus_Request__circ_end,  // assign(index, value) function pointer
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__resize_function__Hiwinmodbus_Request__circ_end  // resize(index) function pointer
  },
  {
    "joint",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, joint),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "dir",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Request, dir),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_members = {
  "hiwin_interfaces__srv",  // message namespace
  "Hiwinmodbus_Request",  // message name
  12,  // number of fields
  sizeof(hiwin_interfaces__srv__Hiwinmodbus_Request),
  hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_member_array,  // message members
  hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_type_support_handle = {
  0,
  &hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hiwin_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus_Request)() {
  if (!hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_type_support_handle.typesupport_identifier) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &hiwin_interfaces__srv__Hiwinmodbus_Request__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__rosidl_typesupport_introspection_c.h"
// already included above
// #include "hiwin_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__functions.h"
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  hiwin_interfaces__srv__Hiwinmodbus_Response__init(message_memory);
}

void hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_fini_function(void * message_memory)
{
  hiwin_interfaces__srv__Hiwinmodbus_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_member_array[1] = {
  {
    "arm_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__Hiwinmodbus_Response, arm_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_members = {
  "hiwin_interfaces__srv",  // message namespace
  "Hiwinmodbus_Response",  // message name
  1,  // number of fields
  sizeof(hiwin_interfaces__srv__Hiwinmodbus_Response),
  hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_member_array,  // message members
  hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_type_support_handle = {
  0,
  &hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hiwin_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus_Response)() {
  if (!hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_type_support_handle.typesupport_identifier) {
    hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &hiwin_interfaces__srv__Hiwinmodbus_Response__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "hiwin_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_members = {
  "hiwin_interfaces__srv",  // service namespace
  "Hiwinmodbus",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_Request_message_type_support_handle,
  NULL  // response message
  // hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_Response_message_type_support_handle
};

static rosidl_service_type_support_t hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_type_support_handle = {
  0,
  &hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hiwin_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus)() {
  if (!hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_type_support_handle.typesupport_identifier) {
    hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, Hiwinmodbus_Response)()->data;
  }

  return &hiwin_interfaces__srv__detail__hiwinmodbus__rosidl_typesupport_introspection_c__Hiwinmodbus_service_type_support_handle;
}

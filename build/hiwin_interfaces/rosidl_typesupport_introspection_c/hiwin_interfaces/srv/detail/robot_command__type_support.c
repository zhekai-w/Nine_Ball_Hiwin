// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "hiwin_interfaces/srv/detail/robot_command__rosidl_typesupport_introspection_c.h"
#include "hiwin_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "hiwin_interfaces/srv/detail/robot_command__functions.h"
#include "hiwin_interfaces/srv/detail/robot_command__struct.h"


// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/twist.h"
// Member `pose`
#include "geometry_msgs/msg/detail/twist__rosidl_typesupport_introspection_c.h"
// Member `circ_s`
// Member `circ_end`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  hiwin_interfaces__srv__RobotCommand_Request__init(message_memory);
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_fini_function(void * message_memory)
{
  hiwin_interfaces__srv__RobotCommand_Request__fini(message_memory);
}

size_t hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__size_function__RobotCommand_Request__joints(
  const void * untyped_member)
{
  (void)untyped_member;
  return 6;
}

const void * hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__joints(
  const void * untyped_member, size_t index)
{
  const double * member =
    (const double *)(untyped_member);
  return &member[index];
}

void * hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__joints(
  void * untyped_member, size_t index)
{
  double * member =
    (double *)(untyped_member);
  return &member[index];
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Request__joints(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__joints(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Request__joints(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__joints(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

size_t hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__size_function__RobotCommand_Request__circ_s(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__circ_s(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__circ_s(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Request__circ_s(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__circ_s(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Request__circ_s(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__circ_s(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__resize_function__RobotCommand_Request__circ_s(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__size_function__RobotCommand_Request__circ_end(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__circ_end(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__circ_end(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Request__circ_end(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__circ_end(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Request__circ_end(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__circ_end(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__resize_function__RobotCommand_Request__circ_end(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_member_array[19] = {
  {
    "do_timer",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, do_timer),  // bytes offset in struct
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
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, holding),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "cmd_mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, cmd_mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "cmd_type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, cmd_type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "velocity",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, velocity),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "acceleration",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, acceleration),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tool",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, tool),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "base",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, base),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "base_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, base_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "tool_num",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, tool_num),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "digital_input_pin",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, digital_input_pin),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "digital_output_pin",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, digital_output_pin),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "digital_output_cmd",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, digital_output_cmd),  // bytes offset in struct
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
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, pose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "joints",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    6,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, joints),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__size_function__RobotCommand_Request__joints,  // size() function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__joints,  // get_const(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__joints,  // get(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Request__joints,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Request__joints,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "circ_s",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, circ_s),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__size_function__RobotCommand_Request__circ_s,  // size() function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__circ_s,  // get_const(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__circ_s,  // get(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Request__circ_s,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Request__circ_s,  // assign(index, value) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__resize_function__RobotCommand_Request__circ_s  // resize(index) function pointer
  },
  {
    "circ_end",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, circ_end),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__size_function__RobotCommand_Request__circ_end,  // size() function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Request__circ_end,  // get_const(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__get_function__RobotCommand_Request__circ_end,  // get(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Request__circ_end,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Request__circ_end,  // assign(index, value) function pointer
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__resize_function__RobotCommand_Request__circ_end  // resize(index) function pointer
  },
  {
    "jog_joint",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, jog_joint),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "jog_dir",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Request, jog_dir),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_members = {
  "hiwin_interfaces__srv",  // message namespace
  "RobotCommand_Request",  // message name
  19,  // number of fields
  sizeof(hiwin_interfaces__srv__RobotCommand_Request),
  hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_member_array,  // message members
  hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_type_support_handle = {
  0,
  &hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hiwin_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand_Request)() {
  hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_member_array[13].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Twist)();
  if (!hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_type_support_handle.typesupport_identifier) {
    hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &hiwin_interfaces__srv__RobotCommand_Request__rosidl_typesupport_introspection_c__RobotCommand_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__rosidl_typesupport_introspection_c.h"
// already included above
// #include "hiwin_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__functions.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__struct.h"


// Include directives for member types
// Member `current_position`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  hiwin_interfaces__srv__RobotCommand_Response__init(message_memory);
}

void hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_fini_function(void * message_memory)
{
  hiwin_interfaces__srv__RobotCommand_Response__fini(message_memory);
}

size_t hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__size_function__RobotCommand_Response__current_position(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Response__current_position(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__get_function__RobotCommand_Response__current_position(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Response__current_position(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Response__current_position(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Response__current_position(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__get_function__RobotCommand_Response__current_position(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__resize_function__RobotCommand_Response__current_position(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_member_array[3] = {
  {
    "arm_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Response, arm_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "digital_state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Response, digital_state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "current_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces__srv__RobotCommand_Response, current_position),  // bytes offset in struct
    NULL,  // default value
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__size_function__RobotCommand_Response__current_position,  // size() function pointer
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__get_const_function__RobotCommand_Response__current_position,  // get_const(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__get_function__RobotCommand_Response__current_position,  // get(index) function pointer
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__fetch_function__RobotCommand_Response__current_position,  // fetch(index, &value) function pointer
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__assign_function__RobotCommand_Response__current_position,  // assign(index, value) function pointer
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__resize_function__RobotCommand_Response__current_position  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_members = {
  "hiwin_interfaces__srv",  // message namespace
  "RobotCommand_Response",  // message name
  3,  // number of fields
  sizeof(hiwin_interfaces__srv__RobotCommand_Response),
  hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_member_array,  // message members
  hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_type_support_handle = {
  0,
  &hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hiwin_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand_Response)() {
  if (!hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_type_support_handle.typesupport_identifier) {
    hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &hiwin_interfaces__srv__RobotCommand_Response__rosidl_typesupport_introspection_c__RobotCommand_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "hiwin_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_members = {
  "hiwin_interfaces__srv",  // service namespace
  "RobotCommand",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_Request_message_type_support_handle,
  NULL  // response message
  // hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_Response_message_type_support_handle
};

static rosidl_service_type_support_t hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_type_support_handle = {
  0,
  &hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_hiwin_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand)() {
  if (!hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_type_support_handle.typesupport_identifier) {
    hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, hiwin_interfaces, srv, RobotCommand_Response)()->data;
  }

  return &hiwin_interfaces__srv__detail__robot_command__rosidl_typesupport_introspection_c__RobotCommand_service_type_support_handle;
}

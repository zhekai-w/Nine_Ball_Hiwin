// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice
#include "hiwin_interfaces/srv/detail/robot_command__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "hiwin_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "hiwin_interfaces/srv/detail/robot_command__struct.h"
#include "hiwin_interfaces/srv/detail/robot_command__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "geometry_msgs/msg/detail/twist__functions.h"  // pose
#include "rosidl_runtime_c/primitives_sequence.h"  // circ_end, circ_s
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // circ_end, circ_s

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_hiwin_interfaces
size_t get_serialized_size_geometry_msgs__msg__Twist(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_hiwin_interfaces
size_t max_serialized_size_geometry_msgs__msg__Twist(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_hiwin_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, geometry_msgs, msg, Twist)();


using _RobotCommand_Request__ros_msg_type = hiwin_interfaces__srv__RobotCommand_Request;

static bool _RobotCommand_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RobotCommand_Request__ros_msg_type * ros_message = static_cast<const _RobotCommand_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: do_timer
  {
    cdr << ros_message->do_timer;
  }

  // Field name: holding
  {
    cdr << (ros_message->holding ? true : false);
  }

  // Field name: cmd_mode
  {
    cdr << ros_message->cmd_mode;
  }

  // Field name: cmd_type
  {
    cdr << ros_message->cmd_type;
  }

  // Field name: velocity
  {
    cdr << ros_message->velocity;
  }

  // Field name: acceleration
  {
    cdr << ros_message->acceleration;
  }

  // Field name: tool
  {
    cdr << ros_message->tool;
  }

  // Field name: base
  {
    cdr << ros_message->base;
  }

  // Field name: base_num
  {
    cdr << ros_message->base_num;
  }

  // Field name: tool_num
  {
    cdr << ros_message->tool_num;
  }

  // Field name: digital_input_pin
  {
    cdr << ros_message->digital_input_pin;
  }

  // Field name: digital_output_pin
  {
    cdr << ros_message->digital_output_pin;
  }

  // Field name: digital_output_cmd
  {
    cdr << ros_message->digital_output_cmd;
  }

  // Field name: pose
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, geometry_msgs, msg, Twist
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->pose, cdr))
    {
      return false;
    }
  }

  // Field name: joints
  {
    size_t size = 6;
    auto array_ptr = ros_message->joints;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: circ_s
  {
    size_t size = ros_message->circ_s.size;
    auto array_ptr = ros_message->circ_s.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: circ_end
  {
    size_t size = ros_message->circ_end.size;
    auto array_ptr = ros_message->circ_end.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: jog_joint
  {
    cdr << ros_message->jog_joint;
  }

  // Field name: jog_dir
  {
    cdr << ros_message->jog_dir;
  }

  return true;
}

static bool _RobotCommand_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RobotCommand_Request__ros_msg_type * ros_message = static_cast<_RobotCommand_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: do_timer
  {
    cdr >> ros_message->do_timer;
  }

  // Field name: holding
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->holding = tmp ? true : false;
  }

  // Field name: cmd_mode
  {
    cdr >> ros_message->cmd_mode;
  }

  // Field name: cmd_type
  {
    cdr >> ros_message->cmd_type;
  }

  // Field name: velocity
  {
    cdr >> ros_message->velocity;
  }

  // Field name: acceleration
  {
    cdr >> ros_message->acceleration;
  }

  // Field name: tool
  {
    cdr >> ros_message->tool;
  }

  // Field name: base
  {
    cdr >> ros_message->base;
  }

  // Field name: base_num
  {
    cdr >> ros_message->base_num;
  }

  // Field name: tool_num
  {
    cdr >> ros_message->tool_num;
  }

  // Field name: digital_input_pin
  {
    cdr >> ros_message->digital_input_pin;
  }

  // Field name: digital_output_pin
  {
    cdr >> ros_message->digital_output_pin;
  }

  // Field name: digital_output_cmd
  {
    cdr >> ros_message->digital_output_cmd;
  }

  // Field name: pose
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, geometry_msgs, msg, Twist
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->pose))
    {
      return false;
    }
  }

  // Field name: joints
  {
    size_t size = 6;
    auto array_ptr = ros_message->joints;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: circ_s
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->circ_s.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->circ_s);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->circ_s, size)) {
      fprintf(stderr, "failed to create array for field 'circ_s'");
      return false;
    }
    auto array_ptr = ros_message->circ_s.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: circ_end
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->circ_end.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->circ_end);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->circ_end, size)) {
      fprintf(stderr, "failed to create array for field 'circ_end'");
      return false;
    }
    auto array_ptr = ros_message->circ_end.data;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: jog_joint
  {
    cdr >> ros_message->jog_joint;
  }

  // Field name: jog_dir
  {
    cdr >> ros_message->jog_dir;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t get_serialized_size_hiwin_interfaces__srv__RobotCommand_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RobotCommand_Request__ros_msg_type * ros_message = static_cast<const _RobotCommand_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name do_timer
  {
    size_t item_size = sizeof(ros_message->do_timer);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name holding
  {
    size_t item_size = sizeof(ros_message->holding);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cmd_mode
  {
    size_t item_size = sizeof(ros_message->cmd_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cmd_type
  {
    size_t item_size = sizeof(ros_message->cmd_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity
  {
    size_t item_size = sizeof(ros_message->velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name acceleration
  {
    size_t item_size = sizeof(ros_message->acceleration);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tool
  {
    size_t item_size = sizeof(ros_message->tool);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name base
  {
    size_t item_size = sizeof(ros_message->base);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name base_num
  {
    size_t item_size = sizeof(ros_message->base_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tool_num
  {
    size_t item_size = sizeof(ros_message->tool_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name digital_input_pin
  {
    size_t item_size = sizeof(ros_message->digital_input_pin);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name digital_output_pin
  {
    size_t item_size = sizeof(ros_message->digital_output_pin);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name digital_output_cmd
  {
    size_t item_size = sizeof(ros_message->digital_output_cmd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pose

  current_alignment += get_serialized_size_geometry_msgs__msg__Twist(
    &(ros_message->pose), current_alignment);
  // field.name joints
  {
    size_t array_size = 6;
    auto array_ptr = ros_message->joints;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name circ_s
  {
    size_t array_size = ros_message->circ_s.size;
    auto array_ptr = ros_message->circ_s.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name circ_end
  {
    size_t array_size = ros_message->circ_end.size;
    auto array_ptr = ros_message->circ_end.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name jog_joint
  {
    size_t item_size = sizeof(ros_message->jog_joint);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name jog_dir
  {
    size_t item_size = sizeof(ros_message->jog_dir);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _RobotCommand_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_hiwin_interfaces__srv__RobotCommand_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t max_serialized_size_hiwin_interfaces__srv__RobotCommand_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: do_timer
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: holding
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: cmd_mode
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: cmd_type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: acceleration
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: tool
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: base
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: base_num
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: tool_num
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: digital_input_pin
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: digital_output_pin
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: digital_output_cmd
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: pose
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size;
      inner_size =
        max_serialized_size_geometry_msgs__msg__Twist(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }
  // member: joints
  {
    size_t array_size = 6;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: circ_s
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: circ_end
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: jog_joint
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: jog_dir
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = hiwin_interfaces__srv__RobotCommand_Request;
    is_plain =
      (
      offsetof(DataType, jog_dir) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RobotCommand_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_hiwin_interfaces__srv__RobotCommand_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RobotCommand_Request = {
  "hiwin_interfaces::srv",
  "RobotCommand_Request",
  _RobotCommand_Request__cdr_serialize,
  _RobotCommand_Request__cdr_deserialize,
  _RobotCommand_Request__get_serialized_size,
  _RobotCommand_Request__max_serialized_size
};

static rosidl_message_type_support_t _RobotCommand_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RobotCommand_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, RobotCommand_Request)() {
  return &_RobotCommand_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "hiwin_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__struct.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"  // current_position
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"  // current_position

// forward declare type support functions


using _RobotCommand_Response__ros_msg_type = hiwin_interfaces__srv__RobotCommand_Response;

static bool _RobotCommand_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RobotCommand_Response__ros_msg_type * ros_message = static_cast<const _RobotCommand_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: arm_state
  {
    cdr << ros_message->arm_state;
  }

  // Field name: digital_state
  {
    cdr << ros_message->digital_state;
  }

  // Field name: current_position
  {
    size_t size = ros_message->current_position.size;
    auto array_ptr = ros_message->current_position.data;
    cdr << static_cast<uint32_t>(size);
    cdr.serializeArray(array_ptr, size);
  }

  return true;
}

static bool _RobotCommand_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RobotCommand_Response__ros_msg_type * ros_message = static_cast<_RobotCommand_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: arm_state
  {
    cdr >> ros_message->arm_state;
  }

  // Field name: digital_state
  {
    cdr >> ros_message->digital_state;
  }

  // Field name: current_position
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->current_position.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->current_position);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->current_position, size)) {
      fprintf(stderr, "failed to create array for field 'current_position'");
      return false;
    }
    auto array_ptr = ros_message->current_position.data;
    cdr.deserializeArray(array_ptr, size);
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t get_serialized_size_hiwin_interfaces__srv__RobotCommand_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RobotCommand_Response__ros_msg_type * ros_message = static_cast<const _RobotCommand_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name arm_state
  {
    size_t item_size = sizeof(ros_message->arm_state);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name digital_state
  {
    size_t item_size = sizeof(ros_message->digital_state);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name current_position
  {
    size_t array_size = ros_message->current_position.size;
    auto array_ptr = ros_message->current_position.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _RobotCommand_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_hiwin_interfaces__srv__RobotCommand_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t max_serialized_size_hiwin_interfaces__srv__RobotCommand_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: arm_state
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: digital_state
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: current_position
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = hiwin_interfaces__srv__RobotCommand_Response;
    is_plain =
      (
      offsetof(DataType, current_position) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RobotCommand_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_hiwin_interfaces__srv__RobotCommand_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RobotCommand_Response = {
  "hiwin_interfaces::srv",
  "RobotCommand_Response",
  _RobotCommand_Response__cdr_serialize,
  _RobotCommand_Response__cdr_deserialize,
  _RobotCommand_Response__get_serialized_size,
  _RobotCommand_Response__max_serialized_size
};

static rosidl_message_type_support_t _RobotCommand_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RobotCommand_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, RobotCommand_Response)() {
  return &_RobotCommand_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "hiwin_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "hiwin_interfaces/srv/robot_command.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t RobotCommand__callbacks = {
  "hiwin_interfaces::srv",
  "RobotCommand",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, RobotCommand_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, RobotCommand_Response)(),
};

static rosidl_service_type_support_t RobotCommand__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &RobotCommand__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, RobotCommand)() {
  return &RobotCommand__handle;
}

#if defined(__cplusplus)
}
#endif

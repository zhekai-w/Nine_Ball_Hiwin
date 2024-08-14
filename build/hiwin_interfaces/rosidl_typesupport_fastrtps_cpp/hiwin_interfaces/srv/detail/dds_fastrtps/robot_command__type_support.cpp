// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice
#include "hiwin_interfaces/srv/detail/robot_command__rosidl_typesupport_fastrtps_cpp.hpp"
#include "hiwin_interfaces/srv/detail/robot_command__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace geometry_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const geometry_msgs::msg::Twist &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  geometry_msgs::msg::Twist &);
size_t get_serialized_size(
  const geometry_msgs::msg::Twist &,
  size_t current_alignment);
size_t
max_serialized_size_Twist(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace geometry_msgs


namespace hiwin_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_serialize(
  const hiwin_interfaces::srv::RobotCommand_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: do_timer
  cdr << ros_message.do_timer;
  // Member: holding
  cdr << (ros_message.holding ? true : false);
  // Member: cmd_mode
  cdr << ros_message.cmd_mode;
  // Member: cmd_type
  cdr << ros_message.cmd_type;
  // Member: velocity
  cdr << ros_message.velocity;
  // Member: acceleration
  cdr << ros_message.acceleration;
  // Member: tool
  cdr << ros_message.tool;
  // Member: base
  cdr << ros_message.base;
  // Member: base_num
  cdr << ros_message.base_num;
  // Member: tool_num
  cdr << ros_message.tool_num;
  // Member: digital_input_pin
  cdr << ros_message.digital_input_pin;
  // Member: digital_output_pin
  cdr << ros_message.digital_output_pin;
  // Member: digital_output_cmd
  cdr << ros_message.digital_output_cmd;
  // Member: pose
  geometry_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.pose,
    cdr);
  // Member: joints
  {
    cdr << ros_message.joints;
  }
  // Member: circ_s
  {
    cdr << ros_message.circ_s;
  }
  // Member: circ_end
  {
    cdr << ros_message.circ_end;
  }
  // Member: jog_joint
  cdr << ros_message.jog_joint;
  // Member: jog_dir
  cdr << ros_message.jog_dir;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  hiwin_interfaces::srv::RobotCommand_Request & ros_message)
{
  // Member: do_timer
  cdr >> ros_message.do_timer;

  // Member: holding
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.holding = tmp ? true : false;
  }

  // Member: cmd_mode
  cdr >> ros_message.cmd_mode;

  // Member: cmd_type
  cdr >> ros_message.cmd_type;

  // Member: velocity
  cdr >> ros_message.velocity;

  // Member: acceleration
  cdr >> ros_message.acceleration;

  // Member: tool
  cdr >> ros_message.tool;

  // Member: base
  cdr >> ros_message.base;

  // Member: base_num
  cdr >> ros_message.base_num;

  // Member: tool_num
  cdr >> ros_message.tool_num;

  // Member: digital_input_pin
  cdr >> ros_message.digital_input_pin;

  // Member: digital_output_pin
  cdr >> ros_message.digital_output_pin;

  // Member: digital_output_cmd
  cdr >> ros_message.digital_output_cmd;

  // Member: pose
  geometry_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.pose);

  // Member: joints
  {
    cdr >> ros_message.joints;
  }

  // Member: circ_s
  {
    cdr >> ros_message.circ_s;
  }

  // Member: circ_end
  {
    cdr >> ros_message.circ_end;
  }

  // Member: jog_joint
  cdr >> ros_message.jog_joint;

  // Member: jog_dir
  cdr >> ros_message.jog_dir;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
get_serialized_size(
  const hiwin_interfaces::srv::RobotCommand_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: do_timer
  {
    size_t item_size = sizeof(ros_message.do_timer);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: holding
  {
    size_t item_size = sizeof(ros_message.holding);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: cmd_mode
  {
    size_t item_size = sizeof(ros_message.cmd_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: cmd_type
  {
    size_t item_size = sizeof(ros_message.cmd_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity
  {
    size_t item_size = sizeof(ros_message.velocity);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: acceleration
  {
    size_t item_size = sizeof(ros_message.acceleration);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: tool
  {
    size_t item_size = sizeof(ros_message.tool);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: base
  {
    size_t item_size = sizeof(ros_message.base);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: base_num
  {
    size_t item_size = sizeof(ros_message.base_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: tool_num
  {
    size_t item_size = sizeof(ros_message.tool_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: digital_input_pin
  {
    size_t item_size = sizeof(ros_message.digital_input_pin);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: digital_output_pin
  {
    size_t item_size = sizeof(ros_message.digital_output_pin);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: digital_output_cmd
  {
    size_t item_size = sizeof(ros_message.digital_output_cmd);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: pose

  current_alignment +=
    geometry_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.pose, current_alignment);
  // Member: joints
  {
    size_t array_size = 6;
    size_t item_size = sizeof(ros_message.joints[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: circ_s
  {
    size_t array_size = ros_message.circ_s.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.circ_s[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: circ_end
  {
    size_t array_size = ros_message.circ_end.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.circ_end[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: jog_joint
  {
    size_t item_size = sizeof(ros_message.jog_joint);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: jog_dir
  {
    size_t item_size = sizeof(ros_message.jog_dir);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
max_serialized_size_RobotCommand_Request(
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


  // Member: do_timer
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: holding
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: cmd_mode
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: cmd_type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: velocity
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: acceleration
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: tool
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: base
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: base_num
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: tool_num
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: digital_input_pin
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: digital_output_pin
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: digital_output_cmd
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: pose
  {
    size_t array_size = 1;


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        geometry_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_Twist(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  // Member: joints
  {
    size_t array_size = 6;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: circ_s
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

  // Member: circ_end
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

  // Member: jog_joint
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: jog_dir
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
    using DataType = hiwin_interfaces::srv::RobotCommand_Request;
    is_plain =
      (
      offsetof(DataType, jog_dir) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _RobotCommand_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::RobotCommand_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _RobotCommand_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<hiwin_interfaces::srv::RobotCommand_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _RobotCommand_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::RobotCommand_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _RobotCommand_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_RobotCommand_Request(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _RobotCommand_Request__callbacks = {
  "hiwin_interfaces::srv",
  "RobotCommand_Request",
  _RobotCommand_Request__cdr_serialize,
  _RobotCommand_Request__cdr_deserialize,
  _RobotCommand_Request__get_serialized_size,
  _RobotCommand_Request__max_serialized_size
};

static rosidl_message_type_support_t _RobotCommand_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_RobotCommand_Request__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace hiwin_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_hiwin_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<hiwin_interfaces::srv::RobotCommand_Request>()
{
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_RobotCommand_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, RobotCommand_Request)() {
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_RobotCommand_Request__handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include <limits>
// already included above
// #include <stdexcept>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
// already included above
// #include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace hiwin_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_serialize(
  const hiwin_interfaces::srv::RobotCommand_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: arm_state
  cdr << ros_message.arm_state;
  // Member: digital_state
  cdr << ros_message.digital_state;
  // Member: current_position
  {
    cdr << ros_message.current_position;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  hiwin_interfaces::srv::RobotCommand_Response & ros_message)
{
  // Member: arm_state
  cdr >> ros_message.arm_state;

  // Member: digital_state
  cdr >> ros_message.digital_state;

  // Member: current_position
  {
    cdr >> ros_message.current_position;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
get_serialized_size(
  const hiwin_interfaces::srv::RobotCommand_Response & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: arm_state
  {
    size_t item_size = sizeof(ros_message.arm_state);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: digital_state
  {
    size_t item_size = sizeof(ros_message.digital_state);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: current_position
  {
    size_t array_size = ros_message.current_position.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.current_position[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
max_serialized_size_RobotCommand_Response(
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


  // Member: arm_state
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: digital_state
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: current_position
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
    using DataType = hiwin_interfaces::srv::RobotCommand_Response;
    is_plain =
      (
      offsetof(DataType, current_position) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _RobotCommand_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::RobotCommand_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _RobotCommand_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<hiwin_interfaces::srv::RobotCommand_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _RobotCommand_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::RobotCommand_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _RobotCommand_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_RobotCommand_Response(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _RobotCommand_Response__callbacks = {
  "hiwin_interfaces::srv",
  "RobotCommand_Response",
  _RobotCommand_Response__cdr_serialize,
  _RobotCommand_Response__cdr_deserialize,
  _RobotCommand_Response__get_serialized_size,
  _RobotCommand_Response__max_serialized_size
};

static rosidl_message_type_support_t _RobotCommand_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_RobotCommand_Response__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace hiwin_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_hiwin_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<hiwin_interfaces::srv::RobotCommand_Response>()
{
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_RobotCommand_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, RobotCommand_Response)() {
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_RobotCommand_Response__handle;
}

#ifdef __cplusplus
}
#endif

#include "rmw/error_handling.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support_decl.hpp"

namespace hiwin_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

static service_type_support_callbacks_t _RobotCommand__callbacks = {
  "hiwin_interfaces::srv",
  "RobotCommand",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, RobotCommand_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, RobotCommand_Response)(),
};

static rosidl_service_type_support_t _RobotCommand__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_RobotCommand__callbacks,
  get_service_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace hiwin_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_hiwin_interfaces
const rosidl_service_type_support_t *
get_service_type_support_handle<hiwin_interfaces::srv::RobotCommand>()
{
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_RobotCommand__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, RobotCommand)() {
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_RobotCommand__handle;
}

#ifdef __cplusplus
}
#endif

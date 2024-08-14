// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__TRAITS_HPP_
#define HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "hiwin_interfaces/srv/detail/robot_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/twist__traits.hpp"

namespace hiwin_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const RobotCommand_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: do_timer
  {
    out << "do_timer: ";
    rosidl_generator_traits::value_to_yaml(msg.do_timer, out);
    out << ", ";
  }

  // member: holding
  {
    out << "holding: ";
    rosidl_generator_traits::value_to_yaml(msg.holding, out);
    out << ", ";
  }

  // member: cmd_mode
  {
    out << "cmd_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_mode, out);
    out << ", ";
  }

  // member: cmd_type
  {
    out << "cmd_type: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_type, out);
    out << ", ";
  }

  // member: velocity
  {
    out << "velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity, out);
    out << ", ";
  }

  // member: acceleration
  {
    out << "acceleration: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration, out);
    out << ", ";
  }

  // member: tool
  {
    out << "tool: ";
    rosidl_generator_traits::value_to_yaml(msg.tool, out);
    out << ", ";
  }

  // member: base
  {
    out << "base: ";
    rosidl_generator_traits::value_to_yaml(msg.base, out);
    out << ", ";
  }

  // member: base_num
  {
    out << "base_num: ";
    rosidl_generator_traits::value_to_yaml(msg.base_num, out);
    out << ", ";
  }

  // member: tool_num
  {
    out << "tool_num: ";
    rosidl_generator_traits::value_to_yaml(msg.tool_num, out);
    out << ", ";
  }

  // member: digital_input_pin
  {
    out << "digital_input_pin: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_input_pin, out);
    out << ", ";
  }

  // member: digital_output_pin
  {
    out << "digital_output_pin: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_output_pin, out);
    out << ", ";
  }

  // member: digital_output_cmd
  {
    out << "digital_output_cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_output_cmd, out);
    out << ", ";
  }

  // member: pose
  {
    out << "pose: ";
    to_flow_style_yaml(msg.pose, out);
    out << ", ";
  }

  // member: joints
  {
    if (msg.joints.size() == 0) {
      out << "joints: []";
    } else {
      out << "joints: [";
      size_t pending_items = msg.joints.size();
      for (auto item : msg.joints) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: circ_s
  {
    if (msg.circ_s.size() == 0) {
      out << "circ_s: []";
    } else {
      out << "circ_s: [";
      size_t pending_items = msg.circ_s.size();
      for (auto item : msg.circ_s) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: circ_end
  {
    if (msg.circ_end.size() == 0) {
      out << "circ_end: []";
    } else {
      out << "circ_end: [";
      size_t pending_items = msg.circ_end.size();
      for (auto item : msg.circ_end) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: jog_joint
  {
    out << "jog_joint: ";
    rosidl_generator_traits::value_to_yaml(msg.jog_joint, out);
    out << ", ";
  }

  // member: jog_dir
  {
    out << "jog_dir: ";
    rosidl_generator_traits::value_to_yaml(msg.jog_dir, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: do_timer
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "do_timer: ";
    rosidl_generator_traits::value_to_yaml(msg.do_timer, out);
    out << "\n";
  }

  // member: holding
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "holding: ";
    rosidl_generator_traits::value_to_yaml(msg.holding, out);
    out << "\n";
  }

  // member: cmd_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_mode, out);
    out << "\n";
  }

  // member: cmd_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_type: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_type, out);
    out << "\n";
  }

  // member: velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity: ";
    rosidl_generator_traits::value_to_yaml(msg.velocity, out);
    out << "\n";
  }

  // member: acceleration
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acceleration: ";
    rosidl_generator_traits::value_to_yaml(msg.acceleration, out);
    out << "\n";
  }

  // member: tool
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tool: ";
    rosidl_generator_traits::value_to_yaml(msg.tool, out);
    out << "\n";
  }

  // member: base
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "base: ";
    rosidl_generator_traits::value_to_yaml(msg.base, out);
    out << "\n";
  }

  // member: base_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "base_num: ";
    rosidl_generator_traits::value_to_yaml(msg.base_num, out);
    out << "\n";
  }

  // member: tool_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tool_num: ";
    rosidl_generator_traits::value_to_yaml(msg.tool_num, out);
    out << "\n";
  }

  // member: digital_input_pin
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "digital_input_pin: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_input_pin, out);
    out << "\n";
  }

  // member: digital_output_pin
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "digital_output_pin: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_output_pin, out);
    out << "\n";
  }

  // member: digital_output_cmd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "digital_output_cmd: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_output_cmd, out);
    out << "\n";
  }

  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose:\n";
    to_block_style_yaml(msg.pose, out, indentation + 2);
  }

  // member: joints
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.joints.size() == 0) {
      out << "joints: []\n";
    } else {
      out << "joints:\n";
      for (auto item : msg.joints) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: circ_s
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.circ_s.size() == 0) {
      out << "circ_s: []\n";
    } else {
      out << "circ_s:\n";
      for (auto item : msg.circ_s) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: circ_end
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.circ_end.size() == 0) {
      out << "circ_end: []\n";
    } else {
      out << "circ_end:\n";
      for (auto item : msg.circ_end) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: jog_joint
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "jog_joint: ";
    rosidl_generator_traits::value_to_yaml(msg.jog_joint, out);
    out << "\n";
  }

  // member: jog_dir
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "jog_dir: ";
    rosidl_generator_traits::value_to_yaml(msg.jog_dir, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotCommand_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace hiwin_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use hiwin_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const hiwin_interfaces::srv::RobotCommand_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  hiwin_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use hiwin_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const hiwin_interfaces::srv::RobotCommand_Request & msg)
{
  return hiwin_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<hiwin_interfaces::srv::RobotCommand_Request>()
{
  return "hiwin_interfaces::srv::RobotCommand_Request";
}

template<>
inline const char * name<hiwin_interfaces::srv::RobotCommand_Request>()
{
  return "hiwin_interfaces/srv/RobotCommand_Request";
}

template<>
struct has_fixed_size<hiwin_interfaces::srv::RobotCommand_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<hiwin_interfaces::srv::RobotCommand_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<hiwin_interfaces::srv::RobotCommand_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace hiwin_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const RobotCommand_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: arm_state
  {
    out << "arm_state: ";
    rosidl_generator_traits::value_to_yaml(msg.arm_state, out);
    out << ", ";
  }

  // member: digital_state
  {
    out << "digital_state: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_state, out);
    out << ", ";
  }

  // member: current_position
  {
    if (msg.current_position.size() == 0) {
      out << "current_position: []";
    } else {
      out << "current_position: [";
      size_t pending_items = msg.current_position.size();
      for (auto item : msg.current_position) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: arm_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "arm_state: ";
    rosidl_generator_traits::value_to_yaml(msg.arm_state, out);
    out << "\n";
  }

  // member: digital_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "digital_state: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_state, out);
    out << "\n";
  }

  // member: current_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.current_position.size() == 0) {
      out << "current_position: []\n";
    } else {
      out << "current_position:\n";
      for (auto item : msg.current_position) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotCommand_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace hiwin_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use hiwin_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const hiwin_interfaces::srv::RobotCommand_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  hiwin_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use hiwin_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const hiwin_interfaces::srv::RobotCommand_Response & msg)
{
  return hiwin_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<hiwin_interfaces::srv::RobotCommand_Response>()
{
  return "hiwin_interfaces::srv::RobotCommand_Response";
}

template<>
inline const char * name<hiwin_interfaces::srv::RobotCommand_Response>()
{
  return "hiwin_interfaces/srv/RobotCommand_Response";
}

template<>
struct has_fixed_size<hiwin_interfaces::srv::RobotCommand_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<hiwin_interfaces::srv::RobotCommand_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<hiwin_interfaces::srv::RobotCommand_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<hiwin_interfaces::srv::RobotCommand>()
{
  return "hiwin_interfaces::srv::RobotCommand";
}

template<>
inline const char * name<hiwin_interfaces::srv::RobotCommand>()
{
  return "hiwin_interfaces/srv/RobotCommand";
}

template<>
struct has_fixed_size<hiwin_interfaces::srv::RobotCommand>
  : std::integral_constant<
    bool,
    has_fixed_size<hiwin_interfaces::srv::RobotCommand_Request>::value &&
    has_fixed_size<hiwin_interfaces::srv::RobotCommand_Response>::value
  >
{
};

template<>
struct has_bounded_size<hiwin_interfaces::srv::RobotCommand>
  : std::integral_constant<
    bool,
    has_bounded_size<hiwin_interfaces::srv::RobotCommand_Request>::value &&
    has_bounded_size<hiwin_interfaces::srv::RobotCommand_Response>::value
  >
{
};

template<>
struct is_service<hiwin_interfaces::srv::RobotCommand>
  : std::true_type
{
};

template<>
struct is_service_request<hiwin_interfaces::srv::RobotCommand_Request>
  : std::true_type
{
};

template<>
struct is_service_response<hiwin_interfaces::srv::RobotCommand_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__TRAITS_HPP_

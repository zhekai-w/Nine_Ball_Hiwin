// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__TRAITS_HPP_
#define HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace hiwin_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Hiwinmodbus_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: mode
  {
    out << "mode: ";
    rosidl_generator_traits::value_to_yaml(msg.mode, out);
    out << ", ";
  }

  // member: holding
  {
    out << "holding: ";
    rosidl_generator_traits::value_to_yaml(msg.holding, out);
    out << ", ";
  }

  // member: type
  {
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
    out << ", ";
  }

  // member: vel
  {
    out << "vel: ";
    rosidl_generator_traits::value_to_yaml(msg.vel, out);
    out << ", ";
  }

  // member: acc
  {
    out << "acc: ";
    rosidl_generator_traits::value_to_yaml(msg.acc, out);
    out << ", ";
  }

  // member: digital_output
  {
    out << "digital_output: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_output, out);
    out << ", ";
  }

  // member: onoff
  {
    out << "onoff: ";
    rosidl_generator_traits::value_to_yaml(msg.onoff, out);
    out << ", ";
  }

  // member: pose
  {
    if (msg.pose.size() == 0) {
      out << "pose: []";
    } else {
      out << "pose: [";
      size_t pending_items = msg.pose.size();
      for (auto item : msg.pose) {
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

  // member: joint
  {
    out << "joint: ";
    rosidl_generator_traits::value_to_yaml(msg.joint, out);
    out << ", ";
  }

  // member: dir
  {
    out << "dir: ";
    rosidl_generator_traits::value_to_yaml(msg.dir, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Hiwinmodbus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "mode: ";
    rosidl_generator_traits::value_to_yaml(msg.mode, out);
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

  // member: type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
    out << "\n";
  }

  // member: vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "vel: ";
    rosidl_generator_traits::value_to_yaml(msg.vel, out);
    out << "\n";
  }

  // member: acc
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "acc: ";
    rosidl_generator_traits::value_to_yaml(msg.acc, out);
    out << "\n";
  }

  // member: digital_output
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "digital_output: ";
    rosidl_generator_traits::value_to_yaml(msg.digital_output, out);
    out << "\n";
  }

  // member: onoff
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "onoff: ";
    rosidl_generator_traits::value_to_yaml(msg.onoff, out);
    out << "\n";
  }

  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pose.size() == 0) {
      out << "pose: []\n";
    } else {
      out << "pose:\n";
      for (auto item : msg.pose) {
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

  // member: joint
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "joint: ";
    rosidl_generator_traits::value_to_yaml(msg.joint, out);
    out << "\n";
  }

  // member: dir
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dir: ";
    rosidl_generator_traits::value_to_yaml(msg.dir, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Hiwinmodbus_Request & msg, bool use_flow_style = false)
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
  const hiwin_interfaces::srv::Hiwinmodbus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  hiwin_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use hiwin_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
{
  return hiwin_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<hiwin_interfaces::srv::Hiwinmodbus_Request>()
{
  return "hiwin_interfaces::srv::Hiwinmodbus_Request";
}

template<>
inline const char * name<hiwin_interfaces::srv::Hiwinmodbus_Request>()
{
  return "hiwin_interfaces/srv/Hiwinmodbus_Request";
}

template<>
struct has_fixed_size<hiwin_interfaces::srv::Hiwinmodbus_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<hiwin_interfaces::srv::Hiwinmodbus_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<hiwin_interfaces::srv::Hiwinmodbus_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace hiwin_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Hiwinmodbus_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: arm_state
  {
    out << "arm_state: ";
    rosidl_generator_traits::value_to_yaml(msg.arm_state, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Hiwinmodbus_Response & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Hiwinmodbus_Response & msg, bool use_flow_style = false)
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
  const hiwin_interfaces::srv::Hiwinmodbus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  hiwin_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use hiwin_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const hiwin_interfaces::srv::Hiwinmodbus_Response & msg)
{
  return hiwin_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<hiwin_interfaces::srv::Hiwinmodbus_Response>()
{
  return "hiwin_interfaces::srv::Hiwinmodbus_Response";
}

template<>
inline const char * name<hiwin_interfaces::srv::Hiwinmodbus_Response>()
{
  return "hiwin_interfaces/srv/Hiwinmodbus_Response";
}

template<>
struct has_fixed_size<hiwin_interfaces::srv::Hiwinmodbus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<hiwin_interfaces::srv::Hiwinmodbus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<hiwin_interfaces::srv::Hiwinmodbus_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<hiwin_interfaces::srv::Hiwinmodbus>()
{
  return "hiwin_interfaces::srv::Hiwinmodbus";
}

template<>
inline const char * name<hiwin_interfaces::srv::Hiwinmodbus>()
{
  return "hiwin_interfaces/srv/Hiwinmodbus";
}

template<>
struct has_fixed_size<hiwin_interfaces::srv::Hiwinmodbus>
  : std::integral_constant<
    bool,
    has_fixed_size<hiwin_interfaces::srv::Hiwinmodbus_Request>::value &&
    has_fixed_size<hiwin_interfaces::srv::Hiwinmodbus_Response>::value
  >
{
};

template<>
struct has_bounded_size<hiwin_interfaces::srv::Hiwinmodbus>
  : std::integral_constant<
    bool,
    has_bounded_size<hiwin_interfaces::srv::Hiwinmodbus_Request>::value &&
    has_bounded_size<hiwin_interfaces::srv::Hiwinmodbus_Response>::value
  >
{
};

template<>
struct is_service<hiwin_interfaces::srv::Hiwinmodbus>
  : std::true_type
{
};

template<>
struct is_service_request<hiwin_interfaces::srv::Hiwinmodbus_Request>
  : std::true_type
{
};

template<>
struct is_service_response<hiwin_interfaces::srv::Hiwinmodbus_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__TRAITS_HPP_

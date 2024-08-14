// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__TRAITS_HPP_
#define DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "detect_interface/msg/detail/detection_results__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'bounding_boxes'
#include "detect_interface/msg/detail/bounding_box__traits.hpp"

namespace detect_interface
{

namespace msg
{

inline void to_flow_style_yaml(
  const DetectionResults & msg,
  std::ostream & out)
{
  out << "{";
  // member: labels
  {
    if (msg.labels.size() == 0) {
      out << "labels: []";
    } else {
      out << "labels: [";
      size_t pending_items = msg.labels.size();
      for (auto item : msg.labels) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: scores
  {
    if (msg.scores.size() == 0) {
      out << "scores: []";
    } else {
      out << "scores: [";
      size_t pending_items = msg.scores.size();
      for (auto item : msg.scores) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: bounding_boxes
  {
    if (msg.bounding_boxes.size() == 0) {
      out << "bounding_boxes: []";
    } else {
      out << "bounding_boxes: [";
      size_t pending_items = msg.bounding_boxes.size();
      for (auto item : msg.bounding_boxes) {
        to_flow_style_yaml(item, out);
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
  const DetectionResults & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: labels
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.labels.size() == 0) {
      out << "labels: []\n";
    } else {
      out << "labels:\n";
      for (auto item : msg.labels) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: scores
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.scores.size() == 0) {
      out << "scores: []\n";
    } else {
      out << "scores:\n";
      for (auto item : msg.scores) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: bounding_boxes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.bounding_boxes.size() == 0) {
      out << "bounding_boxes: []\n";
    } else {
      out << "bounding_boxes:\n";
      for (auto item : msg.bounding_boxes) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DetectionResults & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace detect_interface

namespace rosidl_generator_traits
{

[[deprecated("use detect_interface::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const detect_interface::msg::DetectionResults & msg,
  std::ostream & out, size_t indentation = 0)
{
  detect_interface::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use detect_interface::msg::to_yaml() instead")]]
inline std::string to_yaml(const detect_interface::msg::DetectionResults & msg)
{
  return detect_interface::msg::to_yaml(msg);
}

template<>
inline const char * data_type<detect_interface::msg::DetectionResults>()
{
  return "detect_interface::msg::DetectionResults";
}

template<>
inline const char * name<detect_interface::msg::DetectionResults>()
{
  return "detect_interface/msg/DetectionResults";
}

template<>
struct has_fixed_size<detect_interface::msg::DetectionResults>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<detect_interface::msg::DetectionResults>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<detect_interface::msg::DetectionResults>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__TRAITS_HPP_

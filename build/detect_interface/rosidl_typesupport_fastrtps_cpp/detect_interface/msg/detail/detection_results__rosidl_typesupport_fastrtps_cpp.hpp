// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "detect_interface/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "detect_interface/msg/detail/detection_results__struct.hpp"

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

#include "fastcdr/Cdr.h"

namespace detect_interface
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
cdr_serialize(
  const detect_interface::msg::DetectionResults & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  detect_interface::msg::DetectionResults & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
get_serialized_size(
  const detect_interface::msg::DetectionResults & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
max_serialized_size_DetectionResults(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace detect_interface

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, detect_interface, msg, DetectionResults)();

#ifdef __cplusplus
}
#endif

#endif  // DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

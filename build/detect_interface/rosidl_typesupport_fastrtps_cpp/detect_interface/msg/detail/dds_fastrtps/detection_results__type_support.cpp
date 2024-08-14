// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice
#include "detect_interface/msg/detail/detection_results__rosidl_typesupport_fastrtps_cpp.hpp"
#include "detect_interface/msg/detail/detection_results__struct.hpp"

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
namespace detect_interface
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const detect_interface::msg::BoundingBox &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  detect_interface::msg::BoundingBox &);
size_t get_serialized_size(
  const detect_interface::msg::BoundingBox &,
  size_t current_alignment);
size_t
max_serialized_size_BoundingBox(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace detect_interface


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
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: labels
  {
    cdr << ros_message.labels;
  }
  // Member: scores
  {
    cdr << ros_message.scores;
  }
  // Member: bounding_boxes
  {
    size_t size = ros_message.bounding_boxes.size();
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; i++) {
      detect_interface::msg::typesupport_fastrtps_cpp::cdr_serialize(
        ros_message.bounding_boxes[i],
        cdr);
    }
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  detect_interface::msg::DetectionResults & ros_message)
{
  // Member: labels
  {
    cdr >> ros_message.labels;
  }

  // Member: scores
  {
    cdr >> ros_message.scores;
  }

  // Member: bounding_boxes
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    ros_message.bounding_boxes.resize(size);
    for (size_t i = 0; i < size; i++) {
      detect_interface::msg::typesupport_fastrtps_cpp::cdr_deserialize(
        cdr, ros_message.bounding_boxes[i]);
    }
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
get_serialized_size(
  const detect_interface::msg::DetectionResults & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: labels
  {
    size_t array_size = ros_message.labels.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (ros_message.labels[index].size() + 1);
    }
  }
  // Member: scores
  {
    size_t array_size = ros_message.scores.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.scores[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bounding_boxes
  {
    size_t array_size = ros_message.bounding_boxes.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        detect_interface::msg::typesupport_fastrtps_cpp::get_serialized_size(
        ros_message.bounding_boxes[index], current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_detect_interface
max_serialized_size_DetectionResults(
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


  // Member: labels
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: scores
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: bounding_boxes
  {
    size_t array_size = 0;
    full_bounded = false;
    is_plain = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);


    last_member_size = 0;
    for (size_t index = 0; index < array_size; ++index) {
      bool inner_full_bounded;
      bool inner_is_plain;
      size_t inner_size =
        detect_interface::msg::typesupport_fastrtps_cpp::max_serialized_size_BoundingBox(
        inner_full_bounded, inner_is_plain, current_alignment);
      last_member_size += inner_size;
      current_alignment += inner_size;
      full_bounded &= inner_full_bounded;
      is_plain &= inner_is_plain;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = detect_interface::msg::DetectionResults;
    is_plain =
      (
      offsetof(DataType, bounding_boxes) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _DetectionResults__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const detect_interface::msg::DetectionResults *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _DetectionResults__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<detect_interface::msg::DetectionResults *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _DetectionResults__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const detect_interface::msg::DetectionResults *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _DetectionResults__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_DetectionResults(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _DetectionResults__callbacks = {
  "detect_interface::msg",
  "DetectionResults",
  _DetectionResults__cdr_serialize,
  _DetectionResults__cdr_deserialize,
  _DetectionResults__get_serialized_size,
  _DetectionResults__max_serialized_size
};

static rosidl_message_type_support_t _DetectionResults__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_DetectionResults__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace detect_interface

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_detect_interface
const rosidl_message_type_support_t *
get_message_type_support_handle<detect_interface::msg::DetectionResults>()
{
  return &detect_interface::msg::typesupport_fastrtps_cpp::_DetectionResults__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, detect_interface, msg, DetectionResults)() {
  return &detect_interface::msg::typesupport_fastrtps_cpp::_DetectionResults__handle;
}

#ifdef __cplusplus
}
#endif

// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice
#include "hiwin_interfaces/srv/detail/hiwinmodbus__rosidl_typesupport_fastrtps_cpp.hpp"
#include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.hpp"

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

namespace hiwin_interfaces
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_serialize(
  const hiwin_interfaces::srv::Hiwinmodbus_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: mode
  cdr << ros_message.mode;
  // Member: holding
  cdr << (ros_message.holding ? true : false);
  // Member: type
  cdr << ros_message.type;
  // Member: vel
  cdr << ros_message.vel;
  // Member: acc
  cdr << ros_message.acc;
  // Member: digital_output
  cdr << ros_message.digital_output;
  // Member: onoff
  cdr << ros_message.onoff;
  // Member: pose
  {
    cdr << ros_message.pose;
  }
  // Member: circ_s
  {
    cdr << ros_message.circ_s;
  }
  // Member: circ_end
  {
    cdr << ros_message.circ_end;
  }
  // Member: joint
  cdr << ros_message.joint;
  // Member: dir
  cdr << ros_message.dir;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  hiwin_interfaces::srv::Hiwinmodbus_Request & ros_message)
{
  // Member: mode
  cdr >> ros_message.mode;

  // Member: holding
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.holding = tmp ? true : false;
  }

  // Member: type
  cdr >> ros_message.type;

  // Member: vel
  cdr >> ros_message.vel;

  // Member: acc
  cdr >> ros_message.acc;

  // Member: digital_output
  cdr >> ros_message.digital_output;

  // Member: onoff
  cdr >> ros_message.onoff;

  // Member: pose
  {
    cdr >> ros_message.pose;
  }

  // Member: circ_s
  {
    cdr >> ros_message.circ_s;
  }

  // Member: circ_end
  {
    cdr >> ros_message.circ_end;
  }

  // Member: joint
  cdr >> ros_message.joint;

  // Member: dir
  cdr >> ros_message.dir;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
get_serialized_size(
  const hiwin_interfaces::srv::Hiwinmodbus_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: mode
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.mode.size() + 1);
  // Member: holding
  {
    size_t item_size = sizeof(ros_message.holding);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: type
  {
    size_t item_size = sizeof(ros_message.type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: vel
  {
    size_t item_size = sizeof(ros_message.vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: acc
  {
    size_t item_size = sizeof(ros_message.acc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: digital_output
  {
    size_t item_size = sizeof(ros_message.digital_output);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: onoff
  {
    size_t item_size = sizeof(ros_message.onoff);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: pose
  {
    size_t array_size = ros_message.pose.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    size_t item_size = sizeof(ros_message.pose[0]);
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
  // Member: joint
  {
    size_t item_size = sizeof(ros_message.joint);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: dir
  {
    size_t item_size = sizeof(ros_message.dir);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
max_serialized_size_Hiwinmodbus_Request(
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


  // Member: mode
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: holding
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: acc
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: digital_output
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: onoff
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: pose
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

  // Member: joint
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: dir
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = hiwin_interfaces::srv::Hiwinmodbus_Request;
    is_plain =
      (
      offsetof(DataType, dir) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _Hiwinmodbus_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::Hiwinmodbus_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Hiwinmodbus_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<hiwin_interfaces::srv::Hiwinmodbus_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Hiwinmodbus_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::Hiwinmodbus_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Hiwinmodbus_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Hiwinmodbus_Request(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Hiwinmodbus_Request__callbacks = {
  "hiwin_interfaces::srv",
  "Hiwinmodbus_Request",
  _Hiwinmodbus_Request__cdr_serialize,
  _Hiwinmodbus_Request__cdr_deserialize,
  _Hiwinmodbus_Request__get_serialized_size,
  _Hiwinmodbus_Request__max_serialized_size
};

static rosidl_message_type_support_t _Hiwinmodbus_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Hiwinmodbus_Request__callbacks,
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
get_message_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus_Request>()
{
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_Hiwinmodbus_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, Hiwinmodbus_Request)() {
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_Hiwinmodbus_Request__handle;
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
  const hiwin_interfaces::srv::Hiwinmodbus_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: arm_state
  cdr << ros_message.arm_state;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  hiwin_interfaces::srv::Hiwinmodbus_Response & ros_message)
{
  // Member: arm_state
  cdr >> ros_message.arm_state;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
get_serialized_size(
  const hiwin_interfaces::srv::Hiwinmodbus_Response & ros_message,
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

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hiwin_interfaces
max_serialized_size_Hiwinmodbus_Response(
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

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = hiwin_interfaces::srv::Hiwinmodbus_Response;
    is_plain =
      (
      offsetof(DataType, arm_state) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _Hiwinmodbus_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::Hiwinmodbus_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Hiwinmodbus_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<hiwin_interfaces::srv::Hiwinmodbus_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Hiwinmodbus_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const hiwin_interfaces::srv::Hiwinmodbus_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Hiwinmodbus_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Hiwinmodbus_Response(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Hiwinmodbus_Response__callbacks = {
  "hiwin_interfaces::srv",
  "Hiwinmodbus_Response",
  _Hiwinmodbus_Response__cdr_serialize,
  _Hiwinmodbus_Response__cdr_deserialize,
  _Hiwinmodbus_Response__get_serialized_size,
  _Hiwinmodbus_Response__max_serialized_size
};

static rosidl_message_type_support_t _Hiwinmodbus_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Hiwinmodbus_Response__callbacks,
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
get_message_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus_Response>()
{
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_Hiwinmodbus_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, Hiwinmodbus_Response)() {
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_Hiwinmodbus_Response__handle;
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

static service_type_support_callbacks_t _Hiwinmodbus__callbacks = {
  "hiwin_interfaces::srv",
  "Hiwinmodbus",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, Hiwinmodbus_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, Hiwinmodbus_Response)(),
};

static rosidl_service_type_support_t _Hiwinmodbus__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Hiwinmodbus__callbacks,
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
get_service_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus>()
{
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_Hiwinmodbus__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hiwin_interfaces, srv, Hiwinmodbus)() {
  return &hiwin_interfaces::srv::typesupport_fastrtps_cpp::_Hiwinmodbus__handle;
}

#ifdef __cplusplus
}
#endif

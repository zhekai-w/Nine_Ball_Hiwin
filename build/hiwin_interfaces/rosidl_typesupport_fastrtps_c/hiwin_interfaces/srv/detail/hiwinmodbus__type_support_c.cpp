// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice
#include "hiwin_interfaces/srv/detail/hiwinmodbus__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "hiwin_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.h"
#include "hiwin_interfaces/srv/detail/hiwinmodbus__functions.h"
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

#include "rosidl_runtime_c/primitives_sequence.h"  // circ_end, circ_s, pose
#include "rosidl_runtime_c/primitives_sequence_functions.h"  // circ_end, circ_s, pose
#include "rosidl_runtime_c/string.h"  // mode
#include "rosidl_runtime_c/string_functions.h"  // mode

// forward declare type support functions


using _Hiwinmodbus_Request__ros_msg_type = hiwin_interfaces__srv__Hiwinmodbus_Request;

static bool _Hiwinmodbus_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Hiwinmodbus_Request__ros_msg_type * ros_message = static_cast<const _Hiwinmodbus_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: mode
  {
    const rosidl_runtime_c__String * str = &ros_message->mode;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  // Field name: holding
  {
    cdr << (ros_message->holding ? true : false);
  }

  // Field name: type
  {
    cdr << ros_message->type;
  }

  // Field name: vel
  {
    cdr << ros_message->vel;
  }

  // Field name: acc
  {
    cdr << ros_message->acc;
  }

  // Field name: digital_output
  {
    cdr << ros_message->digital_output;
  }

  // Field name: onoff
  {
    cdr << ros_message->onoff;
  }

  // Field name: pose
  {
    size_t size = ros_message->pose.size;
    auto array_ptr = ros_message->pose.data;
    cdr << static_cast<uint32_t>(size);
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

  // Field name: joint
  {
    cdr << ros_message->joint;
  }

  // Field name: dir
  {
    cdr << ros_message->dir;
  }

  return true;
}

static bool _Hiwinmodbus_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Hiwinmodbus_Request__ros_msg_type * ros_message = static_cast<_Hiwinmodbus_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: mode
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->mode.data) {
      rosidl_runtime_c__String__init(&ros_message->mode);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->mode,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'mode'\n");
      return false;
    }
  }

  // Field name: holding
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->holding = tmp ? true : false;
  }

  // Field name: type
  {
    cdr >> ros_message->type;
  }

  // Field name: vel
  {
    cdr >> ros_message->vel;
  }

  // Field name: acc
  {
    cdr >> ros_message->acc;
  }

  // Field name: digital_output
  {
    cdr >> ros_message->digital_output;
  }

  // Field name: onoff
  {
    cdr >> ros_message->onoff;
  }

  // Field name: pose
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->pose.data) {
      rosidl_runtime_c__double__Sequence__fini(&ros_message->pose);
    }
    if (!rosidl_runtime_c__double__Sequence__init(&ros_message->pose, size)) {
      fprintf(stderr, "failed to create array for field 'pose'");
      return false;
    }
    auto array_ptr = ros_message->pose.data;
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

  // Field name: joint
  {
    cdr >> ros_message->joint;
  }

  // Field name: dir
  {
    cdr >> ros_message->dir;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t get_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Hiwinmodbus_Request__ros_msg_type * ros_message = static_cast<const _Hiwinmodbus_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name mode
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->mode.size + 1);
  // field.name holding
  {
    size_t item_size = sizeof(ros_message->holding);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name type
  {
    size_t item_size = sizeof(ros_message->type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vel
  {
    size_t item_size = sizeof(ros_message->vel);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name acc
  {
    size_t item_size = sizeof(ros_message->acc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name digital_output
  {
    size_t item_size = sizeof(ros_message->digital_output);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name onoff
  {
    size_t item_size = sizeof(ros_message->onoff);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pose
  {
    size_t array_size = ros_message->pose.size;
    auto array_ptr = ros_message->pose.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
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
  // field.name joint
  {
    size_t item_size = sizeof(ros_message->joint);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dir
  {
    size_t item_size = sizeof(ros_message->dir);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Hiwinmodbus_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t max_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Request(
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

  // member: mode
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
  // member: holding
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: type
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vel
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: acc
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: digital_output
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: onoff
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: pose
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
  // member: joint
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: dir
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
    using DataType = hiwin_interfaces__srv__Hiwinmodbus_Request;
    is_plain =
      (
      offsetof(DataType, dir) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Hiwinmodbus_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Hiwinmodbus_Request = {
  "hiwin_interfaces::srv",
  "Hiwinmodbus_Request",
  _Hiwinmodbus_Request__cdr_serialize,
  _Hiwinmodbus_Request__cdr_deserialize,
  _Hiwinmodbus_Request__get_serialized_size,
  _Hiwinmodbus_Request__max_serialized_size
};

static rosidl_message_type_support_t _Hiwinmodbus_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Hiwinmodbus_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, Hiwinmodbus_Request)() {
  return &_Hiwinmodbus_Request__type_support;
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
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.h"
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__functions.h"
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


// forward declare type support functions


using _Hiwinmodbus_Response__ros_msg_type = hiwin_interfaces__srv__Hiwinmodbus_Response;

static bool _Hiwinmodbus_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Hiwinmodbus_Response__ros_msg_type * ros_message = static_cast<const _Hiwinmodbus_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: arm_state
  {
    cdr << ros_message->arm_state;
  }

  return true;
}

static bool _Hiwinmodbus_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Hiwinmodbus_Response__ros_msg_type * ros_message = static_cast<_Hiwinmodbus_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: arm_state
  {
    cdr >> ros_message->arm_state;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t get_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Hiwinmodbus_Response__ros_msg_type * ros_message = static_cast<const _Hiwinmodbus_Response__ros_msg_type *>(untyped_ros_message);
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

  return current_alignment - initial_alignment;
}

static uint32_t _Hiwinmodbus_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hiwin_interfaces
size_t max_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Response(
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

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = hiwin_interfaces__srv__Hiwinmodbus_Response;
    is_plain =
      (
      offsetof(DataType, arm_state) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _Hiwinmodbus_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_hiwin_interfaces__srv__Hiwinmodbus_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Hiwinmodbus_Response = {
  "hiwin_interfaces::srv",
  "Hiwinmodbus_Response",
  _Hiwinmodbus_Response__cdr_serialize,
  _Hiwinmodbus_Response__cdr_deserialize,
  _Hiwinmodbus_Response__get_serialized_size,
  _Hiwinmodbus_Response__max_serialized_size
};

static rosidl_message_type_support_t _Hiwinmodbus_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Hiwinmodbus_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, Hiwinmodbus_Response)() {
  return &_Hiwinmodbus_Response__type_support;
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
#include "hiwin_interfaces/srv/hiwinmodbus.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t Hiwinmodbus__callbacks = {
  "hiwin_interfaces::srv",
  "Hiwinmodbus",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, Hiwinmodbus_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, Hiwinmodbus_Response)(),
};

static rosidl_service_type_support_t Hiwinmodbus__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &Hiwinmodbus__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hiwin_interfaces, srv, Hiwinmodbus)() {
  return &Hiwinmodbus__handle;
}

#if defined(__cplusplus)
}
#endif

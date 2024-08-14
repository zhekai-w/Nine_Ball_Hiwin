// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace hiwin_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void Hiwinmodbus_Request_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) hiwin_interfaces::srv::Hiwinmodbus_Request(_init);
}

void Hiwinmodbus_Request_fini_function(void * message_memory)
{
  auto typed_message = static_cast<hiwin_interfaces::srv::Hiwinmodbus_Request *>(message_memory);
  typed_message->~Hiwinmodbus_Request();
}

size_t size_function__Hiwinmodbus_Request__pose(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Hiwinmodbus_Request__pose(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__Hiwinmodbus_Request__pose(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__Hiwinmodbus_Request__pose(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__Hiwinmodbus_Request__pose(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__Hiwinmodbus_Request__pose(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__Hiwinmodbus_Request__pose(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__Hiwinmodbus_Request__pose(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Hiwinmodbus_Request__circ_s(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Hiwinmodbus_Request__circ_s(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__Hiwinmodbus_Request__circ_s(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__Hiwinmodbus_Request__circ_s(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__Hiwinmodbus_Request__circ_s(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__Hiwinmodbus_Request__circ_s(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__Hiwinmodbus_Request__circ_s(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__Hiwinmodbus_Request__circ_s(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Hiwinmodbus_Request__circ_end(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<double> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Hiwinmodbus_Request__circ_end(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<double> *>(untyped_member);
  return &member[index];
}

void * get_function__Hiwinmodbus_Request__circ_end(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<double> *>(untyped_member);
  return &member[index];
}

void fetch_function__Hiwinmodbus_Request__circ_end(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const double *>(
    get_const_function__Hiwinmodbus_Request__circ_end(untyped_member, index));
  auto & value = *reinterpret_cast<double *>(untyped_value);
  value = item;
}

void assign_function__Hiwinmodbus_Request__circ_end(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<double *>(
    get_function__Hiwinmodbus_Request__circ_end(untyped_member, index));
  const auto & value = *reinterpret_cast<const double *>(untyped_value);
  item = value;
}

void resize_function__Hiwinmodbus_Request__circ_end(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<double> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Hiwinmodbus_Request_message_member_array[12] = {
  {
    "mode",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, mode),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "holding",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, holding),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "type",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, type),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "vel",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, vel),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "acc",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, acc),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "digital_output",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, digital_output),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "onoff",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, onoff),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "pose",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, pose),  // bytes offset in struct
    nullptr,  // default value
    size_function__Hiwinmodbus_Request__pose,  // size() function pointer
    get_const_function__Hiwinmodbus_Request__pose,  // get_const(index) function pointer
    get_function__Hiwinmodbus_Request__pose,  // get(index) function pointer
    fetch_function__Hiwinmodbus_Request__pose,  // fetch(index, &value) function pointer
    assign_function__Hiwinmodbus_Request__pose,  // assign(index, value) function pointer
    resize_function__Hiwinmodbus_Request__pose  // resize(index) function pointer
  },
  {
    "circ_s",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, circ_s),  // bytes offset in struct
    nullptr,  // default value
    size_function__Hiwinmodbus_Request__circ_s,  // size() function pointer
    get_const_function__Hiwinmodbus_Request__circ_s,  // get_const(index) function pointer
    get_function__Hiwinmodbus_Request__circ_s,  // get(index) function pointer
    fetch_function__Hiwinmodbus_Request__circ_s,  // fetch(index, &value) function pointer
    assign_function__Hiwinmodbus_Request__circ_s,  // assign(index, value) function pointer
    resize_function__Hiwinmodbus_Request__circ_s  // resize(index) function pointer
  },
  {
    "circ_end",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, circ_end),  // bytes offset in struct
    nullptr,  // default value
    size_function__Hiwinmodbus_Request__circ_end,  // size() function pointer
    get_const_function__Hiwinmodbus_Request__circ_end,  // get_const(index) function pointer
    get_function__Hiwinmodbus_Request__circ_end,  // get(index) function pointer
    fetch_function__Hiwinmodbus_Request__circ_end,  // fetch(index, &value) function pointer
    assign_function__Hiwinmodbus_Request__circ_end,  // assign(index, value) function pointer
    resize_function__Hiwinmodbus_Request__circ_end  // resize(index) function pointer
  },
  {
    "joint",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, joint),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "dir",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Request, dir),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Hiwinmodbus_Request_message_members = {
  "hiwin_interfaces::srv",  // message namespace
  "Hiwinmodbus_Request",  // message name
  12,  // number of fields
  sizeof(hiwin_interfaces::srv::Hiwinmodbus_Request),
  Hiwinmodbus_Request_message_member_array,  // message members
  Hiwinmodbus_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  Hiwinmodbus_Request_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Hiwinmodbus_Request_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Hiwinmodbus_Request_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace hiwin_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus_Request>()
{
  return &::hiwin_interfaces::srv::rosidl_typesupport_introspection_cpp::Hiwinmodbus_Request_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, hiwin_interfaces, srv, Hiwinmodbus_Request)() {
  return &::hiwin_interfaces::srv::rosidl_typesupport_introspection_cpp::Hiwinmodbus_Request_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include "array"
// already included above
// #include "cstddef"
// already included above
// #include "string"
// already included above
// #include "vector"
// already included above
// #include "rosidl_runtime_c/message_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/field_types.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace hiwin_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

void Hiwinmodbus_Response_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) hiwin_interfaces::srv::Hiwinmodbus_Response(_init);
}

void Hiwinmodbus_Response_fini_function(void * message_memory)
{
  auto typed_message = static_cast<hiwin_interfaces::srv::Hiwinmodbus_Response *>(message_memory);
  typed_message->~Hiwinmodbus_Response();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Hiwinmodbus_Response_message_member_array[1] = {
  {
    "arm_state",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hiwin_interfaces::srv::Hiwinmodbus_Response, arm_state),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Hiwinmodbus_Response_message_members = {
  "hiwin_interfaces::srv",  // message namespace
  "Hiwinmodbus_Response",  // message name
  1,  // number of fields
  sizeof(hiwin_interfaces::srv::Hiwinmodbus_Response),
  Hiwinmodbus_Response_message_member_array,  // message members
  Hiwinmodbus_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  Hiwinmodbus_Response_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Hiwinmodbus_Response_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Hiwinmodbus_Response_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace hiwin_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus_Response>()
{
  return &::hiwin_interfaces::srv::rosidl_typesupport_introspection_cpp::Hiwinmodbus_Response_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, hiwin_interfaces, srv, Hiwinmodbus_Response)() {
  return &::hiwin_interfaces::srv::rosidl_typesupport_introspection_cpp::Hiwinmodbus_Response_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_interface/macros.h"
// already included above
// #include "rosidl_typesupport_introspection_cpp/visibility_control.h"
// already included above
// #include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/service_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/service_type_support_decl.hpp"

namespace hiwin_interfaces
{

namespace srv
{

namespace rosidl_typesupport_introspection_cpp
{

// this is intentionally not const to allow initialization later to prevent an initialization race
static ::rosidl_typesupport_introspection_cpp::ServiceMembers Hiwinmodbus_service_members = {
  "hiwin_interfaces::srv",  // service namespace
  "Hiwinmodbus",  // service name
  // these two fields are initialized below on the first access
  // see get_service_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus>()
  nullptr,  // request message
  nullptr  // response message
};

static const rosidl_service_type_support_t Hiwinmodbus_service_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Hiwinmodbus_service_members,
  get_service_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace srv

}  // namespace hiwin_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
get_service_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus>()
{
  // get a handle to the value to be returned
  auto service_type_support =
    &::hiwin_interfaces::srv::rosidl_typesupport_introspection_cpp::Hiwinmodbus_service_type_support_handle;
  // get a non-const and properly typed version of the data void *
  auto service_members = const_cast<::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
    static_cast<const ::rosidl_typesupport_introspection_cpp::ServiceMembers *>(
      service_type_support->data));
  // make sure that both the request_members_ and the response_members_ are initialized
  // if they are not, initialize them
  if (
    service_members->request_members_ == nullptr ||
    service_members->response_members_ == nullptr)
  {
    // initialize the request_members_ with the static function from the external library
    service_members->request_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::hiwin_interfaces::srv::Hiwinmodbus_Request
      >()->data
      );
    // initialize the response_members_ with the static function from the external library
    service_members->response_members_ = static_cast<
      const ::rosidl_typesupport_introspection_cpp::MessageMembers *
      >(
      ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<
        ::hiwin_interfaces::srv::Hiwinmodbus_Response
      >()->data
      );
  }
  // finally return the properly initialized service_type_support handle
  return service_type_support;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, hiwin_interfaces, srv, Hiwinmodbus)() {
  return ::rosidl_typesupport_introspection_cpp::get_service_type_support_handle<hiwin_interfaces::srv::Hiwinmodbus>();
}

#ifdef __cplusplus
}
#endif

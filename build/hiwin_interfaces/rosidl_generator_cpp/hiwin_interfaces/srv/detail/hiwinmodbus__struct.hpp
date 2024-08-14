// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__STRUCT_HPP_
#define HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Request __attribute__((deprecated))
#else
# define DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Request __declspec(deprecated)
#endif

namespace hiwin_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Hiwinmodbus_Request_
{
  using Type = Hiwinmodbus_Request_<ContainerAllocator>;

  explicit Hiwinmodbus_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = "";
      this->holding = false;
      this->type = 0l;
      this->vel = 0l;
      this->acc = 0l;
      this->digital_output = 0l;
      this->onoff = 0l;
      this->joint = 0l;
      this->dir = 0l;
    }
  }

  explicit Hiwinmodbus_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : mode(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = "";
      this->holding = false;
      this->type = 0l;
      this->vel = 0l;
      this->acc = 0l;
      this->digital_output = 0l;
      this->onoff = 0l;
      this->joint = 0l;
      this->dir = 0l;
    }
  }

  // field types and members
  using _mode_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _mode_type mode;
  using _holding_type =
    bool;
  _holding_type holding;
  using _type_type =
    int32_t;
  _type_type type;
  using _vel_type =
    int32_t;
  _vel_type vel;
  using _acc_type =
    int32_t;
  _acc_type acc;
  using _digital_output_type =
    int32_t;
  _digital_output_type digital_output;
  using _onoff_type =
    int32_t;
  _onoff_type onoff;
  using _pose_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _pose_type pose;
  using _circ_s_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _circ_s_type circ_s;
  using _circ_end_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _circ_end_type circ_end;
  using _joint_type =
    int32_t;
  _joint_type joint;
  using _dir_type =
    int32_t;
  _dir_type dir;

  // setters for named parameter idiom
  Type & set__mode(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->mode = _arg;
    return *this;
  }
  Type & set__holding(
    const bool & _arg)
  {
    this->holding = _arg;
    return *this;
  }
  Type & set__type(
    const int32_t & _arg)
  {
    this->type = _arg;
    return *this;
  }
  Type & set__vel(
    const int32_t & _arg)
  {
    this->vel = _arg;
    return *this;
  }
  Type & set__acc(
    const int32_t & _arg)
  {
    this->acc = _arg;
    return *this;
  }
  Type & set__digital_output(
    const int32_t & _arg)
  {
    this->digital_output = _arg;
    return *this;
  }
  Type & set__onoff(
    const int32_t & _arg)
  {
    this->onoff = _arg;
    return *this;
  }
  Type & set__pose(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->pose = _arg;
    return *this;
  }
  Type & set__circ_s(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->circ_s = _arg;
    return *this;
  }
  Type & set__circ_end(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->circ_end = _arg;
    return *this;
  }
  Type & set__joint(
    const int32_t & _arg)
  {
    this->joint = _arg;
    return *this;
  }
  Type & set__dir(
    const int32_t & _arg)
  {
    this->dir = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Request
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Request
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Hiwinmodbus_Request_ & other) const
  {
    if (this->mode != other.mode) {
      return false;
    }
    if (this->holding != other.holding) {
      return false;
    }
    if (this->type != other.type) {
      return false;
    }
    if (this->vel != other.vel) {
      return false;
    }
    if (this->acc != other.acc) {
      return false;
    }
    if (this->digital_output != other.digital_output) {
      return false;
    }
    if (this->onoff != other.onoff) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    if (this->circ_s != other.circ_s) {
      return false;
    }
    if (this->circ_end != other.circ_end) {
      return false;
    }
    if (this->joint != other.joint) {
      return false;
    }
    if (this->dir != other.dir) {
      return false;
    }
    return true;
  }
  bool operator!=(const Hiwinmodbus_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Hiwinmodbus_Request_

// alias to use template instance with default allocator
using Hiwinmodbus_Request =
  hiwin_interfaces::srv::Hiwinmodbus_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace hiwin_interfaces


#ifndef _WIN32
# define DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Response __attribute__((deprecated))
#else
# define DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Response __declspec(deprecated)
#endif

namespace hiwin_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Hiwinmodbus_Response_
{
  using Type = Hiwinmodbus_Response_<ContainerAllocator>;

  explicit Hiwinmodbus_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->arm_state = 0l;
    }
  }

  explicit Hiwinmodbus_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->arm_state = 0l;
    }
  }

  // field types and members
  using _arm_state_type =
    int32_t;
  _arm_state_type arm_state;

  // setters for named parameter idiom
  Type & set__arm_state(
    const int32_t & _arg)
  {
    this->arm_state = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Response
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hiwin_interfaces__srv__Hiwinmodbus_Response
    std::shared_ptr<hiwin_interfaces::srv::Hiwinmodbus_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Hiwinmodbus_Response_ & other) const
  {
    if (this->arm_state != other.arm_state) {
      return false;
    }
    return true;
  }
  bool operator!=(const Hiwinmodbus_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Hiwinmodbus_Response_

// alias to use template instance with default allocator
using Hiwinmodbus_Response =
  hiwin_interfaces::srv::Hiwinmodbus_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace hiwin_interfaces

namespace hiwin_interfaces
{

namespace srv
{

struct Hiwinmodbus
{
  using Request = hiwin_interfaces::srv::Hiwinmodbus_Request;
  using Response = hiwin_interfaces::srv::Hiwinmodbus_Response;
};

}  // namespace srv

}  // namespace hiwin_interfaces

#endif  // HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__STRUCT_HPP_

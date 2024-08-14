// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__STRUCT_HPP_
#define HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/twist__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__hiwin_interfaces__srv__RobotCommand_Request __attribute__((deprecated))
#else
# define DEPRECATED__hiwin_interfaces__srv__RobotCommand_Request __declspec(deprecated)
#endif

namespace hiwin_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct RobotCommand_Request_
{
  using Type = RobotCommand_Request_<ContainerAllocator>;

  explicit RobotCommand_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->do_timer = 0;
      this->holding = false;
      this->cmd_mode = 0;
      this->cmd_type = 0;
      this->velocity = 0;
      this->acceleration = 0;
      this->tool = 0;
      this->base = 0;
      this->base_num = 0;
      this->tool_num = 0;
      this->digital_input_pin = 0;
      this->digital_output_pin = 0;
      this->digital_output_cmd = 0;
      std::fill<typename std::array<double, 6>::iterator, double>(this->joints.begin(), this->joints.end(), 0.0);
      this->jog_joint = 0;
      this->jog_dir = 0;
    }
  }

  explicit RobotCommand_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : pose(_alloc, _init),
    joints(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->do_timer = 0;
      this->holding = false;
      this->cmd_mode = 0;
      this->cmd_type = 0;
      this->velocity = 0;
      this->acceleration = 0;
      this->tool = 0;
      this->base = 0;
      this->base_num = 0;
      this->tool_num = 0;
      this->digital_input_pin = 0;
      this->digital_output_pin = 0;
      this->digital_output_cmd = 0;
      std::fill<typename std::array<double, 6>::iterator, double>(this->joints.begin(), this->joints.end(), 0.0);
      this->jog_joint = 0;
      this->jog_dir = 0;
    }
  }

  // field types and members
  using _do_timer_type =
    uint8_t;
  _do_timer_type do_timer;
  using _holding_type =
    bool;
  _holding_type holding;
  using _cmd_mode_type =
    uint8_t;
  _cmd_mode_type cmd_mode;
  using _cmd_type_type =
    uint8_t;
  _cmd_type_type cmd_type;
  using _velocity_type =
    uint8_t;
  _velocity_type velocity;
  using _acceleration_type =
    uint8_t;
  _acceleration_type acceleration;
  using _tool_type =
    uint8_t;
  _tool_type tool;
  using _base_type =
    uint8_t;
  _base_type base;
  using _base_num_type =
    uint8_t;
  _base_num_type base_num;
  using _tool_num_type =
    uint8_t;
  _tool_num_type tool_num;
  using _digital_input_pin_type =
    uint8_t;
  _digital_input_pin_type digital_input_pin;
  using _digital_output_pin_type =
    uint8_t;
  _digital_output_pin_type digital_output_pin;
  using _digital_output_cmd_type =
    uint8_t;
  _digital_output_cmd_type digital_output_cmd;
  using _pose_type =
    geometry_msgs::msg::Twist_<ContainerAllocator>;
  _pose_type pose;
  using _joints_type =
    std::array<double, 6>;
  _joints_type joints;
  using _circ_s_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _circ_s_type circ_s;
  using _circ_end_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _circ_end_type circ_end;
  using _jog_joint_type =
    int8_t;
  _jog_joint_type jog_joint;
  using _jog_dir_type =
    int8_t;
  _jog_dir_type jog_dir;

  // setters for named parameter idiom
  Type & set__do_timer(
    const uint8_t & _arg)
  {
    this->do_timer = _arg;
    return *this;
  }
  Type & set__holding(
    const bool & _arg)
  {
    this->holding = _arg;
    return *this;
  }
  Type & set__cmd_mode(
    const uint8_t & _arg)
  {
    this->cmd_mode = _arg;
    return *this;
  }
  Type & set__cmd_type(
    const uint8_t & _arg)
  {
    this->cmd_type = _arg;
    return *this;
  }
  Type & set__velocity(
    const uint8_t & _arg)
  {
    this->velocity = _arg;
    return *this;
  }
  Type & set__acceleration(
    const uint8_t & _arg)
  {
    this->acceleration = _arg;
    return *this;
  }
  Type & set__tool(
    const uint8_t & _arg)
  {
    this->tool = _arg;
    return *this;
  }
  Type & set__base(
    const uint8_t & _arg)
  {
    this->base = _arg;
    return *this;
  }
  Type & set__base_num(
    const uint8_t & _arg)
  {
    this->base_num = _arg;
    return *this;
  }
  Type & set__tool_num(
    const uint8_t & _arg)
  {
    this->tool_num = _arg;
    return *this;
  }
  Type & set__digital_input_pin(
    const uint8_t & _arg)
  {
    this->digital_input_pin = _arg;
    return *this;
  }
  Type & set__digital_output_pin(
    const uint8_t & _arg)
  {
    this->digital_output_pin = _arg;
    return *this;
  }
  Type & set__digital_output_cmd(
    const uint8_t & _arg)
  {
    this->digital_output_cmd = _arg;
    return *this;
  }
  Type & set__pose(
    const geometry_msgs::msg::Twist_<ContainerAllocator> & _arg)
  {
    this->pose = _arg;
    return *this;
  }
  Type & set__joints(
    const std::array<double, 6> & _arg)
  {
    this->joints = _arg;
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
  Type & set__jog_joint(
    const int8_t & _arg)
  {
    this->jog_joint = _arg;
    return *this;
  }
  Type & set__jog_dir(
    const int8_t & _arg)
  {
    this->jog_dir = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t EXCITE =
    1u;
  static constexpr uint8_t PTP =
    2u;
  static constexpr uint8_t LINE =
    3u;
  static constexpr uint8_t CIRC =
    4u;
  static constexpr uint8_t DIGITAL_OUTPUT =
    5u;
  static constexpr uint8_t HOME =
    6u;
  static constexpr uint8_t JOG =
    7u;
  static constexpr uint8_t CHECK_JOINT =
    8u;
  static constexpr uint8_t CHECK_POSE =
    9u;
  static constexpr uint8_t CLOSE =
    10u;
  static constexpr uint8_t WAITING =
    11u;
  static constexpr uint8_t READ_DI =
    12u;
  static constexpr uint8_t SET_BASE =
    13u;
  static constexpr uint8_t SET_TOOL =
    14u;
  static constexpr uint8_t MOTION_STOP =
    15u;
  static constexpr uint8_t JOINTS_CMD =
    0u;
  static constexpr uint8_t POSE_CMD =
    1u;
  static constexpr uint8_t DIGITAL_ON =
    1u;
  static constexpr uint8_t DIGITAL_OFF =
    0u;

  // pointer types
  using RawPtr =
    hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hiwin_interfaces__srv__RobotCommand_Request
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hiwin_interfaces__srv__RobotCommand_Request
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotCommand_Request_ & other) const
  {
    if (this->do_timer != other.do_timer) {
      return false;
    }
    if (this->holding != other.holding) {
      return false;
    }
    if (this->cmd_mode != other.cmd_mode) {
      return false;
    }
    if (this->cmd_type != other.cmd_type) {
      return false;
    }
    if (this->velocity != other.velocity) {
      return false;
    }
    if (this->acceleration != other.acceleration) {
      return false;
    }
    if (this->tool != other.tool) {
      return false;
    }
    if (this->base != other.base) {
      return false;
    }
    if (this->base_num != other.base_num) {
      return false;
    }
    if (this->tool_num != other.tool_num) {
      return false;
    }
    if (this->digital_input_pin != other.digital_input_pin) {
      return false;
    }
    if (this->digital_output_pin != other.digital_output_pin) {
      return false;
    }
    if (this->digital_output_cmd != other.digital_output_cmd) {
      return false;
    }
    if (this->pose != other.pose) {
      return false;
    }
    if (this->joints != other.joints) {
      return false;
    }
    if (this->circ_s != other.circ_s) {
      return false;
    }
    if (this->circ_end != other.circ_end) {
      return false;
    }
    if (this->jog_joint != other.jog_joint) {
      return false;
    }
    if (this->jog_dir != other.jog_dir) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotCommand_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotCommand_Request_

// alias to use template instance with default allocator
using RobotCommand_Request =
  hiwin_interfaces::srv::RobotCommand_Request_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::EXCITE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::PTP;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::LINE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::CIRC;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::DIGITAL_OUTPUT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::HOME;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::JOG;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::CHECK_JOINT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::CHECK_POSE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::CLOSE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::WAITING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::READ_DI;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::SET_BASE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::SET_TOOL;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::MOTION_STOP;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::JOINTS_CMD;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::POSE_CMD;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::DIGITAL_ON;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Request_<ContainerAllocator>::DIGITAL_OFF;
#endif  // __cplusplus < 201703L

}  // namespace srv

}  // namespace hiwin_interfaces


#ifndef _WIN32
# define DEPRECATED__hiwin_interfaces__srv__RobotCommand_Response __attribute__((deprecated))
#else
# define DEPRECATED__hiwin_interfaces__srv__RobotCommand_Response __declspec(deprecated)
#endif

namespace hiwin_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct RobotCommand_Response_
{
  using Type = RobotCommand_Response_<ContainerAllocator>;

  explicit RobotCommand_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->arm_state = 0;
      this->digital_state = 0;
    }
  }

  explicit RobotCommand_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->arm_state = 0;
      this->digital_state = 0;
    }
  }

  // field types and members
  using _arm_state_type =
    uint8_t;
  _arm_state_type arm_state;
  using _digital_state_type =
    uint8_t;
  _digital_state_type digital_state;
  using _current_position_type =
    std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>>;
  _current_position_type current_position;

  // setters for named parameter idiom
  Type & set__arm_state(
    const uint8_t & _arg)
  {
    this->arm_state = _arg;
    return *this;
  }
  Type & set__digital_state(
    const uint8_t & _arg)
  {
    this->digital_state = _arg;
    return *this;
  }
  Type & set__current_position(
    const std::vector<double, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<double>> & _arg)
  {
    this->current_position = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t IDLE =
    1u;
  static constexpr uint8_t RUNNING =
    2u;
  static constexpr uint8_t HOLD =
    3u;
  static constexpr uint8_t DELAY =
    4u;

  // pointer types
  using RawPtr =
    hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hiwin_interfaces__srv__RobotCommand_Response
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hiwin_interfaces__srv__RobotCommand_Response
    std::shared_ptr<hiwin_interfaces::srv::RobotCommand_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotCommand_Response_ & other) const
  {
    if (this->arm_state != other.arm_state) {
      return false;
    }
    if (this->digital_state != other.digital_state) {
      return false;
    }
    if (this->current_position != other.current_position) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotCommand_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotCommand_Response_

// alias to use template instance with default allocator
using RobotCommand_Response =
  hiwin_interfaces::srv::RobotCommand_Response_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Response_<ContainerAllocator>::IDLE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Response_<ContainerAllocator>::RUNNING;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Response_<ContainerAllocator>::HOLD;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t RobotCommand_Response_<ContainerAllocator>::DELAY;
#endif  // __cplusplus < 201703L

}  // namespace srv

}  // namespace hiwin_interfaces

namespace hiwin_interfaces
{

namespace srv
{

struct RobotCommand
{
  using Request = hiwin_interfaces::srv::RobotCommand_Request;
  using Response = hiwin_interfaces::srv::RobotCommand_Response;
};

}  // namespace srv

}  // namespace hiwin_interfaces

#endif  // HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__STRUCT_HPP_

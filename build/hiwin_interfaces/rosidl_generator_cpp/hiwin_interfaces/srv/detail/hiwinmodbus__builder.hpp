// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__BUILDER_HPP_
#define HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hiwin_interfaces/srv/detail/hiwinmodbus__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hiwin_interfaces
{

namespace srv
{

namespace builder
{

class Init_Hiwinmodbus_Request_dir
{
public:
  explicit Init_Hiwinmodbus_Request_dir(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  ::hiwin_interfaces::srv::Hiwinmodbus_Request dir(::hiwin_interfaces::srv::Hiwinmodbus_Request::_dir_type arg)
  {
    msg_.dir = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_joint
{
public:
  explicit Init_Hiwinmodbus_Request_joint(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_dir joint(::hiwin_interfaces::srv::Hiwinmodbus_Request::_joint_type arg)
  {
    msg_.joint = std::move(arg);
    return Init_Hiwinmodbus_Request_dir(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_circ_end
{
public:
  explicit Init_Hiwinmodbus_Request_circ_end(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_joint circ_end(::hiwin_interfaces::srv::Hiwinmodbus_Request::_circ_end_type arg)
  {
    msg_.circ_end = std::move(arg);
    return Init_Hiwinmodbus_Request_joint(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_circ_s
{
public:
  explicit Init_Hiwinmodbus_Request_circ_s(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_circ_end circ_s(::hiwin_interfaces::srv::Hiwinmodbus_Request::_circ_s_type arg)
  {
    msg_.circ_s = std::move(arg);
    return Init_Hiwinmodbus_Request_circ_end(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_pose
{
public:
  explicit Init_Hiwinmodbus_Request_pose(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_circ_s pose(::hiwin_interfaces::srv::Hiwinmodbus_Request::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_Hiwinmodbus_Request_circ_s(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_onoff
{
public:
  explicit Init_Hiwinmodbus_Request_onoff(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_pose onoff(::hiwin_interfaces::srv::Hiwinmodbus_Request::_onoff_type arg)
  {
    msg_.onoff = std::move(arg);
    return Init_Hiwinmodbus_Request_pose(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_digital_output
{
public:
  explicit Init_Hiwinmodbus_Request_digital_output(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_onoff digital_output(::hiwin_interfaces::srv::Hiwinmodbus_Request::_digital_output_type arg)
  {
    msg_.digital_output = std::move(arg);
    return Init_Hiwinmodbus_Request_onoff(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_acc
{
public:
  explicit Init_Hiwinmodbus_Request_acc(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_digital_output acc(::hiwin_interfaces::srv::Hiwinmodbus_Request::_acc_type arg)
  {
    msg_.acc = std::move(arg);
    return Init_Hiwinmodbus_Request_digital_output(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_vel
{
public:
  explicit Init_Hiwinmodbus_Request_vel(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_acc vel(::hiwin_interfaces::srv::Hiwinmodbus_Request::_vel_type arg)
  {
    msg_.vel = std::move(arg);
    return Init_Hiwinmodbus_Request_acc(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_type
{
public:
  explicit Init_Hiwinmodbus_Request_type(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_vel type(::hiwin_interfaces::srv::Hiwinmodbus_Request::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_Hiwinmodbus_Request_vel(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_holding
{
public:
  explicit Init_Hiwinmodbus_Request_holding(::hiwin_interfaces::srv::Hiwinmodbus_Request & msg)
  : msg_(msg)
  {}
  Init_Hiwinmodbus_Request_type holding(::hiwin_interfaces::srv::Hiwinmodbus_Request::_holding_type arg)
  {
    msg_.holding = std::move(arg);
    return Init_Hiwinmodbus_Request_type(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

class Init_Hiwinmodbus_Request_mode
{
public:
  Init_Hiwinmodbus_Request_mode()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Hiwinmodbus_Request_holding mode(::hiwin_interfaces::srv::Hiwinmodbus_Request::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_Hiwinmodbus_Request_holding(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::hiwin_interfaces::srv::Hiwinmodbus_Request>()
{
  return hiwin_interfaces::srv::builder::Init_Hiwinmodbus_Request_mode();
}

}  // namespace hiwin_interfaces


namespace hiwin_interfaces
{

namespace srv
{

namespace builder
{

class Init_Hiwinmodbus_Response_arm_state
{
public:
  Init_Hiwinmodbus_Response_arm_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::hiwin_interfaces::srv::Hiwinmodbus_Response arm_state(::hiwin_interfaces::srv::Hiwinmodbus_Response::_arm_state_type arg)
  {
    msg_.arm_state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hiwin_interfaces::srv::Hiwinmodbus_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::hiwin_interfaces::srv::Hiwinmodbus_Response>()
{
  return hiwin_interfaces::srv::builder::Init_Hiwinmodbus_Response_arm_state();
}

}  // namespace hiwin_interfaces

#endif  // HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__BUILDER_HPP_

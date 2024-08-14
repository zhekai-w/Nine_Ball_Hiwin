// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__BUILDER_HPP_
#define HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hiwin_interfaces/srv/detail/robot_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hiwin_interfaces
{

namespace srv
{

namespace builder
{

class Init_RobotCommand_Request_jog_dir
{
public:
  explicit Init_RobotCommand_Request_jog_dir(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  ::hiwin_interfaces::srv::RobotCommand_Request jog_dir(::hiwin_interfaces::srv::RobotCommand_Request::_jog_dir_type arg)
  {
    msg_.jog_dir = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_jog_joint
{
public:
  explicit Init_RobotCommand_Request_jog_joint(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_jog_dir jog_joint(::hiwin_interfaces::srv::RobotCommand_Request::_jog_joint_type arg)
  {
    msg_.jog_joint = std::move(arg);
    return Init_RobotCommand_Request_jog_dir(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_circ_end
{
public:
  explicit Init_RobotCommand_Request_circ_end(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_jog_joint circ_end(::hiwin_interfaces::srv::RobotCommand_Request::_circ_end_type arg)
  {
    msg_.circ_end = std::move(arg);
    return Init_RobotCommand_Request_jog_joint(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_circ_s
{
public:
  explicit Init_RobotCommand_Request_circ_s(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_circ_end circ_s(::hiwin_interfaces::srv::RobotCommand_Request::_circ_s_type arg)
  {
    msg_.circ_s = std::move(arg);
    return Init_RobotCommand_Request_circ_end(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_joints
{
public:
  explicit Init_RobotCommand_Request_joints(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_circ_s joints(::hiwin_interfaces::srv::RobotCommand_Request::_joints_type arg)
  {
    msg_.joints = std::move(arg);
    return Init_RobotCommand_Request_circ_s(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_pose
{
public:
  explicit Init_RobotCommand_Request_pose(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_joints pose(::hiwin_interfaces::srv::RobotCommand_Request::_pose_type arg)
  {
    msg_.pose = std::move(arg);
    return Init_RobotCommand_Request_joints(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_digital_output_cmd
{
public:
  explicit Init_RobotCommand_Request_digital_output_cmd(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_pose digital_output_cmd(::hiwin_interfaces::srv::RobotCommand_Request::_digital_output_cmd_type arg)
  {
    msg_.digital_output_cmd = std::move(arg);
    return Init_RobotCommand_Request_pose(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_digital_output_pin
{
public:
  explicit Init_RobotCommand_Request_digital_output_pin(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_digital_output_cmd digital_output_pin(::hiwin_interfaces::srv::RobotCommand_Request::_digital_output_pin_type arg)
  {
    msg_.digital_output_pin = std::move(arg);
    return Init_RobotCommand_Request_digital_output_cmd(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_digital_input_pin
{
public:
  explicit Init_RobotCommand_Request_digital_input_pin(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_digital_output_pin digital_input_pin(::hiwin_interfaces::srv::RobotCommand_Request::_digital_input_pin_type arg)
  {
    msg_.digital_input_pin = std::move(arg);
    return Init_RobotCommand_Request_digital_output_pin(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_tool_num
{
public:
  explicit Init_RobotCommand_Request_tool_num(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_digital_input_pin tool_num(::hiwin_interfaces::srv::RobotCommand_Request::_tool_num_type arg)
  {
    msg_.tool_num = std::move(arg);
    return Init_RobotCommand_Request_digital_input_pin(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_base_num
{
public:
  explicit Init_RobotCommand_Request_base_num(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_tool_num base_num(::hiwin_interfaces::srv::RobotCommand_Request::_base_num_type arg)
  {
    msg_.base_num = std::move(arg);
    return Init_RobotCommand_Request_tool_num(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_base
{
public:
  explicit Init_RobotCommand_Request_base(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_base_num base(::hiwin_interfaces::srv::RobotCommand_Request::_base_type arg)
  {
    msg_.base = std::move(arg);
    return Init_RobotCommand_Request_base_num(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_tool
{
public:
  explicit Init_RobotCommand_Request_tool(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_base tool(::hiwin_interfaces::srv::RobotCommand_Request::_tool_type arg)
  {
    msg_.tool = std::move(arg);
    return Init_RobotCommand_Request_base(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_acceleration
{
public:
  explicit Init_RobotCommand_Request_acceleration(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_tool acceleration(::hiwin_interfaces::srv::RobotCommand_Request::_acceleration_type arg)
  {
    msg_.acceleration = std::move(arg);
    return Init_RobotCommand_Request_tool(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_velocity
{
public:
  explicit Init_RobotCommand_Request_velocity(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_acceleration velocity(::hiwin_interfaces::srv::RobotCommand_Request::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_RobotCommand_Request_acceleration(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_cmd_type
{
public:
  explicit Init_RobotCommand_Request_cmd_type(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_velocity cmd_type(::hiwin_interfaces::srv::RobotCommand_Request::_cmd_type_type arg)
  {
    msg_.cmd_type = std::move(arg);
    return Init_RobotCommand_Request_velocity(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_cmd_mode
{
public:
  explicit Init_RobotCommand_Request_cmd_mode(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_cmd_type cmd_mode(::hiwin_interfaces::srv::RobotCommand_Request::_cmd_mode_type arg)
  {
    msg_.cmd_mode = std::move(arg);
    return Init_RobotCommand_Request_cmd_type(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_holding
{
public:
  explicit Init_RobotCommand_Request_holding(::hiwin_interfaces::srv::RobotCommand_Request & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Request_cmd_mode holding(::hiwin_interfaces::srv::RobotCommand_Request::_holding_type arg)
  {
    msg_.holding = std::move(arg);
    return Init_RobotCommand_Request_cmd_mode(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

class Init_RobotCommand_Request_do_timer
{
public:
  Init_RobotCommand_Request_do_timer()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotCommand_Request_holding do_timer(::hiwin_interfaces::srv::RobotCommand_Request::_do_timer_type arg)
  {
    msg_.do_timer = std::move(arg);
    return Init_RobotCommand_Request_holding(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::hiwin_interfaces::srv::RobotCommand_Request>()
{
  return hiwin_interfaces::srv::builder::Init_RobotCommand_Request_do_timer();
}

}  // namespace hiwin_interfaces


namespace hiwin_interfaces
{

namespace srv
{

namespace builder
{

class Init_RobotCommand_Response_current_position
{
public:
  explicit Init_RobotCommand_Response_current_position(::hiwin_interfaces::srv::RobotCommand_Response & msg)
  : msg_(msg)
  {}
  ::hiwin_interfaces::srv::RobotCommand_Response current_position(::hiwin_interfaces::srv::RobotCommand_Response::_current_position_type arg)
  {
    msg_.current_position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Response msg_;
};

class Init_RobotCommand_Response_digital_state
{
public:
  explicit Init_RobotCommand_Response_digital_state(::hiwin_interfaces::srv::RobotCommand_Response & msg)
  : msg_(msg)
  {}
  Init_RobotCommand_Response_current_position digital_state(::hiwin_interfaces::srv::RobotCommand_Response::_digital_state_type arg)
  {
    msg_.digital_state = std::move(arg);
    return Init_RobotCommand_Response_current_position(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Response msg_;
};

class Init_RobotCommand_Response_arm_state
{
public:
  Init_RobotCommand_Response_arm_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotCommand_Response_digital_state arm_state(::hiwin_interfaces::srv::RobotCommand_Response::_arm_state_type arg)
  {
    msg_.arm_state = std::move(arg);
    return Init_RobotCommand_Response_digital_state(msg_);
  }

private:
  ::hiwin_interfaces::srv::RobotCommand_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::hiwin_interfaces::srv::RobotCommand_Response>()
{
  return hiwin_interfaces::srv::builder::Init_RobotCommand_Response_arm_state();
}

}  // namespace hiwin_interfaces

#endif  // HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__BUILDER_HPP_

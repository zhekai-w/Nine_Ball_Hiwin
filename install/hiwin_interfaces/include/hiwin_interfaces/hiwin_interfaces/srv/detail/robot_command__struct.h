// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__STRUCT_H_
#define HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'EXCITE'.
/**
  * mode
 */
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__EXCITE = 1
};

/// Constant 'PTP'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__PTP = 2
};

/// Constant 'LINE'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__LINE = 3
};

/// Constant 'CIRC'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__CIRC = 4
};

/// Constant 'DIGITAL_OUTPUT'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__DIGITAL_OUTPUT = 5
};

/// Constant 'HOME'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__HOME = 6
};

/// Constant 'JOG'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__JOG = 7
};

/// Constant 'CHECK_JOINT'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__CHECK_JOINT = 8
};

/// Constant 'CHECK_POSE'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__CHECK_POSE = 9
};

/// Constant 'CLOSE'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__CLOSE = 10
};

/// Constant 'WAITING'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__WAITING = 11
};

/// Constant 'READ_DI'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__READ_DI = 12
};

/// Constant 'SET_BASE'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__SET_BASE = 13
};

/// Constant 'SET_TOOL'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__SET_TOOL = 14
};

/// Constant 'MOTION_STOP'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__MOTION_STOP = 15
};

/// Constant 'JOINTS_CMD'.
/**
  * cmd type
 */
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__JOINTS_CMD = 0
};

/// Constant 'POSE_CMD'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__POSE_CMD = 1
};

/// Constant 'DIGITAL_ON'.
/**
  * digital_output_cmd
 */
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__DIGITAL_ON = 1
};

/// Constant 'DIGITAL_OFF'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Request__DIGITAL_OFF = 0
};

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/twist__struct.h"
// Member 'circ_s'
// Member 'circ_end'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/RobotCommand in the package hiwin_interfaces.
typedef struct hiwin_interfaces__srv__RobotCommand_Request
{
  uint8_t do_timer;
  bool holding;
  uint8_t cmd_mode;
  uint8_t cmd_type;
  uint8_t velocity;
  uint8_t acceleration;
  uint8_t tool;
  uint8_t base;
  uint8_t base_num;
  uint8_t tool_num;
  uint8_t digital_input_pin;
  uint8_t digital_output_pin;
  uint8_t digital_output_cmd;
  /// for POSE_CMD
  geometry_msgs__msg__Twist pose;
  /// for JOINTS_CMD
  double joints[6];
  rosidl_runtime_c__double__Sequence circ_s;
  rosidl_runtime_c__double__Sequence circ_end;
  /// for JOG mode
  int8_t jog_joint;
  int8_t jog_dir;
} hiwin_interfaces__srv__RobotCommand_Request;

// Struct for a sequence of hiwin_interfaces__srv__RobotCommand_Request.
typedef struct hiwin_interfaces__srv__RobotCommand_Request__Sequence
{
  hiwin_interfaces__srv__RobotCommand_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hiwin_interfaces__srv__RobotCommand_Request__Sequence;


// Constants defined in the message

/// Constant 'IDLE'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Response__IDLE = 1
};

/// Constant 'RUNNING'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Response__RUNNING = 2
};

/// Constant 'HOLD'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Response__HOLD = 3
};

/// Constant 'DELAY'.
enum
{
  hiwin_interfaces__srv__RobotCommand_Response__DELAY = 4
};

// Include directives for member types
// Member 'current_position'
// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/RobotCommand in the package hiwin_interfaces.
typedef struct hiwin_interfaces__srv__RobotCommand_Response
{
  uint8_t arm_state;
  uint8_t digital_state;
  rosidl_runtime_c__double__Sequence current_position;
} hiwin_interfaces__srv__RobotCommand_Response;

// Struct for a sequence of hiwin_interfaces__srv__RobotCommand_Response.
typedef struct hiwin_interfaces__srv__RobotCommand_Response__Sequence
{
  hiwin_interfaces__srv__RobotCommand_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hiwin_interfaces__srv__RobotCommand_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__STRUCT_H_

// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__STRUCT_H_
#define HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'mode'
#include "rosidl_runtime_c/string.h"
// Member 'pose'
// Member 'circ_s'
// Member 'circ_end'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/Hiwinmodbus in the package hiwin_interfaces.
typedef struct hiwin_interfaces__srv__Hiwinmodbus_Request
{
  rosidl_runtime_c__String mode;
  bool holding;
  int32_t type;
  int32_t vel;
  int32_t acc;
  int32_t digital_output;
  int32_t onoff;
  /// Digital_output[DO_Num, 0or1]
  rosidl_runtime_c__double__Sequence pose;
  rosidl_runtime_c__double__Sequence circ_s;
  rosidl_runtime_c__double__Sequence circ_end;
  int32_t joint;
  int32_t dir;
} hiwin_interfaces__srv__Hiwinmodbus_Request;

// Struct for a sequence of hiwin_interfaces__srv__Hiwinmodbus_Request.
typedef struct hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence
{
  hiwin_interfaces__srv__Hiwinmodbus_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Hiwinmodbus in the package hiwin_interfaces.
typedef struct hiwin_interfaces__srv__Hiwinmodbus_Response
{
  int32_t arm_state;
} hiwin_interfaces__srv__Hiwinmodbus_Response;

// Struct for a sequence of hiwin_interfaces__srv__Hiwinmodbus_Response.
typedef struct hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence
{
  hiwin_interfaces__srv__Hiwinmodbus_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HIWIN_INTERFACES__SRV__DETAIL__HIWINMODBUS__STRUCT_H_

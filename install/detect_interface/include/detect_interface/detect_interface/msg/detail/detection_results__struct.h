// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__STRUCT_H_
#define DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'labels'
#include "rosidl_runtime_c/string.h"
// Member 'scores'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'bounding_boxes'
#include "detect_interface/msg/detail/bounding_box__struct.h"

/// Struct defined in msg/DetectionResults in the package detect_interface.
/**
  * DetectionResults.msg
 */
typedef struct detect_interface__msg__DetectionResults
{
  /// Array of object labels
  rosidl_runtime_c__String__Sequence labels;
  /// Array of object confidence scores
  rosidl_runtime_c__float__Sequence scores;
  /// Array of bounding boxes
  detect_interface__msg__BoundingBox__Sequence bounding_boxes;
} detect_interface__msg__DetectionResults;

// Struct for a sequence of detect_interface__msg__DetectionResults.
typedef struct detect_interface__msg__DetectionResults__Sequence
{
  detect_interface__msg__DetectionResults * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} detect_interface__msg__DetectionResults__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__STRUCT_H_

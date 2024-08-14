// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__FUNCTIONS_H_
#define DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "detect_interface/msg/rosidl_generator_c__visibility_control.h"

#include "detect_interface/msg/detail/detection_results__struct.h"

/// Initialize msg/DetectionResults message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * detect_interface__msg__DetectionResults
 * )) before or use
 * detect_interface__msg__DetectionResults__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
bool
detect_interface__msg__DetectionResults__init(detect_interface__msg__DetectionResults * msg);

/// Finalize msg/DetectionResults message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
void
detect_interface__msg__DetectionResults__fini(detect_interface__msg__DetectionResults * msg);

/// Create msg/DetectionResults message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * detect_interface__msg__DetectionResults__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
detect_interface__msg__DetectionResults *
detect_interface__msg__DetectionResults__create();

/// Destroy msg/DetectionResults message.
/**
 * It calls
 * detect_interface__msg__DetectionResults__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
void
detect_interface__msg__DetectionResults__destroy(detect_interface__msg__DetectionResults * msg);

/// Check for msg/DetectionResults message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
bool
detect_interface__msg__DetectionResults__are_equal(const detect_interface__msg__DetectionResults * lhs, const detect_interface__msg__DetectionResults * rhs);

/// Copy a msg/DetectionResults message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
bool
detect_interface__msg__DetectionResults__copy(
  const detect_interface__msg__DetectionResults * input,
  detect_interface__msg__DetectionResults * output);

/// Initialize array of msg/DetectionResults messages.
/**
 * It allocates the memory for the number of elements and calls
 * detect_interface__msg__DetectionResults__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
bool
detect_interface__msg__DetectionResults__Sequence__init(detect_interface__msg__DetectionResults__Sequence * array, size_t size);

/// Finalize array of msg/DetectionResults messages.
/**
 * It calls
 * detect_interface__msg__DetectionResults__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
void
detect_interface__msg__DetectionResults__Sequence__fini(detect_interface__msg__DetectionResults__Sequence * array);

/// Create array of msg/DetectionResults messages.
/**
 * It allocates the memory for the array and calls
 * detect_interface__msg__DetectionResults__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
detect_interface__msg__DetectionResults__Sequence *
detect_interface__msg__DetectionResults__Sequence__create(size_t size);

/// Destroy array of msg/DetectionResults messages.
/**
 * It calls
 * detect_interface__msg__DetectionResults__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
void
detect_interface__msg__DetectionResults__Sequence__destroy(detect_interface__msg__DetectionResults__Sequence * array);

/// Check for msg/DetectionResults message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
bool
detect_interface__msg__DetectionResults__Sequence__are_equal(const detect_interface__msg__DetectionResults__Sequence * lhs, const detect_interface__msg__DetectionResults__Sequence * rhs);

/// Copy an array of msg/DetectionResults messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_detect_interface
bool
detect_interface__msg__DetectionResults__Sequence__copy(
  const detect_interface__msg__DetectionResults__Sequence * input,
  detect_interface__msg__DetectionResults__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__FUNCTIONS_H_

// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice

#ifndef HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__FUNCTIONS_H_
#define HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "hiwin_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "hiwin_interfaces/srv/detail/robot_command__struct.h"

/// Initialize srv/RobotCommand message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * hiwin_interfaces__srv__RobotCommand_Request
 * )) before or use
 * hiwin_interfaces__srv__RobotCommand_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Request__init(hiwin_interfaces__srv__RobotCommand_Request * msg);

/// Finalize srv/RobotCommand message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Request__fini(hiwin_interfaces__srv__RobotCommand_Request * msg);

/// Create srv/RobotCommand message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * hiwin_interfaces__srv__RobotCommand_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
hiwin_interfaces__srv__RobotCommand_Request *
hiwin_interfaces__srv__RobotCommand_Request__create();

/// Destroy srv/RobotCommand message.
/**
 * It calls
 * hiwin_interfaces__srv__RobotCommand_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Request__destroy(hiwin_interfaces__srv__RobotCommand_Request * msg);

/// Check for srv/RobotCommand message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Request__are_equal(const hiwin_interfaces__srv__RobotCommand_Request * lhs, const hiwin_interfaces__srv__RobotCommand_Request * rhs);

/// Copy a srv/RobotCommand message.
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
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Request__copy(
  const hiwin_interfaces__srv__RobotCommand_Request * input,
  hiwin_interfaces__srv__RobotCommand_Request * output);

/// Initialize array of srv/RobotCommand messages.
/**
 * It allocates the memory for the number of elements and calls
 * hiwin_interfaces__srv__RobotCommand_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Request__Sequence__init(hiwin_interfaces__srv__RobotCommand_Request__Sequence * array, size_t size);

/// Finalize array of srv/RobotCommand messages.
/**
 * It calls
 * hiwin_interfaces__srv__RobotCommand_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Request__Sequence__fini(hiwin_interfaces__srv__RobotCommand_Request__Sequence * array);

/// Create array of srv/RobotCommand messages.
/**
 * It allocates the memory for the array and calls
 * hiwin_interfaces__srv__RobotCommand_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
hiwin_interfaces__srv__RobotCommand_Request__Sequence *
hiwin_interfaces__srv__RobotCommand_Request__Sequence__create(size_t size);

/// Destroy array of srv/RobotCommand messages.
/**
 * It calls
 * hiwin_interfaces__srv__RobotCommand_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Request__Sequence__destroy(hiwin_interfaces__srv__RobotCommand_Request__Sequence * array);

/// Check for srv/RobotCommand message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Request__Sequence__are_equal(const hiwin_interfaces__srv__RobotCommand_Request__Sequence * lhs, const hiwin_interfaces__srv__RobotCommand_Request__Sequence * rhs);

/// Copy an array of srv/RobotCommand messages.
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
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Request__Sequence__copy(
  const hiwin_interfaces__srv__RobotCommand_Request__Sequence * input,
  hiwin_interfaces__srv__RobotCommand_Request__Sequence * output);

/// Initialize srv/RobotCommand message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * hiwin_interfaces__srv__RobotCommand_Response
 * )) before or use
 * hiwin_interfaces__srv__RobotCommand_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Response__init(hiwin_interfaces__srv__RobotCommand_Response * msg);

/// Finalize srv/RobotCommand message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Response__fini(hiwin_interfaces__srv__RobotCommand_Response * msg);

/// Create srv/RobotCommand message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * hiwin_interfaces__srv__RobotCommand_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
hiwin_interfaces__srv__RobotCommand_Response *
hiwin_interfaces__srv__RobotCommand_Response__create();

/// Destroy srv/RobotCommand message.
/**
 * It calls
 * hiwin_interfaces__srv__RobotCommand_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Response__destroy(hiwin_interfaces__srv__RobotCommand_Response * msg);

/// Check for srv/RobotCommand message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Response__are_equal(const hiwin_interfaces__srv__RobotCommand_Response * lhs, const hiwin_interfaces__srv__RobotCommand_Response * rhs);

/// Copy a srv/RobotCommand message.
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
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Response__copy(
  const hiwin_interfaces__srv__RobotCommand_Response * input,
  hiwin_interfaces__srv__RobotCommand_Response * output);

/// Initialize array of srv/RobotCommand messages.
/**
 * It allocates the memory for the number of elements and calls
 * hiwin_interfaces__srv__RobotCommand_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Response__Sequence__init(hiwin_interfaces__srv__RobotCommand_Response__Sequence * array, size_t size);

/// Finalize array of srv/RobotCommand messages.
/**
 * It calls
 * hiwin_interfaces__srv__RobotCommand_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Response__Sequence__fini(hiwin_interfaces__srv__RobotCommand_Response__Sequence * array);

/// Create array of srv/RobotCommand messages.
/**
 * It allocates the memory for the array and calls
 * hiwin_interfaces__srv__RobotCommand_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
hiwin_interfaces__srv__RobotCommand_Response__Sequence *
hiwin_interfaces__srv__RobotCommand_Response__Sequence__create(size_t size);

/// Destroy array of srv/RobotCommand messages.
/**
 * It calls
 * hiwin_interfaces__srv__RobotCommand_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
void
hiwin_interfaces__srv__RobotCommand_Response__Sequence__destroy(hiwin_interfaces__srv__RobotCommand_Response__Sequence * array);

/// Check for srv/RobotCommand message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Response__Sequence__are_equal(const hiwin_interfaces__srv__RobotCommand_Response__Sequence * lhs, const hiwin_interfaces__srv__RobotCommand_Response__Sequence * rhs);

/// Copy an array of srv/RobotCommand messages.
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
ROSIDL_GENERATOR_C_PUBLIC_hiwin_interfaces
bool
hiwin_interfaces__srv__RobotCommand_Response__Sequence__copy(
  const hiwin_interfaces__srv__RobotCommand_Response__Sequence * input,
  hiwin_interfaces__srv__RobotCommand_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // HIWIN_INTERFACES__SRV__DETAIL__ROBOT_COMMAND__FUNCTIONS_H_

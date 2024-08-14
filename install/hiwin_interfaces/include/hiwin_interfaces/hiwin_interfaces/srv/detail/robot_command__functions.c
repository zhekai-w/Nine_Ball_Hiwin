// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice
#include "hiwin_interfaces/srv/detail/robot_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `pose`
#include "geometry_msgs/msg/detail/twist__functions.h"
// Member `circ_s`
// Member `circ_end`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
hiwin_interfaces__srv__RobotCommand_Request__init(hiwin_interfaces__srv__RobotCommand_Request * msg)
{
  if (!msg) {
    return false;
  }
  // do_timer
  // holding
  // cmd_mode
  // cmd_type
  // velocity
  // acceleration
  // tool
  // base
  // base_num
  // tool_num
  // digital_input_pin
  // digital_output_pin
  // digital_output_cmd
  // pose
  if (!geometry_msgs__msg__Twist__init(&msg->pose)) {
    hiwin_interfaces__srv__RobotCommand_Request__fini(msg);
    return false;
  }
  // joints
  // circ_s
  if (!rosidl_runtime_c__double__Sequence__init(&msg->circ_s, 0)) {
    hiwin_interfaces__srv__RobotCommand_Request__fini(msg);
    return false;
  }
  // circ_end
  if (!rosidl_runtime_c__double__Sequence__init(&msg->circ_end, 0)) {
    hiwin_interfaces__srv__RobotCommand_Request__fini(msg);
    return false;
  }
  // jog_joint
  // jog_dir
  return true;
}

void
hiwin_interfaces__srv__RobotCommand_Request__fini(hiwin_interfaces__srv__RobotCommand_Request * msg)
{
  if (!msg) {
    return;
  }
  // do_timer
  // holding
  // cmd_mode
  // cmd_type
  // velocity
  // acceleration
  // tool
  // base
  // base_num
  // tool_num
  // digital_input_pin
  // digital_output_pin
  // digital_output_cmd
  // pose
  geometry_msgs__msg__Twist__fini(&msg->pose);
  // joints
  // circ_s
  rosidl_runtime_c__double__Sequence__fini(&msg->circ_s);
  // circ_end
  rosidl_runtime_c__double__Sequence__fini(&msg->circ_end);
  // jog_joint
  // jog_dir
}

bool
hiwin_interfaces__srv__RobotCommand_Request__are_equal(const hiwin_interfaces__srv__RobotCommand_Request * lhs, const hiwin_interfaces__srv__RobotCommand_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // do_timer
  if (lhs->do_timer != rhs->do_timer) {
    return false;
  }
  // holding
  if (lhs->holding != rhs->holding) {
    return false;
  }
  // cmd_mode
  if (lhs->cmd_mode != rhs->cmd_mode) {
    return false;
  }
  // cmd_type
  if (lhs->cmd_type != rhs->cmd_type) {
    return false;
  }
  // velocity
  if (lhs->velocity != rhs->velocity) {
    return false;
  }
  // acceleration
  if (lhs->acceleration != rhs->acceleration) {
    return false;
  }
  // tool
  if (lhs->tool != rhs->tool) {
    return false;
  }
  // base
  if (lhs->base != rhs->base) {
    return false;
  }
  // base_num
  if (lhs->base_num != rhs->base_num) {
    return false;
  }
  // tool_num
  if (lhs->tool_num != rhs->tool_num) {
    return false;
  }
  // digital_input_pin
  if (lhs->digital_input_pin != rhs->digital_input_pin) {
    return false;
  }
  // digital_output_pin
  if (lhs->digital_output_pin != rhs->digital_output_pin) {
    return false;
  }
  // digital_output_cmd
  if (lhs->digital_output_cmd != rhs->digital_output_cmd) {
    return false;
  }
  // pose
  if (!geometry_msgs__msg__Twist__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
  }
  // joints
  for (size_t i = 0; i < 6; ++i) {
    if (lhs->joints[i] != rhs->joints[i]) {
      return false;
    }
  }
  // circ_s
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->circ_s), &(rhs->circ_s)))
  {
    return false;
  }
  // circ_end
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->circ_end), &(rhs->circ_end)))
  {
    return false;
  }
  // jog_joint
  if (lhs->jog_joint != rhs->jog_joint) {
    return false;
  }
  // jog_dir
  if (lhs->jog_dir != rhs->jog_dir) {
    return false;
  }
  return true;
}

bool
hiwin_interfaces__srv__RobotCommand_Request__copy(
  const hiwin_interfaces__srv__RobotCommand_Request * input,
  hiwin_interfaces__srv__RobotCommand_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // do_timer
  output->do_timer = input->do_timer;
  // holding
  output->holding = input->holding;
  // cmd_mode
  output->cmd_mode = input->cmd_mode;
  // cmd_type
  output->cmd_type = input->cmd_type;
  // velocity
  output->velocity = input->velocity;
  // acceleration
  output->acceleration = input->acceleration;
  // tool
  output->tool = input->tool;
  // base
  output->base = input->base;
  // base_num
  output->base_num = input->base_num;
  // tool_num
  output->tool_num = input->tool_num;
  // digital_input_pin
  output->digital_input_pin = input->digital_input_pin;
  // digital_output_pin
  output->digital_output_pin = input->digital_output_pin;
  // digital_output_cmd
  output->digital_output_cmd = input->digital_output_cmd;
  // pose
  if (!geometry_msgs__msg__Twist__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
  }
  // joints
  for (size_t i = 0; i < 6; ++i) {
    output->joints[i] = input->joints[i];
  }
  // circ_s
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->circ_s), &(output->circ_s)))
  {
    return false;
  }
  // circ_end
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->circ_end), &(output->circ_end)))
  {
    return false;
  }
  // jog_joint
  output->jog_joint = input->jog_joint;
  // jog_dir
  output->jog_dir = input->jog_dir;
  return true;
}

hiwin_interfaces__srv__RobotCommand_Request *
hiwin_interfaces__srv__RobotCommand_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__RobotCommand_Request * msg = (hiwin_interfaces__srv__RobotCommand_Request *)allocator.allocate(sizeof(hiwin_interfaces__srv__RobotCommand_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(hiwin_interfaces__srv__RobotCommand_Request));
  bool success = hiwin_interfaces__srv__RobotCommand_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
hiwin_interfaces__srv__RobotCommand_Request__destroy(hiwin_interfaces__srv__RobotCommand_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    hiwin_interfaces__srv__RobotCommand_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
hiwin_interfaces__srv__RobotCommand_Request__Sequence__init(hiwin_interfaces__srv__RobotCommand_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__RobotCommand_Request * data = NULL;

  if (size) {
    data = (hiwin_interfaces__srv__RobotCommand_Request *)allocator.zero_allocate(size, sizeof(hiwin_interfaces__srv__RobotCommand_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = hiwin_interfaces__srv__RobotCommand_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        hiwin_interfaces__srv__RobotCommand_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
hiwin_interfaces__srv__RobotCommand_Request__Sequence__fini(hiwin_interfaces__srv__RobotCommand_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      hiwin_interfaces__srv__RobotCommand_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

hiwin_interfaces__srv__RobotCommand_Request__Sequence *
hiwin_interfaces__srv__RobotCommand_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__RobotCommand_Request__Sequence * array = (hiwin_interfaces__srv__RobotCommand_Request__Sequence *)allocator.allocate(sizeof(hiwin_interfaces__srv__RobotCommand_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = hiwin_interfaces__srv__RobotCommand_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
hiwin_interfaces__srv__RobotCommand_Request__Sequence__destroy(hiwin_interfaces__srv__RobotCommand_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    hiwin_interfaces__srv__RobotCommand_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
hiwin_interfaces__srv__RobotCommand_Request__Sequence__are_equal(const hiwin_interfaces__srv__RobotCommand_Request__Sequence * lhs, const hiwin_interfaces__srv__RobotCommand_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!hiwin_interfaces__srv__RobotCommand_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
hiwin_interfaces__srv__RobotCommand_Request__Sequence__copy(
  const hiwin_interfaces__srv__RobotCommand_Request__Sequence * input,
  hiwin_interfaces__srv__RobotCommand_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(hiwin_interfaces__srv__RobotCommand_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    hiwin_interfaces__srv__RobotCommand_Request * data =
      (hiwin_interfaces__srv__RobotCommand_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!hiwin_interfaces__srv__RobotCommand_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          hiwin_interfaces__srv__RobotCommand_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!hiwin_interfaces__srv__RobotCommand_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `current_position`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
hiwin_interfaces__srv__RobotCommand_Response__init(hiwin_interfaces__srv__RobotCommand_Response * msg)
{
  if (!msg) {
    return false;
  }
  // arm_state
  // digital_state
  // current_position
  if (!rosidl_runtime_c__double__Sequence__init(&msg->current_position, 0)) {
    hiwin_interfaces__srv__RobotCommand_Response__fini(msg);
    return false;
  }
  return true;
}

void
hiwin_interfaces__srv__RobotCommand_Response__fini(hiwin_interfaces__srv__RobotCommand_Response * msg)
{
  if (!msg) {
    return;
  }
  // arm_state
  // digital_state
  // current_position
  rosidl_runtime_c__double__Sequence__fini(&msg->current_position);
}

bool
hiwin_interfaces__srv__RobotCommand_Response__are_equal(const hiwin_interfaces__srv__RobotCommand_Response * lhs, const hiwin_interfaces__srv__RobotCommand_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // arm_state
  if (lhs->arm_state != rhs->arm_state) {
    return false;
  }
  // digital_state
  if (lhs->digital_state != rhs->digital_state) {
    return false;
  }
  // current_position
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->current_position), &(rhs->current_position)))
  {
    return false;
  }
  return true;
}

bool
hiwin_interfaces__srv__RobotCommand_Response__copy(
  const hiwin_interfaces__srv__RobotCommand_Response * input,
  hiwin_interfaces__srv__RobotCommand_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // arm_state
  output->arm_state = input->arm_state;
  // digital_state
  output->digital_state = input->digital_state;
  // current_position
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->current_position), &(output->current_position)))
  {
    return false;
  }
  return true;
}

hiwin_interfaces__srv__RobotCommand_Response *
hiwin_interfaces__srv__RobotCommand_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__RobotCommand_Response * msg = (hiwin_interfaces__srv__RobotCommand_Response *)allocator.allocate(sizeof(hiwin_interfaces__srv__RobotCommand_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(hiwin_interfaces__srv__RobotCommand_Response));
  bool success = hiwin_interfaces__srv__RobotCommand_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
hiwin_interfaces__srv__RobotCommand_Response__destroy(hiwin_interfaces__srv__RobotCommand_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    hiwin_interfaces__srv__RobotCommand_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
hiwin_interfaces__srv__RobotCommand_Response__Sequence__init(hiwin_interfaces__srv__RobotCommand_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__RobotCommand_Response * data = NULL;

  if (size) {
    data = (hiwin_interfaces__srv__RobotCommand_Response *)allocator.zero_allocate(size, sizeof(hiwin_interfaces__srv__RobotCommand_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = hiwin_interfaces__srv__RobotCommand_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        hiwin_interfaces__srv__RobotCommand_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
hiwin_interfaces__srv__RobotCommand_Response__Sequence__fini(hiwin_interfaces__srv__RobotCommand_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      hiwin_interfaces__srv__RobotCommand_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

hiwin_interfaces__srv__RobotCommand_Response__Sequence *
hiwin_interfaces__srv__RobotCommand_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__RobotCommand_Response__Sequence * array = (hiwin_interfaces__srv__RobotCommand_Response__Sequence *)allocator.allocate(sizeof(hiwin_interfaces__srv__RobotCommand_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = hiwin_interfaces__srv__RobotCommand_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
hiwin_interfaces__srv__RobotCommand_Response__Sequence__destroy(hiwin_interfaces__srv__RobotCommand_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    hiwin_interfaces__srv__RobotCommand_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
hiwin_interfaces__srv__RobotCommand_Response__Sequence__are_equal(const hiwin_interfaces__srv__RobotCommand_Response__Sequence * lhs, const hiwin_interfaces__srv__RobotCommand_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!hiwin_interfaces__srv__RobotCommand_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
hiwin_interfaces__srv__RobotCommand_Response__Sequence__copy(
  const hiwin_interfaces__srv__RobotCommand_Response__Sequence * input,
  hiwin_interfaces__srv__RobotCommand_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(hiwin_interfaces__srv__RobotCommand_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    hiwin_interfaces__srv__RobotCommand_Response * data =
      (hiwin_interfaces__srv__RobotCommand_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!hiwin_interfaces__srv__RobotCommand_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          hiwin_interfaces__srv__RobotCommand_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!hiwin_interfaces__srv__RobotCommand_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

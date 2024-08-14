// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from hiwin_interfaces:srv/Hiwinmodbus.idl
// generated code does not contain a copyright notice
#include "hiwin_interfaces/srv/detail/hiwinmodbus__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `mode`
#include "rosidl_runtime_c/string_functions.h"
// Member `pose`
// Member `circ_s`
// Member `circ_end`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
hiwin_interfaces__srv__Hiwinmodbus_Request__init(hiwin_interfaces__srv__Hiwinmodbus_Request * msg)
{
  if (!msg) {
    return false;
  }
  // mode
  if (!rosidl_runtime_c__String__init(&msg->mode)) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__fini(msg);
    return false;
  }
  // holding
  // type
  // vel
  // acc
  // digital_output
  // onoff
  // pose
  if (!rosidl_runtime_c__double__Sequence__init(&msg->pose, 0)) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__fini(msg);
    return false;
  }
  // circ_s
  if (!rosidl_runtime_c__double__Sequence__init(&msg->circ_s, 0)) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__fini(msg);
    return false;
  }
  // circ_end
  if (!rosidl_runtime_c__double__Sequence__init(&msg->circ_end, 0)) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__fini(msg);
    return false;
  }
  // joint
  // dir
  return true;
}

void
hiwin_interfaces__srv__Hiwinmodbus_Request__fini(hiwin_interfaces__srv__Hiwinmodbus_Request * msg)
{
  if (!msg) {
    return;
  }
  // mode
  rosidl_runtime_c__String__fini(&msg->mode);
  // holding
  // type
  // vel
  // acc
  // digital_output
  // onoff
  // pose
  rosidl_runtime_c__double__Sequence__fini(&msg->pose);
  // circ_s
  rosidl_runtime_c__double__Sequence__fini(&msg->circ_s);
  // circ_end
  rosidl_runtime_c__double__Sequence__fini(&msg->circ_end);
  // joint
  // dir
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Request__are_equal(const hiwin_interfaces__srv__Hiwinmodbus_Request * lhs, const hiwin_interfaces__srv__Hiwinmodbus_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // mode
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->mode), &(rhs->mode)))
  {
    return false;
  }
  // holding
  if (lhs->holding != rhs->holding) {
    return false;
  }
  // type
  if (lhs->type != rhs->type) {
    return false;
  }
  // vel
  if (lhs->vel != rhs->vel) {
    return false;
  }
  // acc
  if (lhs->acc != rhs->acc) {
    return false;
  }
  // digital_output
  if (lhs->digital_output != rhs->digital_output) {
    return false;
  }
  // onoff
  if (lhs->onoff != rhs->onoff) {
    return false;
  }
  // pose
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->pose), &(rhs->pose)))
  {
    return false;
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
  // joint
  if (lhs->joint != rhs->joint) {
    return false;
  }
  // dir
  if (lhs->dir != rhs->dir) {
    return false;
  }
  return true;
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Request__copy(
  const hiwin_interfaces__srv__Hiwinmodbus_Request * input,
  hiwin_interfaces__srv__Hiwinmodbus_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // mode
  if (!rosidl_runtime_c__String__copy(
      &(input->mode), &(output->mode)))
  {
    return false;
  }
  // holding
  output->holding = input->holding;
  // type
  output->type = input->type;
  // vel
  output->vel = input->vel;
  // acc
  output->acc = input->acc;
  // digital_output
  output->digital_output = input->digital_output;
  // onoff
  output->onoff = input->onoff;
  // pose
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->pose), &(output->pose)))
  {
    return false;
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
  // joint
  output->joint = input->joint;
  // dir
  output->dir = input->dir;
  return true;
}

hiwin_interfaces__srv__Hiwinmodbus_Request *
hiwin_interfaces__srv__Hiwinmodbus_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__Hiwinmodbus_Request * msg = (hiwin_interfaces__srv__Hiwinmodbus_Request *)allocator.allocate(sizeof(hiwin_interfaces__srv__Hiwinmodbus_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(hiwin_interfaces__srv__Hiwinmodbus_Request));
  bool success = hiwin_interfaces__srv__Hiwinmodbus_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
hiwin_interfaces__srv__Hiwinmodbus_Request__destroy(hiwin_interfaces__srv__Hiwinmodbus_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__init(hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__Hiwinmodbus_Request * data = NULL;

  if (size) {
    data = (hiwin_interfaces__srv__Hiwinmodbus_Request *)allocator.zero_allocate(size, sizeof(hiwin_interfaces__srv__Hiwinmodbus_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = hiwin_interfaces__srv__Hiwinmodbus_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        hiwin_interfaces__srv__Hiwinmodbus_Request__fini(&data[i - 1]);
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
hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__fini(hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * array)
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
      hiwin_interfaces__srv__Hiwinmodbus_Request__fini(&array->data[i]);
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

hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence *
hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * array = (hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence *)allocator.allocate(sizeof(hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__destroy(hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__are_equal(const hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * lhs, const hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!hiwin_interfaces__srv__Hiwinmodbus_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence__copy(
  const hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * input,
  hiwin_interfaces__srv__Hiwinmodbus_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(hiwin_interfaces__srv__Hiwinmodbus_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    hiwin_interfaces__srv__Hiwinmodbus_Request * data =
      (hiwin_interfaces__srv__Hiwinmodbus_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!hiwin_interfaces__srv__Hiwinmodbus_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          hiwin_interfaces__srv__Hiwinmodbus_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!hiwin_interfaces__srv__Hiwinmodbus_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
hiwin_interfaces__srv__Hiwinmodbus_Response__init(hiwin_interfaces__srv__Hiwinmodbus_Response * msg)
{
  if (!msg) {
    return false;
  }
  // arm_state
  return true;
}

void
hiwin_interfaces__srv__Hiwinmodbus_Response__fini(hiwin_interfaces__srv__Hiwinmodbus_Response * msg)
{
  if (!msg) {
    return;
  }
  // arm_state
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Response__are_equal(const hiwin_interfaces__srv__Hiwinmodbus_Response * lhs, const hiwin_interfaces__srv__Hiwinmodbus_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // arm_state
  if (lhs->arm_state != rhs->arm_state) {
    return false;
  }
  return true;
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Response__copy(
  const hiwin_interfaces__srv__Hiwinmodbus_Response * input,
  hiwin_interfaces__srv__Hiwinmodbus_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // arm_state
  output->arm_state = input->arm_state;
  return true;
}

hiwin_interfaces__srv__Hiwinmodbus_Response *
hiwin_interfaces__srv__Hiwinmodbus_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__Hiwinmodbus_Response * msg = (hiwin_interfaces__srv__Hiwinmodbus_Response *)allocator.allocate(sizeof(hiwin_interfaces__srv__Hiwinmodbus_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(hiwin_interfaces__srv__Hiwinmodbus_Response));
  bool success = hiwin_interfaces__srv__Hiwinmodbus_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
hiwin_interfaces__srv__Hiwinmodbus_Response__destroy(hiwin_interfaces__srv__Hiwinmodbus_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    hiwin_interfaces__srv__Hiwinmodbus_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__init(hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__Hiwinmodbus_Response * data = NULL;

  if (size) {
    data = (hiwin_interfaces__srv__Hiwinmodbus_Response *)allocator.zero_allocate(size, sizeof(hiwin_interfaces__srv__Hiwinmodbus_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = hiwin_interfaces__srv__Hiwinmodbus_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        hiwin_interfaces__srv__Hiwinmodbus_Response__fini(&data[i - 1]);
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
hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__fini(hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * array)
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
      hiwin_interfaces__srv__Hiwinmodbus_Response__fini(&array->data[i]);
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

hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence *
hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * array = (hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence *)allocator.allocate(sizeof(hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__destroy(hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__are_equal(const hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * lhs, const hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!hiwin_interfaces__srv__Hiwinmodbus_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence__copy(
  const hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * input,
  hiwin_interfaces__srv__Hiwinmodbus_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(hiwin_interfaces__srv__Hiwinmodbus_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    hiwin_interfaces__srv__Hiwinmodbus_Response * data =
      (hiwin_interfaces__srv__Hiwinmodbus_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!hiwin_interfaces__srv__Hiwinmodbus_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          hiwin_interfaces__srv__Hiwinmodbus_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!hiwin_interfaces__srv__Hiwinmodbus_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

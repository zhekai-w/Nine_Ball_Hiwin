// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice
#include "detect_interface/msg/detail/detection_results__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `labels`
#include "rosidl_runtime_c/string_functions.h"
// Member `scores`
#include "rosidl_runtime_c/primitives_sequence_functions.h"
// Member `bounding_boxes`
#include "detect_interface/msg/detail/bounding_box__functions.h"

bool
detect_interface__msg__DetectionResults__init(detect_interface__msg__DetectionResults * msg)
{
  if (!msg) {
    return false;
  }
  // labels
  if (!rosidl_runtime_c__String__Sequence__init(&msg->labels, 0)) {
    detect_interface__msg__DetectionResults__fini(msg);
    return false;
  }
  // scores
  if (!rosidl_runtime_c__float__Sequence__init(&msg->scores, 0)) {
    detect_interface__msg__DetectionResults__fini(msg);
    return false;
  }
  // bounding_boxes
  if (!detect_interface__msg__BoundingBox__Sequence__init(&msg->bounding_boxes, 0)) {
    detect_interface__msg__DetectionResults__fini(msg);
    return false;
  }
  return true;
}

void
detect_interface__msg__DetectionResults__fini(detect_interface__msg__DetectionResults * msg)
{
  if (!msg) {
    return;
  }
  // labels
  rosidl_runtime_c__String__Sequence__fini(&msg->labels);
  // scores
  rosidl_runtime_c__float__Sequence__fini(&msg->scores);
  // bounding_boxes
  detect_interface__msg__BoundingBox__Sequence__fini(&msg->bounding_boxes);
}

bool
detect_interface__msg__DetectionResults__are_equal(const detect_interface__msg__DetectionResults * lhs, const detect_interface__msg__DetectionResults * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // labels
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->labels), &(rhs->labels)))
  {
    return false;
  }
  // scores
  if (!rosidl_runtime_c__float__Sequence__are_equal(
      &(lhs->scores), &(rhs->scores)))
  {
    return false;
  }
  // bounding_boxes
  if (!detect_interface__msg__BoundingBox__Sequence__are_equal(
      &(lhs->bounding_boxes), &(rhs->bounding_boxes)))
  {
    return false;
  }
  return true;
}

bool
detect_interface__msg__DetectionResults__copy(
  const detect_interface__msg__DetectionResults * input,
  detect_interface__msg__DetectionResults * output)
{
  if (!input || !output) {
    return false;
  }
  // labels
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->labels), &(output->labels)))
  {
    return false;
  }
  // scores
  if (!rosidl_runtime_c__float__Sequence__copy(
      &(input->scores), &(output->scores)))
  {
    return false;
  }
  // bounding_boxes
  if (!detect_interface__msg__BoundingBox__Sequence__copy(
      &(input->bounding_boxes), &(output->bounding_boxes)))
  {
    return false;
  }
  return true;
}

detect_interface__msg__DetectionResults *
detect_interface__msg__DetectionResults__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  detect_interface__msg__DetectionResults * msg = (detect_interface__msg__DetectionResults *)allocator.allocate(sizeof(detect_interface__msg__DetectionResults), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(detect_interface__msg__DetectionResults));
  bool success = detect_interface__msg__DetectionResults__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
detect_interface__msg__DetectionResults__destroy(detect_interface__msg__DetectionResults * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    detect_interface__msg__DetectionResults__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
detect_interface__msg__DetectionResults__Sequence__init(detect_interface__msg__DetectionResults__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  detect_interface__msg__DetectionResults * data = NULL;

  if (size) {
    data = (detect_interface__msg__DetectionResults *)allocator.zero_allocate(size, sizeof(detect_interface__msg__DetectionResults), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = detect_interface__msg__DetectionResults__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        detect_interface__msg__DetectionResults__fini(&data[i - 1]);
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
detect_interface__msg__DetectionResults__Sequence__fini(detect_interface__msg__DetectionResults__Sequence * array)
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
      detect_interface__msg__DetectionResults__fini(&array->data[i]);
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

detect_interface__msg__DetectionResults__Sequence *
detect_interface__msg__DetectionResults__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  detect_interface__msg__DetectionResults__Sequence * array = (detect_interface__msg__DetectionResults__Sequence *)allocator.allocate(sizeof(detect_interface__msg__DetectionResults__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = detect_interface__msg__DetectionResults__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
detect_interface__msg__DetectionResults__Sequence__destroy(detect_interface__msg__DetectionResults__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    detect_interface__msg__DetectionResults__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
detect_interface__msg__DetectionResults__Sequence__are_equal(const detect_interface__msg__DetectionResults__Sequence * lhs, const detect_interface__msg__DetectionResults__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!detect_interface__msg__DetectionResults__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
detect_interface__msg__DetectionResults__Sequence__copy(
  const detect_interface__msg__DetectionResults__Sequence * input,
  detect_interface__msg__DetectionResults__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(detect_interface__msg__DetectionResults);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    detect_interface__msg__DetectionResults * data =
      (detect_interface__msg__DetectionResults *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!detect_interface__msg__DetectionResults__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          detect_interface__msg__DetectionResults__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!detect_interface__msg__DetectionResults__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}

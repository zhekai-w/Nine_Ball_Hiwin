// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__STRUCT_HPP_
#define DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'bounding_boxes'
#include "detect_interface/msg/detail/bounding_box__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__detect_interface__msg__DetectionResults __attribute__((deprecated))
#else
# define DEPRECATED__detect_interface__msg__DetectionResults __declspec(deprecated)
#endif

namespace detect_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct DetectionResults_
{
  using Type = DetectionResults_<ContainerAllocator>;

  explicit DetectionResults_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
  }

  explicit DetectionResults_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_init;
    (void)_alloc;
  }

  // field types and members
  using _labels_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _labels_type labels;
  using _scores_type =
    std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>>;
  _scores_type scores;
  using _bounding_boxes_type =
    std::vector<detect_interface::msg::BoundingBox_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<detect_interface::msg::BoundingBox_<ContainerAllocator>>>;
  _bounding_boxes_type bounding_boxes;

  // setters for named parameter idiom
  Type & set__labels(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->labels = _arg;
    return *this;
  }
  Type & set__scores(
    const std::vector<float, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<float>> & _arg)
  {
    this->scores = _arg;
    return *this;
  }
  Type & set__bounding_boxes(
    const std::vector<detect_interface::msg::BoundingBox_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<detect_interface::msg::BoundingBox_<ContainerAllocator>>> & _arg)
  {
    this->bounding_boxes = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    detect_interface::msg::DetectionResults_<ContainerAllocator> *;
  using ConstRawPtr =
    const detect_interface::msg::DetectionResults_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      detect_interface::msg::DetectionResults_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      detect_interface::msg::DetectionResults_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__detect_interface__msg__DetectionResults
    std::shared_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__detect_interface__msg__DetectionResults
    std::shared_ptr<detect_interface::msg::DetectionResults_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DetectionResults_ & other) const
  {
    if (this->labels != other.labels) {
      return false;
    }
    if (this->scores != other.scores) {
      return false;
    }
    if (this->bounding_boxes != other.bounding_boxes) {
      return false;
    }
    return true;
  }
  bool operator!=(const DetectionResults_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DetectionResults_

// alias to use template instance with default allocator
using DetectionResults =
  detect_interface::msg::DetectionResults_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace detect_interface

#endif  // DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__STRUCT_HPP_

// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from detect_interface:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__BOUNDING_BOX__STRUCT_HPP_
#define DETECT_INTERFACE__MSG__DETAIL__BOUNDING_BOX__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__detect_interface__msg__BoundingBox __attribute__((deprecated))
#else
# define DEPRECATED__detect_interface__msg__BoundingBox __declspec(deprecated)
#endif

namespace detect_interface
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BoundingBox_
{
  using Type = BoundingBox_<ContainerAllocator>;

  explicit BoundingBox_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->xmin = 0l;
      this->ymin = 0l;
      this->xmax = 0l;
      this->ymax = 0l;
    }
  }

  explicit BoundingBox_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->xmin = 0l;
      this->ymin = 0l;
      this->xmax = 0l;
      this->ymax = 0l;
    }
  }

  // field types and members
  using _xmin_type =
    int32_t;
  _xmin_type xmin;
  using _ymin_type =
    int32_t;
  _ymin_type ymin;
  using _xmax_type =
    int32_t;
  _xmax_type xmax;
  using _ymax_type =
    int32_t;
  _ymax_type ymax;

  // setters for named parameter idiom
  Type & set__xmin(
    const int32_t & _arg)
  {
    this->xmin = _arg;
    return *this;
  }
  Type & set__ymin(
    const int32_t & _arg)
  {
    this->ymin = _arg;
    return *this;
  }
  Type & set__xmax(
    const int32_t & _arg)
  {
    this->xmax = _arg;
    return *this;
  }
  Type & set__ymax(
    const int32_t & _arg)
  {
    this->ymax = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    detect_interface::msg::BoundingBox_<ContainerAllocator> *;
  using ConstRawPtr =
    const detect_interface::msg::BoundingBox_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      detect_interface::msg::BoundingBox_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      detect_interface::msg::BoundingBox_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__detect_interface__msg__BoundingBox
    std::shared_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__detect_interface__msg__BoundingBox
    std::shared_ptr<detect_interface::msg::BoundingBox_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BoundingBox_ & other) const
  {
    if (this->xmin != other.xmin) {
      return false;
    }
    if (this->ymin != other.ymin) {
      return false;
    }
    if (this->xmax != other.xmax) {
      return false;
    }
    if (this->ymax != other.ymax) {
      return false;
    }
    return true;
  }
  bool operator!=(const BoundingBox_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BoundingBox_

// alias to use template instance with default allocator
using BoundingBox =
  detect_interface::msg::BoundingBox_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace detect_interface

#endif  // DETECT_INTERFACE__MSG__DETAIL__BOUNDING_BOX__STRUCT_HPP_

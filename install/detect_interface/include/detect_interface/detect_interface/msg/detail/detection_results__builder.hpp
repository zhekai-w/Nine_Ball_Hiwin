// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from detect_interface:msg/DetectionResults.idl
// generated code does not contain a copyright notice

#ifndef DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__BUILDER_HPP_
#define DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "detect_interface/msg/detail/detection_results__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace detect_interface
{

namespace msg
{

namespace builder
{

class Init_DetectionResults_bounding_boxes
{
public:
  explicit Init_DetectionResults_bounding_boxes(::detect_interface::msg::DetectionResults & msg)
  : msg_(msg)
  {}
  ::detect_interface::msg::DetectionResults bounding_boxes(::detect_interface::msg::DetectionResults::_bounding_boxes_type arg)
  {
    msg_.bounding_boxes = std::move(arg);
    return std::move(msg_);
  }

private:
  ::detect_interface::msg::DetectionResults msg_;
};

class Init_DetectionResults_scores
{
public:
  explicit Init_DetectionResults_scores(::detect_interface::msg::DetectionResults & msg)
  : msg_(msg)
  {}
  Init_DetectionResults_bounding_boxes scores(::detect_interface::msg::DetectionResults::_scores_type arg)
  {
    msg_.scores = std::move(arg);
    return Init_DetectionResults_bounding_boxes(msg_);
  }

private:
  ::detect_interface::msg::DetectionResults msg_;
};

class Init_DetectionResults_labels
{
public:
  Init_DetectionResults_labels()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_DetectionResults_scores labels(::detect_interface::msg::DetectionResults::_labels_type arg)
  {
    msg_.labels = std::move(arg);
    return Init_DetectionResults_scores(msg_);
  }

private:
  ::detect_interface::msg::DetectionResults msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::detect_interface::msg::DetectionResults>()
{
  return detect_interface::msg::builder::Init_DetectionResults_labels();
}

}  // namespace detect_interface

#endif  // DETECT_INTERFACE__MSG__DETAIL__DETECTION_RESULTS__BUILDER_HPP_

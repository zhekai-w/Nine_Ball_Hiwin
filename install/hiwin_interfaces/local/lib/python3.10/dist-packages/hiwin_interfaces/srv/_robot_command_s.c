// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from hiwin_interfaces:srv/RobotCommand.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "hiwin_interfaces/srv/detail/robot_command__struct.h"
#include "hiwin_interfaces/srv/detail/robot_command__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool geometry_msgs__msg__twist__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * geometry_msgs__msg__twist__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool hiwin_interfaces__srv__robot_command__request__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[57];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("hiwin_interfaces.srv._robot_command.RobotCommand_Request", full_classname_dest, 56) == 0);
  }
  hiwin_interfaces__srv__RobotCommand_Request * ros_message = _ros_message;
  {  // do_timer
    PyObject * field = PyObject_GetAttrString(_pymsg, "do_timer");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->do_timer = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // holding
    PyObject * field = PyObject_GetAttrString(_pymsg, "holding");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->holding = (Py_True == field);
    Py_DECREF(field);
  }
  {  // cmd_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "cmd_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->cmd_mode = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // cmd_type
    PyObject * field = PyObject_GetAttrString(_pymsg, "cmd_type");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->cmd_type = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // velocity
    PyObject * field = PyObject_GetAttrString(_pymsg, "velocity");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->velocity = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // acceleration
    PyObject * field = PyObject_GetAttrString(_pymsg, "acceleration");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->acceleration = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tool
    PyObject * field = PyObject_GetAttrString(_pymsg, "tool");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tool = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // base
    PyObject * field = PyObject_GetAttrString(_pymsg, "base");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->base = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // base_num
    PyObject * field = PyObject_GetAttrString(_pymsg, "base_num");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->base_num = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tool_num
    PyObject * field = PyObject_GetAttrString(_pymsg, "tool_num");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tool_num = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // digital_input_pin
    PyObject * field = PyObject_GetAttrString(_pymsg, "digital_input_pin");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->digital_input_pin = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // digital_output_pin
    PyObject * field = PyObject_GetAttrString(_pymsg, "digital_output_pin");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->digital_output_pin = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // digital_output_cmd
    PyObject * field = PyObject_GetAttrString(_pymsg, "digital_output_cmd");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->digital_output_cmd = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // pose
    PyObject * field = PyObject_GetAttrString(_pymsg, "pose");
    if (!field) {
      return false;
    }
    if (!geometry_msgs__msg__twist__convert_from_py(field, &ros_message->pose)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // joints
    PyObject * field = PyObject_GetAttrString(_pymsg, "joints");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
      Py_ssize_t size = 6;
      double * dest = ros_message->joints;
      for (Py_ssize_t i = 0; i < size; ++i) {
        double tmp = *(npy_float64 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // circ_s
    PyObject * field = PyObject_GetAttrString(_pymsg, "circ_s");
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = view.len / sizeof(double);
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->circ_s), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->circ_s.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'circ_s'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->circ_s), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->circ_s.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyFloat_Check(item));
        double tmp = PyFloat_AS_DOUBLE(item);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // circ_end
    PyObject * field = PyObject_GetAttrString(_pymsg, "circ_end");
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = view.len / sizeof(double);
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->circ_end), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->circ_end.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'circ_end'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->circ_end), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->circ_end.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyFloat_Check(item));
        double tmp = PyFloat_AS_DOUBLE(item);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // jog_joint
    PyObject * field = PyObject_GetAttrString(_pymsg, "jog_joint");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->jog_joint = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // jog_dir
    PyObject * field = PyObject_GetAttrString(_pymsg, "jog_dir");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->jog_dir = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * hiwin_interfaces__srv__robot_command__request__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RobotCommand_Request */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("hiwin_interfaces.srv._robot_command");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RobotCommand_Request");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  hiwin_interfaces__srv__RobotCommand_Request * ros_message = (hiwin_interfaces__srv__RobotCommand_Request *)raw_ros_message;
  {  // do_timer
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->do_timer);
    {
      int rc = PyObject_SetAttrString(_pymessage, "do_timer", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // holding
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->holding ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "holding", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cmd_mode
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->cmd_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cmd_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cmd_type
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->cmd_type);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cmd_type", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // velocity
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->velocity);
    {
      int rc = PyObject_SetAttrString(_pymessage, "velocity", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // acceleration
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->acceleration);
    {
      int rc = PyObject_SetAttrString(_pymessage, "acceleration", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tool
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tool);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tool", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // base
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->base);
    {
      int rc = PyObject_SetAttrString(_pymessage, "base", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // base_num
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->base_num);
    {
      int rc = PyObject_SetAttrString(_pymessage, "base_num", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tool_num
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tool_num);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tool_num", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // digital_input_pin
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->digital_input_pin);
    {
      int rc = PyObject_SetAttrString(_pymessage, "digital_input_pin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // digital_output_pin
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->digital_output_pin);
    {
      int rc = PyObject_SetAttrString(_pymessage, "digital_output_pin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // digital_output_cmd
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->digital_output_cmd);
    {
      int rc = PyObject_SetAttrString(_pymessage, "digital_output_cmd", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // pose
    PyObject * field = NULL;
    field = geometry_msgs__msg__twist__convert_to_py(&ros_message->pose);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "pose", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // joints
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "joints");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_FLOAT64);
    assert(sizeof(npy_float64) == sizeof(double));
    npy_float64 * dst = (npy_float64 *)PyArray_GETPTR1(seq_field, 0);
    double * src = &(ros_message->joints[0]);
    memcpy(dst, src, 6 * sizeof(double));
    Py_DECREF(field);
  }
  {  // circ_s
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "circ_s");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
    // ensure that itemsize matches the sizeof of the ROS message field
    PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
    assert(itemsize_attr != NULL);
    size_t itemsize = PyLong_AsSize_t(itemsize_attr);
    Py_DECREF(itemsize_attr);
    if (itemsize != sizeof(double)) {
      PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
      Py_DECREF(field);
      return NULL;
    }
    // clear the array, poor approach to remove potential default values
    Py_ssize_t length = PyObject_Length(field);
    if (-1 == length) {
      Py_DECREF(field);
      return NULL;
    }
    if (length > 0) {
      PyObject * pop = PyObject_GetAttrString(field, "pop");
      assert(pop != NULL);
      for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject * ret = PyObject_CallFunctionObjArgs(pop, NULL);
        if (!ret) {
          Py_DECREF(pop);
          Py_DECREF(field);
          return NULL;
        }
        Py_DECREF(ret);
      }
      Py_DECREF(pop);
    }
    if (ros_message->circ_s.size > 0) {
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      double * src = &(ros_message->circ_s.data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->circ_s.size * sizeof(double));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
    }
    Py_DECREF(field);
  }
  {  // circ_end
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "circ_end");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
    // ensure that itemsize matches the sizeof of the ROS message field
    PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
    assert(itemsize_attr != NULL);
    size_t itemsize = PyLong_AsSize_t(itemsize_attr);
    Py_DECREF(itemsize_attr);
    if (itemsize != sizeof(double)) {
      PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
      Py_DECREF(field);
      return NULL;
    }
    // clear the array, poor approach to remove potential default values
    Py_ssize_t length = PyObject_Length(field);
    if (-1 == length) {
      Py_DECREF(field);
      return NULL;
    }
    if (length > 0) {
      PyObject * pop = PyObject_GetAttrString(field, "pop");
      assert(pop != NULL);
      for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject * ret = PyObject_CallFunctionObjArgs(pop, NULL);
        if (!ret) {
          Py_DECREF(pop);
          Py_DECREF(field);
          return NULL;
        }
        Py_DECREF(ret);
      }
      Py_DECREF(pop);
    }
    if (ros_message->circ_end.size > 0) {
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      double * src = &(ros_message->circ_end.data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->circ_end.size * sizeof(double));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
    }
    Py_DECREF(field);
  }
  {  // jog_joint
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->jog_joint);
    {
      int rc = PyObject_SetAttrString(_pymessage, "jog_joint", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // jog_dir
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->jog_dir);
    {
      int rc = PyObject_SetAttrString(_pymessage, "jog_dir", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
// already included above
// #include <Python.h>
// already included above
// #include <stdbool.h>
// already included above
// #include "numpy/ndarrayobject.h"
// already included above
// #include "rosidl_runtime_c/visibility_control.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__struct.h"
// already included above
// #include "hiwin_interfaces/srv/detail/robot_command__functions.h"

// already included above
// #include "rosidl_runtime_c/primitives_sequence.h"
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool hiwin_interfaces__srv__robot_command__response__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[58];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("hiwin_interfaces.srv._robot_command.RobotCommand_Response", full_classname_dest, 57) == 0);
  }
  hiwin_interfaces__srv__RobotCommand_Response * ros_message = _ros_message;
  {  // arm_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "arm_state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->arm_state = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // digital_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "digital_state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->digital_state = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // current_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "current_position");
    if (!field) {
      return false;
    }
    if (PyObject_CheckBuffer(field)) {
      // Optimization for converting arrays of primitives
      Py_buffer view;
      int rc = PyObject_GetBuffer(field, &view, PyBUF_SIMPLE);
      if (rc < 0) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = view.len / sizeof(double);
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->current_position), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->current_position.data;
      rc = PyBuffer_ToContiguous(dest, &view, view.len, 'C');
      if (rc < 0) {
        PyBuffer_Release(&view);
        Py_DECREF(field);
        return false;
      }
      PyBuffer_Release(&view);
    } else {
      PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'current_position'");
      if (!seq_field) {
        Py_DECREF(field);
        return false;
      }
      Py_ssize_t size = PySequence_Size(field);
      if (-1 == size) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      if (!rosidl_runtime_c__double__Sequence__init(&(ros_message->current_position), size)) {
        PyErr_SetString(PyExc_RuntimeError, "unable to create double__Sequence ros_message");
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
      double * dest = ros_message->current_position.data;
      for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject * item = PySequence_Fast_GET_ITEM(seq_field, i);
        if (!item) {
          Py_DECREF(seq_field);
          Py_DECREF(field);
          return false;
        }
        assert(PyFloat_Check(item));
        double tmp = PyFloat_AS_DOUBLE(item);
        memcpy(&dest[i], &tmp, sizeof(double));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * hiwin_interfaces__srv__robot_command__response__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RobotCommand_Response */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("hiwin_interfaces.srv._robot_command");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RobotCommand_Response");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  hiwin_interfaces__srv__RobotCommand_Response * ros_message = (hiwin_interfaces__srv__RobotCommand_Response *)raw_ros_message;
  {  // arm_state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->arm_state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "arm_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // digital_state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->digital_state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "digital_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // current_position
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "current_position");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "array.array") == 0);
    // ensure that itemsize matches the sizeof of the ROS message field
    PyObject * itemsize_attr = PyObject_GetAttrString(field, "itemsize");
    assert(itemsize_attr != NULL);
    size_t itemsize = PyLong_AsSize_t(itemsize_attr);
    Py_DECREF(itemsize_attr);
    if (itemsize != sizeof(double)) {
      PyErr_SetString(PyExc_RuntimeError, "itemsize doesn't match expectation");
      Py_DECREF(field);
      return NULL;
    }
    // clear the array, poor approach to remove potential default values
    Py_ssize_t length = PyObject_Length(field);
    if (-1 == length) {
      Py_DECREF(field);
      return NULL;
    }
    if (length > 0) {
      PyObject * pop = PyObject_GetAttrString(field, "pop");
      assert(pop != NULL);
      for (Py_ssize_t i = 0; i < length; ++i) {
        PyObject * ret = PyObject_CallFunctionObjArgs(pop, NULL);
        if (!ret) {
          Py_DECREF(pop);
          Py_DECREF(field);
          return NULL;
        }
        Py_DECREF(ret);
      }
      Py_DECREF(pop);
    }
    if (ros_message->current_position.size > 0) {
      // populating the array.array using the frombytes method
      PyObject * frombytes = PyObject_GetAttrString(field, "frombytes");
      assert(frombytes != NULL);
      double * src = &(ros_message->current_position.data[0]);
      PyObject * data = PyBytes_FromStringAndSize((const char *)src, ros_message->current_position.size * sizeof(double));
      assert(data != NULL);
      PyObject * ret = PyObject_CallFunctionObjArgs(frombytes, data, NULL);
      Py_DECREF(data);
      Py_DECREF(frombytes);
      if (!ret) {
        Py_DECREF(field);
        return NULL;
      }
      Py_DECREF(ret);
    }
    Py_DECREF(field);
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

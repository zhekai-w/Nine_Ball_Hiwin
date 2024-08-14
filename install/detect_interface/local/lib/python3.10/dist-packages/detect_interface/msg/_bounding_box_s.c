// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from detect_interface:msg/BoundingBox.idl
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
#include "detect_interface/msg/detail/bounding_box__struct.h"
#include "detect_interface/msg/detail/bounding_box__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool detect_interface__msg__bounding_box__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[47];
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
    assert(strncmp("detect_interface.msg._bounding_box.BoundingBox", full_classname_dest, 46) == 0);
  }
  detect_interface__msg__BoundingBox * ros_message = _ros_message;
  {  // xmin
    PyObject * field = PyObject_GetAttrString(_pymsg, "xmin");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->xmin = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // ymin
    PyObject * field = PyObject_GetAttrString(_pymsg, "ymin");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ymin = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // xmax
    PyObject * field = PyObject_GetAttrString(_pymsg, "xmax");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->xmax = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // ymax
    PyObject * field = PyObject_GetAttrString(_pymsg, "ymax");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ymax = (int32_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * detect_interface__msg__bounding_box__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of BoundingBox */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("detect_interface.msg._bounding_box");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "BoundingBox");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  detect_interface__msg__BoundingBox * ros_message = (detect_interface__msg__BoundingBox *)raw_ros_message;
  {  // xmin
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->xmin);
    {
      int rc = PyObject_SetAttrString(_pymessage, "xmin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ymin
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->ymin);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ymin", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // xmax
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->xmax);
    {
      int rc = PyObject_SetAttrString(_pymessage, "xmax", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ymax
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->ymax);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ymax", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}

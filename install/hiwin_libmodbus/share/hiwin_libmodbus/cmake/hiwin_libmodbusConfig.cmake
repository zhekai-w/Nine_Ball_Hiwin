# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_hiwin_libmodbus_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED hiwin_libmodbus_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(hiwin_libmodbus_FOUND FALSE)
  elseif(NOT hiwin_libmodbus_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(hiwin_libmodbus_FOUND FALSE)
  endif()
  return()
endif()
set(_hiwin_libmodbus_CONFIG_INCLUDED TRUE)

# output package information
if(NOT hiwin_libmodbus_FIND_QUIETLY)
  message(STATUS "Found hiwin_libmodbus: 0.0.0 (${hiwin_libmodbus_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'hiwin_libmodbus' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${hiwin_libmodbus_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(hiwin_libmodbus_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake;ament_cmake_export_targets-extras.cmake")
foreach(_extra ${_extras})
  include("${hiwin_libmodbus_DIR}/${_extra}")
endforeach()

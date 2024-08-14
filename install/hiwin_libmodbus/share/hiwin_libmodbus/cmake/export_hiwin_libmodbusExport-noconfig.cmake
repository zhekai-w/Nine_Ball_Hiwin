#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "hiwin_libmodbus::hiwin_libmodbus" for configuration ""
set_property(TARGET hiwin_libmodbus::hiwin_libmodbus APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(hiwin_libmodbus::hiwin_libmodbus PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libhiwin_libmodbus.so"
  IMPORTED_SONAME_NOCONFIG "libhiwin_libmodbus.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS hiwin_libmodbus::hiwin_libmodbus )
list(APPEND _IMPORT_CHECK_FILES_FOR_hiwin_libmodbus::hiwin_libmodbus "${_IMPORT_PREFIX}/lib/libhiwin_libmodbus.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)

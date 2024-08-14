#ifndef HIWIN_LIBMODBUS__VISIBILITY_CONTROL_H_
#define HIWIN_LIBMODBUS__VISIBILITY_CONTROL_H_

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define HIWIN_LIBMODBUS_EXPORT __attribute__ ((dllexport))
    #define HIWIN_LIBMODBUS_IMPORT __attribute__ ((dllimport))
  #else
    #define HIWIN_LIBMODBUS_EXPORT __declspec(dllexport)
    #define HIWIN_LIBMODBUS_IMPORT __declspec(dllimport)
  #endif
  #ifdef HIWIN_LIBMODBUS_BUILDING_LIBRARY
    #define HIWIN_LIBMODBUS_PUBLIC HIWIN_LIBMODBUS_EXPORT
  #else
    #define HIWIN_LIBMODBUS_PUBLIC HIWIN_LIBMODBUS_IMPORT
  #endif
  #define HIWIN_LIBMODBUS_PUBLIC_TYPE HIWIN_LIBMODBUS_PUBLIC
  #define HIWIN_LIBMODBUS_LOCAL
#else
  #define HIWIN_LIBMODBUS_EXPORT __attribute__ ((visibility("default")))
  #define HIWIN_LIBMODBUS_IMPORT
  #if __GNUC__ >= 4
    #define HIWIN_LIBMODBUS_PUBLIC __attribute__ ((visibility("default")))
    #define HIWIN_LIBMODBUS_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define HIWIN_LIBMODBUS_PUBLIC
    #define HIWIN_LIBMODBUS_LOCAL
  #endif
  #define HIWIN_LIBMODBUS_PUBLIC_TYPE
#endif

#endif  // HIWIN_LIBMODBUS__VISIBILITY_CONTROL_H_

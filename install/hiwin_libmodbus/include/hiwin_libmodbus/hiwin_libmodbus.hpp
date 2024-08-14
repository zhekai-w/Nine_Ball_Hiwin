#ifndef HIWIN_LIBMODBUS__HIWIN_LIBMODBUS_HPP_
#define HIWIN_LIBMODBUS__HIWIN_LIBMODBUS_HPP_

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <errno.h>
#include <string>
#include <vector>
#include <typeinfo>
 
#include <modbus.h>
 
#define MODBUS_SERVER_IP       "192.168.0.1"
#define MODBUS_SERVER_PORT     502

#define REGISTERS_ADDRESS      201
#define ROBOT_MOVE_STATE       524
#define MOVE_STATE_LEN         1
#define MAX_READ_REGISTERS     1
// #define MODBUS_TIMEOUT_SEC     3
// #define MODBUS_TIMEOUT_USEC    0

#include "hiwin_libmodbus/visibility_control.h"

// namespace hiwin_libmodbus
// {

class HiwinLibmodbus
{
public:
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  HiwinLibmodbus();
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  virtual ~HiwinLibmodbus();
  // TODO: The function name should follow the coding style
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void Holding_Registers_init();
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void MOTOR_EXCITE();
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  int libModbus_Connect(const std::string& ip_address);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  int libModbus_Connect(const wchar_t *ip_address);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  int libModbus_Connect(const char *ip_address);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void Modbus_Close();
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void Arm_State_REGISTERS(int &arm_state);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void Read_REGISTERS(int addr, int &state);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void Read_DI(int addr, int &state);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void DO(int DO_Num, int active);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void HOME();
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void getArmJoints(std::vector<double> &Joints);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void getArmPose(std::vector<double> &Pose);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void PTP(
    uint16_t type, uint16_t vel, uint16_t acc, uint16_t TOOL, uint16_t BASE, const std::vector<double> GOAL);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void PTP(
    uint16_t type, uint16_t vel, uint16_t acc, uint16_t TOOL, uint16_t BASE, const double *GOAL);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void LIN(
    uint16_t type, uint16_t vel, uint16_t acc, uint16_t TOOL, uint16_t BASE, const std::vector<double> GOAL);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void LIN(
    uint16_t type, uint16_t vel, uint16_t acc, uint16_t TOOL, uint16_t BASE, const double *GOAL);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void CIRC(
    uint16_t vel, uint16_t acc, uint16_t TOOL, uint16_t BASE, const std::vector<double> CIRC_s, const std::vector<double> CIRC_end);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void CIRC(
    uint16_t vel, uint16_t acc, uint16_t TOOL, uint16_t BASE, const double *CIRC_s, const double *CIRC_end);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void JOG(
    uint16_t joint,uint16_t dir);
  void SET_BASE(uint16_t base_num, const std::vector<double> POSE);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void SET_BASE(uint16_t base_num, const double *POSE);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void SET_TOOL(uint16_t tool_num, const std::vector<double> POSE);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void SET_TOOL(uint16_t tool_num, const double *POSE);
  HIWIN_LIBMODBUS_PUBLIC_TYPE
  void Motion_Stop();
  

  int qqq{0};
  // int ArmState;



  int A1_Low;
  int A1_High; 
  int A2_Low;
  int A2_High; 
  int A3_Low;
  int A3_High; 
  int A4_Low;
  int A4_High;
  int A5_Low;
  int A5_High;
  int A6_Low;
  int A6_High;
  double joint1;
  double joint2;
  double joint3;
  double joint4;
  double joint5;
  double joint6;

  int X_Low;
  int X_High; 
  int Y_Low;
  int Y_High; 
  int Z_Low;
  int Z_High; 
  int RX_Low;
  int RX_High;
  int RY_Low;
  int RY_High;
  int RZ_Low;
  int RZ_High;
  double posex;
  double posey;
  double posez;
  double rx;
  double ry;  
  double rz;  

private:
  modbus_t        *ctx_{nullptr};
  int             wrt_{0};
  int             ret_{0};
  int             i;
  // int             joint1_{0};
  // int             joint2_{0};
  // int             joint3_{0};
  // int             joint4_{0};
  // int             joint5_{0};
  // int             joint6_{0};
  // int             xpose_{0};
  // int             ypose_{0};
  // int             zpose_{0};
  // int             rxpose_{0};
  // int             rypose_{0};
  // int             rzpose_{0};
};

// }  // namespace hiwin_libmodbus

#endif  // HIWIN_LIBMODBUS__HIWIN_LIBMODBUS_HPP_

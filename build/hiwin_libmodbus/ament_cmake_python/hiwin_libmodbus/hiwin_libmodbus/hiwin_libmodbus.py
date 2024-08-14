from ctypes import CDLL, c_double, c_int, c_void_p, c_void_p, c_wchar_p
from ament_index_python.packages import get_package_prefix

class HiwinLibmodbus(object):
  def __init__(self):
    pkg_path = get_package_prefix("hiwin_libmodbus")
    self.hiwin_lib = CDLL(pkg_path + "/lib/libhiwin_libmodbus_ctype_wrapper.so")
    self.hiwin_lib.HiwinLibmodbusConstructor.restype = c_void_p
    
    self.hiwin_lib.HiwinLibmodbusDestructor.argtypes = [c_void_p]
    self.hiwin_lib.Holding_Registers_init.argtypes = [c_void_p]
    self.hiwin_lib.libModbus_Connect.argtypes = [c_void_p, c_wchar_p]
    self.hiwin_lib.Modbus_Close.argtypes = [c_void_p]
    self.hiwin_lib.Arm_State_REGISTERS.argtypes = [c_void_p]
    self.hiwin_lib.Read_REGISTERS.argtypes = [c_void_p, c_int]
    self.hiwin_lib.DO.argtypes = [c_void_p, c_int, c_int]
    self.hiwin_lib.HOME.argtypes = [c_void_p]
    self.hiwin_lib.PTP.argtypes = [c_void_p, c_int, c_int, c_int, c_int, c_int]
    self.hiwin_lib.LIN.argtypes = [c_void_p, c_int, c_int, c_int, c_int, c_int]
    self.hiwin_lib.CIRC.argtypes = [c_void_p, c_int, c_int, c_int, c_int]
    self.hiwin_lib.JOG.argtypes = [c_void_p, c_int, c_int]

    self.hiwin_libmodbus_ptr = self.hiwin_lib.HiwinLibmodbusConstructor()

  def __del__(self):
    self.hiwin_lib.HiwinLibmodbusDestructor(self.hiwin_libmodbus_ptr)
  
  def Holding_Registers_init(self):
    self.hiwin_lib.Holding_Registers_init(self.hiwin_libmodbus_ptr)
    return

  def libModbus_Connect(self, ip_address='192.168.0.1'):
    return self.hiwin_lib.libModbus_Connect(self.hiwin_libmodbus_ptr, ip_address)

  def Modbus_Close(self):
    self.hiwin_lib.Modbus_Close(self.hiwin_libmodbus_ptr)
    return

  def Arm_State_REGISTERS(self):
    return self.hiwin_lib.Arm_State_REGISTERS(self.hiwin_libmodbus_ptr)

  def Read_REGISTERS(self, addr):
    return self.hiwin_lib.Read_REGISTERS(self.hiwin_libmodbus_ptr, addr)

  def DO(self, DO_Num, x):
    self.hiwin_lib.DO(self.hiwin_libmodbus_ptr, DO_Num, x)
    return

  def HOME(self):
    self.hiwin_lib.HOME(self.hiwin_libmodbus_ptr)
    return

  def PTP(self, type, vel, acc, TOOL, BASE, Angle):
    c_angle = self.list_to_double_array(Angle)
    self.hiwin_lib.PTP(self.hiwin_libmodbus_ptr, type, vel, acc, TOOL, BASE, c_angle)
    return

  def LIN(self, type, vel, acc, TOOL, BASE, XYZ):
    xyz = self.list_to_double_array(XYZ)
    self.hiwin_lib.LIN(self.hiwin_libmodbus_ptr, type, vel, acc, TOOL, BASE, xyz)
    return

  def CIRC(self, vel, acc, TOOL, BASE, CIRC_s, CIRC_end):
    c_circ_s = self.list_to_double_array(CIRC_s)
    c_circ_end = self.list_to_double_array(CIRC_end)
    self.hiwin_lib.CIRC(self.hiwin_libmodbus_ptr, vel, acc, TOOL, BASE, c_circ_s, c_circ_end)
    return

  def JOG(self, vel, acc, TOOL, BASE, CIRC_s, CIRC_end):
    self.hiwin_lib.JOG(self.hiwin_libmodbus_ptr, vel, acc, TOOL, BASE, CIRC_s, CIRC_end)
    return

  def list_to_double_array(self, list):
    return (c_double * len(list))(*list)
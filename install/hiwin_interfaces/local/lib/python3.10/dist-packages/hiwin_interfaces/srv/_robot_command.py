# generated from rosidl_generator_py/resource/_idl.py.em
# with input from hiwin_interfaces:srv/RobotCommand.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'circ_s'
# Member 'circ_end'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'joints'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RobotCommand_Request(type):
    """Metaclass of message 'RobotCommand_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'EXCITE': 1,
        'PTP': 2,
        'LINE': 3,
        'CIRC': 4,
        'DIGITAL_OUTPUT': 5,
        'HOME': 6,
        'JOG': 7,
        'CHECK_JOINT': 8,
        'CHECK_POSE': 9,
        'CLOSE': 10,
        'WAITING': 11,
        'READ_DI': 12,
        'SET_BASE': 13,
        'SET_TOOL': 14,
        'MOTION_STOP': 15,
        'JOINTS_CMD': 0,
        'POSE_CMD': 1,
        'DIGITAL_ON': 1,
        'DIGITAL_OFF': 0,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('hiwin_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'hiwin_interfaces.srv.RobotCommand_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__robot_command__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__robot_command__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__robot_command__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__robot_command__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__robot_command__request

            from geometry_msgs.msg import Twist
            if Twist.__class__._TYPE_SUPPORT is None:
                Twist.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'EXCITE': cls.__constants['EXCITE'],
            'PTP': cls.__constants['PTP'],
            'LINE': cls.__constants['LINE'],
            'CIRC': cls.__constants['CIRC'],
            'DIGITAL_OUTPUT': cls.__constants['DIGITAL_OUTPUT'],
            'HOME': cls.__constants['HOME'],
            'JOG': cls.__constants['JOG'],
            'CHECK_JOINT': cls.__constants['CHECK_JOINT'],
            'CHECK_POSE': cls.__constants['CHECK_POSE'],
            'CLOSE': cls.__constants['CLOSE'],
            'WAITING': cls.__constants['WAITING'],
            'READ_DI': cls.__constants['READ_DI'],
            'SET_BASE': cls.__constants['SET_BASE'],
            'SET_TOOL': cls.__constants['SET_TOOL'],
            'MOTION_STOP': cls.__constants['MOTION_STOP'],
            'JOINTS_CMD': cls.__constants['JOINTS_CMD'],
            'POSE_CMD': cls.__constants['POSE_CMD'],
            'DIGITAL_ON': cls.__constants['DIGITAL_ON'],
            'DIGITAL_OFF': cls.__constants['DIGITAL_OFF'],
        }

    @property
    def EXCITE(self):
        """Message constant 'EXCITE'."""
        return Metaclass_RobotCommand_Request.__constants['EXCITE']

    @property
    def PTP(self):
        """Message constant 'PTP'."""
        return Metaclass_RobotCommand_Request.__constants['PTP']

    @property
    def LINE(self):
        """Message constant 'LINE'."""
        return Metaclass_RobotCommand_Request.__constants['LINE']

    @property
    def CIRC(self):
        """Message constant 'CIRC'."""
        return Metaclass_RobotCommand_Request.__constants['CIRC']

    @property
    def DIGITAL_OUTPUT(self):
        """Message constant 'DIGITAL_OUTPUT'."""
        return Metaclass_RobotCommand_Request.__constants['DIGITAL_OUTPUT']

    @property
    def HOME(self):
        """Message constant 'HOME'."""
        return Metaclass_RobotCommand_Request.__constants['HOME']

    @property
    def JOG(self):
        """Message constant 'JOG'."""
        return Metaclass_RobotCommand_Request.__constants['JOG']

    @property
    def CHECK_JOINT(self):
        """Message constant 'CHECK_JOINT'."""
        return Metaclass_RobotCommand_Request.__constants['CHECK_JOINT']

    @property
    def CHECK_POSE(self):
        """Message constant 'CHECK_POSE'."""
        return Metaclass_RobotCommand_Request.__constants['CHECK_POSE']

    @property
    def CLOSE(self):
        """Message constant 'CLOSE'."""
        return Metaclass_RobotCommand_Request.__constants['CLOSE']

    @property
    def WAITING(self):
        """Message constant 'WAITING'."""
        return Metaclass_RobotCommand_Request.__constants['WAITING']

    @property
    def READ_DI(self):
        """Message constant 'READ_DI'."""
        return Metaclass_RobotCommand_Request.__constants['READ_DI']

    @property
    def SET_BASE(self):
        """Message constant 'SET_BASE'."""
        return Metaclass_RobotCommand_Request.__constants['SET_BASE']

    @property
    def SET_TOOL(self):
        """Message constant 'SET_TOOL'."""
        return Metaclass_RobotCommand_Request.__constants['SET_TOOL']

    @property
    def MOTION_STOP(self):
        """Message constant 'MOTION_STOP'."""
        return Metaclass_RobotCommand_Request.__constants['MOTION_STOP']

    @property
    def JOINTS_CMD(self):
        """Message constant 'JOINTS_CMD'."""
        return Metaclass_RobotCommand_Request.__constants['JOINTS_CMD']

    @property
    def POSE_CMD(self):
        """Message constant 'POSE_CMD'."""
        return Metaclass_RobotCommand_Request.__constants['POSE_CMD']

    @property
    def DIGITAL_ON(self):
        """Message constant 'DIGITAL_ON'."""
        return Metaclass_RobotCommand_Request.__constants['DIGITAL_ON']

    @property
    def DIGITAL_OFF(self):
        """Message constant 'DIGITAL_OFF'."""
        return Metaclass_RobotCommand_Request.__constants['DIGITAL_OFF']


class RobotCommand_Request(metaclass=Metaclass_RobotCommand_Request):
    """
    Message class 'RobotCommand_Request'.

    Constants:
      EXCITE
      PTP
      LINE
      CIRC
      DIGITAL_OUTPUT
      HOME
      JOG
      CHECK_JOINT
      CHECK_POSE
      CLOSE
      WAITING
      READ_DI
      SET_BASE
      SET_TOOL
      MOTION_STOP
      JOINTS_CMD
      POSE_CMD
      DIGITAL_ON
      DIGITAL_OFF
    """

    __slots__ = [
        '_do_timer',
        '_holding',
        '_cmd_mode',
        '_cmd_type',
        '_velocity',
        '_acceleration',
        '_tool',
        '_base',
        '_base_num',
        '_tool_num',
        '_digital_input_pin',
        '_digital_output_pin',
        '_digital_output_cmd',
        '_pose',
        '_joints',
        '_circ_s',
        '_circ_end',
        '_jog_joint',
        '_jog_dir',
    ]

    _fields_and_field_types = {
        'do_timer': 'uint8',
        'holding': 'boolean',
        'cmd_mode': 'uint8',
        'cmd_type': 'uint8',
        'velocity': 'uint8',
        'acceleration': 'uint8',
        'tool': 'uint8',
        'base': 'uint8',
        'base_num': 'uint8',
        'tool_num': 'uint8',
        'digital_input_pin': 'uint8',
        'digital_output_pin': 'uint8',
        'digital_output_cmd': 'uint8',
        'pose': 'geometry_msgs/Twist',
        'joints': 'double[6]',
        'circ_s': 'sequence<double>',
        'circ_end': 'sequence<double>',
        'jog_joint': 'int8',
        'jog_dir': 'int8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Twist'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('double'), 6),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.do_timer = kwargs.get('do_timer', int())
        self.holding = kwargs.get('holding', bool())
        self.cmd_mode = kwargs.get('cmd_mode', int())
        self.cmd_type = kwargs.get('cmd_type', int())
        self.velocity = kwargs.get('velocity', int())
        self.acceleration = kwargs.get('acceleration', int())
        self.tool = kwargs.get('tool', int())
        self.base = kwargs.get('base', int())
        self.base_num = kwargs.get('base_num', int())
        self.tool_num = kwargs.get('tool_num', int())
        self.digital_input_pin = kwargs.get('digital_input_pin', int())
        self.digital_output_pin = kwargs.get('digital_output_pin', int())
        self.digital_output_cmd = kwargs.get('digital_output_cmd', int())
        from geometry_msgs.msg import Twist
        self.pose = kwargs.get('pose', Twist())
        if 'joints' not in kwargs:
            self.joints = numpy.zeros(6, dtype=numpy.float64)
        else:
            self.joints = numpy.array(kwargs.get('joints'), dtype=numpy.float64)
            assert self.joints.shape == (6, )
        self.circ_s = array.array('d', kwargs.get('circ_s', []))
        self.circ_end = array.array('d', kwargs.get('circ_end', []))
        self.jog_joint = kwargs.get('jog_joint', int())
        self.jog_dir = kwargs.get('jog_dir', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.do_timer != other.do_timer:
            return False
        if self.holding != other.holding:
            return False
        if self.cmd_mode != other.cmd_mode:
            return False
        if self.cmd_type != other.cmd_type:
            return False
        if self.velocity != other.velocity:
            return False
        if self.acceleration != other.acceleration:
            return False
        if self.tool != other.tool:
            return False
        if self.base != other.base:
            return False
        if self.base_num != other.base_num:
            return False
        if self.tool_num != other.tool_num:
            return False
        if self.digital_input_pin != other.digital_input_pin:
            return False
        if self.digital_output_pin != other.digital_output_pin:
            return False
        if self.digital_output_cmd != other.digital_output_cmd:
            return False
        if self.pose != other.pose:
            return False
        if all(self.joints != other.joints):
            return False
        if self.circ_s != other.circ_s:
            return False
        if self.circ_end != other.circ_end:
            return False
        if self.jog_joint != other.jog_joint:
            return False
        if self.jog_dir != other.jog_dir:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def do_timer(self):
        """Message field 'do_timer'."""
        return self._do_timer

    @do_timer.setter
    def do_timer(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'do_timer' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'do_timer' field must be an unsigned integer in [0, 255]"
        self._do_timer = value

    @builtins.property
    def holding(self):
        """Message field 'holding'."""
        return self._holding

    @holding.setter
    def holding(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'holding' field must be of type 'bool'"
        self._holding = value

    @builtins.property
    def cmd_mode(self):
        """Message field 'cmd_mode'."""
        return self._cmd_mode

    @cmd_mode.setter
    def cmd_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cmd_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'cmd_mode' field must be an unsigned integer in [0, 255]"
        self._cmd_mode = value

    @builtins.property
    def cmd_type(self):
        """Message field 'cmd_type'."""
        return self._cmd_type

    @cmd_type.setter
    def cmd_type(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cmd_type' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'cmd_type' field must be an unsigned integer in [0, 255]"
        self._cmd_type = value

    @builtins.property
    def velocity(self):
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'velocity' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'velocity' field must be an unsigned integer in [0, 255]"
        self._velocity = value

    @builtins.property
    def acceleration(self):
        """Message field 'acceleration'."""
        return self._acceleration

    @acceleration.setter
    def acceleration(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'acceleration' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'acceleration' field must be an unsigned integer in [0, 255]"
        self._acceleration = value

    @builtins.property
    def tool(self):
        """Message field 'tool'."""
        return self._tool

    @tool.setter
    def tool(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tool' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'tool' field must be an unsigned integer in [0, 255]"
        self._tool = value

    @builtins.property
    def base(self):
        """Message field 'base'."""
        return self._base

    @base.setter
    def base(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'base' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'base' field must be an unsigned integer in [0, 255]"
        self._base = value

    @builtins.property
    def base_num(self):
        """Message field 'base_num'."""
        return self._base_num

    @base_num.setter
    def base_num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'base_num' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'base_num' field must be an unsigned integer in [0, 255]"
        self._base_num = value

    @builtins.property
    def tool_num(self):
        """Message field 'tool_num'."""
        return self._tool_num

    @tool_num.setter
    def tool_num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tool_num' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'tool_num' field must be an unsigned integer in [0, 255]"
        self._tool_num = value

    @builtins.property
    def digital_input_pin(self):
        """Message field 'digital_input_pin'."""
        return self._digital_input_pin

    @digital_input_pin.setter
    def digital_input_pin(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'digital_input_pin' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'digital_input_pin' field must be an unsigned integer in [0, 255]"
        self._digital_input_pin = value

    @builtins.property
    def digital_output_pin(self):
        """Message field 'digital_output_pin'."""
        return self._digital_output_pin

    @digital_output_pin.setter
    def digital_output_pin(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'digital_output_pin' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'digital_output_pin' field must be an unsigned integer in [0, 255]"
        self._digital_output_pin = value

    @builtins.property
    def digital_output_cmd(self):
        """Message field 'digital_output_cmd'."""
        return self._digital_output_cmd

    @digital_output_cmd.setter
    def digital_output_cmd(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'digital_output_cmd' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'digital_output_cmd' field must be an unsigned integer in [0, 255]"
        self._digital_output_cmd = value

    @builtins.property
    def pose(self):
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value):
        if __debug__:
            from geometry_msgs.msg import Twist
            assert \
                isinstance(value, Twist), \
                "The 'pose' field must be a sub message of type 'Twist'"
        self._pose = value

    @builtins.property
    def joints(self):
        """Message field 'joints'."""
        return self._joints

    @joints.setter
    def joints(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.float64, \
                "The 'joints' numpy.ndarray() must have the dtype of 'numpy.float64'"
            assert value.size == 6, \
                "The 'joints' numpy.ndarray() must have a size of 6"
            self._joints = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 6 and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'joints' field must be a set or sequence with length 6 and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._joints = numpy.array(value, dtype=numpy.float64)

    @builtins.property
    def circ_s(self):
        """Message field 'circ_s'."""
        return self._circ_s

    @circ_s.setter
    def circ_s(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'circ_s' array.array() must have the type code of 'd'"
            self._circ_s = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'circ_s' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._circ_s = array.array('d', value)

    @builtins.property
    def circ_end(self):
        """Message field 'circ_end'."""
        return self._circ_end

    @circ_end.setter
    def circ_end(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'circ_end' array.array() must have the type code of 'd'"
            self._circ_end = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'circ_end' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._circ_end = array.array('d', value)

    @builtins.property
    def jog_joint(self):
        """Message field 'jog_joint'."""
        return self._jog_joint

    @jog_joint.setter
    def jog_joint(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'jog_joint' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'jog_joint' field must be an integer in [-128, 127]"
        self._jog_joint = value

    @builtins.property
    def jog_dir(self):
        """Message field 'jog_dir'."""
        return self._jog_dir

    @jog_dir.setter
    def jog_dir(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'jog_dir' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'jog_dir' field must be an integer in [-128, 127]"
        self._jog_dir = value


# Import statements for member types

# Member 'current_position'
# already imported above
# import array

# already imported above
# import builtins

# already imported above
# import math

# already imported above
# import rosidl_parser.definition


class Metaclass_RobotCommand_Response(type):
    """Metaclass of message 'RobotCommand_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
        'IDLE': 1,
        'RUNNING': 2,
        'HOLD': 3,
        'DELAY': 4,
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('hiwin_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'hiwin_interfaces.srv.RobotCommand_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__robot_command__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__robot_command__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__robot_command__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__robot_command__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__robot_command__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'IDLE': cls.__constants['IDLE'],
            'RUNNING': cls.__constants['RUNNING'],
            'HOLD': cls.__constants['HOLD'],
            'DELAY': cls.__constants['DELAY'],
        }

    @property
    def IDLE(self):
        """Message constant 'IDLE'."""
        return Metaclass_RobotCommand_Response.__constants['IDLE']

    @property
    def RUNNING(self):
        """Message constant 'RUNNING'."""
        return Metaclass_RobotCommand_Response.__constants['RUNNING']

    @property
    def HOLD(self):
        """Message constant 'HOLD'."""
        return Metaclass_RobotCommand_Response.__constants['HOLD']

    @property
    def DELAY(self):
        """Message constant 'DELAY'."""
        return Metaclass_RobotCommand_Response.__constants['DELAY']


class RobotCommand_Response(metaclass=Metaclass_RobotCommand_Response):
    """
    Message class 'RobotCommand_Response'.

    Constants:
      IDLE
      RUNNING
      HOLD
      DELAY
    """

    __slots__ = [
        '_arm_state',
        '_digital_state',
        '_current_position',
    ]

    _fields_and_field_types = {
        'arm_state': 'uint8',
        'digital_state': 'uint8',
        'current_position': 'sequence<double>',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.arm_state = kwargs.get('arm_state', int())
        self.digital_state = kwargs.get('digital_state', int())
        self.current_position = array.array('d', kwargs.get('current_position', []))

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.arm_state != other.arm_state:
            return False
        if self.digital_state != other.digital_state:
            return False
        if self.current_position != other.current_position:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def arm_state(self):
        """Message field 'arm_state'."""
        return self._arm_state

    @arm_state.setter
    def arm_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'arm_state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'arm_state' field must be an unsigned integer in [0, 255]"
        self._arm_state = value

    @builtins.property
    def digital_state(self):
        """Message field 'digital_state'."""
        return self._digital_state

    @digital_state.setter
    def digital_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'digital_state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'digital_state' field must be an unsigned integer in [0, 255]"
        self._digital_state = value

    @builtins.property
    def current_position(self):
        """Message field 'current_position'."""
        return self._current_position

    @current_position.setter
    def current_position(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'current_position' array.array() must have the type code of 'd'"
            self._current_position = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 all(isinstance(v, float) for v in value) and
                 all(not (val < -1.7976931348623157e+308 or val > 1.7976931348623157e+308) or math.isinf(val) for val in value)), \
                "The 'current_position' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._current_position = array.array('d', value)


class Metaclass_RobotCommand(type):
    """Metaclass of service 'RobotCommand'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('hiwin_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'hiwin_interfaces.srv.RobotCommand')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__robot_command

            from hiwin_interfaces.srv import _robot_command
            if _robot_command.Metaclass_RobotCommand_Request._TYPE_SUPPORT is None:
                _robot_command.Metaclass_RobotCommand_Request.__import_type_support__()
            if _robot_command.Metaclass_RobotCommand_Response._TYPE_SUPPORT is None:
                _robot_command.Metaclass_RobotCommand_Response.__import_type_support__()


class RobotCommand(metaclass=Metaclass_RobotCommand):
    from hiwin_interfaces.srv._robot_command import RobotCommand_Request as Request
    from hiwin_interfaces.srv._robot_command import RobotCommand_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')

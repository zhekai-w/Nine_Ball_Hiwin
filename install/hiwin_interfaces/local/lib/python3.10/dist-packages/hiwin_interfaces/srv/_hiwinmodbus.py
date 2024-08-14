# generated from rosidl_generator_py/resource/_idl.py.em
# with input from hiwin_interfaces:srv/Hiwinmodbus.idl
# generated code does not contain a copyright notice


# Import statements for member types

# Member 'pose'
# Member 'circ_s'
# Member 'circ_end'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Hiwinmodbus_Request(type):
    """Metaclass of message 'Hiwinmodbus_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
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
                'hiwin_interfaces.srv.Hiwinmodbus_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__hiwinmodbus__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__hiwinmodbus__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__hiwinmodbus__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__hiwinmodbus__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__hiwinmodbus__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Hiwinmodbus_Request(metaclass=Metaclass_Hiwinmodbus_Request):
    """Message class 'Hiwinmodbus_Request'."""

    __slots__ = [
        '_mode',
        '_holding',
        '_type',
        '_vel',
        '_acc',
        '_digital_output',
        '_onoff',
        '_pose',
        '_circ_s',
        '_circ_end',
        '_joint',
        '_dir',
    ]

    _fields_and_field_types = {
        'mode': 'string',
        'holding': 'boolean',
        'type': 'int32',
        'vel': 'int32',
        'acc': 'int32',
        'digital_output': 'int32',
        'onoff': 'int32',
        'pose': 'sequence<double>',
        'circ_s': 'sequence<double>',
        'circ_end': 'sequence<double>',
        'joint': 'int32',
        'dir': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('double')),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.mode = kwargs.get('mode', str())
        self.holding = kwargs.get('holding', bool())
        self.type = kwargs.get('type', int())
        self.vel = kwargs.get('vel', int())
        self.acc = kwargs.get('acc', int())
        self.digital_output = kwargs.get('digital_output', int())
        self.onoff = kwargs.get('onoff', int())
        self.pose = array.array('d', kwargs.get('pose', []))
        self.circ_s = array.array('d', kwargs.get('circ_s', []))
        self.circ_end = array.array('d', kwargs.get('circ_end', []))
        self.joint = kwargs.get('joint', int())
        self.dir = kwargs.get('dir', int())

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
        if self.mode != other.mode:
            return False
        if self.holding != other.holding:
            return False
        if self.type != other.type:
            return False
        if self.vel != other.vel:
            return False
        if self.acc != other.acc:
            return False
        if self.digital_output != other.digital_output:
            return False
        if self.onoff != other.onoff:
            return False
        if self.pose != other.pose:
            return False
        if self.circ_s != other.circ_s:
            return False
        if self.circ_end != other.circ_end:
            return False
        if self.joint != other.joint:
            return False
        if self.dir != other.dir:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def mode(self):
        """Message field 'mode'."""
        return self._mode

    @mode.setter
    def mode(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'mode' field must be of type 'str'"
        self._mode = value

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

    @builtins.property  # noqa: A003
    def type(self):  # noqa: A003
        """Message field 'type'."""
        return self._type

    @type.setter  # noqa: A003
    def type(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'type' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'type' field must be an integer in [-2147483648, 2147483647]"
        self._type = value

    @builtins.property
    def vel(self):
        """Message field 'vel'."""
        return self._vel

    @vel.setter
    def vel(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'vel' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'vel' field must be an integer in [-2147483648, 2147483647]"
        self._vel = value

    @builtins.property
    def acc(self):
        """Message field 'acc'."""
        return self._acc

    @acc.setter
    def acc(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'acc' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'acc' field must be an integer in [-2147483648, 2147483647]"
        self._acc = value

    @builtins.property
    def digital_output(self):
        """Message field 'digital_output'."""
        return self._digital_output

    @digital_output.setter
    def digital_output(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'digital_output' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'digital_output' field must be an integer in [-2147483648, 2147483647]"
        self._digital_output = value

    @builtins.property
    def onoff(self):
        """Message field 'onoff'."""
        return self._onoff

    @onoff.setter
    def onoff(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'onoff' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'onoff' field must be an integer in [-2147483648, 2147483647]"
        self._onoff = value

    @builtins.property
    def pose(self):
        """Message field 'pose'."""
        return self._pose

    @pose.setter
    def pose(self, value):
        if isinstance(value, array.array):
            assert value.typecode == 'd', \
                "The 'pose' array.array() must have the type code of 'd'"
            self._pose = value
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
                "The 'pose' field must be a set or sequence and each value of type 'float' and each double in [-179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000, 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368.000000]"
        self._pose = array.array('d', value)

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
    def joint(self):
        """Message field 'joint'."""
        return self._joint

    @joint.setter
    def joint(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'joint' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'joint' field must be an integer in [-2147483648, 2147483647]"
        self._joint = value

    @builtins.property  # noqa: A003
    def dir(self):  # noqa: A003
        """Message field 'dir'."""
        return self._dir

    @dir.setter  # noqa: A003
    def dir(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dir' field must be of type 'int'"
            assert value >= -2147483648 and value < 2147483648, \
                "The 'dir' field must be an integer in [-2147483648, 2147483647]"
        self._dir = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_Hiwinmodbus_Response(type):
    """Metaclass of message 'Hiwinmodbus_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
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
                'hiwin_interfaces.srv.Hiwinmodbus_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__hiwinmodbus__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__hiwinmodbus__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__hiwinmodbus__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__hiwinmodbus__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__hiwinmodbus__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Hiwinmodbus_Response(metaclass=Metaclass_Hiwinmodbus_Response):
    """Message class 'Hiwinmodbus_Response'."""

    __slots__ = [
        '_arm_state',
    ]

    _fields_and_field_types = {
        'arm_state': 'int32',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int32'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.arm_state = kwargs.get('arm_state', int())

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
            assert value >= -2147483648 and value < 2147483648, \
                "The 'arm_state' field must be an integer in [-2147483648, 2147483647]"
        self._arm_state = value


class Metaclass_Hiwinmodbus(type):
    """Metaclass of service 'Hiwinmodbus'."""

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
                'hiwin_interfaces.srv.Hiwinmodbus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__hiwinmodbus

            from hiwin_interfaces.srv import _hiwinmodbus
            if _hiwinmodbus.Metaclass_Hiwinmodbus_Request._TYPE_SUPPORT is None:
                _hiwinmodbus.Metaclass_Hiwinmodbus_Request.__import_type_support__()
            if _hiwinmodbus.Metaclass_Hiwinmodbus_Response._TYPE_SUPPORT is None:
                _hiwinmodbus.Metaclass_Hiwinmodbus_Response.__import_type_support__()


class Hiwinmodbus(metaclass=Metaclass_Hiwinmodbus):
    from hiwin_interfaces.srv._hiwinmodbus import Hiwinmodbus_Request as Request
    from hiwin_interfaces.srv._hiwinmodbus import Hiwinmodbus_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')

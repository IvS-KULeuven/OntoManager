# === imports ===

import tc2_mc2


# This file (mtcs_common.py) was automatically generated at 2017-02-06T17:06:09.671415 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class InitializationStates:
        SHUTDOWN = 0
        INITIALIZING = 1
        INITIALIZING_FAILED = 2
        INITIALIZED = 3
        LOCKED = 4

class OperatorStates:
        NONE = 0
        OBSERVER = 1
        TECH = 2

class OperatingStates:
        AUTO = 0
        MANUAL = 1

class LimitSwitches:
        POSITIVE_LIMIT_SWITCH = 0
        NEGATIVE_LIMIT_SWITCH = 1

class Units:
        DEGREE = 0
        RADIAN = 1
        PERCENT = 2
        RADIANS_PER_SECOND = 3
        DEGREES_PER_SECOND = 4
        MILLIMETERS_PER_SECOND = 5
        REVOLUTIONS_PER_SECOND = 6
        REVOLUTIONS_PER_MINUTE = 7
        AMPS = 8
        MILLIAMPS = 9
        MILLIMETER = 10
        MICROMETER = 11
        DEGREES_CELSIUS = 12
        KELVIN = 13
        BAR = 14
        PASCAL = 15
        UNITLESS = 16
        NEWTON = 17
        DECANEWTON = 18
        VOLT = 19
        MILLIVOLT = 20
        HERTZ = 21
        G = 22
        MILLIG = 23
        NEWTONMETER = 24
        ARCSECONDS = 25
        ARCSECONDS_PER_SECOND = 26
        RADIANS_PER_SQUARE_SECOND = 27
        DEGREES_PER_SQUARE_SECOND = 28
        ARCSECONDS_PER_SQUARE_SECOND = 29
        METERS_PER_SECOND = 30
        HECTOPASCAL = 31
        SECONDS = 32
        MINUTES = 33
        MILLIMETERS_PER_HOUR = 34
        HITS_PER_SQUARE_CENTIMETER = 35
        HITS_PER_SQUARE_CENTIMETER_PER_HOUR = 36

class RequestResults:
        ACCEPTED = 0
        REJECTED = 1

class DriveOperatingModes:
        OPERATING_MODE_NONE = 0
        OPERATING_MODE_TORQUE_CONTROL = 1
        OPERATING_MODE_VELOCITY_CONTROL = 2
        OPERATING_MODE_POSITION_CONTROL = 3

class DriveBrakeStates:
        BRAKE_AUTOMATIC = 0
        BRAKE_FORCE_LOCK = 1
        BRAKE_FORCE_UNLOCK = 2


# === STRUCTS ===

class AX52XXDriveParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("channelA", ns, AX52XXDriveChannel, 'Channel A')
        self.__addInstance__("channelB", ns, AX52XXDriveChannel, 'Channel B')

class BaseAxisProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("moveAbsolute", ns, McMoveAbsoluteProcess, 'Move absolute')
        self.__addInstance__("moveRelative", ns, McMoveRelativeProcess, 'Move relative')
        self.__addInstance__("moveVelocity", ns, McMoveVelocityProcess, 'Move at a constant velocity')
        self.__addInstance__("reset", ns, McProcess, 'Reset any errors')
        self.__addInstance__("stop", ns, McProcess, 'Stop any movement')
        self.__addInstance__("stopParametrized", ns, McStopProcess, 'Stop any movement')
        self.__addInstance__("power", ns, McPowerProcess, 'Power on/off the axis')
        self.__addInstance__("gearIn", ns, McProcess, 'Couple to master axis')
        self.__addInstance__("gearOut", ns, McProcess, 'Decouple from master axis')
        self.__addInstance__("initialize", ns, Process, 'Start initializing the axis')
        self.__addInstance__("setPosition", ns, McSetPositionProcess, 'Set the axis position')
        self.__addInstance__("enableExtSetGen", ns, McProcess, 'Enable the external setpoint generator')
        self.__addInstance__("disableExtSetGen", ns, McProcess, 'Disable the external setpoint generator')
        self.__addInstance__("forceCalibration", ns, McProcess, 'Force the calibration (homing) flag to TRUE')
        self.__addInstance__("resetCalibration", ns, McProcess, 'Reset the calibration (homing) flag to FALSE')
        self.__addInstance__("readParameter", ns, McReadParameter, 'Read a numerical parameter')
        self.__addInstance__("readBoolParameter", ns, McReadBoolParameter, 'Read a boolean parameter')
        self.__addInstance__("writeParameter", ns, McWriteParameter, 'Write a numerical parameter')
        self.__addInstance__("writeBoolParameter", ns, McWriteBoolParameter, 'Write a boolean parameter')

class FaulhaberDriveProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("write", ns, SDOWriteProcess, 'Write a number of bytes to the drive')
        self.__addInstance__("read", ns, SDOReadProcess, 'Read a number of bytes from the drive')
        self.__addInstance__("initialize", ns, Process, 'Initialize the drive according to the config')

class AX52XXDriveChannelProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("read", ns, SoEReadProcess, 'Read a number of bytes from the drive')
        self.__addInstance__("write", ns, SoEWriteProcess, 'Write a number of bytes to the drive')
        self.__addInstance__("update", ns, Process, 'Update the actual values')
        self.__addInstance__("reset", ns, SoEResetProcess, 'Reset the drive channel')
        self.__addInstance__("acknowledgeSafetyError", ns, Process, 'Acknowledge the safety card error state')
        self.__addInstance__("setBrake", ns, SetBrakeProcess, 'Update the actual values')

class IncrementalEncoderProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enableCounterResetC", ns, Process, 'Enable the counter reset on the C pulse')
        self.__addInstance__("disableCounterResetC", ns, Process, 'Disable the counter reset on the C pulse')

class SimpleRelayProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("setEnabled", ns, SetEnabledProcess, 'Set the relay enabled or disabled')

class ConfigManagerProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("save", ns, WriteXmlProcess, 'Save the currently active config to disk')
        self.__addInstance__("load", ns, ReadXmlProcess, 'Load the config from disk')
        self.__addInstance__("activate", ns, ActivateProcess, 'Activate the loaded config')

class BaseProcessStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the process enabled or not?')
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the process busy or not?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the process in a healthy state or not?')
        self.__addInstance__("startedStatus", ns, StartedStatus, 'Is the process started or not?')

class ProcessStepStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the process step enabled or not?')

class BaseAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the NcAxis in a busy state?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the NcAxis in a healthy state?')
        self.__addInstance__("poweredStatus", ns, PoweredStatus, 'Is the NcAxis powered?')
        self.__addInstance__("extSetGenStatus", ns, EnabledStatus, 'Is the NcAxis its external setpoint generator enabled?')
        self.__addInstance__("motionStatus", ns, MotionStatus, 'Is the NcAxis moving forward or backward or standing still?')

class FaulhaberDriveStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the NcAxis in a busy state?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the NcAxis in a healthy state?')

class AX52XXDriveChannelStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the drive in a busy state?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the drive in a healthy state?')

class AX52XXDriveStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the drive in a busy state?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the drive in a healthy state?')

class SSIEncoderStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the device in a healthy state?')

class IncrementalEncoderStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the device in a healthy state?')
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the device in a busy state?')

class EtherCatDeviceStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the device in a healthy state?')

class CANopenBusStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the device in a healthy state?')

class CurrentMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement valid?')

class VoltageMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the voltage being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class TemperatureMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the temperature being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class PressureMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the pressure being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class FrequencyMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the frequency being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class GForceMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')

class RelativeHumidityMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the relative humidity being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class ForceMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the force being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class LinearPositionMeasurement16Statuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the position being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class LinearPositionMeasurementU32Statuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, EnabledStatus, 'Is the position being measured?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the measurement OK?')
        self.__addInstance__("alarmStatus", ns, HiHiLoLoAlarmStatus, 'Alarm status')

class SimpleRelayStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the SimpleRelay in a busy state?')

class ConfigManagerStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, BusyStatus, 'Is the config manager in a busy state?')
        self.__addInstance__("healthStatus", ns, HealthStatus, 'Is the config manager in a healthy state?')

class HiHiLoLoAlarmConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("enabled", ns, 'Is the alarm enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("loLo", ns, 'LowLow alarm limit (produces ERROR)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("lo", ns, 'Low alarm limit (produces WARNING)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("hi", ns, 'High alarm limit (produces WARNING)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("hiHi", ns, 'HighHigh alarm limit (produces ERROR)', datatype=pyuaf.util.primitives.Double, permissions='')

class MeasurementConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("enabled", ns, 'Is the quantity being measured? (Can be false e.g. if the sensor is deliberately not connected (yet).)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("offset", ns, 'Offset to be added to the measured value (default: 0 = no offset)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("alarms", ns, HiHiLoLoAlarmConfig, 'Config')

class FaulhaberDriveConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("sendAtInitialization", ns, 'Send the complete config to the drive during initialization', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("CANopenBusNetId", ns, 'The CANopen bus NetId, as configured via TwinCAT, e.g. &#39;172.16.2.131.2.1&#39;', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("CANopenNodePort", ns, 'The CANopen node port number, as configured via TwinCAT, e.g. 1005', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("modesOfOperation", ns, '0x6060.0: Operating mode changeover', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("polarity", ns, '0x607E.0: Direction of rotation', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("maxProfileVelocity", ns, '0x607F.0: Maximum velocity, in rpm', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("negativeLimitSwitch", ns, '0x2310.1: Lower limit switch configuration', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("positiveLimitSwitch", ns, '0x2310.2: Upper limit switch configuration', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("homingSwitch", ns, '0x2310.3: Homing switch configuration', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("limitSwitchPolarity", ns, '0x2310.5: Limit switch positive edge', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("continuousCurrentLimit", ns, '0x2333.1: Continuous current limit, in milliamps', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("peakCurrentLimit", ns, '0x2333.2: Peak current limit, in milliamps', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("velocityControlProportionalTerm", ns, '0x2331.1: Proportional term (gain) of the velocity control mode', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("velocityControlIntegralTerm", ns, '0x2331.2: Integral term (gain) of the velocity control mode', datatype=pyuaf.util.primitives.Int16, permissions='')

class InstrumentConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the instrument', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("doInitialThermalFocus", ns, 'Do a thermal focus when changing to this instrument', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("changeM3", ns, 'Change M3 to the focal station with the same name as the instrument', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("moveKnownPosition", ns, 'Move the axes to a known position (defined by the &#39;moveKnownPositionName&#39; config entry) before turning off derotators', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("moveKnownPositionName", ns, 'Name of the known position to move to before turning off derotators', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("powerOnRoc", ns, 'Turn on the Cassegrain derotator if needed', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("powerOffRoc", ns, 'Turn off the Cassegrain derotator if needed', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("powerOnRon", ns, 'Turn on the Nasmyth B derotator if needed', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("powerOffRon", ns, 'Turn off the Nasmyth B derotator if needed', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("loadPointingModel", ns, 'Load the pointing model with the same name as the instrument', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("rocActive", ns, 'True if the Cassegrain rotator is active (irrespective of its power status).', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("ronActive", ns, 'True if the Nasmyth rotator is active (irrespective of its power status)', datatype=pyuaf.util.primitives.Boolean, permissions='')

class ChangeSetpointProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("setpoint", ns, 'New setpoint value', datatype=pyuaf.util.primitives.Double, permissions='')

class McMoveAbsoluteProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("position", ns, 'New position setpoint', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxVelocity", ns, 'Maximum velocity', datatype=pyuaf.util.primitives.Double, permissions='')

class McMoveRelativeProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("distance", ns, 'Distance to move', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxVelocity", ns, 'Maximum velocity', datatype=pyuaf.util.primitives.Double, permissions='')

class McPowerProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("enable", ns, 'Enable the power or not', datatype=pyuaf.util.primitives.Boolean, permissions='')

class McSetPositionProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("value", ns, 'New position to be taken over by the encoder', datatype=pyuaf.util.primitives.Double, permissions='')

class McStopProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("deceleration", ns, 'Deceleration (use 0 for default). If non zero, then also jerk must be non zero!', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("jerk", ns, 'Jerk (use 0 for default). If non zero, then also deceleration must be non zero!', datatype=pyuaf.util.primitives.Double, permissions='')

class McMoveVelocityProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("value", ns, 'New velocity', datatype=pyuaf.util.primitives.Double, permissions='')

class SetEnabledProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("enabled", ns, 'True to enable, false to disable', datatype=pyuaf.util.primitives.Boolean, permissions='')

class McWriteParameterArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("parameterNumber", ns, 'Number of the parameter', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("value", ns, 'Value to write', datatype=pyuaf.util.primitives.Double, permissions='')

class McReadParameterArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("parameterNumber", ns, 'Number of the parameter', datatype=pyuaf.util.primitives.UInt16, permissions='')

class McWriteBoolParameterArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("parameterNumber", ns, 'Number of the parameter', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("value", ns, 'Value to write', datatype=pyuaf.util.primitives.Boolean, permissions='')

class McReadBoolParameterArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("parameterNumber", ns, 'Number of the parameter', datatype=pyuaf.util.primitives.UInt16, permissions='')

class SDOReadProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("index", ns, 'SDO Index', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("subindex", ns, 'SDO SubIndex', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("noOfBytes", ns, 'Number of bytes to be read', datatype=pyuaf.util.primitives.Int32, permissions='')

class SDOWriteProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("index", ns, 'SDO Index', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("subindex", ns, 'SDO SubIndex', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("noOfBytes", ns, 'Number of bytes to be written', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("value1Byte", ns, 'Value to be written if noOfBytes is 1', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("value2Bytes", ns, 'Value to be written if noOfBytes is 2', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("value4Bytes", ns, 'Value to be written if noOfBytes is 4', datatype=pyuaf.util.primitives.Int32, permissions='')

class SoEReadProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("index", ns, 'SDO Index', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("noOfBytes", ns, 'Number of bytes to be read', datatype=pyuaf.util.primitives.Int32, permissions='')

class SoEWriteProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("index", ns, 'SDO Index', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("noOfBytes", ns, 'Number of bytes to be written', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("value1Byte", ns, 'Value to be written if noOfBytes is 1', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("value2Bytes", ns, 'Value to be written if noOfBytes is 2', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("value4Bytes", ns, 'Value to be written if noOfBytes is 4', datatype=pyuaf.util.primitives.Int32, permissions='')

class SetBrakeProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newState", ns, 'Requested brake state', datatype=DriveBrakeStates, permissions='')

class ChangeOperatingStateProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New operating state (e.g. AUTO, MANUAL)', datatype=OperatingStates, permissions='')

class ChangeOperatorStateProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New operator state (e.g. OBSERVER, TECH, ...)', datatype=OperatorStates, permissions='')
        self.__addVariable__("password", ns, 'Password (only sometimes required, e.g. to go from OBSERVER to TECH)', datatype=pyuaf.util.primitives.String, permissions='')

class ReadXmlProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("filePath", ns, 'Full path of the filename to read', datatype=pyuaf.util.primitives.String, permissions='')

class WriteXmlProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("filePath", ns, 'Full path of the filename to write', datatype=pyuaf.util.primitives.String, permissions='')


# === FBs ===

class ApertureStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isOpen", ns, 'TRUE if the &#39;open&#39; limit switch is active', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isClosed", ns, 'TRUE if the &#39;open&#39; limit switch is active', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("open", ns, 'The aperture is open', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("closed", ns, 'The aperture is closed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("partiallyOpen", ns, 'The aperture is partially open', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("undefined", ns, 'The aperture status is undefined', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class BusyStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isBusy", ns, 'TRUE if busy', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("idle", ns, 'The subject is idle', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("busy", ns, 'The subject is busy', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class StartedStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isStarted", ns, 'TRUE if started', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("started", ns, 'The subject is started', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("notStarted", ns, 'The subject is started', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class EnabledStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isEnabled", ns, 'TRUE if enabled', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("enabled", ns, 'The subject is enabled', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("disabled", ns, 'The subject is disabled', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class PoweredStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isEnabled", ns, 'TRUE if power is enabled', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("enabled", ns, 'The power is enabled', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("disabled", ns, 'The power is disabled', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class HealthStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isGood", ns, 'TRUE if the subject is in Good health', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("hasWarning", ns, 'TRUE to add a warning to the Good health state', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("good", ns, 'The subject is in Good health', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("warning", ns, 'The subject is in Good health, but there are one or more warnings present', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bad", ns, 'The subject is in Bad health', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class InitializationStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("state", ns, 'Enum!', datatype=InitializationStates, permissions='')
        self.__addVariable__("shutdown", ns, 'Shutdown', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("initializing", ns, 'Initializing', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("initializingFailed", ns, 'Initializing failed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("initialized", ns, 'Initialized', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("locked", ns, 'Locked', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class MotionStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actVel", ns, 'Actual velocity', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("tolerance", ns, 'Tolerance (should be positive)!', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("forward", ns, 'Moving forwared', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("backward", ns, 'Moving backward', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("standstill", ns, 'Standing still', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class HiHiLoLoAlarmStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addInstance__("config", ns, HiHiLoLoAlarmConfig, 'Config')
        self.__addVariable__("value", ns, 'Value in the correct units to compare to the values from the config', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("disabled", ns, 'The alarm is disabled', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("hiHi", ns, 'HighHigh limit active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("hi", ns, 'High limit active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("ok", ns, 'The value is within normal range', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("lo", ns, 'Low limit active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("loLo", ns, 'LowLow limit active', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class OpeningStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isOpening", ns, 'TRUE if opening', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isClosing", ns, 'TRUE if closing', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("opening", ns, 'Opening', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("closing", ns, 'Closing', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("standstill", ns, 'Standing still', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class OperatorStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("state", ns, 'Enum!', datatype=OperatorStates, permissions='')
        self.__addVariable__("none", ns, 'None', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("tech", ns, 'Tech', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("observer", ns, 'Observer', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class OperatingStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("state", ns, 'Enum!', datatype=OperatingStates, permissions='')
        self.__addVariable__("auto", ns, 'Auto', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("manual", ns, 'Manual', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class ActivityStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isMoving", ns, 'TRUE if moving', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isAwake", ns, 'TRUE if awake', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("moving", ns, 'Opening', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("awake", ns, 'Opening', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("sleeping", ns, 'Opening', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class SM_QuantityValue(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("value", ns, 'Numeric value', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addVariable__("unit", ns, 'Unit of the numeric value', datatype=Units, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')

class QuantityValue(SM_QuantityValue):
    def __init__(self, parent, name, ns, info):
        SM_QuantityValue.__init__(self, parent, name, ns, info)

class SM_AngularPosition(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newDegreesValue", ns, 'New position value in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("radians", ns, QuantityValue, 'Angular position in radians')
        self.__addInstance__("degrees", ns, QuantityValue, 'Angular position in degrees')
        self.__addInstance__("arcseconds", ns, QuantityValue, 'Angular position in arcseconds')

class AngularPosition(SM_AngularPosition):
    def __init__(self, parent, name, ns, info):
        SM_AngularPosition.__init__(self, parent, name, ns, info)

class SM_LinearPosition(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newMillimetersValue", ns, 'New position value in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("millimeters", ns, QuantityValue, 'Linear position in millimeters')
        self.__addInstance__("micrometers", ns, QuantityValue, 'Linear position in micrometers')

class LinearPosition(SM_LinearPosition):
    def __init__(self, parent, name, ns, info):
        SM_LinearPosition.__init__(self, parent, name, ns, info)

class SM_AngularVelocity(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newDegreesPerSecondValue", ns, 'New velocity value in degrees per second', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("radiansPerSecond", ns, QuantityValue, 'Angular velocity in radians per second')
        self.__addInstance__("degreesPerSecond", ns, QuantityValue, 'Angular velocity in degrees per second')
        self.__addInstance__("arcsecondsPerSecond", ns, QuantityValue, 'Angular velocity in arcseconds per second')

class AngularVelocity(SM_AngularVelocity):
    def __init__(self, parent, name, ns, info):
        SM_AngularVelocity.__init__(self, parent, name, ns, info)

class SM_AngularAcceleration(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newDegreesPerSquareSecondValue", ns, 'New velocity value in degrees per second^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("radiansPerSquareSecond", ns, QuantityValue, 'Angular velocity in radians per second^2')
        self.__addInstance__("degreesPerSquareSecond", ns, QuantityValue, 'Angular velocity in degrees per second^2')
        self.__addInstance__("arcsecondsPerSquareSecond", ns, QuantityValue, 'Angular velocity in arcseconds per second^2')

class AngularAcceleration(SM_AngularAcceleration):
    def __init__(self, parent, name, ns, info):
        SM_AngularAcceleration.__init__(self, parent, name, ns, info)

class SM_LinearVelocity(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newMillimetersPerSecondValue", ns, 'New velocity value in millimeters per second', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("millimetersPerSecond", ns, QuantityValue, 'Linear velocity in millimeters per second')

class LinearVelocity(SM_LinearVelocity):
    def __init__(self, parent, name, ns, info):
        SM_LinearVelocity.__init__(self, parent, name, ns, info)

class SM_Voltage(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newVoltValue", ns, 'New voltage', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("volt", ns, QuantityValue, 'Voltage in Volt')
        self.__addInstance__("milliVolt", ns, QuantityValue, 'Voltage in millivolt')

class Voltage(SM_Voltage):
    def __init__(self, parent, name, ns, info):
        SM_Voltage.__init__(self, parent, name, ns, info)

class SM_GForce(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newMilliGValue", ns, 'New milliG value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("g", ns, QuantityValue, 'Acceleration in g units')
        self.__addInstance__("milliG", ns, QuantityValue, 'Acceleration in in milli g units')

class GForce(SM_GForce):
    def __init__(self, parent, name, ns, info):
        SM_GForce.__init__(self, parent, name, ns, info)

class SM_Current(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newAmpsValue", ns, 'New current in amps', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("amps", ns, QuantityValue, 'Current in amps')
        self.__addInstance__("milliAmps", ns, QuantityValue, 'Current in milliamps')

class Current(SM_Current):
    def __init__(self, parent, name, ns, info):
        SM_Current.__init__(self, parent, name, ns, info)

class SM_Torque(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newNewtonmeterValue", ns, 'New torque in Nm', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("newtonmeter", ns, QuantityValue, 'Torque in Nm')

class Torque(SM_Torque):
    def __init__(self, parent, name, ns, info):
        SM_Torque.__init__(self, parent, name, ns, info)

class SM_TorqueLimit(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newFractionValue", ns, 'New torque limit as a unitless fraction (between 0 and 1)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxNewtonmeter", ns, 'Newtonmeters corresponding to 100 percent (fraction=1)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("unitless", ns, QuantityValue, 'Torque limit as a unitless fraction')
        self.__addInstance__("percent", ns, QuantityValue, 'Torque limit in percent')
        self.__addInstance__("newtonmeter", ns, QuantityValue, 'Torque in Nm')

class TorqueLimit(SM_TorqueLimit):
    def __init__(self, parent, name, ns, info):
        SM_TorqueLimit.__init__(self, parent, name, ns, info)

class SM_AverageCurrent(Current):

    def __init__(self, parent, name, ns, info):
        Current.__init__(self, parent, name, ns, info)

class AverageCurrent(SM_AverageCurrent):
    def __init__(self, parent, name, ns, info):
        SM_AverageCurrent.__init__(self, parent, name, ns, info)

class SM_Duration(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newSecondsValue", ns, 'New duration in seconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("seconds", ns, QuantityValue, 'Duration in seconds')
        self.__addInstance__("minutes", ns, QuantityValue, 'Duration in minutes')

class Duration(SM_Duration):
    def __init__(self, parent, name, ns, info):
        SM_Duration.__init__(self, parent, name, ns, info)

class SM_Temperature(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newCelsiusValue", ns, 'New temperature in degrees Celsius', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("celsius", ns, QuantityValue, 'Temperature in degrees Celsius')
        self.__addInstance__("kelvin", ns, QuantityValue, 'Temperature in Kelvin')

class Temperature(SM_Temperature):
    def __init__(self, parent, name, ns, info):
        SM_Temperature.__init__(self, parent, name, ns, info)

class SM_Pressure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newBarValue", ns, 'New pressure in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("bar", ns, QuantityValue, 'Pressure in Bar')
        self.__addInstance__("pascal", ns, QuantityValue, 'Pressure in Pascal')
        self.__addInstance__("hectoPascal", ns, QuantityValue, 'Pressure in HectoPascal')

class Pressure(SM_Pressure):
    def __init__(self, parent, name, ns, info):
        SM_Pressure.__init__(self, parent, name, ns, info)

class SM_Frequency(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newHertzValue", ns, 'New frequency in Hz', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("hertz", ns, QuantityValue, 'Frequency in Hertz')

class Frequency(SM_Frequency):
    def __init__(self, parent, name, ns, info):
        SM_Frequency.__init__(self, parent, name, ns, info)

class SM_Force(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newNewtonValue", ns, 'New force in Newton', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("newton", ns, QuantityValue, 'Force in Newton')
        self.__addInstance__("decaNewton", ns, QuantityValue, 'Force in decaNewton')

class Force(SM_Force):
    def __init__(self, parent, name, ns, info):
        SM_Force.__init__(self, parent, name, ns, info)

class SM_Fraction(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("newFractionValue", ns, 'New fraction (between 0 and 1)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("unitless", ns, QuantityValue, 'Fraction as a unitless value between 0 and 1')
        self.__addInstance__("percent", ns, QuantityValue, 'Fraction as a percentage value between 0 and 100')

class Fraction(SM_Fraction):
    def __init__(self, parent, name, ns, info):
        SM_Fraction.__init__(self, parent, name, ns, info)

class SM_BaseProcess(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Should the trigger be enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, BaseProcessStatuses, 'Statuses of the state machine')
        self.__addVariable__("do_request", ns, 'Write TRUE to request the start of the process', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("do_request_result", ns, 'Result of the request', datatype=RequestResults, permissions='')

class BaseProcess(SM_BaseProcess):
    def __init__(self, parent, name, ns, info):
        SM_BaseProcess.__init__(self, parent, name, ns, info)

class SM_BaseMcProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("errorId", ns, 'Error ID according to Beckhoff/PlcOpen Motion Control', datatype=pyuaf.util.primitives.Int32, permissions='r')

class BaseMcProcess(SM_BaseMcProcess):
    def __init__(self, parent, name, ns, info):
        SM_BaseMcProcess.__init__(self, parent, name, ns, info)

class SM_ProcessStep(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is the step enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, ProcessStepStatuses, 'Statuses of the state machine')

class ProcessStep(SM_ProcessStep):
    def __init__(self, parent, name, ns, info):
        SM_ProcessStep.__init__(self, parent, name, ns, info)

class SM_BaseXmlDataSrvProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("errorId", ns, 'Error ID according to Beckhoff XML Data Server library', datatype=pyuaf.util.primitives.Int32, permissions='r')

class BaseXmlDataSrvProcess(SM_BaseXmlDataSrvProcess):
    def __init__(self, parent, name, ns, info):
        SM_BaseXmlDataSrvProcess.__init__(self, parent, name, ns, info)

class SM_BaseAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("axis_ref", ns, tc2_mc2.AXIS_REF, 'The AXIS_REF to be linked to the NC I/O')
        self.__addVariable__("isGearingSupported", ns, 'Is gearIn/gearOut supported?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("standstillTolerance", ns, 'Tolerance in [main units] per second: if &lt; ABS(this value), then the axis is considered to be standing still', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("isJogEnabled", ns, 'True if jog is enabled', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, BaseAxisStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, BaseAxisProcesses, 'Processes of the state machine')

class BaseAxis(SM_BaseAxis):
    def __init__(self, parent, name, ns, info):
        SM_BaseAxis.__init__(self, parent, name, ns, info)

class SM_AngularAxis(BaseAxis):

    def __init__(self, parent, name, ns, info):
        BaseAxis.__init__(self, parent, name, ns, info)
        self.__addInstance__("actPos", ns, AngularPosition, 'Actual position of the axis')
        self.__addInstance__("actVel", ns, AngularVelocity, 'Actual velocity of the axis')

class AngularAxis(SM_AngularAxis):
    def __init__(self, parent, name, ns, info):
        SM_AngularAxis.__init__(self, parent, name, ns, info)

class SM_LinearAxis(BaseAxis):

    def __init__(self, parent, name, ns, info):
        BaseAxis.__init__(self, parent, name, ns, info)
        self.__addInstance__("actPos", ns, LinearPosition, 'Actual position of the axis')
        self.__addInstance__("actVel", ns, LinearVelocity, 'Actual velocity of the axis')

class LinearAxis(SM_LinearAxis):
    def __init__(self, parent, name, ns, info):
        SM_LinearAxis.__init__(self, parent, name, ns, info)

class SM_FaulhaberDrive(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("config", ns, FaulhaberDriveConfig, 'Faulhaber drive config')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("newMilliampsValue", ns, 'Current in milliamps, linked to PDO', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actualCurrent", ns, Current, 'Actual current')
        self.__addInstance__("averageCurrent", ns, AverageCurrent, 'Average current')
        self.__addInstance__("statuses", ns, FaulhaberDriveStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, FaulhaberDriveProcesses, 'Processes of the state machine')

class FaulhaberDrive(SM_FaulhaberDrive):
    def __init__(self, parent, name, ns, info):
        SM_FaulhaberDrive.__init__(self, parent, name, ns, info)

class SM_AX52XXDriveChannel(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("errorC1D", ns, 'Class 1 Diagnostic (C1D', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("torqueFeedbackValue", ns, 'Torque feedback, cyclically updated by the drive channel', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("torqueCommandValue", ns, 'Torque command (only in case of torque control!)', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("digitalInputs", ns, 'Digital inputs (e.g. bit 0 = 1 if input 0 = high), cyclically updated by the drive channel', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("digitalOutputs", ns, 'Digital outputs (e.g. bit 0 = 1 if input 0 = high), cyclically updated by the drive channel', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("safetyOptionState", ns, 'Safety option state (P-0-2002)', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("diagnosticNumber", ns, 'Diagnostic number', datatype=pyuaf.util.primitives.Int32, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("isInSafetate", ns, 'True if the drive is in safe state', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("actualTorqueFeedback", ns, Torque, 'The actual torque feedback value (updated constantly!)')
        self.__addInstance__("channelPeakCurrent", ns, Current, 'The configured channel peak current')
        self.__addInstance__("channelRatedCurrent", ns, Current, 'The configured channel peak current')
        self.__addInstance__("continuousStallTorque", ns, Torque, 'The motor continuous stall torque')
        self.__addInstance__("continuousStallCurrent", ns, Current, 'The motor continuous stall current')
        self.__addVariable__("torqueConstant", ns, 'The motor torque constant, in Nm/A', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addInstance__("bipolarTorqueLimit", ns, TorqueLimit, 'The drive bipolar torque limit')
        self.__addInstance__("positiveTorqueLimit", ns, TorqueLimit, 'The drive positive torque limit')
        self.__addInstance__("negativeTorqueLimit", ns, TorqueLimit, 'The drive negative torque limit')
        self.__addVariable__("operatingMode", ns, 'The drive operating mode, as an ENUM value', datatype=DriveOperatingModes, permissions='r')
        self.__addVariable__("operatingModeDescription", ns, 'The drive operating mode, as a descriptive text', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("brakeState", ns, 'The drive brake state, as an ENUM value', datatype=DriveBrakeStates, permissions='r')
        self.__addVariable__("brakeStateDescription", ns, 'The drive brake state, as a descriptive text', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("torqueCommand", ns, TorqueLimit, 'The torque command (only in case of torque control!)')
        self.__addVariable__("safetyErrorAck", ns, 'Error acknowledge of AX5805 safety card', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, AX52XXDriveChannelStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, AX52XXDriveChannelProcesses, 'Processes of the state machine')

class AX52XXDriveChannel(SM_AX52XXDriveChannel):
    def __init__(self, parent, name, ns, info):
        SM_AX52XXDriveChannel.__init__(self, parent, name, ns, info)

class SM_AX52XXDrive(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, AX52XXDriveStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AX52XXDriveParts, 'Parts of the state machine')

class AX52XXDrive(SM_AX52XXDrive):
    def __init__(self, parent, name, ns, info):
        SM_AX52XXDrive.__init__(self, parent, name, ns, info)

class SM_SSIEncoder(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("counterValue", ns, 'Counter value', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("status", ns, 'Status', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("dataError", ns, 'Data error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("frameError", ns, 'Frame error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powerFailure", ns, 'Power failure', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("syncError", ns, 'Sync error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, SSIEncoderStatuses, 'Statuses of the state machine')

class SSIEncoder(SM_SSIEncoder):
    def __init__(self, parent, name, ns, info):
        SM_SSIEncoder.__init__(self, parent, name, ns, info)

class SM_IncrementalEncoder(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("counterValue", ns, 'Actual counter value', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("status", ns, 'Status', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("setCounterValue", ns, 'Counter value to be set', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("setCounter", ns, 'Counter value to be set', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("enableLatchC", ns, 'Enable latch C', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("latchCValid", ns, 'Bit 0: Latch C valid', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("latchExternValid", ns, 'Bit 1: Latch extern valid', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("setCounterDone", ns, 'Bit 2: Set counter done', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("counterUnderflow", ns, 'Bit 3: Counter undeflow', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("counterOverflow", ns, 'Bit 4: Counter overflow', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("statusOfInputStatus", ns, 'Bit 5: Status of input status', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("openCircuit", ns, 'Bit 6: Open circuit', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("extrapolationStall", ns, 'Bit 7: Extrapolation stall', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("statusOfInputA", ns, 'Bit 8: Status of input A', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("statusOfInputB", ns, 'Bit 9: Status of input B', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("statusOfInputC", ns, 'Bit 10: Status of input C', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("statusOfInputGate", ns, 'Bit 11: Status of input gate', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("statusOfExternLatch", ns, 'Bit 12: Status of external latch', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("syncError", ns, 'Bit 13: Sync error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, IncrementalEncoderStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, IncrementalEncoderProcesses, 'Processes of the state machine')

class IncrementalEncoder(SM_IncrementalEncoder):
    def __init__(self, parent, name, ns, info):
        SM_IncrementalEncoder.__init__(self, parent, name, ns, info)

class SM_EtherCatDevice(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("id", ns, 'Label according to the electric schemes', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("typeId", ns, 'Manufacturer type, e.g. EL1008', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("wcState", ns, '0 = Data valid, 1 = Data invalid', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("infoData", ns, 'EtherCAT state', datatype=pyuaf.util.primitives.Int16, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, EtherCatDeviceStatuses, 'Statuses of the state machine')

class EtherCatDevice(SM_EtherCatDevice):
    def __init__(self, parent, name, ns, info):
        SM_EtherCatDevice.__init__(self, parent, name, ns, info)

class SM_CANopenBus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("error", ns, 'Number of boxes with BoxState unequal to 0', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("canState", ns, 'CAN state (See system manager for bit interpretation', datatype=pyuaf.util.primitives.Int16, permissions='r')
        self.__addVariable__("rxErrorCounter", ns, 'RxError-counter of the CAN controller', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("txErrorCounter", ns, 'TxError-counter of the CAN controller', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, CANopenBusStatuses, 'Statuses of the state machine')

class CANopenBus(SM_CANopenBus):
    def __init__(self, parent, name, ns, info):
        SM_CANopenBus.__init__(self, parent, name, ns, info)

class SM_CurrentMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("microAmpsValue", ns, 'Measured current in microamps', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("current", ns, Current, 'The measured current')
        self.__addInstance__("statuses", ns, CurrentMeasurementStatuses, 'Statuses of the state machine')

class CurrentMeasurement(SM_CurrentMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_CurrentMeasurement.__init__(self, parent, name, ns, info)

class SM_VoltageMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = volt.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, Voltage, 'Actual value')
        self.__addInstance__("average", ns, Voltage, 'Moving average value')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, VoltageMeasurementStatuses, 'Statuses of the state machine')

class VoltageMeasurement(SM_VoltageMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_VoltageMeasurement.__init__(self, parent, name, ns, info)

class SM_TemperatureMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = temperature.degrees.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, Temperature, 'Actual value')
        self.__addInstance__("average", ns, Temperature, 'Moving average value')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, TemperatureMeasurementStatuses, 'Statuses of the state machine')

class TemperatureMeasurement(SM_TemperatureMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_TemperatureMeasurement.__init__(self, parent, name, ns, info)

class SM_PressureMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = bar.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, Pressure, 'Actual value')
        self.__addInstance__("average", ns, Pressure, 'Moving average value')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, PressureMeasurementStatuses, 'Statuses of the state machine')

class PressureMeasurement(SM_PressureMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_PressureMeasurement.__init__(self, parent, name, ns, info)

class SM_FrequencyMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = hertz.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, Frequency, 'Actual value')
        self.__addInstance__("average", ns, Frequency, 'Moving average value')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, FrequencyMeasurementStatuses, 'Statuses of the state machine')

class FrequencyMeasurement(SM_FrequencyMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_FrequencyMeasurement.__init__(self, parent, name, ns, info)

class SM_GForceMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("milliGValue", ns, 'Measured raw milliG value (linked to I/O module)', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, GForce, 'Actual value')
        self.__addInstance__("average", ns, GForce, 'Moving average value')
        self.__addInstance__("statuses", ns, GForceMeasurementStatuses, 'Statuses of the state machine')

class GForceMeasurement(SM_GForceMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_GForceMeasurement.__init__(self, parent, name, ns, info)

class SM_RelativeHumidityMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = fraction.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, Fraction, 'Actual value')
        self.__addInstance__("average", ns, Fraction, 'Moving average value')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, RelativeHumidityMeasurementStatuses, 'Statuses of the state machine')

class RelativeHumidityMeasurement(SM_RelativeHumidityMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_RelativeHumidityMeasurement.__init__(self, parent, name, ns, info)

class SM_ForceMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = newton.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, Force, 'Actual value')
        self.__addInstance__("average", ns, Force, 'Moving average value')
        self.__addInstance__("statuses", ns, ForceMeasurementStatuses, 'Statuses of the state machine')

class ForceMeasurement(SM_ForceMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_ForceMeasurement.__init__(self, parent, name, ns, info)

class SM_LinearPositionMeasurement16(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = millimeters.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, LinearPosition, 'Actual value')
        self.__addInstance__("average", ns, LinearPosition, 'Moving average value')
        self.__addInstance__("statuses", ns, LinearPositionMeasurement16Statuses, 'Statuses of the state machine')

class LinearPositionMeasurement16(SM_LinearPositionMeasurement16):
    def __init__(self, parent, name, ns, info):
        SM_LinearPositionMeasurement16.__init__(self, parent, name, ns, info)

class SM_LinearPositionMeasurementU32(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rawValue", ns, 'Measured raw value', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("error", ns, 'Error', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("underrange", ns, 'Underrange', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("overrange", ns, 'Overrange', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("conversionFactor", ns, 'rawValue * conversionFactor = millimeters.value', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, LinearPosition, 'Actual value')
        self.__addInstance__("average", ns, LinearPosition, 'Moving average value')
        self.__addInstance__("statuses", ns, LinearPositionMeasurementU32Statuses, 'Statuses of the state machine')

class LinearPositionMeasurementU32(SM_LinearPositionMeasurementU32):
    def __init__(self, parent, name, ns, info):
        SM_LinearPositionMeasurementU32.__init__(self, parent, name, ns, info)

class SM_SimpleRelay(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("digitalOutput", ns, 'Boolean, to bind to digital output', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, SimpleRelayStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, SimpleRelayProcesses, 'Processes of the state machine')

class SimpleRelay(SM_SimpleRelay):
    def __init__(self, parent, name, ns, info):
        SM_SimpleRelay.__init__(self, parent, name, ns, info)

class SM_ConfigManager(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("filePath", ns, 'Full path of the config filename', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, ConfigManagerStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, ConfigManagerProcesses, 'Processes of the state machine')

class ConfigManager(SM_ConfigManager):
    def __init__(self, parent, name, ns, info):
        SM_ConfigManager.__init__(self, parent, name, ns, info)

class Process(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("testVar", ns, 'At least 1 variable needed because subclass members of an empty class are not exposed by OPC UA (TwinCAT bug!)', datatype=pyuaf.util.primitives.Boolean, permissions='')


class McProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("testVar", ns, 'At least 1 variable needed because subclass members of an empty class are not exposed by OPC UA (TwinCAT bug!)', datatype=pyuaf.util.primitives.Boolean, permissions='')


class ChangeSetpointProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, ChangeSetpointProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, ChangeSetpointProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McMoveAbsoluteProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McMoveAbsoluteProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McMoveAbsoluteProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McMoveRelativeProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McMoveRelativeProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McMoveRelativeProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McPowerProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McPowerProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McPowerProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McSetPositionProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McSetPositionProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McSetPositionProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McStopProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McStopProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McStopProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McMoveVelocityProcess(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McMoveVelocityProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McMoveVelocityProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class SetEnabledProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, SetEnabledProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, SetEnabledProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class McWriteParameter(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McWriteParameterArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McWriteParameterArgs, 'Arguments in use by the process, if do_request was accepted')


class McReadParameter(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("value", ns, 'Value that was read', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("set", ns, McReadParameterArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McReadParameterArgs, 'Arguments in use by the process, if do_request was accepted')


class McWriteBoolParameter(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, McWriteBoolParameterArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McWriteBoolParameterArgs, 'Arguments in use by the process, if do_request was accepted')


class McReadBoolParameter(BaseMcProcess):

    def __init__(self, parent, name, ns, info):
        BaseMcProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("value", ns, 'Value that was read', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addInstance__("set", ns, McReadBoolParameterArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, McReadBoolParameterArgs, 'Arguments in use by the process, if do_request was accepted')


class SDOReadProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("value1Byte", ns, 'Value that has been read, if noOfBytes is 1', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("value2Bytes", ns, 'Value that has been read, if noOfBytes is 2', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("value4Bytes", ns, 'Value that has been read, if noOfBytes is 4', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("errorId", ns, 'Error ID according to Beckhoff', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addInstance__("set", ns, SDOReadProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, SDOReadProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class SDOWriteProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("errorId", ns, 'Error ID according to Beckhoff', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addInstance__("set", ns, SDOWriteProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, SDOWriteProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class SoEReadProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("value1Byte", ns, 'Value that has been read, if noOfBytes is 1', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("value2Bytes", ns, 'Value that has been read, if noOfBytes is 2', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("value4Bytes", ns, 'Value that has been read, if noOfBytes is 4', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("adsErrorId", ns, 'ADS error ID ', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("sercosErrorId", ns, 'Sercos error ID ', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addInstance__("set", ns, SoEReadProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, SoEReadProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class SoEWriteProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("adsErrorId", ns, 'ADS error ID ', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("sercosErrorId", ns, 'Sercos error ID ', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addInstance__("set", ns, SoEWriteProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, SoEWriteProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class SoEResetProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("adsErrorId", ns, 'ADS error ID ', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("sercosErrorId", ns, 'Sercos error ID ', datatype=pyuaf.util.primitives.Int16, permissions='')


class SetBrakeProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, SetBrakeProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, SetBrakeProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class ChangeOperatingStateProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, ChangeOperatingStateProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, ChangeOperatingStateProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class ChangeOperatorStateProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, ChangeOperatorStateProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, ChangeOperatorStateProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class ReadXmlProcess(BaseXmlDataSrvProcess):

    def __init__(self, parent, name, ns, info):
        BaseXmlDataSrvProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, ReadXmlProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, ReadXmlProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class WriteXmlProcess(BaseXmlDataSrvProcess):

    def __init__(self, parent, name, ns, info):
        BaseXmlDataSrvProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, WriteXmlProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, WriteXmlProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class ActivateProcess(BaseProcess):

    def __init__(self, parent, name, ns, info):
        BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("testVar", ns, 'At least 1 variable needed because subclass members of an empty class are not exposed by OPC UA (TwinCAT bug!)', datatype=pyuaf.util.primitives.Boolean, permissions='')




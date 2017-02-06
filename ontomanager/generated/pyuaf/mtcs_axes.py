# === imports ===

import mtcs_common
import mtcs_tmc


# This file (mtcs_axes.py) was automatically generated at 2017-02-03T09:53:56.397815 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class AxesIds:
        AZI = 0
        ABL = 1
        ELE = 2
        ROC = 3
        RON = 4

class AxesMoveUnits:
        DEGREES = 0
        RADIANS = 1
        ARCSECONDS = 2

class AxesAlphaUnits:
        HOURS = 0
        DEGREES = 1
        RADIANS = 2

class AxesDeltaUnits:
        DEGREES = 0
        RADIANS = 1

class AxesMuUnits:
        ARCSECONDS_PER_YEAR = 0
        MILLIARCSECONDS_PER_YEAR = 1
        DEGREES_PER_YEAR = 2
        RADIANS_PER_YEAR = 3

class AxesMoveVelocityUnits:
        DEGREES_PER_SECOND = 0
        ARCSECONDS_PER_SECOND = 1
        RADIANS_PER_SECOND = 2
        ARCSECONDS_PER_MINUTE = 3
        ARCSECONDS_PER_HOUR = 4

class AxesRotatorActivity:
        NONE_ACTIVE = 0
        ROC_ACTIVE = 1
        RON_ACTIVE = 2


# === STRUCTS ===

class AxesParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("azi", ns, AxesAzimuthAxis, 'The azimuth axis')
        self.__addInstance__("ele", ns, AxesElevationAxis, 'The elevation axis')
        self.__addInstance__("roc", ns, AxesRotationAxis, 'The cassegrain derotator axis')
        self.__addInstance__("ron", ns, AxesRotationAxis, 'The nasmyth derotator axis')
        self.__addInstance__("io", ns, AxesIO, 'I/O modules and drives')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')
        self.__addInstance__("tpoint", ns, AxesPointingModelsSetup, 'The TPOINT models setup')

class AxesAzimuthAxisParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("virtualAxis", ns, mtcs_common.AngularAxis, 'The virtual AZI axis')
        self.__addInstance__("physicalAxis", ns, mtcs_common.AngularAxis, 'The physical AZI axis')
        self.__addInstance__("ablAxis", ns, mtcs_common.AngularAxis, 'The (anti-backlash) ABL axis')
        self.__addInstance__("lida1", ns, mtcs_common.IncrementalEncoder, 'The external (LIDA) encoder no. 1')
        self.__addInstance__("lida2", ns, mtcs_common.IncrementalEncoder, 'The external (LIDA) encoder no. 2')
        self.__addInstance__("lida3", ns, mtcs_common.IncrementalEncoder, 'The external (LIDA) encoder no. 3')
        self.__addInstance__("lida4", ns, mtcs_common.IncrementalEncoder, 'The external (LIDA) encoder no. 4')
        self.__addInstance__("absoluteEncoder", ns, mtcs_common.SSIEncoder, 'The external absolute encoder')

class AxesElevationAxisParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("virtualAxis", ns, mtcs_common.AngularAxis, 'The virtual axis')
        self.__addInstance__("physicalAxis", ns, mtcs_common.AngularAxis, 'The physical ELE axis')
        self.__addInstance__("lida1", ns, mtcs_common.IncrementalEncoder, 'The external (LIDA) encoder no. 1')
        self.__addInstance__("lida2", ns, mtcs_common.IncrementalEncoder, 'The external (LIDA) encoder no. 2')
        self.__addInstance__("absoluteEncoder", ns, mtcs_common.SSIEncoder, 'The external absolute encoder')

class AxesRotationAxisParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("virtualAxis", ns, mtcs_common.AngularAxis, 'The virtual axis')
        self.__addInstance__("physicalAxis", ns, mtcs_common.AngularAxis, 'The physical axis')

class AxesPointingModelSetupParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class AxesPointingModelsSetupParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("model0", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model1", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model2", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model3", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model4", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model5", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model6", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model7", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model8", ns, AxesPointingModelSetup, '')
        self.__addInstance__("model9", ns, AxesPointingModelSetup, '')

class AxesIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("aziDrive", ns, mtcs_common.AX52XXDrive, 'The AX5000 drive for the AZI en ROC motors')
        self.__addInstance__("ablDrive", ns, mtcs_common.AX52XXDrive, 'The AX5000 drive for the ABL en RON motors')
        self.__addInstance__("eleDrive", ns, mtcs_common.AX52XXDrive, 'The AX5000 drive for the ELE en FW motors')
        self.__addInstance__("TA_AZID", ns, mtcs_common.EtherCatDevice, 'Telescope Axis - AZID')
        self.__addInstance__("TA_ABLD", ns, mtcs_common.EtherCatDevice, 'Telescope Axis - ABLD')
        self.__addInstance__("TA_ELED", ns, mtcs_common.EtherCatDevice, 'Telescope Axis - ELED')
        self.__addInstance__("TE_COU", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - COU')
        self.__addInstance__("TE_EN1", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN1')
        self.__addInstance__("TE_EN2", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN2')
        self.__addInstance__("TE_EN3", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN3')
        self.__addInstance__("TE_EN4", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN4')
        self.__addInstance__("TE_EN5", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN5')
        self.__addInstance__("TE_EN6", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN6')
        self.__addInstance__("TE_EN7", ns, mtcs_common.EtherCatDevice, 'Telescope Encoders - EN7')

class AxesProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the axis (no homing)')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')
        self.__addInstance__("setTarget", ns, AxesSetTargetProcess, 'Set a new target')
        self.__addInstance__("point", ns, AxesPointProcess, 'Point the telescope to a new target')
        self.__addInstance__("pointRelative", ns, AxesPointRelativeProcess, 'Point the telescope relative to the current target')
        self.__addInstance__("stop", ns, AxesStopProcess, 'Stop the axes (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("quickStop", ns, AxesStopProcess, 'Quickly stop the axes (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("powerOn", ns, AxesMultiPowerOnProcess, 'Power on the axes')
        self.__addInstance__("powerOff", ns, AxesPowerOffProcess, 'Power off the axes')
        self.__addInstance__("doHoming", ns, AxesDoHomingProcess, 'Do a homing of the axes')
        self.__addInstance__("moveAbsolute", ns, AxesMultiMoveProcess, 'Move the axes in alt-azimuth to an absolute position')
        self.__addInstance__("moveRelative", ns, AxesMultiMoveProcess, 'Move the axes in alt-azimuth relative to the current position')
        self.__addInstance__("moveKnownPosition", ns, AxesMoveKnownPositionProcess, 'Move the axes to the given known position')
        self.__addInstance__("enablePointingModel", ns, AxesEnablePointingModelProcess, 'Enable a pointing model with the given name')
        self.__addInstance__("disablePointingModel", ns, mtcs_common.Process, 'Disable the currently active pointing model')
        self.__addInstance__("setAlphaDeltaVelocity", ns, AxesSetAlphaDeltaVelocityProcess, 'Set an additional alpha/delta velocity (e.g. to track solar system objects)')

class AxesAzimuthAxisProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("moveAbsolute", ns, AxesMoveAbsoluteProcess, 'Move the axis in an absolute way')
        self.__addInstance__("moveRelative", ns, AxesMoveRelativeProcess, 'Move the axis relative to the current position')
        self.__addInstance__("moveVelocity", ns, AxesMoveVelocityProcess, 'Move the axis endlessly with the given velocity')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the axis (no homing)')
        self.__addInstance__("moveOutOfLimitSwitch", ns, AxesMoveOutOfLimitSwitchProcess, 'Move out of a limit switch')
        self.__addInstance__("powerOn", ns, AxesPowerOnProcess, 'Power on the axis')
        self.__addInstance__("powerOff", ns, AxesPowerOffProcess, 'Power off the axis')
        self.__addInstance__("doHoming", ns, AxesDoHomingProcess, 'Do a homing of the axis')
        self.__addInstance__("stop", ns, AxesStopProcess, 'Stop the axis (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("quickStop", ns, AxesStopProcess, 'Quickly stop the axes (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("unlockBrake", ns, AxesUnlockBrakeProcess, 'Temporarily unlock the brake')
        self.__addInstance__("setPosition", ns, AxesSetPositionProcess, 'Set the axis to the given position')

class AxesElevationAxisProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("moveAbsolute", ns, AxesMoveAbsoluteProcess, 'Move the axis in an absolute way')
        self.__addInstance__("moveRelative", ns, AxesMoveRelativeProcess, 'Move the axis relative to the current position')
        self.__addInstance__("moveVelocity", ns, AxesMoveVelocityProcess, 'Move the axis endlessly with the given velocity')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the axis (no homing)')
        self.__addInstance__("moveOutOfLimitSwitch", ns, AxesMoveOutOfLimitSwitchProcess, 'Move out of a limit switch')
        self.__addInstance__("powerOn", ns, AxesPowerOnProcess, 'Power on the axis')
        self.__addInstance__("powerOff", ns, AxesPowerOffProcess, 'Power off the axis')
        self.__addInstance__("doHoming", ns, AxesDoHomingProcess, 'Do a homing of the axis')
        self.__addInstance__("stop", ns, AxesStopProcess, 'Stop the axis (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("quickStop", ns, AxesStopProcess, 'Quickly stop the axes (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("setPosition", ns, AxesSetPositionProcess, 'Set the axis to the given position')
        self.__addInstance__("unlockBrake", ns, AxesUnlockBrakeProcess, 'Temporarily unlock the brake')

class AxesRotationAxisProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("moveAbsolute", ns, AxesMoveAbsoluteProcess, 'Move the axis in an absolute way')
        self.__addInstance__("moveRelative", ns, AxesMoveRelativeProcess, 'Move the axis relative to the current position')
        self.__addInstance__("moveVelocity", ns, AxesMoveVelocityProcess, 'Move the axis endlessly with the given velocity')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the axis (no homing)')
        self.__addInstance__("moveOutOfLimitSwitch", ns, AxesMoveOutOfLimitSwitchProcess, 'Move out of a limit switch')
        self.__addInstance__("powerOn", ns, AxesPowerOnProcess, 'Power on the axis')
        self.__addInstance__("powerOff", ns, AxesPowerOffProcess, 'Power off the axis')
        self.__addInstance__("stop", ns, AxesStopProcess, 'Stop the axis (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("quickStop", ns, AxesStopProcess, 'Quickly stop the axes (i.e. stop pointing, tracking, moving, ...)')
        self.__addInstance__("setPosition", ns, AxesSetPositionProcess, 'Set the axis to the given position')

class AxesStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, '')

class AxesTargetStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')

class AxesFeedbackStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')

class AxesAzimuthAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the axis in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis in a healthy state?')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, 'Is the axis powered on or off?')

class AxesElevationAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the axis in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis in a healthy state?')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, 'Is the axis powered on or off?')

class AxesRotationAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the axis in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis in a healthy state?')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, 'Is the axis powered on or off?')

class AxesPointingModelsSetupStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the pointing models setup in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the pointing models setup in a healthy state?')

class AxesIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class AxesLocationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("longitude", ns, 'Observatory location: longitude [degrees, positive = E, negative = W]', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("latitude", ns, 'Observatory location: latitude [degrees, positive = N, negative = S]', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("height", ns, 'Observatory location: height above sea-level [m]', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("polarMotionX", ns, 'Earth polar motion x in degrees', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("polarMotionY", ns, 'Earth polar motion y in degrees', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("nutationDx", ns, 'Nutation adjustment dX in degrees', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("nutationDy", ns, 'Nutation adjustment dY in degrees', datatype=pyuaf.util.primitives.Float, permissions='')

class AxesLocalConditionsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("useTemperatureFromSensors", ns, 'True if the temperature from the sensors should be used, false to use the temperature from the config', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("configuredTemperature", ns, 'Local temperature in degrees, fixed by config', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("configuredPressure", ns, 'Local temperature in hectoPascal = millibar, fixed by config', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("useRelativeHumidityFromSensors", ns, 'True if the temperature from the sensors should be used, false to use the temperature from the config', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("configuredRelativeHumidity", ns, 'Local relative humidity as a fraction (0...1), fixed by config', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("configuredObservingWavelength", ns, 'Observing wavelength in microns, fixed by config', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("troposphericLapseRate", ns, 'Tropospheric lapse rate in K/m', datatype=pyuaf.util.primitives.Float, permissions='')

class AxesAzimuthConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("absoluteEncoderOffset", ns, 'Offset in degrees, of the absolute encoder, w.r.t. zero', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("absoluteEncoderInvert", ns, 'TRUE to invert the counting direction of the absolute encoder', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("lidasInvert", ns, 'TRUE to invert the counting direction of the LIDAs', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("moveOutOfLimitSwitchDistance", ns, 'How many degrees should the moveOutOfLimitSwitch process try to move?', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("positiveLimitSwitchInput", ns, 'Which input (0-7) represents the positive limit switch?', datatype=pyuaf.util.primitives.SByte, permissions='')
        self.__addVariable__("negativeLimitSwitchInput", ns, 'Which input (0-7) represents the negative limit switch?', datatype=pyuaf.util.primitives.SByte, permissions='')
        self.__addVariable__("minPositionLimitVirtualAxis", ns, 'Limit the minimum position of the virtual axis to this value in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionLimitVirtualAxis", ns, 'Limit the maximum position of the virtual axis to this value in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minPositionLimitPhysicalAxis", ns, 'Limit the minimum position of the physical axis to this value in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionLimitPhysicalAxis", ns, 'Limit the maximum position of the physical axis to this value in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("velocityLimit", ns, 'Limit the velocity of the axis to this value in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("accelerationLimit", ns, 'Limit the acceleration (or deceleration) of the axis to this value in degrees/sec^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minPositionSetpoint", ns, 'The minimum position setpoint of the axis in degrees (should be a bit before the minPositionLimit)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionSetpoint", ns, 'The maximum position setpoint of the axis in degrees (should be a bit before the maxPositionLimit)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxVelocitySetpoint", ns, 'The maximum velocity setpoint of the axis in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxAccelerationSetpoint", ns, 'The maximum acceleration setpoint of the axis in degrees/sec^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("slipLimit", ns, 'If the difference between the LIDA-encoder and motor-encoder positions is above this value in degrees, then we have detected slip', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablMaxTorqueRiseSpeed", ns, 'The ABL torque can rise maximum ... Nm/s on the telescope axis (always &gt;0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablMaxTorqueFallSpeed", ns, 'The ABL torque can fall maximum ... Nm/s on the telescope axis (always &gt;0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablMaxTorque", ns, 'The maximum ABL torque in Nm/s on the telescope axis (always &gt;0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablMinTorque", ns, 'The minimum ABL torque in Nm/s on the telescope axis (always &gt;0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablZeroAccTorque", ns, 'The ABL torque when the axis is not accelerating or decelerating (always &gt;0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablTorqueOutputOverride", ns, 'Scale the ABL output torque by this fraction value (only for testing purposes, must be 1 normally!)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ablPositiveTorque", ns, 'True if a positive torque must be applied, false if a negative torque must be applied', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("aziAndAblSameDirection", ns, 'True if the AZI and ABL axes rotate in the same direction?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("homingHomePosition", ns, 'The position of the homing mark (in degrees), with respect to the absolute zero', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingStartAbsEncPosition", ns, 'Absolute encoder position where the homing should go to first, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingGotoStartVelocity", ns, 'Velocity when going to the start position, in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingVelocity", ns, 'Velocity to search for the homing mark, in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingRange", ns, 'Maximum distance to be covered while searching for the homing mark, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("quickStopDeceleration", ns, 'Quick stop deceleration, in degrees/sec2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("quickStopJerk", ns, 'Quick stop jerk, in degrees/sec3', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesElevationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("absoluteEncoderOffset", ns, 'Offset in degrees, of the absolute encoder, w.r.t. zero', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("absoluteEncoderInvert", ns, 'TRUE to invert the counting direction', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("lidasInvert", ns, 'TRUE to invert the counting direction of the LIDAs', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("moveOutOfLimitSwitchDistance", ns, 'How many degrees should the moveOutOfLimitSwitch process try to move?', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("positiveLimitSwitchInput", ns, 'Which input (0-7) represents the positive limit switch?', datatype=pyuaf.util.primitives.SByte, permissions='')
        self.__addVariable__("negativeLimitSwitchInput", ns, 'Which input (0-7) represents the negative limit switch?', datatype=pyuaf.util.primitives.SByte, permissions='')
        self.__addVariable__("minPositionLimitVirtualAxis", ns, 'Limit the minimum position of the axis to this value in degrees, of the virtual axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionLimitVirtualAxis", ns, 'Limit the maximum position of the axis to this value in degrees, of the virtual axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minPositionLimitPhysicalAxis", ns, 'Limit the minimum position of the axis to this value in degrees, of the physical axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionLimitPhysicalAxis", ns, 'Limit the maximum position of the axis to this value in degrees, of the physical axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("velocityLimit", ns, 'Limit the velocity of the axis to this value in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("accelerationLimit", ns, 'Limit the acceleration (or deceleration) of the axis to this value in degrees/sec^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minPositionSetpoint", ns, 'The minimum position setpoint of the axis in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionSetpoint", ns, 'The maximum position setpoint of the axis in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxVelocitySetpoint", ns, 'The maximum velocity setpoint of the axis in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxAccelerationSetpoint", ns, 'The maximum acceleration setpoint of the axis in degrees/sec^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("slipLimit", ns, 'If the difference between the LIDA-encoder and motor-encoder positions is above this value in degrees, then we have detected slip', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingHomePosition", ns, 'The position of the homing mark (in degrees), with respect to the absolute zero', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingStartAbsEncPosition", ns, 'Absolute encoder position where the homing should go to first, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingGotoStartVelocity", ns, 'Velocity when going to the start position, in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingVelocity", ns, 'Velocity to search for the homing mark, in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingRange", ns, 'Maximum distance to be covered while searching for the homing mark, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("quickStopDeceleration", ns, 'Quick stop deceleration, in degrees/sec2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("quickStopJerk", ns, 'Quick stop jerk, in degrees/sec3', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesRotationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("motorEncoderOffset", ns, 'Offset in degrees, of the absolute motor encoder, w.r.t. zero', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("moveOutOfLimitSwitchDistance", ns, 'How many degrees should the moveOutOfLimitSwitch process try to move?', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("positiveLimitSwitchInput", ns, 'Which input (0-7) represents the positive limit switch?', datatype=pyuaf.util.primitives.SByte, permissions='')
        self.__addVariable__("negativeLimitSwitchInput", ns, 'Which input (0-7) represents the negative limit switch?', datatype=pyuaf.util.primitives.SByte, permissions='')
        self.__addVariable__("minPositionLimitVirtualAxis", ns, 'Limit the minimum position of the axis to this value in degrees, of the virtual axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionLimitVirtualAxis", ns, 'Limit the maximum position of the axis to this value in degrees, of the virtual axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minPositionLimitPhysicalAxis", ns, 'Limit the minimum position of the axis to this value in degrees, of the physical axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionLimitPhysicalAxis", ns, 'Limit the maximum position of the axis to this value in degrees, of the physical axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("velocityLimit", ns, 'Limit the velocity of the axis to this value in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("accelerationLimit", ns, 'Limit the acceleration (or deceleration) of the axis to this value in degrees/sec^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minPositionSetpoint", ns, 'The minimum position setpoint of the axis in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionSetpoint", ns, 'The maximum position setpoint of the axis in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxVelocitySetpoint", ns, 'The maximum velocity setpoint of the axis in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxAccelerationSetpoint", ns, 'The maximum acceleration setpoint of the axis in degrees/sec^2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("quickStopDeceleration", ns, 'Quick stop deceleration, in degrees/sec2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("quickStopJerk", ns, 'Quick stop jerk, in degrees/sec3', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesKnownPositionConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'The name of the position (e.g. &#39;PARK&#39;)', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("allowObserver", ns, 'Can an observer switch to this position?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("azi", ns, 'Azimuth in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ele", ns, 'Elevation in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("roc", ns, 'Cassegrain rotation in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ron", ns, 'Nasmyth B rotation in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("doAzi", ns, 'Change the azimuth axis to the &#39;azi&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doEle", ns, 'Change the elevation axis to the &#39;ele&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRoc", ns, 'Change the cassegrain rotation axis to the &#39;roc&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRon", ns, 'Change the nasmyth rotation axis to the &#39;ron&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')

class AxesKnownPositionsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position0", ns, AxesKnownPositionConfig, 'Known position 0')
        self.__addInstance__("position1", ns, AxesKnownPositionConfig, 'Known position 1')
        self.__addInstance__("position2", ns, AxesKnownPositionConfig, 'Known position 2')
        self.__addInstance__("position3", ns, AxesKnownPositionConfig, 'Known position 3')
        self.__addInstance__("position4", ns, AxesKnownPositionConfig, 'Known position 4')
        self.__addInstance__("position5", ns, AxesKnownPositionConfig, 'Known position 5')
        self.__addInstance__("position6", ns, AxesKnownPositionConfig, 'Known position 6')
        self.__addInstance__("position7", ns, AxesKnownPositionConfig, 'Known position 7')
        self.__addInstance__("position8", ns, AxesKnownPositionConfig, 'Known position 8')
        self.__addInstance__("position9", ns, AxesKnownPositionConfig, 'Known position 9')
        self.__addInstance__("position10", ns, AxesKnownPositionConfig, 'Known position 10')
        self.__addInstance__("position11", ns, AxesKnownPositionConfig, 'Known position 11')
        self.__addInstance__("position12", ns, AxesKnownPositionConfig, 'Known position 12')
        self.__addInstance__("position13", ns, AxesKnownPositionConfig, 'Known position 13')
        self.__addInstance__("position14", ns, AxesKnownPositionConfig, 'Known position 14')
        self.__addInstance__("position15", ns, AxesKnownPositionConfig, 'Known position 15')
        self.__addInstance__("position16", ns, AxesKnownPositionConfig, 'Known position 16')
        self.__addInstance__("position17", ns, AxesKnownPositionConfig, 'Known position 17')
        self.__addInstance__("position18", ns, AxesKnownPositionConfig, 'Known position 18')
        self.__addInstance__("position19", ns, AxesKnownPositionConfig, 'Known position 19')

class AxesConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("location", ns, AxesLocationConfig, 'Location of the observatory')
        self.__addInstance__("localConditions", ns, AxesLocalConditionsConfig, 'Location of the observatory')
        self.__addInstance__("knownPositions", ns, AxesKnownPositionsConfig, 'Known (predefined) positions (e.g. could be Park, Cover, Park winter, Mirror washing, ...)')
        self.__addInstance__("azi", ns, AxesAzimuthConfig, 'Azimuth axis')
        self.__addInstance__("ele", ns, AxesElevationConfig, 'Elevation axis')
        self.__addInstance__("roc", ns, AxesRotationConfig, 'Cassegrain rotation axis')
        self.__addInstance__("ron", ns, AxesRotationConfig, 'Nasmyth rotation axis')
        self.__addVariable__("cassegrainRotatorName", ns, 'Name of the Cassegrain rotator', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("nasmythRotatorName", ns, 'Name of the Nasmyth rotator', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("rocGuiAngle", ns, 'Amgle to show ROC in the GUI', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ronGuiAngle", ns, 'Amgle to show RON in the GUI', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("knownPositionToleranceAzi", ns, 'Tolerance (in degrees) to determine if the telescope is at a known position in azi direction', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("knownPositionToleranceEle", ns, 'Tolerance (in degrees) to determine if the telescope is at a known position in ele direction', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("knownPositionToleranceRoc", ns, 'Tolerance (in degrees) to determine if the telescope is at a known position in roc direction', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("knownPositionToleranceRon", ns, 'Tolerance (in degrees) to determine if the telescope is at a known position in ron direction', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rocPositionAngleSign", ns, '-1 to invert the sign of the PA for the cas derotator, 1 for positive', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("ronPositionAngleSign", ns, '-1 to invert the sign of the PA for the cas derotator, 1 for positive', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("tpointAziSign", ns, '-1 or 1 to invert input for TPOINT: A', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("tpointEleSign", ns, '-1 or 1 to invert input for TPOINT: E ', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("tpointDeltaAziSign", ns, '-1 or 1 to invert input for TPOINT: DA', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("tpointDeltaEleSign", ns, '-1 or 1 to invert input for TPOINT: DE', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("tpointOldFormulas", ns, 'True to use the old formulas', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("tpointConvertRawAlphaDelta", ns, 'If True, raw encoder values will be converted to feedback.alpha and feedback.delta, instead of corrected encoder values. Only use for tech stuff!', datatype=pyuaf.util.primitives.Boolean, permissions='')

class AxesPointingModelConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'This name can be matched against the instrument name in the MTCS config and the focal station name in the M3 config.', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("IE", ns, 'Index error in elevation', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("IA", ns, 'Index error in azimuth', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("CA", ns, 'Nonperpendicularity of elevation and pointing axes', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("AN", ns, 'NS misalignment of azimuth axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("AW", ns, 'EW misalignment of azimuth axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("NPAE", ns, 'Nonperpendicularity of azimuth and elevation axes', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("NRX", ns, 'Horizontal displacement of Nasmyth rotation', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("NRY", ns, 'Vertical displacement of Nasmyth rotation', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ACES", ns, 'Az centering error (sin component)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ACEC", ns, 'Az centering error (cos component)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ECES", ns, 'El centering error (sin component)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ECEC", ns, 'El centering error (cos component)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("TF", ns, 'Tube flexure - sin(zeta) law', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("TX", ns, 'Tube flexure - tan(zeta) law', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("FLOP", ns, 'Constant vertical displacement', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("POX", ns, 'The x-coordinate of a pointing origin on a derotator', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("POY", ns, 'The y-coordinate of a pointing origin on a derotator', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesSetTargetProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("alphaUnits", ns, 'The units in which alpha is given', datatype=AxesAlphaUnits, permissions='')
        self.__addVariable__("alpha", ns, 'Right ascention, in the units of the alphaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("deltaUnits", ns, 'The units in which delta is given', datatype=AxesDeltaUnits, permissions='')
        self.__addVariable__("delta", ns, 'Declination, in the units of the deltaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("muUnits", ns, 'The units in which muAlpha and muDelta are given', datatype=AxesMuUnits, permissions='')
        self.__addVariable__("muAlpha", ns, 'Right ascention proper motion, the units of muUmits (do not multiply by cos(delta)!)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("muDelta", ns, 'Declination proper motion, in radians/year', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("parallax", ns, 'Object parallax, in arcseconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("radialVelocity", ns, 'Object radial velocity, in km/s', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("epoch", ns, 'Epoch, e.g. 2000.0', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesPointProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("alphaUnits", ns, 'The units in which alpha is given', datatype=AxesAlphaUnits, permissions='')
        self.__addVariable__("alpha", ns, 'Right ascention, in the units of the alphaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("deltaUnits", ns, 'The units in which delta is given', datatype=AxesDeltaUnits, permissions='')
        self.__addVariable__("delta", ns, 'Declination, in the units of the deltaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("muUnits", ns, 'The units in which muAlpha and muDelta are given', datatype=AxesMuUnits, permissions='')
        self.__addVariable__("muAlpha", ns, 'Right ascention proper motion, the units of muUmits (do not multiply by cos(delta)!)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("muDelta", ns, 'Declination proper motion, in radians/year', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("parallax", ns, 'Object parallax, in arcseconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("radialVelocity", ns, 'Object radial velocity, in km/s', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("epoch", ns, 'Epoch, e.g. 2000.0', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("tracking", ns, 'True to start tracking the object, false to Only do a pointing', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("rotUnits", ns, 'Units of the &#39;rot&#39;, &#39;roc&#39; and &#39;ron&#39; arguments (RADIANS, DEGREES, ARCSECONDS, ...)', datatype=AxesMoveUnits, permissions='')
        self.__addVariable__("rotOffset", ns, 'Offset to move the currently active rotator (incompatible with &#39;roc&#39; and &#39;ron&#39; args)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rocOffset", ns, 'Offset to move the cassegrain rotation axis (incompatible with &#39;rot&#39; arg)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ronOffset", ns, 'Offset to move the nasmyth rotation axis (incompatible with &#39;rot&#39; arg)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("doRotOffset", ns, 'True to move the currently active rotator, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRocOffset", ns, 'True to move the cassegrain rotation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRonOffset", ns, 'True to move the nasmyth rotation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')

class AxesPointRelativeProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("alphaUnits", ns, 'The units in which alpha is given', datatype=AxesAlphaUnits, permissions='')
        self.__addVariable__("alpha", ns, 'Right ascention, in the units of the alphaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("deltaUnits", ns, 'The units in which delta is given', datatype=AxesDeltaUnits, permissions='')
        self.__addVariable__("delta", ns, 'Declination, in the units of the deltaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesMoveRelativeProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("units", ns, 'Units of the &#39;value&#39; argument (RADIANS, DEGREES, ARCSECONDS, ...)', datatype=AxesMoveUnits, permissions='')
        self.__addVariable__("value", ns, 'Move the axis with this value (which units depends on the &#39;units&#39; argument)', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesMoveAbsoluteProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("units", ns, 'Units of the &#39;value&#39; argument (RADIANS, DEGREES, ARCSECONDS, ...)', datatype=AxesMoveUnits, permissions='')
        self.__addVariable__("value", ns, 'Move the axis to this value (which units depends on the &#39;units&#39; argument) + the optional offset', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("offset", ns, 'Optional extra offset (which will not be added to the &#39;startPos&#39;', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesMoveKnownPositionProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the position to move to', datatype=pyuaf.util.primitives.String, permissions='')

class AxesMoveVelocityProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("units", ns, 'Units of the &#39;value&#39; argument (RADIANS_PER_SECOND, DEGREES_PER_SECOND, ...)', datatype=AxesMoveVelocityUnits, permissions='')
        self.__addVariable__("value", ns, 'Move the axis with this velocity (which units depends on the &#39;units&#39; argument)', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesMoveOutOfLimitSwitchProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("switch", ns, 'Positive or negative limit switch', datatype=mtcs_common.LimitSwitches, permissions='')

class AxesMultiPowerOnProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("azi", ns, 'TRUE to power on AZI', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("ele", ns, 'TRUE to power on ELE', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("roc", ns, 'TRUE to power on ROC', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("ron", ns, 'TRUE to power on RON', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("fw", ns, 'TRUE to power on FW', datatype=pyuaf.util.primitives.Boolean, permissions='')

class AxesSetAlphaDeltaVelocityProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("units", ns, 'Units of the alphaVelocity and deltaVelocity', datatype=AxesMoveVelocityUnits, permissions='')
        self.__addVariable__("alphaVelocity", ns, 'Velocity in alpha direction', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("deltaVelocity", ns, 'Velocity in delta direction', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesMultiMoveProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("units", ns, 'Units of the &#39;azi&#39;, &#39;ele&#39;, &#39;roc&#39; and &#39;ron&#39; arguments (RADIANS, DEGREES, ARCSECONDS, ...)', datatype=AxesMoveUnits, permissions='')
        self.__addVariable__("azi", ns, 'Angle to move the azimuth axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ele", ns, 'Angle to move the elevation axis', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rot", ns, 'Angle to move the currently active rotator (incompatible with &#39;roc&#39; and &#39;ron&#39; args)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("roc", ns, 'Angle to move the cassegrain rotation axis (incompatible with &#39;rot&#39; arg)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ron", ns, 'Angle to move the nasmyth rotation axis (incompatible with &#39;rot&#39; arg)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("doAzi", ns, 'True to move the azimuth axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doEle", ns, 'True to move the elevation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRot", ns, 'True to move the currently active rotator, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRoc", ns, 'True to move the cassegrain rotation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRon", ns, 'True to move the nasmyth rotation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("preferMostTravel", ns, 'Only in case of relative movement during tracking: If possible, go to the position where there is most travel (if the telescope is tracking). If false, it will go there the quickest way possible.', datatype=pyuaf.util.primitives.Boolean, permissions='')

class AxesEnablePointingModelProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the pointing model', datatype=pyuaf.util.primitives.String, permissions='')

class AxesUnlockBrakeProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("seconds", ns, 'Unlock the brake for this number of seconds (0 means forever)', datatype=pyuaf.util.primitives.Double, permissions='')

class AxesSetPositionProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("value", ns, 'New position to be taken over by the axis', datatype=pyuaf.util.primitives.Double, permissions='')


# === FBs ===

class SM_Axes(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, AxesConfig, 'Editable configuration of the Axes subsystem')
        self.__addInstance__("fromCppAxes", ns, mtcs_tmc.TmcToPlcAxes, 'Data from the C++ task')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("isPoweredOffByPersonInDome", ns, 'True if the axes are powered off due to a person entering the dome', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isPointing", ns, 'True if the telescope is pointing', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isLimitsReached", ns, 'True if a positiom limit is reached', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isTracking", ns, 'True if the telescope is tracking', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isOffsetting", ns, 'True if the telescope is offsetting (movin', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isAtKnownPosition", ns, 'True if the telescope is at a known position', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isPointingModelActive", ns, 'Is a pointing model currently active?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("activeRotator", ns, 'Which rotator is active?', datatype=AxesRotatorActivity, permissions='r')
        self.__addVariable__("actualKnownPositionName", ns, 'Name of the known position if isAtKnownPosition is True', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("config", ns, AxesConfig, 'Active configuration of the Axes subsystem')
        self.__addInstance__("toCppAxes", ns, mtcs_tmc.TmcFromPlcAxes, 'Data to the C++ task')
        self.__addInstance__("activePointingModel", ns, AxesPointingModelConfig, 'Currently active TPoint model (if isPointingModelActive is TRUE)')
        self.__addVariable__("activePointingModelNumber", ns, 'Number of the currently active TPoint model (if isPointingModelActive is TRUE), -1 if no model is active', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addInstance__("target", ns, AxesTarget, 'The actual target')
        self.__addInstance__("feedback", ns, AxesFeedback, 'The actual feedback')
        self.__addInstance__("statuses", ns, AxesStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AxesParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, AxesProcesses, 'Processes of the state machine')

class Axes(SM_Axes):
    def __init__(self, parent, name, ns, info):
        SM_Axes.__init__(self, parent, name, ns, info)

class SM_AxesTarget(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isGiven", ns, 'True if the target is given, false if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isValid", ns, 'True if the target is valid, false if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isTooLow", ns, 'True if the target is too low to calculate, false if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("alpha", ns, mtcs_common.AngularPosition, 'The alpha coordinate (Right Ascention)')
        self.__addInstance__("delta", ns, mtcs_common.AngularPosition, 'The delta coordinate (Declination)')
        self.__addVariable__("muAlpha", ns, 'Right ascention proper motion, in arcseconds/year (not multiplied by cos(delta)!)', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addVariable__("muDelta", ns, 'Declination proper motion, in arcseconds/year', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addVariable__("parallax", ns, 'Object parallax, in arcseconds', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addVariable__("radialVelocity", ns, 'Object radial velocity, in km/s', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addVariable__("epoch", ns, 'Epoch, e.g. 2000.0', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addInstance__("alphaVelocity", ns, mtcs_common.AngularVelocity, 'Additional target velocity (e.g. for solar system objects) in alpha direction')
        self.__addInstance__("deltaVelocity", ns, mtcs_common.AngularVelocity, 'Additional target velocity (e.g. for solar system objects) in delta direction')
        self.__addInstance__("alphaTravelled", ns, mtcs_common.AngularPosition, 'Alpha traveled so far due to the alphaVelocity')
        self.__addInstance__("deltaTravelled", ns, mtcs_common.AngularPosition, 'Delta traveled so far due to the deltaVelocity')
        self.__addInstance__("alphaOffsetted", ns, mtcs_common.AngularPosition, 'Alpha offsetted so far due to the alphaOffset')
        self.__addInstance__("deltaOffsetted", ns, mtcs_common.AngularPosition, 'Delta offsetted so far due to the deltaOffset')
        self.__addInstance__("alphaStart", ns, mtcs_common.AngularPosition, 'Original alpha without traveling (=alpha - alphaTraveled - alphaOffsetted)')
        self.__addInstance__("deltaStart", ns, mtcs_common.AngularPosition, 'Original delta without traveling (=delta - deltaTraveled - deltaOffsetted)')
        self.__addInstance__("aziPos", ns, mtcs_common.AngularPosition, 'The azimuth target position, as calculated by SLALIBl')
        self.__addInstance__("aziVelo", ns, mtcs_common.AngularVelocity, 'The azimuth target velocity, as calculated by SLALIB')
        self.__addInstance__("aziAcc", ns, mtcs_common.AngularAcceleration, 'The azimuth target acceleration, as calculated by SLALIB')
        self.__addInstance__("elePos", ns, mtcs_common.AngularPosition, 'The elevation target position, as calculated by SLALIB')
        self.__addInstance__("eleVelo", ns, mtcs_common.AngularVelocity, 'The elevation target velocity, as calculated by SLALIB')
        self.__addInstance__("eleAcc", ns, mtcs_common.AngularAcceleration, 'The elevation target acceleration, as calculated by SLALIB')
        self.__addInstance__("paPos", ns, mtcs_common.AngularPosition, 'The position angle target position, as calculated by SLALIB')
        self.__addInstance__("paVelo", ns, mtcs_common.AngularVelocity, 'The position angle target velocity, as calculated by SLALIB')
        self.__addInstance__("paAcc", ns, mtcs_common.AngularAcceleration, 'The position angle target acceleration, as calculated by SLALIB')
        self.__addInstance__("aziPointingModelOffset", ns, mtcs_common.AngularPosition, 'The azimuth pointing model offset calculated by the TPoint model')
        self.__addInstance__("elePointingModelOffset", ns, mtcs_common.AngularPosition, 'The elevation pointing model offset calculated by the TPoint model')
        self.__addInstance__("correctedAzi", ns, mtcs_common.AngularPosition, 'The azimuth target position, as calculated by SLALIB, corrected by the TPoint model')
        self.__addInstance__("correctedEle", ns, mtcs_common.AngularPosition, 'The elevation target position, as calculated by SLALIB, corrected by the TPoint model')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, AxesTargetStatuses, 'Statuses of the state machine')

class AxesTarget(SM_AxesTarget):
    def __init__(self, parent, name, ns, info):
        SM_AxesTarget.__init__(self, parent, name, ns, info)

class SM_AxesFeedback(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isValid", ns, 'True if the feedback is valid, false if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isTooLow", ns, 'True if the feedback is too low to calculate, false if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("alpha", ns, mtcs_common.AngularPosition, 'The alpha coordinate (Right Ascention)')
        self.__addInstance__("delta", ns, mtcs_common.AngularPosition, 'The delta coordinate (Declination)')
        self.__addInstance__("aziPos", ns, mtcs_common.AngularPosition, 'The measured AZI position, corrected by TPoint, and normalized to [0..2*PI]')
        self.__addInstance__("elePos", ns, mtcs_common.AngularPosition, 'The measured ELE position, corrected by TPoint, normalized to [-PI..PI]')
        self.__addInstance__("rocPos", ns, mtcs_common.AngularPosition, 'The measured ROC position, normalized to [-PI..PI]')
        self.__addInstance__("ronPos", ns, mtcs_common.AngularPosition, 'The measured RON position, normalized to [-PI..PI]')
        self.__addInstance__("rotPos", ns, mtcs_common.AngularPosition, 'The measured position of the currently active rotator (ROC or RON), normalized to [-PI..PI]')
        self.__addInstance__("rotOffset", ns, mtcs_common.AngularPosition, 'The active rotator offset, to North')
        self.__addInstance__("rocOffset", ns, mtcs_common.AngularPosition, 'The cassegrain rotator offset, to North')
        self.__addInstance__("ronOffset", ns, mtcs_common.AngularPosition, 'The nasmyth rotator offset, to North')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, AxesFeedbackStatuses, 'Statuses of the state machine')

class AxesFeedback(SM_AxesFeedback):
    def __init__(self, parent, name, ns, info):
        SM_AxesFeedback.__init__(self, parent, name, ns, info)

class SM_AxesAzimuthAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("id", ns, 'Id of this axis', datatype=AxesIds, permissions='r')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("REDUCTION_AZI_TO_TEL", ns, 'The mechanical reduction between absolute encoder and telescope', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("REDUCTION_ABL_TO_TEL", ns, 'The mechanical reduction between absolute encoder and telescope', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("REDUCTION_ABS_ENC_TO_TEL", ns, 'The mechanical reduction between absolute encoder and telescope', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("slipError", ns, 'TRUE if the motor appears to be slipping w.r.t. the external encoder', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("positiveLimitSwitchError", ns, 'TRUE if the positive limit switch has detected the axis', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("negativeLimitSwitchError", ns, 'TRUE if the negative limit switch has detected the axis', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("setPosLimitReached", ns, 'TRUE if the setpoint position has reached its limit', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("deviation1SecAverage", ns, mtcs_common.AngularPosition, 'The deviation between target position and actual position, as a 1 second moving average')
        self.__addInstance__("deviation1SecRMS", ns, mtcs_common.AngularPosition, 'The deviation between target position and actual position, as a 1 second moving RMS error')
        self.__addInstance__("targetPos", ns, mtcs_common.AngularPosition, 'The target position')
        self.__addInstance__("targetOffset", ns, mtcs_common.AngularPosition, 'Cumulative offset of targetPos. Equals targetPos - targetStart')
        self.__addInstance__("targetStart", ns, mtcs_common.AngularPosition, 'Last absolute movement end position of the axis')
        self.__addInstance__("setPos", ns, mtcs_common.AngularPosition, 'The setpoint position (same as parts.physicalAxis!)')
        self.__addInstance__("setVelo", ns, mtcs_common.AngularVelocity, 'The setpoint velocity (same as parts.physicalAxis!)')
        self.__addInstance__("setAcc", ns, mtcs_common.AngularAcceleration, 'The setpoint acceleration (same as parts.physicalAxis!)')
        self.__addInstance__("actPos", ns, mtcs_common.AngularPosition, 'The actual position (same as parts.physicalAxis!)')
        self.__addInstance__("actVelo", ns, mtcs_common.AngularVelocity, 'The actual velocity (same as parts.physicalAxis!)')
        self.__addInstance__("actAcc", ns, mtcs_common.AngularAcceleration, 'The actual acceleration (same as parts.physicalAxis!)')
        self.__addInstance__("actTorqueAzi", ns, mtcs_common.Torque, 'The actual torque on the telescope axis by the AZI motor')
        self.__addInstance__("actTorqueAbl", ns, mtcs_common.Torque, 'The actual torque on the telescope axis by the ABL motor')
        self.__addInstance__("lida1Position", ns, mtcs_common.AngularPosition, 'Position of the telescope according to LIDA encoder no. 1')
        self.__addInstance__("lida2Position", ns, mtcs_common.AngularPosition, 'Position of the telescope according to LIDA encoder no. 2')
        self.__addInstance__("lida3Position", ns, mtcs_common.AngularPosition, 'Position of the telescope according to LIDA encoder no. 3')
        self.__addInstance__("lida4Position", ns, mtcs_common.AngularPosition, 'Position of the telescope according to LIDA encoder no. 4')
        self.__addInstance__("lidaAveragePosition", ns, mtcs_common.AngularPosition, 'Position of the telescope according to the average of the LIDA encoders')
        self.__addInstance__("absoluteEncoderPosition", ns, mtcs_common.AngularPosition, 'The position of the axis, based on the absolute encoder')
        self.__addInstance__("statuses", ns, AxesAzimuthAxisStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AxesAzimuthAxisParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, AxesAzimuthAxisProcesses, 'Processes of the state machine')

class AxesAzimuthAxis(SM_AxesAzimuthAxis):
    def __init__(self, parent, name, ns, info):
        SM_AxesAzimuthAxis.__init__(self, parent, name, ns, info)

class SM_AxesElevationAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("id", ns, 'Id of this axis', datatype=AxesIds, permissions='r')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("REDUCTION_MOT_TO_TEL", ns, 'The mechanical reduction between absolute encoder and telescope', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("REDUCTION_ABS_ENC_TO_TEL", ns, 'The mechanical reduction between absolute encoder and telescope', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("slipError", ns, 'TRUE if the motor appears to be slipping w.r.t. the external encoder', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("positiveLimitSwitchError", ns, 'TRUE if the positive limit switch has detected the axis', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("negativeLimitSwitchError", ns, 'TRUE if the negative limit switch has detected the axis', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("setPosLimitReached", ns, 'TRUE if the setpoint position has reached its limit', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("deviation1SecAverage", ns, mtcs_common.AngularPosition, 'The deviation between target position and actual position, as a 1 second moving average')
        self.__addInstance__("deviation1SecRMS", ns, mtcs_common.AngularPosition, 'The deviation between target position and actual position, as a 1 second moving RMS error')
        self.__addInstance__("targetPos", ns, mtcs_common.AngularPosition, 'The target position')
        self.__addInstance__("targetOffset", ns, mtcs_common.AngularPosition, 'Cumulative offset of targetPos. Equals targetPos - targetStart')
        self.__addInstance__("targetStart", ns, mtcs_common.AngularPosition, 'Last absolute movement end position of the axis')
        self.__addInstance__("setPos", ns, mtcs_common.AngularPosition, 'The setpoint position (same as parts.physicalAxis!)')
        self.__addInstance__("setVelo", ns, mtcs_common.AngularVelocity, 'The setpoint velocity (same as parts.physicalAxis!)')
        self.__addInstance__("setAcc", ns, mtcs_common.AngularAcceleration, 'The setpoint acceleration (same as parts.physicalAxis!)')
        self.__addInstance__("actPos", ns, mtcs_common.AngularPosition, 'The actual position (same as parts.physicalAxis!)')
        self.__addInstance__("actVelo", ns, mtcs_common.AngularVelocity, 'The actual velocity (same as parts.physicalAxis!)')
        self.__addInstance__("actAcc", ns, mtcs_common.AngularAcceleration, 'The actual acceleration (same as parts.physicalAxis!)')
        self.__addInstance__("actTorque", ns, mtcs_common.Torque, 'The actual torque on the telescope axis by the ELE motor')
        self.__addInstance__("lida1Position", ns, mtcs_common.AngularPosition, 'Position of the telescope according to LIDA encoder no. 1')
        self.__addInstance__("lida2Position", ns, mtcs_common.AngularPosition, 'Position of the telescope according to LIDA encoder no. 2')
        self.__addInstance__("lidaAveragePosition", ns, mtcs_common.AngularPosition, 'Position of the telescope according to the average of the LIDA encoders')
        self.__addInstance__("absoluteEncoderPosition", ns, mtcs_common.AngularPosition, 'Position of the telescope according to the absolute encoder')
        self.__addInstance__("statuses", ns, AxesElevationAxisStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AxesElevationAxisParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, AxesElevationAxisProcesses, 'Processes of the state machine')

class AxesElevationAxis(SM_AxesElevationAxis):
    def __init__(self, parent, name, ns, info):
        SM_AxesElevationAxis.__init__(self, parent, name, ns, info)

class SM_AxesRotationAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("id", ns, 'Id of this axis', datatype=AxesIds, permissions='r')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("positiveLimitSwitchError", ns, 'TRUE if the positive limit switch has detected the axis', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("negativeLimitSwitchError", ns, 'TRUE if the negative limit switch has detected the axis', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("setPosLimitReached", ns, 'TRUE if the setpoint position has reached its limit', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("deviation1SecAverage", ns, mtcs_common.AngularPosition, 'The deviation between target position and actual position, as a 1 second moving average')
        self.__addInstance__("deviation1SecRMS", ns, mtcs_common.AngularPosition, 'The deviation between target position and actual position, as a 1 second moving RMS error')
        self.__addInstance__("targetPos", ns, mtcs_common.AngularPosition, 'The target position')
        self.__addInstance__("targetOffset", ns, mtcs_common.AngularPosition, 'Cumulative offset of targetPos. Equals targetPos - targetStart')
        self.__addInstance__("targetStart", ns, mtcs_common.AngularPosition, 'Last absolute movement end position of the axis')
        self.__addInstance__("setPos", ns, mtcs_common.AngularPosition, 'The setpoint position (same as parts.physicalAxis!)')
        self.__addInstance__("setVelo", ns, mtcs_common.AngularVelocity, 'The setpoint velocity (same as parts.physicalAxis!)')
        self.__addInstance__("setAcc", ns, mtcs_common.AngularAcceleration, 'The setpoint acceleration (same as parts.physicalAxis!)')
        self.__addInstance__("actPos", ns, mtcs_common.AngularPosition, 'The actual position (same as parts.eleAxis!)')
        self.__addInstance__("actVelo", ns, mtcs_common.AngularVelocity, 'The actual velocity (same as parts.eleAxis!)')
        self.__addInstance__("actAcc", ns, mtcs_common.AngularAcceleration, 'The actual acceleration (same as parts.eleAxis!)')
        self.__addInstance__("actTorque", ns, mtcs_common.Torque, 'The actual torque on the telescope axis by the ELE motor')
        self.__addInstance__("statuses", ns, AxesRotationAxisStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AxesRotationAxisParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, AxesRotationAxisProcesses, 'Processes of the state machine')

class AxesRotationAxis(SM_AxesRotationAxis):
    def __init__(self, parent, name, ns, info):
        SM_AxesRotationAxis.__init__(self, parent, name, ns, info)

class SM_AxesPointingModelSetup(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, AxesPointingModelConfig, 'Editable configuration of the particular TPOINT model')
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, AxesPointingModelConfig, 'Active configuration of the particular TPOINT model')
        self.__addInstance__("parts", ns, AxesPointingModelSetupParts, 'Parts of the state machine')

class AxesPointingModelSetup(SM_AxesPointingModelSetup):
    def __init__(self, parent, name, ns, info):
        SM_AxesPointingModelSetup.__init__(self, parent, name, ns, info)

class SM_AxesPointingModelsSetup(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, AxesPointingModelsSetupStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AxesPointingModelsSetupParts, 'Parts of the state machine')

class AxesPointingModelsSetup(SM_AxesPointingModelsSetup):
    def __init__(self, parent, name, ns, info):
        SM_AxesPointingModelsSetup.__init__(self, parent, name, ns, info)

class SM_AxesIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, AxesIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, AxesIOParts, 'Parts of the state machine')

class AxesIO(SM_AxesIO):
    def __init__(self, parent, name, ns, info):
        SM_AxesIO.__init__(self, parent, name, ns, info)

class AxesSetTargetProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesSetTargetProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesSetTargetProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesPointProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State of the process', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addInstance__("set", ns, AxesPointProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesPointProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesPointRelativeProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesPointRelativeProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesPointRelativeProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesMoveRelativeProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesMoveRelativeProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMoveRelativeProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesMoveAbsoluteProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesMoveAbsoluteProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMoveAbsoluteProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesMoveKnownPositionProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesMoveKnownPositionProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMoveKnownPositionProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesMoveVelocityProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesMoveVelocityProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMoveVelocityProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesMoveOutOfLimitSwitchProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesMoveOutOfLimitSwitchProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMoveOutOfLimitSwitchProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesPowerOnProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State of the process', datatype=pyuaf.util.primitives.UInt16, permissions='')


class AxesMultiPowerOnProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State of the process', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addInstance__("set", ns, AxesMultiPowerOnProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMultiPowerOnProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesPowerOffProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State of the process', datatype=pyuaf.util.primitives.UInt16, permissions='')


class AxesStopProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State of the process', datatype=pyuaf.util.primitives.UInt16, permissions='')


class AxesSetAlphaDeltaVelocityProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesSetAlphaDeltaVelocityProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesSetAlphaDeltaVelocityProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesDoHomingProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State of the process', datatype=pyuaf.util.primitives.UInt16, permissions='')


class AxesMultiMoveProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addVariable__("waitingForAzi", ns, 'True if the process is waiting for AZI', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("waitingForEle", ns, 'True if the process is waiting for ELE', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("waitingForRoc", ns, 'True if the process is waiting for ROC', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("waitingForRon", ns, 'True if the process is waiting for RON', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addInstance__("set", ns, AxesMultiMoveProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesMultiMoveProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesEnablePointingModelProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesEnablePointingModelProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesEnablePointingModelProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesUnlockBrakeProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesUnlockBrakeProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesUnlockBrakeProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class AxesSetPositionProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, AxesSetPositionProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, AxesSetPositionProcessArgs, 'Arguments in use by the process, if do_request was accepted')




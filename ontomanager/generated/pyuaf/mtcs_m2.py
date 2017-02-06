# === imports ===

import mtcs_common
import mtcs_m3


# This file (mtcs_m2.py) was automatically generated at 2017-02-03T09:55:44.775734 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class M2Axes:
        X = 0
        Y = 1
        Z = 2
        TILTX = 3
        TILTY = 4

class M2MoveProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        MOVING = 3
        MOVING_TO_ANTI_BACKLASH_POSITION = 4
        MOVING_CLOSE_TO_FINAL_POSITION = 5
        MOVING_TO_FINAL_POSITION = 6
        ERROR = 7
        ABORTING = 8


# === STRUCTS ===

class M2Parts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("powerRelay", ns, mtcs_common.SimpleRelay, 'Relay to power on/off the power of the M2 field electricity')
        self.__addInstance__("heater", ns, mtcs_common.SimpleRelay, 'Digital output to power on/off the heater of M2')
        self.__addInstance__("x", ns, M2XAxis, 'The X axis')
        self.__addInstance__("y", ns, M2YAxis, 'The Y axis')
        self.__addInstance__("z", ns, M2ZAxis, 'The Z axis')
        self.__addInstance__("tiltX", ns, M2TiltXAxis, 'The TiltX axis')
        self.__addInstance__("tiltY", ns, M2TiltYAxis, 'The TiltY axis')
        self.__addInstance__("multiplexer", ns, M2Multiplexer, 'The multiplexer inputs and outputs')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')
        self.__addInstance__("moveStepsProcedure", ns, M2MoveStepsProcedure, 'The move steps procedure')
        self.__addInstance__("movePositionProcedure", ns, M2MovePositionProcedure, 'The move to a certain position procedure')

class M2MultiplexerParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("A", ns, mtcs_common.SimpleRelay, 'Output A of the multiplexer corresponding with the selected axis')
        self.__addInstance__("B", ns, mtcs_common.SimpleRelay, 'Output B of the multiplexer corresponding with the selected axis')
        self.__addInstance__("C", ns, mtcs_common.SimpleRelay, 'Output C of the multiplexer corresponding with the selected axis')
        self.__addInstance__("driveEnable", ns, mtcs_common.SimpleRelay, 'Enabled (TRUE) if the drive selected by the multiplexer must be enabled, Disabled (FALSE) if it must be disabled')
        self.__addInstance__("CW", ns, mtcs_common.SimpleRelay, 'Enabled (TRUE) if the motor selected by the multiplexer will run in CW direction (- motion on the screw), Disabled (FALSE) if it will run in CCW direction (+ motion on the screw)')
        self.__addInstance__("release", ns, mtcs_common.SimpleRelay, 'Disabled (FALSE) if the motor selected by the multiplexer must be braking, Enabled (TRUE) if it must be released')

class M2ZAxisParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("highSpeed", ns, mtcs_common.SimpleRelay, 'Enabled (TRUE) to enable the high-speed motion of the Z axis, Disabled (FALSE) to leave it low-speed')
        self.__addInstance__("encoder", ns, mtcs_common.SSIEncoder, 'The SSI encoder of the Z axis')

class M2Processes(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')
        self.__addInstance__("moveAbsolute", ns, M2MoveProcess, 'Move the position of one axis in an absolute way')
        self.__addInstance__("moveRelative", ns, M2MoveProcess, 'Move the position of one axis relative to the current position')
        self.__addInstance__("moveSteps", ns, M2MoveStepsProcess, 'Move the position of one axis by providing a number of steps (i.e. motor pulses)')
        self.__addInstance__("doThermalFocus", ns, mtcs_common.Process, 'Do a thermal focus for the currently active focus')
        self.__addInstance__("doThermalFocusForStationName", ns, M2DoThermalFocusForStationName, 'Do a thermal focus for a specified focal station (based on the configured name of the station)')
        self.__addInstance__("doThermalFocusForStationPosition", ns, M2DoThermalFocusForStationPosition, 'Do a thermal focus for a specified focal station (based on the station numerical ID)')
        self.__addInstance__("verifyFixedPositions", ns, mtcs_common.Process, 'Verify (and adjust if necessary) the fixed positions of X, Y, TiltX, and TiltY')
        self.__addInstance__("powerOn", ns, mtcs_common.Process, 'Power on the M2 electricity')
        self.__addInstance__("powerOff", ns, mtcs_common.Process, 'Power off the M2 electricity')
        self.__addInstance__("abort", ns, mtcs_common.Process, 'Abort the move procedure')

class M2MultiplexerProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("selectAxis", ns, M2SelectAxisProcess, 'Select an axis')

class M2Statuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class M2MultiplexerStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the selected drive healthy?')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the selected drive busy?')

class M2XAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis healthy?')

class M2YAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis healthy?')

class M2TiltXAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis healthy?')

class M2TiltYAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis healthy?')

class M2ZAxisStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the axis healthy?')

class M2MoveStepsProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M2MoveStepsProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M2MoveStepsProcedure in a healthy state?')

class M2MovePositionProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M2MoveAbsoluteProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M2MoveAbsoluteProcedure in a healthy state?')

class M2Config(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("x", ns, M2PotentiometerAxisConfig, 'The config of the X axis')
        self.__addInstance__("y", ns, M2PotentiometerAxisConfig, 'The config of the Y axis')
        self.__addInstance__("z", ns, M2ZAxisConfig, 'The config of the Z axis')
        self.__addInstance__("tiltX", ns, M2PotentiometerAxisConfig, 'The config of the tiltX axis')
        self.__addInstance__("tiltY", ns, M2PotentiometerAxisConfig, 'The config of the tiltY axis')
        self.__addInstance__("thermalFocus", ns, M2ThermalFocusConfig, 'The thermal focus coefficients for all focal stations')
        self.__addVariable__("waitAfterPowerOn", ns, 'Time (in seconds) to wait after the field electricity of M2 have been powered on', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("waitAfterPowerOff", ns, 'Time (in seconds) to wait after the field electricity of M2 have been powered off', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("powerOffTimeout", ns, 'If no new command is sent to M2 within this time (in seconds) after completion of the last command, M2 will be powered off automatically', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedXPosition", ns, 'The fixed X position in mm', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedXPositionTolerance", ns, 'If the X position is within fixedXPosition +/- this tolerance, there&#39;s no need to adjust it', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedYPosition", ns, 'The fixed Y position in mm', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedYPositionTolerance", ns, 'If the Y position is within fixedYPosition +/- this tolerance, there&#39;s no need to adjust it', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedTiltXPosition", ns, 'The fixed TiltX position in mm', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedTiltXPositionTolerance", ns, 'If the TiltX position is within fixedTiltXPosition +/- this tolerance, there&#39;s no need to adjust it', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedTiltYPosition", ns, 'The fixed TiltY position in mm', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("fixedTiltYPositionTolerance", ns, 'If the TiltY position is within fixedTiltYPosition +/- this tolerance, there&#39;s no need to adjust it', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("verifyFixedPositinsOnThermalFocus", ns, 'Each time a theremal focus is done, verify the fixed positions (and adjust them if they fall out of the tolerance)', datatype=pyuaf.util.primitives.Boolean, permissions='')

class M2ThermalFocusStationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("offset", ns, 'focus = offset + topCoefficient*topTemperature + centreCoefficient*centreTemperature + mirrorCellCoefficient*mirrorCellTemperature', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("topCoefficient", ns, 'focus = offset + topCoefficient*topTemperature + centreCoefficient*centreTemperature + mirrorCellCoefficient*mirrorCellTemperature', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("centreCoefficient", ns, 'focus = offset + topCoefficient*topTemperature + centreCoefficient*centreTemperature + mirrorCellCoefficient*mirrorCellTemperature', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("mirrorCellCoefficient", ns, 'focus = offset + topCoefficient*topTemperature + centreCoefficient*centreTemperature + mirrorCellCoefficient*mirrorCellTemperature', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ThermalFocusConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("cassegrain", ns, M2ThermalFocusStationConfig, 'Cassegrain thermal focus config')
        self.__addInstance__("nasmythA", ns, M2ThermalFocusStationConfig, 'Nasmyth A thermal focus config')
        self.__addInstance__("nasmythB", ns, M2ThermalFocusStationConfig, 'Nasmyth B thermal focus config')
        self.__addInstance__("nasmythC", ns, M2ThermalFocusStationConfig, 'Nasmyth C thermal focus config')
        self.__addInstance__("nasmythD", ns, M2ThermalFocusStationConfig, 'Nasmyth D thermal focus config')
        self.__addInstance__("other0", ns, M2ThermalFocusStationConfig, 'Other 0 thermal focus config')
        self.__addInstance__("other1", ns, M2ThermalFocusStationConfig, 'Other 1 thermal focus config')
        self.__addInstance__("other2", ns, M2ThermalFocusStationConfig, 'Other 2 thermal focus config')
        self.__addInstance__("other3", ns, M2ThermalFocusStationConfig, 'Other 3 thermal focus config')
        self.__addInstance__("other4", ns, M2ThermalFocusStationConfig, 'Other 4 thermal focus config')

class M2AxisGeneralConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("measurement", ns, mtcs_common.MeasurementConfig, 'Configure the position measurement')
        self.__addVariable__("stoppingSteps", ns, 'The number of steps to be expected between the time at which the PLC realizes that the brake release signal must be set, and the time that the axis is fully stopped (for Z axis: at low speed)', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("finalSenseCW", ns, 'TRUE if the motor final sense must be ClockWise (- motion on the screw), FALSE if the motor final sense must be CounterClockWise (+ motion on the screw) (for Z axis: at low speed)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("closePosition", ns, 'The number of steps between the Close position (C) and final position (F)', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("antiBacklashPosition", ns, 'The number of steps between the Anti-backlash position (A) and final position (F)', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("waitAfterMove", ns, 'Time (in seconds) to wait after the axis has been moved', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("timeout", ns, 'Timeout for a movement, in seconds (for Z-axis: at low speed)', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ZAxisConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("general", ns, M2AxisGeneralConfig, 'Settings which are general for all axes')
        self.__addVariable__("highSpeedStoppingSteps", ns, 'The number of steps to be expected between the time at which the PLC realizes that the brake release signal must be set, and the time that the axis is fully stopped at high speed', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("highSpeedTimeout", ns, 'Timeout for a fast movement of the Z axis (in seconds)', datatype=pyuaf.util.primitives.Double, permissions='')

class M2PotentiometerAxisConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("general", ns, M2AxisGeneralConfig, 'Settings which are general for all axes')
        self.__addVariable__("voltageCorrectionFactor", ns, 'Position = voltage * correctionFactor * voltageToPosition', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ConstantsZ(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("MOT_TO_RED_RATIO", ns, 'Motor reduction ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("RED_TO_SCREW_RATIO", ns, 'Transmission ratio between the motor reduction and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_TO_ENC_RATIO", ns, 'Transmission ratio between the encoder and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MIN_POSITION", ns, 'Minimum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MAX_POSITION", ns, 'Maximum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_PITCH", ns, 'Screw pitch, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("FEEDBACK_RESOLUTION", ns, 'Motor feedback resolution (pulses per revolution of the motor rotor)', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ConstantsX(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("MOT_TO_RED_RATIO", ns, 'Motor reduction ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("RED_TO_SCREW_RATIO", ns, 'Transmission ratio between the motor reduction and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_TO_POT_RATIO", ns, 'Transmission ratio between the potentiometer and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MIN_POSITION", ns, 'Minimum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MAX_POSITION", ns, 'Maximum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_PITCH", ns, 'Screw pitch, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("FEEDBACK_RESOLUTION", ns, 'Motor feedback resolution (pulses per revolution of the motor rotor)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("POTENTIOMETER_REVOLUTIONS", ns, 'Max number of revolutions of the potentiometer', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ConstantsY(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("MOT_TO_RED_RATIO", ns, 'Motor reduction ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("RED_TO_SCREW_RATIO", ns, 'Transmission ratio between the motor reduction and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_TO_POT_RATIO", ns, 'Transmission ratio between the potentiometer and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MIN_POSITION", ns, 'Minimum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MAX_POSITION", ns, 'Maximum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_PITCH", ns, 'Screw pitch, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("FEEDBACK_RESOLUTION", ns, 'Motor feedback resolution (pulses per revolution of the motor rotor)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("POTENTIOMETER_REVOLUTIONS", ns, 'Max number of revolutions of the potentiometer', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ConstantsTiltX(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("MOT_TO_RED_RATIO", ns, 'Motor reduction ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("RED_TO_SCREW_RATIO", ns, 'Transmission ratio between the motor reduction and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_TO_POT_RATIO", ns, 'Transmission ratio between the potentiometer and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MIN_POSITION", ns, 'Minimum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MAX_POSITION", ns, 'Maximum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_PITCH", ns, 'Screw pitch, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("FEEDBACK_RESOLUTION", ns, 'Motor feedback resolution (pulses per revolution of the motor rotor)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("POTENTIOMETER_REVOLUTIONS", ns, 'Max number of revolutions of the potentiometer', datatype=pyuaf.util.primitives.Double, permissions='')

class M2ConstantsTiltY(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("MOT_TO_RED_RATIO", ns, 'Motor reduction ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("RED_TO_SCREW_RATIO", ns, 'Transmission ratio between the motor reduction and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_TO_POT_RATIO", ns, 'Transmission ratio between the potentiometer and the screw', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MIN_POSITION", ns, 'Minimum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("MAX_POSITION", ns, 'Maximum position of the axis, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SCREW_PITCH", ns, 'Screw pitch, in micrometer', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("FEEDBACK_RESOLUTION", ns, 'Motor feedback resolution (pulses per revolution of the motor rotor)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("POTENTIOMETER_REVOLUTIONS", ns, 'Max number of revolutions of the potentiometer', datatype=pyuaf.util.primitives.Double, permissions='')

class M2SelectAxisProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("axis", ns, 'The axis to select', datatype=M2Axes, permissions='')

class M2MoveProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("axis", ns, 'The axis to move', datatype=M2Axes, permissions='')
        self.__addVariable__("position", ns, 'Move to a certain position in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')

class M2MoveStepsProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("axis", ns, 'The axis to move', datatype=M2Axes, permissions='')
        self.__addVariable__("steps", ns, 'Move a certain number of steps', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("cw", ns, 'True if the axis should be moved in CW (negative) direction', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("fast", ns, 'True if the axis should be moved fast (only used in case of Z-axis!)', datatype=pyuaf.util.primitives.Boolean, permissions='')

class M2DoThermalFocusForStationPositionArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("station", ns, 'The station numerical ID for which the thermal focus should be executed', datatype=mtcs_m3.M3PositionIDs, permissions='')

class M2DoThermalFocusForStationNameArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("station", ns, 'The configured station name, for which the thermal focus should be executed', datatype=pyuaf.util.primitives.String, permissions='')


# === FBs ===

class SM_M2(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, M2Config, 'Editable configuration of the M2 subsystem')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, M2Config, 'Active configuration of the M2 subsystem')
        self.__addVariable__("selectedAxis", ns, 'The axis which is currently selected by the multiplexer', datatype=M2Axes, permissions='r')
        self.__addVariable__("selectedAxisName", ns, 'The name of the axis which is currently selected by the multiplexer', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("powerOffTimer", ns, 'Number of seconds before the power of the M2 field electricity will be powered off automatically', datatype=pyuaf.util.primitives.Double, permissions='r')
        self.__addInstance__("thermalFocusCassegrain", ns, mtcs_common.LinearPosition, 'Thermal focus position for cassegrain')
        self.__addInstance__("thermalFocusNasmythA", ns, mtcs_common.LinearPosition, 'Thermal focus position for nasmyth A')
        self.__addInstance__("thermalFocusNasmythB", ns, mtcs_common.LinearPosition, 'Thermal focus position for nasmyth B')
        self.__addInstance__("thermalFocusNasmythC", ns, mtcs_common.LinearPosition, 'Thermal focus position for nasmyth C')
        self.__addInstance__("thermalFocusNasmythD", ns, mtcs_common.LinearPosition, 'Thermal focus position for nasmyth D')
        self.__addInstance__("thermalFocusActualFocalStation", ns, mtcs_common.LinearPosition, 'Thermal focus position for nasmyth D')
        self.__addInstance__("statuses", ns, M2Statuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M2Parts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M2Processes, 'Processes of the state machine')

class M2(SM_M2):
    def __init__(self, parent, name, ns, info):
        SM_M2.__init__(self, parent, name, ns, info)

class SM_M2Multiplexer(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("noFault", ns, 'FALSE if the drive selected by the multiplexer is in faulty state, TRUE if it is in a healthy state', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isEnabled", ns, 'TRUE if the multiplexer is enabled, FALSE if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powered", ns, 'TRUE if the axis is powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M2MultiplexerStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M2MultiplexerParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M2MultiplexerProcesses, 'Processes of the state machine')

class M2Multiplexer(SM_M2Multiplexer):
    def __init__(self, parent, name, ns, info):
        SM_M2Multiplexer.__init__(self, parent, name, ns, info)

class SM_M2XAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position", ns, mtcs_common.LinearPositionMeasurement16, 'Actual position of the axis')
        self.__addVariable__("backlashLifted", ns, 'TRUE if the backlash was previously lifted', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powered", ns, 'TRUE if the axis is powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("constants", ns, M2ConstantsX, 'Some constants particular for this axis')
        self.__addInstance__("statuses", ns, M2XAxisStatuses, 'Statuses of the state machine')

class M2XAxis(SM_M2XAxis):
    def __init__(self, parent, name, ns, info):
        SM_M2XAxis.__init__(self, parent, name, ns, info)

class SM_M2YAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position", ns, mtcs_common.LinearPositionMeasurement16, 'Actual position of the axis')
        self.__addVariable__("backlashLifted", ns, 'TRUE if the backlash was previously lifted', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powered", ns, 'TRUE if the axis is powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("constants", ns, M2ConstantsY, 'Some constants particular for this axis')
        self.__addInstance__("statuses", ns, M2YAxisStatuses, 'Statuses of the state machine')

class M2YAxis(SM_M2YAxis):
    def __init__(self, parent, name, ns, info):
        SM_M2YAxis.__init__(self, parent, name, ns, info)

class SM_M2TiltXAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position", ns, mtcs_common.LinearPositionMeasurement16, 'Actual position of the axis')
        self.__addVariable__("backlashLifted", ns, 'TRUE if the backlash was previously lifted', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powered", ns, 'TRUE if the axis is powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("constants", ns, M2ConstantsTiltX, 'Some constants particular for this axis')
        self.__addInstance__("statuses", ns, M2TiltXAxisStatuses, 'Statuses of the state machine')

class M2TiltXAxis(SM_M2TiltXAxis):
    def __init__(self, parent, name, ns, info):
        SM_M2TiltXAxis.__init__(self, parent, name, ns, info)

class SM_M2TiltYAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position", ns, mtcs_common.LinearPositionMeasurement16, 'Actual position of the axis')
        self.__addVariable__("backlashLifted", ns, 'TRUE if the backlash was previously lifted', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powered", ns, 'TRUE if the axis is powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("constants", ns, M2ConstantsTiltY, 'Some constants particular for this axis')
        self.__addInstance__("statuses", ns, M2TiltYAxisStatuses, 'Statuses of the state machine')

class M2TiltYAxis(SM_M2TiltYAxis):
    def __init__(self, parent, name, ns, info):
        SM_M2TiltYAxis.__init__(self, parent, name, ns, info)

class SM_M2ZAxis(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position", ns, mtcs_common.LinearPositionMeasurementU32, 'Actual position of the axis')
        self.__addVariable__("backlashLifted", ns, 'TRUE if the backlash was previously lifted', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("powered", ns, 'TRUE if the axis is powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isEnabled", ns, 'TRUE if the Z axis control is enabled, FALSE if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("constants", ns, M2ConstantsZ, 'Some constants particular for this axis')
        self.__addInstance__("statuses", ns, M2ZAxisStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M2ZAxisParts, 'Parts of the state machine')

class M2ZAxis(SM_M2ZAxis):
    def __init__(self, parent, name, ns, info):
        SM_M2ZAxis.__init__(self, parent, name, ns, info)

class SM_M2MoveStepsProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New state, to be set by the manual implementation', datatype=M2MoveProcedureStates, permissions='r')
        self.__addVariable__("actualCounterValue", ns, 'Actual counter value', datatype=pyuaf.util.primitives.Int32, permissions='r')
        self.__addVariable__("stepsRemaining", ns, 'Number of steps remaining', datatype=pyuaf.util.primitives.Int32, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M2MoveStepsProcedureStatuses, 'Statuses of the state machine')

class M2MoveStepsProcedure(SM_M2MoveStepsProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M2MoveStepsProcedure.__init__(self, parent, name, ns, info)

class SM_M2MovePositionProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New state, to be set by the manual implementation', datatype=M2MoveProcedureStates, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M2MovePositionProcedureStatuses, 'Statuses of the state machine')

class M2MovePositionProcedure(SM_M2MovePositionProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M2MovePositionProcedure.__init__(self, parent, name, ns, info)

class M2SelectAxisProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M2SelectAxisProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M2SelectAxisProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class M2MoveProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M2MoveProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M2MoveProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class M2MoveStepsProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M2MoveStepsProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M2MoveStepsProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class M2DoThermalFocusForStationPosition(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M2DoThermalFocusForStationPositionArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M2DoThermalFocusForStationPositionArgs, 'Arguments in use by the process, if do_request was accepted')


class M2DoThermalFocusForStationName(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M2DoThermalFocusForStationNameArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M2DoThermalFocusForStationNameArgs, 'Arguments in use by the process, if do_request was accepted')




# === imports ===

import mtcs_common


# This file (mtcs_m3.py) was automatically generated at 2017-02-03T09:55:37.180511 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class M3PositionIDs:
        UNKNOWN = 0
        CASSEGRAIN = 1
        NASMYTH_A = 2
        NASMYTH_B = 3
        NASMYTH_C = 4
        NASMYTH_D = 5
        OTHER_0 = 6
        OTHER_1 = 7
        OTHER_2 = 8
        OTHER_3 = 9
        OTHER_4 = 10

class M3GotoProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        GOING_TO_POSITION = 3
        IMPROVING_POSITION = 4
        ERROR = 5
        RESETTING = 6
        ABORTING = 7

class M3RotateProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        DECOUPLING_AXES = 3
        ENABLING_AXES = 4
        UNDOING_OFFSET = 5
        COUPLING_AXES = 6
        BOTH_GOING_TO_TARGET_PLUS_OFFSET = 7
        DECOUPLING_AXES_AGAIN = 8
        MOVING_ABL_TO_FINAL_POSITION = 9
        DISABLING_ABL = 10
        MOVING_POS_TO_FINAL_POSITION = 11
        IMPROVING_POSITION = 12
        DISABLING_POS = 13
        ERROR = 14
        RESETTING = 15
        ABORTING = 16

class M3TranslateProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        ENABLING_AXIS = 3
        MOVING = 4
        IMPROVING_POSITION = 5
        DISABLING_AXIS = 6
        ERROR = 7
        RESETTING = 8
        ABORTING = 9

class M3TranslationHomingProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        ENABLING_AXIS = 3
        MOVE_TO_LIMIT_SWITCH = 4
        WAIT_FOR_LIMIT_SWITCH = 5
        STOP = 6
        APPLY_HOMING_SETTINGS = 7
        MOVE_TO_MECH_STOP = 8
        WAIT_FOR_MECH_STOP = 9
        SET_ZERO_POSITION = 10
        DISABLE_AXIS = 11
        RESETTING = 12
        ERROR = 13
        ABORTING = 14

class M3CalibrateRotationProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        DECOUPLING_AXES = 3
        ENABLING_AXES = 4
        COUPLING_AXES = 5
        GOING_TO_START_POSITION = 6
        DECOUPLING_AXES_AGAIN = 7
        START_MOVING = 8
        WAIT_UNTIL_MOVING_STABLE = 9
        WAIT_UNTIL_RANGE_PASSED = 10
        HALT = 11
        GO_TO_CLUTCH_ZERO_TORQUE = 12
        DISABLING_AXES = 13
        WAIT_UNTIL_STANDSTILL = 14
        SYNC_AXES = 15
        ERROR = 16
        RESETTING = 17
        ABORTING = 18

class M3TargetStates:
        NO_TARGET_GIVEN = 0
        KNOWN_POSITION = 1
        NEW_POSITION = 2


# === STRUCTS ===

class M3Parts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("rotation", ns, M3Rotation, 'Rotation mechanism')
        self.__addInstance__("translation", ns, M3Translation, 'Translation mechanism')
        self.__addInstance__("io", ns, M3IO, 'I/O modules')
        self.__addInstance__("gotoProcedure", ns, M3GotoProcedure, 'The goto procedure')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class M3RotationParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("positioningAxis", ns, mtcs_common.AngularAxis, 'Positioning axis: SSI encoder + Faulhaber drive')
        self.__addInstance__("antiBacklashAxis", ns, mtcs_common.AngularAxis, 'Anti-backlash Axis: Faulhaber drive + hall sensors')
        self.__addInstance__("positioningDrive", ns, mtcs_common.FaulhaberDrive, 'Positioning drive')
        self.__addInstance__("antiBacklashDrive", ns, mtcs_common.FaulhaberDrive, 'Anti-backlash drive')
        self.__addInstance__("positioningHallAxis", ns, mtcs_common.AngularAxis, 'Only hall sensors')
        self.__addInstance__("gotoProcedure", ns, M3RotationGotoProcedure, 'The goto procedure')
        self.__addInstance__("calibrateProcedure", ns, M3RotationCalibrateProcedure, 'The calibration procedure')

class M3TranslationParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("motorAxis", ns, mtcs_common.LinearAxis, 'Motor axis')
        self.__addInstance__("motorDrive", ns, mtcs_common.FaulhaberDrive, 'Motor drive')
        self.__addInstance__("gotoProcedure", ns, M3TranslationGotoProcedure, 'The goto procedure')
        self.__addInstance__("homingProcedure", ns, M3TranslationHomingProcedure, 'The homing procedure')

class M3IOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("canOpenBus", ns, mtcs_common.CANopenBus, 'CANopen bus')
        self.__addInstance__("coupler", ns, mtcs_common.EtherCatDevice, 'Coupler')
        self.__addInstance__("slot1", ns, mtcs_common.EtherCatDevice, 'Slot 1')
        self.__addInstance__("slot2", ns, mtcs_common.EtherCatDevice, 'Slot 2')
        self.__addInstance__("slot3", ns, mtcs_common.EtherCatDevice, 'Slot 3')
        self.__addInstance__("slot4", ns, mtcs_common.EtherCatDevice, 'Slot 4')

class M3Processes(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset any errors')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')
        self.__addInstance__("gotoKnownPosition", ns, M3GotoKnownPosition, 'Go to the known position with the given name (only in AUTO mode!)')
        self.__addInstance__("gotoNewPosition", ns, M3GotoNewPosition, 'Go to the new position with the given settings (only in AUTO mode!)')
        self.__addInstance__("abort", ns, mtcs_common.Process, 'Abort the goto procedure')

class M3RotationProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("goto", ns, M3RotationGoto, 'Start moving the rotation stage to the given position')
        self.__addInstance__("abort", ns, mtcs_common.Process, 'Abort any running procedures')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset any errors')
        self.__addInstance__("calibrate", ns, mtcs_common.Process, 'Start calibrating the rotation stage')

class M3TranslationProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("goto", ns, M3TranslationGoto, 'Start moving the translation stage to the given position')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset any errors')
        self.__addInstance__("abort", ns, mtcs_common.Process, 'Abort any running procedures')
        self.__addInstance__("startHoming", ns, mtcs_common.Process, 'Start the homing procedure')

class M3RotationTargetStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("targetStatus", ns, M3TargetStatus, '')

class M3TranslationTargetStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("targetStatus", ns, M3TargetStatus, '')

class M3Statuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("apertureStatus", ns, mtcs_common.ApertureStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class M3GotoProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M3GotoProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M3GotoProcedure in a healthy state?')

class M3RotationStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')

class M3RotationGotoProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M3RotationGotoProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M3RotationGotoProcedure in a healthy state?')

class M3RotationCalibrateProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M3RotationCalibrateProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M3RotationCalibrateProcedure in a healthy state?')

class M3TranslationStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')

class M3TranslationGotoProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M3GotoProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M3GotoProcedure in a healthy state?')

class M3TranslationHomingProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the M3GotoProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the M3GotoProcedure in a healthy state?')

class M3IOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class M3PositionConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'The name of the M3 position', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("rotationPosition", ns, 'The position of the rotation stage in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rotationOffset", ns, 'The offset between the positions of the two motors of the rotation stage in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("translationPosition", ns, 'The position of the translation stage in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("doRotation", ns, 'Do a rotation for this position (TRUE) or not (FALSE)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doTranslation", ns, 'Do a translation for this position (TRUE) or not (FALSE)', datatype=pyuaf.util.primitives.Boolean, permissions='')

class M3KnownPositionsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("cassegrain", ns, M3PositionConfig, 'Cassegrain')
        self.__addInstance__("nasmythA", ns, M3PositionConfig, 'Nasmyth A')
        self.__addInstance__("nasmythB", ns, M3PositionConfig, 'Nasmyth B')
        self.__addInstance__("nasmythC", ns, M3PositionConfig, 'Nasmyth C')
        self.__addInstance__("nasmythD", ns, M3PositionConfig, 'Nasmyth D')
        self.__addInstance__("other0", ns, M3PositionConfig, 'Freely choosable position 0')
        self.__addInstance__("other1", ns, M3PositionConfig, 'Freely choosable position 1')
        self.__addInstance__("other2", ns, M3PositionConfig, 'Freely choosable position 2')
        self.__addInstance__("other3", ns, M3PositionConfig, 'Freely choosable position 3')
        self.__addInstance__("other4", ns, M3PositionConfig, 'Freely choosable position 4')

class M3RotationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("standstillTolerance", ns, 'The tolerance for which the axis appears to be standing still, in degrees/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("motorToMirrorRatio", ns, 'The motor-to-mirror transmission ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("encoderToMirrorRatio", ns, 'The encoder-to-mirror transmission ratio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("positioningDrive", ns, mtcs_common.FaulhaberDriveConfig, 'The config of the positioning faulhaber drive')
        self.__addInstance__("antiBacklashDrive", ns, mtcs_common.FaulhaberDriveConfig, 'The config of the anti-backlash faulhaber drive')
        self.__addVariable__("negativeSoftLimit", ns, 'Negative soft limit, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("positiveSoftLimit", ns, 'Negative soft limit, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionError", ns, 'Maximum position error, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxOffsetError", ns, 'Maximum position error, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("gotoOffsetVelocity", ns, 'Velocity to move from/to the offset position, in degrees/sec on the MOTOR reduction exit shaft reference system', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("gotoTargetVelocity", ns, 'Velocity to move to the target, in degrees/sec on the MIRROR reference system', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("gotoImprovingPositionTime", ns, 'Time while the Goto procedure may improve the position, in seconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("calibrateStartPosition", ns, 'Mirror position (in degrees) to start the calibration from', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("calibrateMoveToZeroTorqueVelocity", ns, 'Velocity to move to the zero-torque position, in degrees/sec on the MIRROR reference system', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("calibrateVelocity", ns, 'Velocity during which the current is being measured, in degrees/sec on the MIRROR reference system', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("calibrateRange", ns, 'Position range where the current is being measured, in degrees on the MOTOR reference system', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("calibrateOffset", ns, 'Degrees between zero-torque position and minimum-torque position, on the MOTOR reference system', datatype=pyuaf.util.primitives.Double, permissions='')

class M3TranslationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("homingContinuousCurrentLimit", ns, 'The continuous current limit for the translation stage motor in milliAmps, during homing', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("homingPeakCurrentLimit", ns, 'The peak current limit for the translation stage motor in milliAmps, during homing', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("homingSearchLimitSwitchVelocity", ns, 'The velocity of the motor shaft during homing, in mm/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("homingToHardwareStopVelocity", ns, 'The velocity of the motor shaft during homing, in mm/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("standstillTolerance", ns, 'The tolerance for which the axis appears to be standing still, in mm/sec', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("motorDrive", ns, mtcs_common.FaulhaberDriveConfig, 'The config of the faulhaber drive')
        self.__addVariable__("negativeSoftLimit", ns, 'Negative soft limit, in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("positiveSoftLimit", ns, 'Negative soft limit, in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxPositionError", ns, 'Maximum position error, in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("drawCassegrainLimit", ns, 'Below this limit (in millimeters) the mirror will be drawn flipped away', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("drawNasmythLimit", ns, 'Above this limit (in millimeters) the mirror will be drawn frontal', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("gotoImprovingPositionTime", ns, 'Time while the Goto procedure may improve the position, in seconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("gotoVelocity", ns, 'Velocity to go to a new position, in degrees/second', datatype=pyuaf.util.primitives.Double, permissions='')

class M3Config(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("knownPositions", ns, M3KnownPositionsConfig, 'All known M3 positions')
        self.__addInstance__("rotation", ns, M3RotationConfig, 'The settings of the rotation stage')
        self.__addInstance__("translation", ns, M3TranslationConfig, 'The settings of the translation stage')
        self.__addVariable__("moveAfterInitialization", ns, 'Move the mirror to a known position after initialization', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("moveAfterInitializationPosition", ns, 'Move the mirror to this position after initialization', datatype=pyuaf.util.primitives.String, permissions='')

class M3GotoKnownPositionArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the position (must be configured in M3Config.knownPositions!)', datatype=pyuaf.util.primitives.String, permissions='')

class M3GotoNewPositionArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rotationPosition", ns, 'Position of the rotation stage, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rotationOffset", ns, 'Offset between the motors of the rotation stage, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("translationPosition", ns, 'Position of the rotation stage, in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("doRotation", ns, 'Do a rotation for this position (TRUE) or not (FALSE)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doTranslation", ns, 'Do a translation for this position (TRUE) or not (FALSE)', datatype=pyuaf.util.primitives.Boolean, permissions='')

class M3RotationGotoArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("position", ns, 'Position setpoint of the rotation stage, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("offset", ns, 'Offset setpoint between the motors of the rotation stage, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')

class M3TranslationGotoArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("position", ns, 'Position setpoint of the translation stage, in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')


# === FBs ===

class M3TargetStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("superState", ns, 'Super state (TRUE if the super state is active, or if there is no super state)', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("state", ns, 'Enum!', datatype=M3TargetStates, permissions='')
        self.__addVariable__("noTargetGiven", ns, 'No target given', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("knownPosition", ns, 'Known position', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("newPosition", ns, 'Undefined', datatype=pyuaf.util.primitives.Boolean, permissions='r')


class SM_M3RotationTarget(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isTargetGiven", ns, 'TRUE if a target is given', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("newPositionDegrees", ns, 'New target position in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("newOffsetDegrees", ns, 'New target offset in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("name", ns, 'Name of the target (only in case the position and offset match an entry in the config!)', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("position", ns, mtcs_common.AngularPosition, 'Target position for M3 rotation (only in case statuses.targetStatus.noTargetGiven is FALSE)')
        self.__addInstance__("offset", ns, mtcs_common.AngularPosition, 'Target offset for M3 rotation (only in case statuses.targetStatus.noTargetGiven is FALSE)')
        self.__addInstance__("statuses", ns, M3RotationTargetStatuses, 'Statuses of the state machine')

class M3RotationTarget(SM_M3RotationTarget):
    def __init__(self, parent, name, ns, info):
        SM_M3RotationTarget.__init__(self, parent, name, ns, info)

class SM_M3TranslationTarget(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isTargetGiven", ns, 'TRUE if a target is given', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("newPositionMillimeters", ns, 'New target position in millimeters', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("name", ns, 'Name of the target (only in case the position matches an entry in the config!)', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("position", ns, mtcs_common.LinearPosition, 'Target position for M3 translation (only in case statuses.targetStatus.noTargetGiven is FALSE)')
        self.__addInstance__("statuses", ns, M3TranslationTargetStatuses, 'Statuses of the state machine')

class M3TranslationTarget(SM_M3TranslationTarget):
    def __init__(self, parent, name, ns, info):
        SM_M3TranslationTarget.__init__(self, parent, name, ns, info)

class SM_M3(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, M3Config, 'Editable configuration of M3')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, M3Config, 'Active configuration of M3')
        self.__addVariable__("actualKnownPositionName", ns, 'Name of the actual position according to config.knownPositions', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("actualKnownPositionID", ns, 'ID of the actual position according to config.knownPositions', datatype=M3PositionIDs, permissions='r')
        self.__addInstance__("statuses", ns, M3Statuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M3Parts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M3Processes, 'Processes of the state machine')

class M3(SM_M3):
    def __init__(self, parent, name, ns, info):
        SM_M3.__init__(self, parent, name, ns, info)

class SM_M3GotoProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New state, to be set by the manual implementation', datatype=M3GotoProcedureStates, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("isGotoAllowed", ns, 'TRUE if a goto command is allowed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, M3GotoProcedureStatuses, 'Statuses of the state machine')

class M3GotoProcedure(SM_M3GotoProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M3GotoProcedure.__init__(self, parent, name, ns, info)

class SM_M3Rotation(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("target", ns, M3RotationTarget, '')
        self.__addVariable__("positiveLimitSwitchActive", ns, 'TRUE if the positive limit switch is active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("negativeLimitSwitchActive", ns, 'TRUE if the negative limit switch is active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actualPosition", ns, mtcs_common.AngularPosition, 'The actual position of the rotation')
        self.__addInstance__("actualPositionError", ns, mtcs_common.AngularPosition, 'The actual position error of the rotation')
        self.__addInstance__("actualOffset", ns, mtcs_common.AngularPosition, 'The actual offset of the rotation')
        self.__addInstance__("actualOffsetError", ns, mtcs_common.AngularPosition, 'The actual offset error of the rotation')
        self.__addInstance__("statuses", ns, M3RotationStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M3RotationParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M3RotationProcesses, 'Processes of the state machine')

class M3Rotation(SM_M3Rotation):
    def __init__(self, parent, name, ns, info):
        SM_M3Rotation.__init__(self, parent, name, ns, info)

class SM_M3RotationGotoProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New state, to be set by the manual implementation', datatype=M3RotateProcedureStates, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("isGotoAllowed", ns, 'TRUE if a goto command is allowed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, M3RotationGotoProcedureStatuses, 'Statuses of the state machine')

class M3RotationGotoProcedure(SM_M3RotationGotoProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M3RotationGotoProcedure.__init__(self, parent, name, ns, info)

class SM_M3RotationCalibrateProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'Current state of the ', datatype=M3CalibrateRotationProcedureStates, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M3RotationCalibrateProcedureStatuses, 'Statuses of the state machine')

class M3RotationCalibrateProcedure(SM_M3RotationCalibrateProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M3RotationCalibrateProcedure.__init__(self, parent, name, ns, info)

class SM_M3Translation(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("target", ns, M3TranslationTarget, '')
        self.__addVariable__("positiveLimitSwitchActive", ns, 'TRUE if the positive limit switch is active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("negativeLimitSwitchActive", ns, 'TRUE if the negative limit switch is active', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actualPosition", ns, mtcs_common.LinearPosition, 'The actual position of the translation')
        self.__addInstance__("actualPositionError", ns, mtcs_common.LinearPosition, 'The actual position error of the translation')
        self.__addInstance__("statuses", ns, M3TranslationStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M3TranslationParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M3TranslationProcesses, 'Processes of the state machine')

class M3Translation(SM_M3Translation):
    def __init__(self, parent, name, ns, info):
        SM_M3Translation.__init__(self, parent, name, ns, info)

class SM_M3TranslationGotoProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New state, to be set by the manual implementation', datatype=M3TranslateProcedureStates, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("isGotoAllowed", ns, 'TRUE if a goto command is allowed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, M3TranslationGotoProcedureStatuses, 'Statuses of the state machine')

class M3TranslationGotoProcedure(SM_M3TranslationGotoProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M3TranslationGotoProcedure.__init__(self, parent, name, ns, info)

class SM_M3TranslationHomingProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'State to be set by the manual implementation', datatype=M3TranslationHomingProcedureStates, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M3TranslationHomingProcedureStatuses, 'Statuses of the state machine')

class M3TranslationHomingProcedure(SM_M3TranslationHomingProcedure):
    def __init__(self, parent, name, ns, info):
        SM_M3TranslationHomingProcedure.__init__(self, parent, name, ns, info)

class SM_M3IO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M3IOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M3IOParts, 'Parts of the state machine')

class M3IO(SM_M3IO):
    def __init__(self, parent, name, ns, info):
        SM_M3IO.__init__(self, parent, name, ns, info)

class M3GotoKnownPosition(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M3GotoKnownPositionArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M3GotoKnownPositionArgs, 'Arguments in use by the process, if do_request was accepted')


class M3GotoNewPosition(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M3GotoNewPositionArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M3GotoNewPositionArgs, 'Arguments in use by the process, if do_request was accepted')


class M3RotationGoto(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M3RotationGotoArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M3RotationGotoArgs, 'Arguments in use by the process, if do_request was accepted')


class M3TranslationGoto(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, M3TranslationGotoArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, M3TranslationGotoArgs, 'Arguments in use by the process, if do_request was accepted')




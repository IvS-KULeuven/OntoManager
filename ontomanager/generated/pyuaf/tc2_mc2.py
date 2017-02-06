# === imports ===



# This file (tc2_mc2.py) was automatically generated at 2016-04-04T14:20:53.170383 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====


# === STRUCTS ===

class ST_AxisStatus(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("UpdateTaskIndex", ns, 'Task-Index of the task that updated this data set', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("UpdateCycleTime", ns, 'Task cycle time of the task which calls the status function', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("CycleCounter", ns, 'PLC cycle counter when this data set updated', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("NcCycleCounter", ns, 'NC cycle counter incremented after NC task updated NcToPlc data structures', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("Error", ns, 'Axis error state', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("ErrorId", ns, 'Axis error code', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("Disabled", ns, 'Disabled state according to the PLCopen motion control statemachine*)', datatype=pyuaf.util.primitives.Double, permissions='')

class PLCTONC_AXIS_REF(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("ControlDWord", ns, 'Control double word', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("Override", ns, 'Velocity override', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("AxisModeRequest", ns, 'Axis operating mode (PLC request)', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("AxisModeDWord", ns, 'Optional mode parameter', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("AxisModeLReal", ns, 'Optional mode parameter', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("PositionCorrection", ns, 'Correction value for current position', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ExtSetPos", ns, 'External position setpoint', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ExtSetVelo", ns, 'External velocity setpoint', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ExtSetAcc", ns, 'External acceleration setpoint', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ExtSetDirection", ns, 'External direction setpoint', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("ExtControllerOutput", ns, 'External controller output', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("GearRatio1", ns, 'Gear ratio for dynamic multi master coupling modes', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("GearRatio2", ns, 'Gear ratio for dynamic multi master coupling modes', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("GearRatio3", ns, 'Gear ratio for dynamic multi master coupling modes', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("GearRatio4", ns, 'Gear ratio for dynamic multi master coupling modes', datatype=pyuaf.util.primitives.Double, permissions='')

class NCTOPLC_AXIS_REF(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("StateDWord", ns, 'Status double word', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("ErrorCode", ns, 'Axis error code', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("AxisState", ns, 'Axis moving status', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("AxisModeConfirmation", ns, 'Axis mode confirmation (feedback from NC)', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("HomingState", ns, 'State of axis calibration (homing)', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("CoupleState", ns, 'Axis coupling state', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("SvbEntries", ns, 'SVB entries/orders (SVB = Set preparation task)', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("SafEntries", ns, 'SAF entries/orders (SAF = Set execution task)', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("AxisId", ns, 'Axis ID', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("OpModeDWord", ns, 'Current operation mode', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("ActiveControlLoopIndex", ns, 'Active control loop index', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("ControlLoopIndex", ns, 'Axis control loop index (0, 1, 2, when multiple control loops are used)', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("ActPos", ns, 'Actual position (absolut value from NC)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ModuloActPos", ns, 'comment : Actual modulo positio', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ModuloActTurns", ns, 'Actual modulo turns', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("ActVelo", ns, 'Actual velocity', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("PosDiff", ns, 'Position difference (lag distance)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SetPos", ns, 'Setpoint position', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SetVelo", ns, 'Setpoint velocity', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("SetAcc", ns, 'Setpoint acceleration', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("TargetPos", ns, 'Estimated target position', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ModuloSetPos", ns, 'Setpoint modulo position', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ModuloSetTurns", ns, 'Setpoint modulo turns', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("CmdNo", ns, 'Continuous actual command number', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("CmdState", ns, 'Command state', datatype=pyuaf.util.primitives.UInt16, permissions='')


# === FBs ===

class AXIS_REF(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("PlcToNc", ns, PLCTONC_AXIS_REF, '')
        self.__addInstance__("NcToPlc", ns, NCTOPLC_AXIS_REF, '')
        self.__addInstance__("Status", ns, ST_AxisStatus, '')




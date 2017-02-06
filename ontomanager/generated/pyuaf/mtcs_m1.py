# === imports ===

import mtcs_common


# This file (mtcs_m1.py) was automatically generated at 2017-02-03T09:55:29.854856 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====


# === STRUCTS ===

class M1Parts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("inclinometer", ns, M1Inclinometer, 'Inclinometer')
        self.__addInstance__("radialSupport", ns, M1RadialSupport, 'Radial support')
        self.__addInstance__("axialSupport", ns, M1AxialSupport, 'Axial support')
        self.__addInstance__("io", ns, M1M2IO, 'I/O modules')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class M1RadialSupportParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("vacuumRelay", ns, mtcs_common.SimpleRelay, 'Switch Radial vacuum ON to retract the radial pads during mirror manipulations.')

class M1M2IOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("COU", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("AI1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("AI2", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("AI3", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("AO1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("DO1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("RES1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("RES2", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("RES3", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("PWR1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("SSI1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("AI4", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("INC1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("P5V1", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("DO2", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("DO3", ns, mtcs_common.EtherCatDevice, '')
        self.__addInstance__("RE1", ns, mtcs_common.EtherCatDevice, '')

class M1Processes(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')

class M1RadialSupportProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("changePressureSetpoint", ns, mtcs_common.ChangeSetpointProcess, 'Change a pressure setpoint, in Bar')
        self.__addInstance__("changePressureSetpointState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state of the pressure setpoint only')

class M1AxialSupportProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("changePressureSetpoint", ns, mtcs_common.ChangeSetpointProcess, 'Change a pressure setpoint, in Bar')
        self.__addInstance__("changePressureSetpointState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state of the pressure setpoint only')

class M1Statuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class M1InclinometerStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the inclinometer elevation trustworthy?')

class M1RadialSupportStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("pressureSetpointStatus", ns, mtcs_common.OperatingStatus, 'Operating status of the radial pressure setpoint')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')

class M1AxialSupportStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("pressureSetpointStatus", ns, mtcs_common.OperatingStatus, 'Operating status of the radial pressure setpoint')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')

class M1M2IOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class M1Config(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("radialSupport", ns, M1RadialSupportConfig, 'Radial support')
        self.__addInstance__("axialSupport", ns, M1AxialSupportConfig, 'Axial support')
        self.__addVariable__("pneumaticSupplySensorFullScale", ns, 'Sensor full scale range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("pneumaticSupplyPressure", ns, mtcs_common.MeasurementConfig, 'Pneumatic supply pressure config, in Bar')
        self.__addInstance__("inclinometerVoltage", ns, mtcs_common.MeasurementConfig, 'Inclinometer voltage measuremennt config, in Volts')

class M1RadialSupportConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("regulatorPressure", ns, mtcs_common.MeasurementConfig, 'Regulator pressure config, in Bar')
        self.__addInstance__("mirrorPressure", ns, mtcs_common.MeasurementConfig, 'Regulator pressure config, in Bar')
        self.__addVariable__("regulatorPressureSensorFullScale", ns, 'Sensor full scale range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("mirrorPressureSensorFullScale", ns, 'Sensor full scale range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("correctionCoefficient", ns, 'Correction coefficient for radial pressure', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controllerLimitMax", ns, 'Maximum output of the controller, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controllerLimitMin", ns, 'Minimum output of the controller, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pressureRegulatorRange", ns, 'Pressure regulator range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')

class M1AxialSupportConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("regulatorPressure", ns, mtcs_common.MeasurementConfig, 'Regulator pressure config, in Bar')
        self.__addInstance__("mirrorPressure", ns, mtcs_common.MeasurementConfig, 'Regulator pressure config, in Bar')
        self.__addInstance__("mirrorSouthForce", ns, mtcs_common.MeasurementConfig, 'Mirror south force config, in decaNewton')
        self.__addInstance__("mirrorNorthEastForce", ns, mtcs_common.MeasurementConfig, 'Mirror north east force config, in decaNewton')
        self.__addInstance__("mirrorNorthWestForce", ns, mtcs_common.MeasurementConfig, 'Mirror north west force config, in decaNewton')
        self.__addInstance__("mirrorAverageForce", ns, mtcs_common.MeasurementConfig, 'Mirror moving average force config, in decaNewton')
        self.__addVariable__("regulatorPressureSensorFullScale", ns, 'Sensor full scale range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("mirrorPressureSensorFullScale", ns, 'Sensor full scale range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("correctionCoefficient", ns, 'Correction coefficient for axial pressure', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controllerKp", ns, 'Proportional factor (gain) of the PI controller', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controllerTn", ns, 'Integral time factor of the PI controller. in seconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controllerLimitMax", ns, 'Maximum output of the controller, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controllerLimitMin", ns, 'Minimum output of the controller, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pressureRegulatorRange", ns, 'Pressure regulator range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')


# === FBs ===

class SM_M1(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, M1Config, 'Editable configuration of the M1 subsystem')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, M1Config, 'Active configuration of the M1 subsystem')
        self.__addInstance__("pneumaticSupplyPressure", ns, mtcs_common.PressureMeasurement, 'Pressure measurement of the pneumatic supply')
        self.__addInstance__("statuses", ns, M1Statuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M1Parts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M1Processes, 'Processes of the state machine')

class M1(SM_M1):
    def __init__(self, parent, name, ns, info):
        SM_M1.__init__(self, parent, name, ns, info)

class SM_M1Inclinometer(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("voltageMeasurement", ns, mtcs_common.VoltageMeasurement, 'Measured voltage')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actualElevation", ns, mtcs_common.AngularPosition, 'Elevation actual value')
        self.__addInstance__("averageElevation", ns, mtcs_common.AngularPosition, 'Elevation average value')
        self.__addInstance__("statuses", ns, M1InclinometerStatuses, 'Statuses of the state machine')

class M1Inclinometer(SM_M1Inclinometer):
    def __init__(self, parent, name, ns, info):
        SM_M1Inclinometer.__init__(self, parent, name, ns, info)

class SM_M1RadialSupport(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("pressureSetpointOutput", ns, 'Output value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("regulatorPressure", ns, mtcs_common.PressureMeasurement, 'Pressure measurement at the regulator')
        self.__addInstance__("mirrorPressure", ns, mtcs_common.PressureMeasurement, 'Pressure measurement at the mirror')
        self.__addInstance__("actualPressureSetpoint", ns, mtcs_common.Pressure, 'Pressure setpoint actually used')
        self.__addInstance__("autoPressureSetpoint", ns, mtcs_common.Pressure, 'Pressure setpoint in AUTO mode')
        self.__addInstance__("manualPressureSetpoint", ns, mtcs_common.Pressure, 'Pressure setpoint in MANUAL mode')
        self.__addInstance__("statuses", ns, M1RadialSupportStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M1RadialSupportParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, M1RadialSupportProcesses, 'Processes of the state machine')

class M1RadialSupport(SM_M1RadialSupport):
    def __init__(self, parent, name, ns, info):
        SM_M1RadialSupport.__init__(self, parent, name, ns, info)

class SM_M1AxialSupport(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("pressureSetpointOutput", ns, 'Output value', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("regulatorPressure", ns, mtcs_common.PressureMeasurement, 'Pressure measurement at the regulator')
        self.__addInstance__("mirrorPressure", ns, mtcs_common.PressureMeasurement, 'Pressure measurement at the mirror')
        self.__addInstance__("mirrorSouthForce", ns, mtcs_common.ForceMeasurement, 'Force measurement South (SO)')
        self.__addInstance__("mirrorNorthEastForce", ns, mtcs_common.ForceMeasurement, 'Force measurement North East (NE)')
        self.__addInstance__("mirrorNorthWestForce", ns, mtcs_common.ForceMeasurement, 'Force measurement North West (NW)')
        self.__addInstance__("mirrorAverageForce", ns, mtcs_common.ForceMeasurement, 'Average of SO, NE and NW')
        self.__addInstance__("actualPressureSetpoint", ns, mtcs_common.Pressure, 'Pressure setpoint actually used')
        self.__addInstance__("autoPressureSetpoint", ns, mtcs_common.Pressure, 'Pressure setpoint in AUTO mode')
        self.__addInstance__("manualPressureSetpoint", ns, mtcs_common.Pressure, 'Pressure setpoint in MANUAL mode')
        self.__addInstance__("controllerSetpoint", ns, mtcs_common.Force, 'Force setpoint of the controller')
        self.__addInstance__("statuses", ns, M1AxialSupportStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, M1AxialSupportProcesses, 'Processes of the state machine')

class M1AxialSupport(SM_M1AxialSupport):
    def __init__(self, parent, name, ns, info):
        SM_M1AxialSupport.__init__(self, parent, name, ns, info)

class SM_M1M2IO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, M1M2IOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, M1M2IOParts, 'Parts of the state machine')

class M1M2IO(SM_M1M2IO):
    def __init__(self, parent, name, ns, info):
        SM_M1M2IO.__init__(self, parent, name, ns, info)



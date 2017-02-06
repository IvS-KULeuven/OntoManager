# === imports ===

import mtcs_common


# This file (mtcs_hydraulics.py) was automatically generated at 2016-06-02T10:45:23.761713 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class HydraulicsPumpsStates:
        STOPPED = 0
        POWERING_ON = 1
        RESETTING_DRIVES = 2
        COMMANDING_SAFETY = 3
        BUILDING_UP_PRESSURE = 4
        RUNNING = 5
        STOPPING = 6
        POWERING_OFF = 7
        MANUAL = 8
        ERROR = 9


# === STRUCTS ===

class HydraulicsParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("pumpsRelay", ns, mtcs_common.SimpleRelay, 'Relay to power on/off the circulation pump')
        self.__addInstance__("pumpsPowerRelay", ns, mtcs_common.SimpleRelay, 'Relay to power on/off the pumps')
        self.__addInstance__("top", ns, HydraulicsSide, 'Top side')
        self.__addInstance__("bottom", ns, HydraulicsSide, 'Bottom side')
        self.__addInstance__("io", ns, HydraulicsIO, 'I/O modules')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class HydraulicsIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("pumpsGroup", ns, HydraulicsPumpsGroupIO, 'PG: Pumps Group')

class HydraulicsPumpsGroupIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("COU", ns, mtcs_common.EtherCatDevice, 'PG:COU (EK1101)')
        self.__addInstance__("DI1", ns, mtcs_common.EtherCatDevice, 'PG:DI1 (EL1008)')
        self.__addInstance__("SI1", ns, mtcs_common.EtherCatDevice, 'PG:SI1 (EL1904)')
        self.__addInstance__("SI2", ns, mtcs_common.EtherCatDevice, 'PG:SI2 (EL1904)')
        self.__addInstance__("SI3", ns, mtcs_common.EtherCatDevice, 'PG:SI3 (EL1904)')
        self.__addInstance__("DI2", ns, mtcs_common.EtherCatDevice, 'PG:DI2 (EL1008)')

class HydraulicsProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')
        self.__addInstance__("startUpPumps", ns, mtcs_common.Process, 'Start up the pumps')
        self.__addInstance__("stopPumps", ns, mtcs_common.Process, 'Stop the pumps')

class HydraulicsSideProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("resetDrive", ns, mtcs_common.Process, 'Reset the drive')
        self.__addInstance__("changeFrequencySetpoint", ns, mtcs_common.ChangeSetpointProcess, 'Change the frequency setpoint, in Hertz')

class HydraulicsStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class HydraulicsSideStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the hydraulics side in a healthy state? Good=RUN, Bad=safe stopped')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the hydraulics side busy?')

class HydraulicsIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class HydraulicsPumpsGroupIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class HydraulicsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("top", ns, HydraulicsSideConfig, 'Top side settings')
        self.__addInstance__("bottom", ns, HydraulicsSideConfig, 'Bottom side settings')
        self.__addVariable__("controlCycleTime", ns, 'Cycle time in seconds of the control loop (old system: 60.0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("controlHysteresis", ns, 'Don&#39;t change the frequency setpoint if the error is below this value (in Hz) (old system: 1.0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("buildUpPressureTime", ns, 'Time in seconds during startup, when the pumps must run at maxFrequency', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("bearingTemperature", ns, mtcs_common.MeasurementConfig, 'Oil temperature measured at the bearing')
        self.__addVariable__("stoppingTime", ns, 'Time in seconds during stopping', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pumpsPowerOnTIme", ns, 'Time in seconds to wait while powering on', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pumpsPowerOffTIme", ns, 'Time in seconds to wait while powering off', datatype=pyuaf.util.primitives.Double, permissions='')

class HydraulicsSideConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("minFrequency", ns, 'Minimum allowed frequency in Hz (old system: 50.0 for both pumps)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("maxFrequency", ns, 'Maximum allowed frequency in Hz (old system: 100.0 for both pumps)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("pressureMeasurement", ns, mtcs_common.MeasurementConfig, 'Pressure measurement config, in Bar')
        self.__addVariable__("pressureSensorFullScale", ns, 'Sensor full scale range, in Bar', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("frequencyMeasurement", ns, mtcs_common.MeasurementConfig, 'Frequency measurement config, in Hertz')
        self.__addVariable__("frequencyMeasurementFullScale", ns, 'Measurement full scale range, in Hertz', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("conversionCoefficientA", ns, 'Coefficient &#39;a&#39; of formula: Frequency[Hz] = a * temp[Celsius]^2 + b * temp[Celsius] + c', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("conversionCoefficientB", ns, 'Coefficient &#39;b&#39; of formula: Frequency[Hz] = a * temp[Celsius]^2 + b * temp[Celsius] + c', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("conversionCoefficientC", ns, 'Coefficient &#39;c&#39; of formula: Frequency[Hz] = a * temp[Celsius]^2 + b * temp[Celsius] + c', datatype=pyuaf.util.primitives.Double, permissions='')


# === FBs ===

class SM_Hydraulics(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, HydraulicsConfig, 'Editable configuration of the Safety subsystem')
        self.__addVariable__("circulationFilterGOK", ns, 'TRUE if there is no overpressure for circulation filter G', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("circulationFilterDOK", ns, 'TRUE if there is no overpressure for circulation filter D', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("oilLevelTooHigh", ns, 'TRUE if the oil level is too high (--&gt; problem!)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsState", ns, 'The current state of the pumps', datatype=HydraulicsPumpsStates, permissions='r')
        self.__addVariable__("pumpsStatus", ns, 'Textual representation of the current pumps status', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("config", ns, HydraulicsConfig, 'Active configuration of the Hydraulics subsystem')
        self.__addInstance__("bearingTemperature", ns, mtcs_common.TemperatureMeasurement, 'Temperature measured at the bearing')
        self.__addInstance__("statuses", ns, HydraulicsStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, HydraulicsParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, HydraulicsProcesses, 'Processes of the state machine')

class Hydraulics(SM_Hydraulics):
    def __init__(self, parent, name, ns, info):
        SM_Hydraulics.__init__(self, parent, name, ns, info)

class SM_HydraulicsSide(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("entranceFilter1OK", ns, 'TRUE if there is no overpressure for entrance filter 1', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("entranceFilter2OK", ns, 'TRUE if there is no overpressure for entrance filter 2', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("entranceFilter3OK", ns, 'TRUE if there is no overpressure for entrance filter 3', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("entranceFilter4OK", ns, 'TRUE if there is no overpressure for entrance filter 4', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("driveTripOK", ns, 'TRIP output of the drive, as copied from the safety system', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("driveRelease", ns, 'Release output of the drive (ReglerFreigabe RFR), as copied from the safety system', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("driveMinFrequency", ns, 'Minimum frequency output of the drive (QMIN), as copied from the safety system', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("pressureMeasurement", ns, mtcs_common.PressureMeasurement, 'Pressure measurement')
        self.__addInstance__("frequencyMeasurement", ns, mtcs_common.FrequencyMeasurement, 'Frequency measurement')
        self.__addInstance__("driveSetpoint", ns, mtcs_common.Frequency, 'Frequency setpoint actually used')
        self.__addVariable__("driveSetpointSignal", ns, 'Raw signal value of the frequency setpoint', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("resetDriveSignal", ns, 'Output to reset the drive', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, HydraulicsSideStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, HydraulicsSideProcesses, 'Processes of the state machine')

class HydraulicsSide(SM_HydraulicsSide):
    def __init__(self, parent, name, ns, info):
        SM_HydraulicsSide.__init__(self, parent, name, ns, info)

class SM_HydraulicsIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, HydraulicsIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, HydraulicsIOParts, 'Parts of the state machine')

class HydraulicsIO(SM_HydraulicsIO):
    def __init__(self, parent, name, ns, info):
        SM_HydraulicsIO.__init__(self, parent, name, ns, info)

class SM_HydraulicsPumpsGroupIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, HydraulicsPumpsGroupIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, HydraulicsPumpsGroupIOParts, 'Parts of the state machine')

class HydraulicsPumpsGroupIO(SM_HydraulicsPumpsGroupIO):
    def __init__(self, parent, name, ns, info):
        SM_HydraulicsPumpsGroupIO.__init__(self, parent, name, ns, info)



# === imports ===

import mtcs_common


# This file (mtcs_telemetry.py) was automatically generated at 2017-02-03T09:55:22.560721 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====


# === STRUCTS ===

class TelemetryParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("temperatures", ns, TelemetryTemperatures, 'All temperature measurements')
        self.__addInstance__("relativeHumidities", ns, TelemetryRelativeHumidities, 'All relative humidity measurements')
        self.__addInstance__("dewpoints", ns, TelemetryDewpoints, 'All calculated dewpoints')
        self.__addInstance__("accelerometers", ns, TelemetryAccelerometers, 'Feedback from the accelerometers (vibrations + angles)')
        self.__addInstance__("io", ns, TelemetryIO, 'I/O modules')
        self.__addInstance__("flatfieldLeds", ns, TelemetryFlatfieldLeds, 'I/O modules')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class TelemetryFlatfieldLedsParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("output1", ns, mtcs_common.SimpleRelay, 'Output 1')
        self.__addInstance__("output2", ns, mtcs_common.SimpleRelay, 'Output 2')
        self.__addInstance__("output3", ns, mtcs_common.SimpleRelay, 'Output 3')
        self.__addInstance__("output4", ns, mtcs_common.SimpleRelay, 'Output 4')
        self.__addInstance__("output5", ns, mtcs_common.SimpleRelay, 'Output 5')
        self.__addInstance__("output6", ns, mtcs_common.SimpleRelay, 'Output 6')
        self.__addInstance__("output7", ns, mtcs_common.SimpleRelay, 'Output 7')
        self.__addInstance__("output8", ns, mtcs_common.SimpleRelay, 'Output 8')

class TelemetryIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("coupler", ns, mtcs_common.EtherCatDevice, 'Coupler')
        self.__addInstance__("slot5", ns, mtcs_common.EtherCatDevice, 'Slot 5')
        self.__addInstance__("slot6", ns, mtcs_common.EtherCatDevice, 'Slot 6')
        self.__addInstance__("slot7", ns, mtcs_common.EtherCatDevice, 'Slot 7')
        self.__addInstance__("slot8", ns, mtcs_common.EtherCatDevice, 'Slot 8')
        self.__addInstance__("slot9", ns, mtcs_common.EtherCatDevice, 'Slot 9')
        self.__addInstance__("slot10", ns, mtcs_common.EtherCatDevice, 'Slot 10')
        self.__addInstance__("slot11", ns, mtcs_common.EtherCatDevice, 'Slot 11')
        self.__addInstance__("slot12", ns, mtcs_common.EtherCatDevice, 'Slot 12')
        self.__addInstance__("slot13", ns, mtcs_common.EtherCatDevice, 'Slot 13')
        self.__addInstance__("tubeAccelerometers", ns, mtcs_common.EtherCatDevice, 'Tube accelerometers')

class TelemetryProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')

class TelemetryTemperaturesStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Are all temperatures in a healthy state?')

class TelemetryRelativeHumiditiesStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Are all relative humidities in a healthy state?')

class TelemetryDewpointStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, mtcs_common.EnabledStatus, 'Is the dewpoint being calculated?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the depoint OK?')
        self.__addInstance__("alarmStatus", ns, mtcs_common.HiHiLoLoAlarmStatus, 'Alarm status')

class TelemetryDewpointsStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Are all dewpoints in a healthy state?')

class TelemetryAccelerometerStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("xEnabledStatus", ns, mtcs_common.EnabledStatus, 'Is the X angle being measured?')
        self.__addInstance__("yEnabledStatus", ns, mtcs_common.EnabledStatus, 'Is the Y angle being measured?')
        self.__addInstance__("xHealthStatus", ns, mtcs_common.HealthStatus, 'Is the X angle measurement OK?')
        self.__addInstance__("yHealthStatus", ns, mtcs_common.HealthStatus, 'Is the Y angle measurement OK?')
        self.__addInstance__("xAlarmStatus", ns, mtcs_common.HiHiLoLoAlarmStatus, 'Alarm status of the X angle')
        self.__addInstance__("yAlarmStatus", ns, mtcs_common.HiHiLoLoAlarmStatus, 'Alarm status of the Y angle')

class TelemetryAccelerometersStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Are all accelerometers in a healthy state?')

class TelemetryStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class TelemetryFlatfieldLedsStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')

class TelemetryIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class TelemetryTemperaturesConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("m1", ns, mtcs_common.MeasurementConfig, 'Temperature of M1')
        self.__addInstance__("mirrorCell", ns, mtcs_common.MeasurementConfig, 'Temperature of the mirror cell')
        self.__addInstance__("m2", ns, mtcs_common.MeasurementConfig, 'Temperature of M2')
        self.__addInstance__("m2Electronics", ns, mtcs_common.MeasurementConfig, 'Temperature of the M2 electricity')
        self.__addInstance__("topTube", ns, mtcs_common.MeasurementConfig, 'Temperature of the top of the tube')
        self.__addInstance__("centreTube", ns, mtcs_common.MeasurementConfig, 'Temperature of the centre of the tube')
        self.__addInstance__("fork", ns, mtcs_common.MeasurementConfig, 'Temperature of the fork')
        self.__addInstance__("nasmythAir", ns, mtcs_common.MeasurementConfig, 'Temperature of the air inside the Nasmyth focal station')
        self.__addInstance__("rem", ns, mtcs_common.MeasurementConfig, 'Temperature inside the REM cabinet')
        self.__addInstance__("rpm", ns, mtcs_common.MeasurementConfig, 'Temperature inside the RPM cabinet')
        self.__addInstance__("hermesTelescopeAdapter", ns, mtcs_common.MeasurementConfig, 'Temperature inside the HERMES telescope adapter')
        self.__addInstance__("topAir", ns, mtcs_common.MeasurementConfig, 'Temperature of the air at the top of the tube')
        self.__addInstance__("insideTube", ns, mtcs_common.MeasurementConfig, 'Temperature of the air inside the tube')

class TelemetryRelativeHumiditiesConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("topAir", ns, mtcs_common.MeasurementConfig, 'Relative humidity of the air at the top of the tube')
        self.__addInstance__("insideTube", ns, mtcs_common.MeasurementConfig, 'Relative humidity of the air inside the tube')

class TelemetryDewpointsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("topAir", ns, mtcs_common.MeasurementConfig, 'Dewpoint of the air at the top of the tube')
        self.__addInstance__("insideTube", ns, mtcs_common.MeasurementConfig, 'Dewpoint of the air inside the tube')

class TelemetryAccelerometerConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("x", ns, mtcs_common.MeasurementConfig, 'X angle')
        self.__addInstance__("y", ns, mtcs_common.MeasurementConfig, 'X angle')

class TelemetryAccelerometersConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("tube", ns, TelemetryAccelerometerConfig, 'Accelerometer box at the tube')

class TelemetryConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("temperatures", ns, TelemetryTemperaturesConfig, 'All temperatures')
        self.__addInstance__("relativeHumidities", ns, TelemetryRelativeHumiditiesConfig, 'All relative humidities')
        self.__addInstance__("dewpoints", ns, TelemetryDewpointsConfig, 'All dewpoints')
        self.__addInstance__("accelerometers", ns, TelemetryAccelerometersConfig, 'All accelerometers')


# === FBs ===

class SM_TelemetryTemperatures(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("m1", ns, mtcs_common.TemperatureMeasurement, 'Temperature of M1')
        self.__addInstance__("mirrorCell", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the mirror cell')
        self.__addInstance__("m2", ns, mtcs_common.TemperatureMeasurement, 'Temperature of M2')
        self.__addInstance__("m2Electronics", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the M2 electricity')
        self.__addInstance__("topTube", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the top of the tube')
        self.__addInstance__("centreTube", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the centre of the tube')
        self.__addInstance__("fork", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the fork')
        self.__addInstance__("nasmythAir", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the air inside the Nasmyth focal station')
        self.__addInstance__("rem", ns, mtcs_common.TemperatureMeasurement, 'Temperature inside the REM cabinet')
        self.__addInstance__("rpm", ns, mtcs_common.TemperatureMeasurement, 'Temperature inside the RPM cabinet')
        self.__addInstance__("hermesTelescopeAdapter", ns, mtcs_common.TemperatureMeasurement, 'Temperature inside the HERMES telescope adapter')
        self.__addInstance__("topAir", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the air at the top of the tube')
        self.__addInstance__("insideTube", ns, mtcs_common.TemperatureMeasurement, 'Temperature of the air inside the tube')
        self.__addInstance__("statuses", ns, TelemetryTemperaturesStatuses, 'Statuses of the state machine')

class TelemetryTemperatures(SM_TelemetryTemperatures):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryTemperatures.__init__(self, parent, name, ns, info)

class SM_TelemetryRelativeHumidities(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("topAir", ns, mtcs_common.RelativeHumidityMeasurement, 'Relative humidity of the air at the top of the tube')
        self.__addInstance__("insideTube", ns, mtcs_common.RelativeHumidityMeasurement, 'Relative humidity of the air inside the tube')
        self.__addInstance__("statuses", ns, TelemetryRelativeHumiditiesStatuses, 'Statuses of the state machine')

class TelemetryRelativeHumidities(SM_TelemetryRelativeHumidities):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryRelativeHumidities.__init__(self, parent, name, ns, info)

class SM_TelemetryDewpoint(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actual", ns, mtcs_common.Temperature, 'Actual dewpoint temperature')
        self.__addInstance__("average", ns, mtcs_common.Temperature, 'Average dewpoint temperature')
        self.__addInstance__("statuses", ns, TelemetryDewpointStatuses, 'Statuses of the state machine')

class TelemetryDewpoint(SM_TelemetryDewpoint):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryDewpoint.__init__(self, parent, name, ns, info)

class SM_TelemetryDewpoints(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("topAir", ns, TelemetryDewpoint, 'Dewpoint of the air at the top of the tube')
        self.__addInstance__("insideTube", ns, TelemetryDewpoint, 'Dewpoint of the air inside the tube')
        self.__addInstance__("statuses", ns, TelemetryDewpointsStatuses, 'Statuses of the state machine')

class TelemetryDewpoints(SM_TelemetryDewpoints):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryDewpoints.__init__(self, parent, name, ns, info)

class SM_TelemetryAccelerometer(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("X1plus", ns, mtcs_common.GForceMeasurement, '+X1 (channel 1 of EP1816-3008)')
        self.__addInstance__("Y1plus", ns, mtcs_common.GForceMeasurement, '+Y1 (channel 2 of EP1816-3008)')
        self.__addInstance__("Z1minus", ns, mtcs_common.GForceMeasurement, '-Z1 (channel 3 of EP1816-3008)')
        self.__addInstance__("Y2plus", ns, mtcs_common.GForceMeasurement, '+Y2 (channel 4 of EP1816-3008)')
        self.__addInstance__("X2minus", ns, mtcs_common.GForceMeasurement, '-X2 (channel 5 of EP1816-3008)')
        self.__addInstance__("Z2minus", ns, mtcs_common.GForceMeasurement, '-Z2 (channel 6 of EP1816-3008)')
        self.__addInstance__("actualXAngle", ns, mtcs_common.AngularPosition, 'Actual X angle')
        self.__addInstance__("actualYAngle", ns, mtcs_common.AngularPosition, 'Actual Y angle')
        self.__addInstance__("averageXAngle", ns, mtcs_common.AngularPosition, 'Average X angle')
        self.__addInstance__("averageYAngle", ns, mtcs_common.AngularPosition, 'Average Y angle')
        self.__addInstance__("statuses", ns, TelemetryAccelerometerStatuses, 'Statuses of the state machine')

class TelemetryAccelerometer(SM_TelemetryAccelerometer):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryAccelerometer.__init__(self, parent, name, ns, info)

class SM_TelemetryAccelerometers(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("tube", ns, TelemetryAccelerometer, 'Accelerometer box at the tube')
        self.__addInstance__("statuses", ns, TelemetryAccelerometersStatuses, 'Statuses of the state machine')

class TelemetryAccelerometers(SM_TelemetryAccelerometers):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryAccelerometers.__init__(self, parent, name, ns, info)

class SM_Telemetry(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, TelemetryConfig, 'Editable configuration of the Telemetry subsystem')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, TelemetryConfig, 'Active configuration of the Telemetry subsystem')
        self.__addInstance__("statuses", ns, TelemetryStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, TelemetryParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, TelemetryProcesses, 'Processes of the state machine')

class Telemetry(SM_Telemetry):
    def __init__(self, parent, name, ns, info):
        SM_Telemetry.__init__(self, parent, name, ns, info)

class SM_TelemetryFlatfieldLeds(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("isEnabled", ns, 'Is control enabled?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, TelemetryFlatfieldLedsStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, TelemetryFlatfieldLedsParts, 'Parts of the state machine')

class TelemetryFlatfieldLeds(SM_TelemetryFlatfieldLeds):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryFlatfieldLeds.__init__(self, parent, name, ns, info)

class SM_TelemetryIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, TelemetryIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, TelemetryIOParts, 'Parts of the state machine')

class TelemetryIO(SM_TelemetryIO):
    def __init__(self, parent, name, ns, info):
        SM_TelemetryIO.__init__(self, parent, name, ns, info)



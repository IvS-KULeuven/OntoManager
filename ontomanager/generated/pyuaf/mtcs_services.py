# === imports ===

import mtcs_common
import mtcs_tmc


# This file (mtcs_services.py) was automatically generated at 2017-02-05T17:05:44.831698 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class ServicesTimingTimeSource:
        LOCAL_CLOCK = 0
        PTP_IEEE_1588 = 1

class ServicesMeteoId:
        WIND_SPEED_MINIMUM = 0
        WIND_SPEED_AVERAGE = 1
        WIND_SPEED_MAXIMUM = 2
        WIND_DIRECTION_MINIMUM = 3
        WIND_DIRECTION_AVERAGE = 4
        WIND_DIRECTION_MAXIMUM = 5
        AIR_PRESSURE = 6
        AIR_TEMPERATURE = 7
        INTERNAL_TEMPERATURE = 8
        RELATIVE_HUMIDITY = 9
        RAIN_ACCUMULATION = 10
        RAIN_DURATION = 11
        RAIN_INTENSITY = 12
        RAIN_PEAK_INTENSITY = 13
        HAIL_ACCUMULATION = 14
        HAIL_DURATION = 15
        HAIL_PEAK_INTENSITY = 16
        HAIL_INTENSITY = 17
        HEATING_TEMPERATURE = 18
        HEATING_VOLTAGE = 19
        SUPPLY_VOLTAGE = 20
        REFERENCE_VOLTAGE = 21


# === STRUCTS ===

class ServicesParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("timing", ns, ServicesTiming, 'Timing service')
        self.__addInstance__("meteo", ns, ServicesMeteo, 'Meteo service')
        self.__addInstance__("io", ns, ServicesIO, 'I/O modules')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class ServicesTimingParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("serialInfo", ns, ServicesTimingSerialInfo, 'Info acquired by serial link')

class ServicesIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("coupler", ns, mtcs_common.EtherCatDevice, 'Coupler')
        self.__addInstance__("slot1", ns, mtcs_common.EtherCatDevice, 'Slot 1')
        self.__addInstance__("slot2", ns, mtcs_common.EtherCatDevice, 'Slot 2')
        self.__addInstance__("slot3", ns, mtcs_common.EtherCatDevice, 'Slot 2')

class ServicesProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')

class ServicesTimingProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)

class ServicesMeteoProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)

class ServicesStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class ServicesTimingStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')

class ServicesTimingSerialInfoStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("portHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("transmissionHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("checksumHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')

class ServicesMeteoMeasurementStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("enabledStatus", ns, mtcs_common.EnabledStatus, 'Is the temperature being measured?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the data valid and within range?')
        self.__addInstance__("alarmStatus", ns, mtcs_common.HiHiLoLoAlarmStatus, 'Alarm status')

class ServicesMeteoStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("meteoHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')

class ServicesIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class ServicesTimingConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("leapSeconds", ns, 'Number of leap seconds, so that UTC = TAI + this value. See ftp://maia.usno.navy.mil/ser7/tai-utc.dat for the latest number.', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("dut", ns, 'Delta UT (= UT1 - UTC). Put to 0.0 to ignore.', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("alwaysUseLocalClock", ns, 'If TRUE, then the local clock (source=LOCAL_CLOCK) will be used even if an external (more accurate!) clock is available', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("ignoreSerialError", ns, 'Don&#39;t show the Servicestiming status as ERROR in case the serial link fails', datatype=pyuaf.util.primitives.Boolean, permissions='')

class ServicesMeteoConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("wetLimit", ns, 'Wet if (rainIntensity+hailIntrelaensity)&gt;wetLimit', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("windSpeedMinimum", ns, mtcs_common.MeasurementConfig, 'Config for the wind speed minimum')
        self.__addInstance__("windSpeedAverage", ns, mtcs_common.MeasurementConfig, 'Config for the wind speed average')
        self.__addInstance__("windSpeedMaximum", ns, mtcs_common.MeasurementConfig, 'Config for the wind speed maximum')
        self.__addInstance__("windDirectionMinimum", ns, mtcs_common.MeasurementConfig, 'Config for the wind direction minimum')
        self.__addInstance__("windDirectionAverage", ns, mtcs_common.MeasurementConfig, 'Config for the wind direction average')
        self.__addInstance__("windDirectionMaximum", ns, mtcs_common.MeasurementConfig, 'Config for the wind direction maximum')
        self.__addInstance__("airPressure", ns, mtcs_common.MeasurementConfig, 'Config for the air pressure')
        self.__addInstance__("airTemperature", ns, mtcs_common.MeasurementConfig, 'Config for the air temperature')
        self.__addInstance__("internalTemperature", ns, mtcs_common.MeasurementConfig, 'Config for the internal temperature')
        self.__addInstance__("relativeHumidity", ns, mtcs_common.MeasurementConfig, 'Config for the relative humidity')
        self.__addInstance__("rainAccumulation", ns, mtcs_common.MeasurementConfig, 'Config for the rain accumulation')
        self.__addInstance__("rainDuration", ns, mtcs_common.MeasurementConfig, 'Config for the rain duration')
        self.__addInstance__("rainIntensity", ns, mtcs_common.MeasurementConfig, 'Config for the rain intensity')
        self.__addInstance__("rainPeakIntensity", ns, mtcs_common.MeasurementConfig, 'Config for the rain peak intensity')
        self.__addInstance__("hailAccumulation", ns, mtcs_common.MeasurementConfig, 'Config for the hail accumulation')
        self.__addInstance__("hailDuration", ns, mtcs_common.MeasurementConfig, 'Config for the hail duration')
        self.__addInstance__("hailIntensity", ns, mtcs_common.MeasurementConfig, 'Config for the hail intensity')
        self.__addInstance__("hailPeakIntensity", ns, mtcs_common.MeasurementConfig, 'Config for the hail peak intensity')
        self.__addInstance__("heatingTemperature", ns, mtcs_common.MeasurementConfig, 'Config for the heating temperature')
        self.__addInstance__("heatingVoltage", ns, mtcs_common.MeasurementConfig, 'Config for the heating voltage')
        self.__addInstance__("supplyVoltage", ns, mtcs_common.MeasurementConfig, 'Config for the supply voltage')
        self.__addInstance__("referenceVoltage", ns, mtcs_common.MeasurementConfig, 'Config for the 3.5 V reference voltage')

class ServicesConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("timing", ns, ServicesTimingConfig, 'Timing config')
        self.__addInstance__("meteo", ns, ServicesMeteoConfig, 'Meteo config')


# === FBs ===

class SM_Services(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, ServicesConfig, 'Editable configuration of the Services subsystem')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, ServicesConfig, 'Active configuration of the Services subsystem')
        self.__addInstance__("statuses", ns, ServicesStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, ServicesParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, ServicesProcesses, 'Processes of the state machine')

class Services(SM_Services):
    def __init__(self, parent, name, ns, info):
        SM_Services.__init__(self, parent, name, ns, info)

class SM_ServicesTiming(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("fromEL6688", ns, mtcs_tmc.TmcFromIoEL6688, 'Data from the EL6688')
        self.__addInstance__("fromEcatMaster", ns, mtcs_tmc.TmcFromIoEcatMaster, 'Data from the EtherCAT master')
        self.__addInstance__("fromCppTiming", ns, mtcs_tmc.TmcToPlcTiming, 'Data from the C++ task')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("toCppTiming", ns, mtcs_tmc.TmcFromPlcTiming, 'Data to the C++ task')
        self.__addVariable__("utcDateString", ns, 'UTC date as a string of format YYYY-MM-DD', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("utcTimeString", ns, 'UTC time as a string of format HH-MM-SS.SSS', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("internalTimestampString", ns, 'String representation of the internal timestamp', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("externalTimestampString", ns, 'String representation of the external timestamp (note: this is TAI, not UTC!)', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, ServicesTimingStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, ServicesTimingParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, ServicesTimingProcesses, 'Processes of the state machine')

class ServicesTiming(SM_ServicesTiming):
    def __init__(self, parent, name, ns, info):
        SM_ServicesTiming.__init__(self, parent, name, ns, info)

class SM_ServicesTimingSerialInfo(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("serialTimeout", ns, 'Is the serial data not being received within time?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("comError", ns, 'Is there any problem with the COM port?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("comErrorID", ns, 'COM error id (see Beckhoff ComError_t)', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("comErrorDescription", ns, 'Description of the COM error id', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("time_h", ns, 'Time: hours (0-24)', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("time_m", ns, 'Time: minutes (0-59)', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("time_s", ns, 'Time: seconds (0-59, or 60 if leap second)', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("latitude_deg", ns, 'Latitude: degrees (0-90)', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("latitude_min", ns, 'Latitude: minutes (0.0-59.99999)', datatype=pyuaf.util.primitives.Float, permissions='r')
        self.__addVariable__("latitude_sign", ns, 'Latitude: sign (either &#39;N&#39; or &#39;S&#39;)', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("longitude_deg", ns, 'Longitude: degrees (0-180)', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("longitude_min", ns, 'Longitude: minutes (0.0-59.99999)', datatype=pyuaf.util.primitives.Float, permissions='r')
        self.__addVariable__("longitude_sign", ns, 'Longitude: sign (either &#39;E&#39; or &#39;W&#39;)', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("positionFix", ns, 'True if a position fix was accomplished, False if not', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("satellitesUsed", ns, 'Number of satellites used', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("horizontalDilutionOfPosition", ns, 'Horizontal dilution of position', datatype=pyuaf.util.primitives.Float, permissions='r')
        self.__addVariable__("meanSeaLevelAltitude", ns, 'Mean altitude above sea level in meters', datatype=pyuaf.util.primitives.Float, permissions='r')
        self.__addVariable__("geoidSeparation", ns, 'Geoid separation in meters', datatype=pyuaf.util.primitives.Float, permissions='r')
        self.__addVariable__("checksum", ns, 'Checksum send by the time server', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addVariable__("calculatedChecksum", ns, 'Checksum calculated by the PLC', datatype=pyuaf.util.primitives.Byte, permissions='r')
        self.__addInstance__("statuses", ns, ServicesTimingSerialInfoStatuses, 'Statuses of the state machine')

class ServicesTimingSerialInfo(SM_ServicesTimingSerialInfo):
    def __init__(self, parent, name, ns, info):
        SM_ServicesTimingSerialInfo.__init__(self, parent, name, ns, info)

class SM_ServicesMeteoMeasurement(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("id", ns, 'ID', datatype=ServicesMeteoId, permissions='r')
        self.__addVariable__("inputString", ns, 'Input string from the meteo station', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("data", ns, mtcs_common.QuantityValue, 'Actual value')
        self.__addVariable__("invalidData", ns, 'True if the data is invalid', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("lastChar", ns, 'Last character', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("name", ns, 'Name of the measurementw', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, ServicesMeteoMeasurementStatuses, 'Statuses of the state machine')

class ServicesMeteoMeasurement(SM_ServicesMeteoMeasurement):
    def __init__(self, parent, name, ns, info):
        SM_ServicesMeteoMeasurement.__init__(self, parent, name, ns, info)

class SM_ServicesMeteo(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("serialTimeout", ns, 'Is the serial data not being received within time?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("comError", ns, 'Is there any problem with the COM port?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("comErrorID", ns, 'COM error id (see Beckhoff ComError_t)', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("comErrorDescription", ns, 'Description of the COM error id', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("windSpeedMinimum", ns, ServicesMeteoMeasurement, 'Wind speed minimum')
        self.__addInstance__("windSpeedAverage", ns, ServicesMeteoMeasurement, 'Wind speed average')
        self.__addInstance__("windSpeedMaximum", ns, ServicesMeteoMeasurement, 'Wind speed maximum')
        self.__addInstance__("windDirectionMinimum", ns, ServicesMeteoMeasurement, 'Wind direction minimum')
        self.__addInstance__("windDirectionAverage", ns, ServicesMeteoMeasurement, 'Wind direction average')
        self.__addInstance__("windDirectionMaximum", ns, ServicesMeteoMeasurement, 'Wind direction maximum')
        self.__addInstance__("airPressure", ns, ServicesMeteoMeasurement, 'Air pressure')
        self.__addInstance__("airTemperature", ns, ServicesMeteoMeasurement, 'Air temperature')
        self.__addInstance__("internalTemperature", ns, ServicesMeteoMeasurement, 'Internal temperature')
        self.__addInstance__("relativeHumidity", ns, ServicesMeteoMeasurement, 'Relative humidity')
        self.__addInstance__("rainAccumulation", ns, ServicesMeteoMeasurement, 'Rain accumulation')
        self.__addInstance__("rainDuration", ns, ServicesMeteoMeasurement, 'Rain duration')
        self.__addInstance__("rainIntensity", ns, ServicesMeteoMeasurement, 'Rain intensity')
        self.__addInstance__("rainPeakIntensity", ns, ServicesMeteoMeasurement, 'Rain peak intensity')
        self.__addInstance__("hailAccumulation", ns, ServicesMeteoMeasurement, 'Hail accumulation')
        self.__addInstance__("hailDuration", ns, ServicesMeteoMeasurement, 'Hail duration')
        self.__addInstance__("hailIntensity", ns, ServicesMeteoMeasurement, 'Hail intensity')
        self.__addInstance__("hailPeakIntensity", ns, ServicesMeteoMeasurement, 'Hail peak intensity')
        self.__addInstance__("heatingTemperature", ns, ServicesMeteoMeasurement, 'Heating temperature')
        self.__addInstance__("heatingVoltage", ns, ServicesMeteoMeasurement, 'Heating voltage')
        self.__addInstance__("supplyVoltage", ns, ServicesMeteoMeasurement, 'Supply voltage')
        self.__addInstance__("referenceVoltage", ns, ServicesMeteoMeasurement, 'Reference voltage')
        self.__addInstance__("durationOK", ns, mtcs_common.Duration, 'Duration that the meteo is OK')
        self.__addInstance__("dewpoint", ns, mtcs_common.Temperature, 'Calculated dewpoint')
        self.__addVariable__("wet", ns, 'Wet if (rainIntensity+hailIntensity) &gt; config.wetLimit', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("heating", ns, 'Heating or not?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("windDirectionMinimumString", ns, 'Average direction of the wind as a string', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("windDirectionAverageString", ns, 'Average direction of the wind as a string', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("windDirectionMaximumString", ns, 'Average direction of the wind as a string', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, ServicesMeteoStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, ServicesMeteoProcesses, 'Processes of the state machine')

class ServicesMeteo(SM_ServicesMeteo):
    def __init__(self, parent, name, ns, info):
        SM_ServicesMeteo.__init__(self, parent, name, ns, info)

class SM_ServicesIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, ServicesIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, ServicesIOParts, 'Parts of the state machine')

class ServicesIO(SM_ServicesIO):
    def __init__(self, parent, name, ns, info):
        SM_ServicesIO.__init__(self, parent, name, ns, info)



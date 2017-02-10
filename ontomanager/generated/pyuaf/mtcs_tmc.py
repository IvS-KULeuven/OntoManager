# === imports ===



# This file (mtcs_tmc.py) was automatically generated at 2017-02-07T14:54:30.549277 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class TmcTimingMode:
        LOCAL_CLOCK = 0
        PTP_IEEE_1588 = 1

class TmcAxesErrors:
        AXES_NO_ERROR = 0
        AXES_OBJECT_RC_OUT_OF_RANGE = 1
        AXES_OBJECT_DC_OUT_OF_RANGE = 2
        AXES_OBJECT_PR_OUT_OF_RANGE = 3
        AXES_OBJECT_PD_OUT_OF_RANGE = 4
        AXES_OBJECT_PX_OUT_OF_RANGE = 5
        AXES_EQ_OUT_OF_RANGE = 6
        AXES_LOCATION_XP_OUT_OF_RANGE = 7
        AXES_LOCATION_YP_OUT_OF_RANGE = 8
        AXES_LOCATION_DX_OUT_OF_RANGE = 9
        AXES_LOCATION_DY_OUT_OF_RANGE = 10
        AXES_LOCATION_ELONG_OUT_OF_RANGE = 11
        AXES_LOCATION_PHI_OUT_OF_RANGE = 12
        AXES_LOCATION_HM_OUT_OF_RANGE = 13
        AXES_LOCATION_TK_OUT_OF_RANGE = 14
        AXES_LOCATION_PHPA_OUT_OF_RANGE = 15
        AXES_LOCATION_RH_OUT_OF_RANGE = 16
        AXES_LOCATION_WLFQ_OUT_OF_RANGE = 17
        AXES_LOCATION_TLR_OUT_OF_RANGE = 18
        AXES_FEEDBACK_AZ_OUT_OF_RANGE = 19
        AXES_FEEDBACK_EL_OUT_OF_RANGE = 20

class TmcTimingErrors:
        TIMING_NO_ERROR = 0
        TIMING_DUT_OUT_OF_RANGE = 1
        TIMING_GETCURDCTIME_FAILED = 2


# === STRUCTS ===

class TmcTarget(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("rc", ns, 'Object mean right ascention (alpha) in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("dc", ns, 'Object mean declination (delta) in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pr", ns, 'Object Right Ascention proper motion in radians/year (do not multiply by cos(dc)!)', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("pd", ns, 'Object declination proper motion in radians/year', datatype=pyuaf.util.primitives.UInt16, permissions='')
        self.__addVariable__("px", ns, 'Object parallax in arcseconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rv", ns, 'Object radial velocity in km/s', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcLocation(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("xp", ns, 'Earth polar motion x in radians', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("yp", ns, 'Earth polar motion y in radians', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("dx", ns, 'Nutation adjustment dX in radians', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("dy", ns, 'Nutation adjustment dY in radians', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("elong", ns, 'East longitude in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("phi", ns, 'latitude in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("hm", ns, 'Height above sea level in meters', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("tk", ns, 'Local temperature in Kelvin', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("phpa", ns, 'Local pressure in hectoPascal = millibar', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("rh", ns, 'Local relative humidity as a fraction (0...1)', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("wlfq", ns, 'Observing wavelength in microns', datatype=pyuaf.util.primitives.Float, permissions='')
        self.__addVariable__("tlr", ns, 'Tropospheric lapse rate in K/m', datatype=pyuaf.util.primitives.Float, permissions='')

class TmcAzEl(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("az", ns, 'Azimuth in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("el", ns, 'Elevation in radians', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcAzElFull(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("az", ns, 'Azimuth in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("azd", ns, 'Azimuth velocity in radians per second', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("azdd", ns, 'Azimuth acceleration in radians/s2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("el", ns, 'Elevation in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("eld", ns, 'Elevation velocity in radians per second', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("eldd", ns, 'Elevation acceleration in radians/s2', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pa", ns, 'Parallactic Angle in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("pad", ns, 'Parallactic Angle velocity in radians per second', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("padd", ns, 'Parallactic Angle acceleration in radians/s2', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcRaDec(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("ra", ns, 'Right ascention (alpha) in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("dec", ns, 'Declination (delta) in radians', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcObserved(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("aob", ns, 'Observed azimuth (radians: North=0, East=PI/2)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("zob", ns, 'Observed zentih distance (radians)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("hob", ns, 'Observed hour angle (radians)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("dob", ns, 'Observed declination (radians)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rob", ns, 'Observed right ascention (radians)', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcTrue(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("elong", ns, 'True longitude of the site (radians, east +ve)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("phi", ns, 'True geodetic latitude of the site (radians)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("daz", ns, 'Azimuth correction for true longitude and latitude (terrestrial - celestial, radians)', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcProcessedTarget(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("given", ns, TmcTarget, 'The originally given target')
        self.__addInstance__("apparent", ns, TmcRaDec, 'Apparent target position')
        self.__addInstance__("quick", ns, TmcAzElFull, 'Quick computation results of target (without atmospheric refraction)')
        self.__addInstance__("observed", ns, TmcObserved, 'Observed target position')
        self.__addInstance__("observedFull", ns, TmcAzElFull, 'Observed target position/velocity/acceleration')
        self.__addVariable__("isValid", ns, 'Is the target valid?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isTooLow", ns, 'Is the target too low?', datatype=pyuaf.util.primitives.Boolean, permissions='')

class TmcProcessedFeedback(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("apparent", ns, TmcRaDec, 'Apparent feedback position')
        self.__addInstance__("mean", ns, TmcRaDec, 'Mean feedback position')
        self.__addVariable__("isValid", ns, 'Is the feedback valid?', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("isTooLow", ns, 'Is the feedback too low?', datatype=pyuaf.util.primitives.Boolean, permissions='')

class TmcDateTime(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("years", ns, 'Years, e.g. 2016', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("months", ns, 'Months, [1..12]', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("days", ns, 'Days, [1..31]', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("hours", ns, 'Hours, [0..23]', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("minutes", ns, 'Minutes, [0..59]', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("seconds", ns, 'Secconds, [0..60] (60 during leap second event!)', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("microseconds", ns, 'Microseconds, [0..999999]', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("fractionOfDay", ns, 'Fraction of the day, [0.0..1.0[', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcUnixTime(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("sec", ns, 'Seconds from Jan 1, 1970', datatype=pyuaf.util.primitives.UInt64, permissions='')
        self.__addVariable__("usec", ns, 'Microseconds', datatype=pyuaf.util.primitives.UInt64, permissions='')

class TmcUtcTime(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("dcTime", ns, 'DC time', datatype=pyuaf.util.primitives.UInt64, permissions='')
        self.__addVariable__("mode", ns, 'Local clock or PTP?', datatype=TmcTimingMode, permissions='')
        self.__addInstance__("unixTime", ns, TmcUnixTime, 'UTC as Unix time')
        self.__addVariable__("mjd", ns, 'UTC as Modified Julian Days', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("dateTime", ns, TmcDateTime, 'EtherCAT master: Offset between DC and TwinCAT time (in ns)')

class TmcUt1Time(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("mjd", ns, 'UT1 as Modified Julian Days', datatype=pyuaf.util.primitives.Double, permissions='')

class TmcFromIoEcatMaster(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("dcToTcTimeOffset", ns, 'EtherCAT master: Offset between DC and TwinCAT time (in ns)', datatype=pyuaf.util.primitives.UInt64, permissions='')
        self.__addVariable__("dcToExtTimeOffset", ns, 'EtherCAT master: Offset between Dc and external time (in ns)', datatype=pyuaf.util.primitives.UInt64, permissions='')

class TmcFromIoEL6688(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("internalTimestamp", ns, 'EL6688 module: internal timestamp', datatype=pyuaf.util.primitives.Int64, permissions='')
        self.__addVariable__("externalTimestamp", ns, 'EL6688 module: external timestamp', datatype=pyuaf.util.primitives.Int64, permissions='')
        self.__addVariable__("notConnected", ns, 'EL6688 module: not connected', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("updateToggle", ns, 'EL6688 module: update toggle', datatype=pyuaf.util.primitives.Boolean, permissions='')

class TmcFromIo(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("fromEL6688", ns, TmcFromIoEL6688, 'Connect to inputs of EL6688')
        self.__addInstance__("fromEcatMaster", ns, TmcFromIoEcatMaster, 'Connect to inputs of EtherCAT master')

class TmcFromPlcAxes(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("object", ns, TmcTarget, 'Target')
        self.__addVariable__("equinox", ns, 'Epoch of mean equinoxes (e.g. 2000.0)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("location", ns, TmcLocation, 'Location of the observatory')
        self.__addInstance__("feedback", ns, TmcAzEl, 'Feedback position (by the encoders)')

class TmcFromPlcTiming(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("dut", ns, 'Delta UT (=UT1 - UTC, floating point between 0 and 1 second)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("leapSeconds", ns, 'Number of leap seconds', datatype=pyuaf.util.primitives.UInt32, permissions='')
        self.__addVariable__("alwaysUseLocalClock", ns, 'If TRUE, then the local clock (source=LOCAL_CLOCK) will be used even if an external (more accurate!) clock is available', datatype=pyuaf.util.primitives.Boolean, permissions='')

class TmcFromPlc(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("fromAxes", ns, TmcFromPlcAxes, 'Connect to outputs of PLC - MTCS - Axes')
        self.__addInstance__("fromTiming", ns, TmcFromPlcTiming, 'Connect to outputs of PLC - MTCS - Services/Timing')

class TmcToPlcAxes(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("polmo", ns, TmcTrue, 'True longitude/latitude/azimuth after polar motion correction')
        self.__addVariable__("last", ns, 'Local apparent sidereal time', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ha", ns, 'Hour angle in radians', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("object", ns, TmcProcessedTarget, 'Processed target')
        self.__addInstance__("feedback", ns, TmcProcessedFeedback, 'Processed feedback')
        self.__addVariable__("error", ns, '0 = no error', datatype=TmcAxesErrors, permissions='')

class TmcToPlcTiming(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("utc", ns, TmcUtcTime, 'UTC time')
        self.__addInstance__("ut1", ns, TmcUt1Time, 'UT1 time')
        self.__addVariable__("error", ns, '0 = no error', datatype=TmcTimingErrors, permissions='')

class TmcToPlc(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("toAxes", ns, TmcToPlcAxes, 'Connect to inputs of PLC - MTCS - Axes')
        self.__addInstance__("toTiming", ns, TmcToPlcTiming, 'Connect to inputs of PLC - MTCS - Services/Timing')


# === FBs ===



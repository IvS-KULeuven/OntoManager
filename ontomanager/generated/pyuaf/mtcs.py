# === imports ===

import mtcs_telemetry
import mtcs_cover
import mtcs_m1
import mtcs_m2
import mtcs_m3
import mtcs_services
import mtcs_safety
import mtcs_hydraulics
import mtcs_axes
import mtcs_dome
import mtcs_common


# This file (mtcs.py) was automatically generated at 2017-02-10T19:12:43.634905 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====


# === STRUCTS ===

class MTCSParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("telemetry", ns, mtcs_telemetry.Telemetry, 'The telemetry')
        self.__addInstance__("cover", ns, mtcs_cover.Cover, 'The Cover of the telescope')
        self.__addInstance__("m1", ns, mtcs_m1.M1, 'The primary mirror of the telescope')
        self.__addInstance__("m2", ns, mtcs_m2.M2, 'The secondary mirror of the telescope')
        self.__addInstance__("m3", ns, mtcs_m3.M3, 'The tertiary mirror of the telescope')
        self.__addInstance__("services", ns, mtcs_services.Services, 'The Services system')
        self.__addInstance__("safety", ns, mtcs_safety.Safety, 'The safety')
        self.__addInstance__("hydraulics", ns, mtcs_hydraulics.Hydraulics, 'The hydraulics')
        self.__addInstance__("axes", ns, mtcs_axes.Axes, 'The axes')
        self.__addInstance__("dome", ns, mtcs_dome.Dome, 'The dome')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class MTCSProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing the whole MTCS')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the whole MTCS')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the whole MTCS')
        self.__addInstance__("changeOperator", ns, mtcs_common.ChangeOperatorStateProcess, 'Change the operator (e.g. OBSERVER, TECH, ...)')
        self.__addInstance__("verifyPassword", ns, mtcs_common.ChangeOperatorStateProcess, 'Only verify the operator password')
        self.__addInstance__("reboot", ns, mtcs_common.Process, 'Reboot the whole MTCS')
        self.__addInstance__("shutdown", ns, mtcs_common.Process, 'Shutdown the whole MTCS')
        self.__addInstance__("wakeUp", ns, mtcs_common.Process, 'Wake up the whole MTCS')
        self.__addInstance__("goToSleep", ns, mtcs_common.Process, 'Let the whole MTCS go to sleep')
        self.__addInstance__("stop", ns, mtcs_common.Process, 'Stop the dome and telescope')
        self.__addInstance__("endOfNight", ns, mtcs_common.Process, 'End of night')
        self.__addInstance__("changeInstrument", ns, MTCSChangeInstrumentProcess, 'Change the instrument')
        self.__addInstance__("park", ns, MTCSParkProcess, 'Park the telescope (including Axes, Dome, M3, ...)')
        self.__addInstance__("point", ns, MTCSPointProcess, 'Point the telescope and dome to a new target')

class MTCSStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatorStatus", ns, mtcs_common.OperatorStatus, '')
        self.__addInstance__("passwordHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("activityStatus", ns, mtcs_common.ActivityStatus, '')

class MTCSInstrumentsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("instrument0", ns, mtcs_common.InstrumentConfig, 'Instrument 0')
        self.__addInstance__("instrument1", ns, mtcs_common.InstrumentConfig, 'Instrument 1')
        self.__addInstance__("instrument2", ns, mtcs_common.InstrumentConfig, 'Instrument 2')
        self.__addInstance__("instrument3", ns, mtcs_common.InstrumentConfig, 'Instrument 3')
        self.__addInstance__("instrument4", ns, mtcs_common.InstrumentConfig, 'Instrument 4')
        self.__addInstance__("instrument5", ns, mtcs_common.InstrumentConfig, 'Instrument 5')
        self.__addInstance__("instrument6", ns, mtcs_common.InstrumentConfig, 'Instrument 6')
        self.__addInstance__("instrument7", ns, mtcs_common.InstrumentConfig, 'Instrument 7')
        self.__addInstance__("instrument8", ns, mtcs_common.InstrumentConfig, 'Instrument 8')
        self.__addInstance__("instrument9", ns, mtcs_common.InstrumentConfig, 'Instrument 9')

class MTCSParkPositionConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'The name of the position (e.g. &#39;PARK&#39;)', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("axes", ns, 'Name of the corresponding Axes position', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("doAxes", ns, 'Change the Axes to the &#39;axes&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("m3", ns, 'Name of the corresponding M3 position', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("doM3", ns, 'Change M3 to the &#39;m3&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("dome", ns, 'Name of the corresponding dome position', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("doDome", ns, 'Change M3 to the &#39;m3&#39; position', datatype=pyuaf.util.primitives.Boolean, permissions='')

class MTCSParkPositionsConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("position0", ns, MTCSParkPositionConfig, 'Park position 0')
        self.__addInstance__("position1", ns, MTCSParkPositionConfig, 'Park position 1')
        self.__addInstance__("position2", ns, MTCSParkPositionConfig, 'Park position 2')
        self.__addInstance__("position3", ns, MTCSParkPositionConfig, 'Park position 3')
        self.__addInstance__("position4", ns, MTCSParkPositionConfig, 'Park position 4')
        self.__addInstance__("position5", ns, MTCSParkPositionConfig, 'Park position 5')
        self.__addInstance__("position6", ns, MTCSParkPositionConfig, 'Park position 6')
        self.__addInstance__("position7", ns, MTCSParkPositionConfig, 'Park position 7')
        self.__addInstance__("position8", ns, MTCSParkPositionConfig, 'Park position 8')
        self.__addInstance__("position9", ns, MTCSParkPositionConfig, 'Park position 9')

class MTCSEndOfNightStepConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("description", ns, 'Description of this step (to show in HMI)', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("parkAxes", ns, 'Park the axes', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("parkAxesPosition", ns, 'Position to park the axes', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("parkAxesWait", ns, 'Wait until the axes is parked', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("parkM3", ns, 'Park M3', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("parkM3Position", ns, 'Position to park M3', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("parkM3Wait", ns, 'Wait until M3 is parked', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("parkDome", ns, 'Park the dome', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("parkDomePosition", ns, 'Position to park the dome', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("parkDomeWait", ns, 'Wait until the dome is parked', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("closeCover", ns, 'Close the cover', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("closeCoverWait", ns, 'Wait until the cover is closed', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("closeDome", ns, 'Close the dome', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("closeDomeWait", ns, 'Wait until the dome is closed', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("stop", ns, 'Stop the axes and dome', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("stopWait", ns, 'Wait until the axes and dome are stopped', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("goToSleep", ns, 'Make the telescope go to sleep', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("goToSleepWait", ns, 'Wait until the telescope is sleeping', datatype=pyuaf.util.primitives.Boolean, permissions='')

class MTCSEndOfNightConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("step0", ns, MTCSEndOfNightStepConfig, 'Step 0')
        self.__addInstance__("step1", ns, MTCSEndOfNightStepConfig, 'Step 1')
        self.__addInstance__("step2", ns, MTCSEndOfNightStepConfig, 'Step 2')
        self.__addInstance__("step3", ns, MTCSEndOfNightStepConfig, 'Step 3')
        self.__addInstance__("step4", ns, MTCSEndOfNightStepConfig, 'Step 4')
        self.__addInstance__("step5", ns, MTCSEndOfNightStepConfig, 'Step 5')
        self.__addInstance__("step6", ns, MTCSEndOfNightStepConfig, 'Step 6')
        self.__addInstance__("step7", ns, MTCSEndOfNightStepConfig, 'Step 7')
        self.__addInstance__("step8", ns, MTCSEndOfNightStepConfig, 'Step 8')
        self.__addInstance__("step9", ns, MTCSEndOfNightStepConfig, 'Step 9')
        self.__addInstance__("step10", ns, MTCSEndOfNightStepConfig, 'Step 10')
        self.__addInstance__("step11", ns, MTCSEndOfNightStepConfig, 'Step 11')
        self.__addInstance__("step12", ns, MTCSEndOfNightStepConfig, 'Step 12')
        self.__addInstance__("step13", ns, MTCSEndOfNightStepConfig, 'Step 13')
        self.__addInstance__("step14", ns, MTCSEndOfNightStepConfig, 'Step 14')
        self.__addInstance__("step15", ns, MTCSEndOfNightStepConfig, 'Step 15')
        self.__addInstance__("step16", ns, MTCSEndOfNightStepConfig, 'Step 16')
        self.__addInstance__("step17", ns, MTCSEndOfNightStepConfig, 'Step 17')
        self.__addInstance__("step18", ns, MTCSEndOfNightStepConfig, 'Step 18')
        self.__addInstance__("step19", ns, MTCSEndOfNightStepConfig, 'Step 19')

class MTCSConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("instruments", ns, MTCSInstrumentsConfig, 'Configure the instruments')
        self.__addInstance__("endOfNight", ns, MTCSEndOfNightConfig, 'Configure the instruments')
        self.__addInstance__("parkPositions", ns, MTCSParkPositionsConfig, 'Configure the park positions of the telescope (dome+telescope+m3+...)')

class MTCSChangeInstrumentProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the instrument', datatype=pyuaf.util.primitives.String, permissions='')

class MTCSParkProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the park position', datatype=pyuaf.util.primitives.String, permissions='')

class MTCSPointProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("alphaUnits", ns, 'The units in which alpha is given', datatype=mtcs_axes.AxesAlphaUnits, permissions='')
        self.__addVariable__("alpha", ns, 'Right ascention, in the units of the alphaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("deltaUnits", ns, 'The units in which delta is given', datatype=mtcs_axes.AxesDeltaUnits, permissions='')
        self.__addVariable__("delta", ns, 'Declination, in the units of the deltaUnits argument', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("muUnits", ns, 'The units in which muAlpha and muDelta are given', datatype=mtcs_axes.AxesMuUnits, permissions='')
        self.__addVariable__("muAlpha", ns, 'Right ascention proper motion, the units of muUmits (do not multiply by cos(delta)!)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("muDelta", ns, 'Declination proper motion, in radians/year', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("parallax", ns, 'Object parallax, in arcseconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("radialVelocity", ns, 'Object radial velocity, in km/s', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("epoch", ns, 'Epoch, e.g. 2000.0', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("tracking", ns, 'True to start tracking the object, false to Only do a pointing', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("rotUnits", ns, 'Units of the &#39;rot&#39;, &#39;roc&#39; and &#39;ron&#39; arguments (RADIANS, DEGREES, ARCSECONDS, ...)', datatype=mtcs_axes.AxesMoveUnits, permissions='')
        self.__addVariable__("rotOffset", ns, 'Offset to move the currently active rotator (incompatible with &#39;roc&#39; and &#39;ron&#39; args)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("rocOffset", ns, 'Offset to move the cassegrain rotation axis (incompatible with &#39;rot&#39; arg)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("ronOffset", ns, 'Offset to move the nasmyth rotation axis (incompatible with &#39;rot&#39; arg)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("doRotOffset", ns, 'True to move the currently active rotator, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRocOffset", ns, 'True to move the cassegrain rotation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doRonOffset", ns, 'True to move the nasmyth rotation axis, false to leave it untouched', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("doDomeTracking", ns, 'True to enable dome tracking', datatype=pyuaf.util.primitives.Boolean, permissions='')


# === FBs ===

class SM_MTCS(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, MTCSConfig, 'Editable configuration of the MTCS')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("noOfFailedOperatorChanges", ns, 'How many times has a wrong password been entered?', datatype=pyuaf.util.primitives.Int16, permissions='r')
        self.__addInstance__("activeInstrument", ns, mtcs_common.InstrumentConfig, 'Config of the currently active instrument (depending on M3 and possibly derotator) *if* isInstrumentActive is TRUE')
        self.__addVariable__("activeInstrumentNumber", ns, 'Number of the currently active instrument (0..9, or -1 if no instrument is active)', datatype=pyuaf.util.primitives.UInt16, permissions='r')
        self.__addVariable__("activeInstrumentName", ns, 'Name of the currently active instrument', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("isInstrumentActive", ns, 'Is an instrument currently active (i.e. is M3 static at a known position?)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("config", ns, MTCSConfig, 'Active configuration of the ServicesTiming subsystem')
        self.__addInstance__("statuses", ns, MTCSStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, MTCSParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, MTCSProcesses, 'Processes of the state machine')

class MTCS(SM_MTCS):
    def __init__(self, parent, name, ns, info):
        SM_MTCS.__init__(self, parent, name, ns, info)

class MTCSChangeInstrumentProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, MTCSChangeInstrumentProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, MTCSChangeInstrumentProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class MTCSParkProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, MTCSParkProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, MTCSParkProcessArgs, 'Arguments in use by the process, if do_request was accepted')


class MTCSPointProcess(mtcs_common.BaseProcess):

    def __init__(self, parent, name, ns, info):
        mtcs_common.BaseProcess.__init__(self, parent, name, ns, info)
        self.__addInstance__("set", ns, MTCSPointProcessArgs, 'Arguments to be set, before writing do_request TRUE')
        self.__addInstance__("get", ns, MTCSPointProcessArgs, 'Arguments in use by the process, if do_request was accepted')




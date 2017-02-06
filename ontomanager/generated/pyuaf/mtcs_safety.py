# === imports ===

import mtcs_common


# This file (mtcs_safety.py) was automatically generated at 2016-06-02T10:45:22.343496 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====


# === STRUCTS ===

class SafetyParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("hydraulics", ns, SafetyHydraulics, 'Hydraulics safety')
        self.__addInstance__("emergencyStops", ns, SafetyEmergencyStops, 'Emergency stops')
        self.__addInstance__("domeAccess", ns, SafetyDomeAccess, 'Dome access')
        self.__addInstance__("motionBlocking", ns, SafetyMotionBlocking, 'Motion blocking')
        self.__addInstance__("io", ns, SafetyIO, 'I/O modules')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class SafetyIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("domeAccess", ns, SafetyDomeAccessIO, 'DA: Dome access I/O')
        self.__addInstance__("hydraulicsAndSafety", ns, SafetyHydraulicsAndSafetyIO, 'HS: Hydraulics and Safety I/O')

class SafetyHydraulicsAndSafetyIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("COU", ns, mtcs_common.EtherCatDevice, 'HS:COU (EK1101)')
        self.__addInstance__("DO1", ns, mtcs_common.EtherCatDevice, 'HS:DO1 (EL2008)')
        self.__addInstance__("SI1", ns, mtcs_common.EtherCatDevice, 'HS:SI1 (EL1904)')
        self.__addInstance__("SI2", ns, mtcs_common.EtherCatDevice, 'HS:SI2 (EL1904)')
        self.__addInstance__("SI3", ns, mtcs_common.EtherCatDevice, 'HS:SI3 (EL1904)')
        self.__addInstance__("SI4", ns, mtcs_common.EtherCatDevice, 'HS:SI4 (EL1904)')
        self.__addInstance__("SL", ns, mtcs_common.EtherCatDevice, 'HS:SL (EL6900)')
        self.__addInstance__("SO1", ns, mtcs_common.EtherCatDevice, 'HS:SO1 (EL2904)')
        self.__addInstance__("AI1", ns, mtcs_common.EtherCatDevice, 'HS:AI1 (EL3102)')
        self.__addInstance__("AI2", ns, mtcs_common.EtherCatDevice, 'HS:AI2 (EL3152)')
        self.__addInstance__("RTD1", ns, mtcs_common.EtherCatDevice, 'HS:RTD1 (EL3202-0010)')
        self.__addInstance__("PWR1", ns, mtcs_common.EtherCatDevice, 'HS:PWR1 (EL9410)')
        self.__addInstance__("AO1", ns, mtcs_common.EtherCatDevice, 'HS:AO1 (EL4132)')

class SafetyDomeAccessIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("COU", ns, mtcs_common.EtherCatDevice, 'DA:COU (EK1101)')
        self.__addInstance__("DI1", ns, mtcs_common.EtherCatDevice, 'DA:DI1 (EL1008)')
        self.__addInstance__("DI2", ns, mtcs_common.EtherCatDevice, 'DA:DI2 (EL1008)')
        self.__addInstance__("DO1", ns, mtcs_common.EtherCatDevice, 'DA:DO1 (EL2008)')
        self.__addInstance__("SI1", ns, mtcs_common.EtherCatDevice, 'DA:SI1 (EL1904)')
        self.__addInstance__("RE1", ns, mtcs_common.EtherCatDevice, 'DA:RE1 (EL2622)')
        self.__addInstance__("RE2", ns, mtcs_common.EtherCatDevice, 'DA:RE2 (EL2622)')

class SafetyDomeAccessParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("lampsRelay1", ns, mtcs_common.SimpleRelay, 'Lamps relay 1')
        self.__addInstance__("lampsRelay2", ns, mtcs_common.SimpleRelay, 'Lamps relay 2')
        self.__addInstance__("lampsRelay3", ns, mtcs_common.SimpleRelay, 'Lamps relay 3')
        self.__addInstance__("lampsRelay4", ns, mtcs_common.SimpleRelay, 'Lamps relay 4')

class SafetyProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the system')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the system')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')

class SafetyHydraulicsProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("startupPumps", ns, mtcs_common.Process, 'Start up the pumps (this will first trigger a reset() command!)')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the errors (including the programmed ones and the TwinSAFE group ones)')

class SafetyEmergencyStopsProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the errors (including the programmed ones and the TwinSAFE group ones)')

class SafetyDomeAccessProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the errors (including the programmed ones and the TwinSAFE group ones)')
        self.__addInstance__("personHasLeft", ns, mtcs_common.Process, 'Unblock the telescope (if possible, i.e. if no E-Stops are active etc.)')
        self.__addInstance__("bypass", ns, mtcs_common.Process, 'Bypass the doors sensors for the number of seconds defined in the config')
        self.__addInstance__("bypassPermanently", ns, mtcs_common.Process, 'Bypass the doors sensors permanently (until re-initialization)')
        self.__addInstance__("stopBypassing", ns, mtcs_common.Process, 'Stop bypassing the doors sensors')

class SafetyMotionBlockingProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset the errors (including the programmed ones and the TwinSAFE group ones)')

class SafetyStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')
        self.__addInstance__("communicationHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("functionBlockHealthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("outputHealthStatus", ns, mtcs_common.HealthStatus, '')

class SafetyIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class SafetyHydraulicsAndSafetyIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class SafetyDomeAccessIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class SafetyHydraulicsStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the safety in a healthy state? Good=RUN, Bad=safe stopped')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the safety busy?')

class SafetyEmergencyStopsStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Are the emergency stops in a healthy state? Good=RUN, Bad=safe stopped')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the safety busy?')

class SafetyDomeAccessStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Are the emergency stops in a healthy state? Good=RUN, Bad=safe stopped')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the safety busy?')

class SafetyMotionBlockingStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the safety busy?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is everything unblocked? Good=unblocked, Bad=safe stopped')

class SafetyDomeAccessAlertConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("pattern", ns, 'Bit pattern, for which bit=high means alert active, bit=low means alert off', datatype=pyuaf.util.primitives.Int32, permissions='')
        self.__addVariable__("patternLength", ns, 'Number of bits of the bitPattern to use (between 1 and 32)', datatype=pyuaf.util.primitives.Byte, permissions='')
        self.__addVariable__("bitLength", ns, 'Sound length of 1 bit, in milliseconds', datatype=pyuaf.util.primitives.Int16, permissions='')
        self.__addVariable__("totalTime", ns, 'The time, in number of milliseconds, during which the pattern is repeated. 0 means repeat forever.', datatype=pyuaf.util.primitives.Int16, permissions='')

class SafetyDomeAccessConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("disabled", ns, 'True if the dome access control system should be disabled permanently.', datatype=pyuaf.util.primitives.Boolean, permissions='')
        self.__addVariable__("bypassTimeAfterPassword", ns, 'Time until during which the doors sensors are being bypassed after entering the password, in seconds', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addInstance__("bypassingSound", ns, SafetyDomeAccessAlertConfig, 'Sound to play when the doors sensors are being bypassed')
        self.__addInstance__("bypassedPermanentlyVisual", ns, SafetyDomeAccessAlertConfig, 'LED pattern to play when the doors sensors are now bypassed permanently')
        self.__addInstance__("doorsOpenedWhenEnteringSound", ns, SafetyDomeAccessAlertConfig, 'Sound to play when a door is being opened for the first time (i.e. when a person is entering)')
        self.__addInstance__("doorsOpenedWhenLeavingSound", ns, SafetyDomeAccessAlertConfig, 'Sound to play when a door is being opened for the 2nd or 3rd or ... time (i.e. when a person is leaving)')
        self.__addInstance__("leavingWhenDoorsClosedSound", ns, SafetyDomeAccessAlertConfig, 'Sound to play when the personHasLeftButton is pressed when the doors are closed')
        self.__addInstance__("leavingWhenDoosOpenedSound", ns, SafetyDomeAccessAlertConfig, 'Sound to play when the personHasLeftButton is pressed when the doors are still open')
        self.__addInstance__("doorsOpenedVisual", ns, SafetyDomeAccessAlertConfig, 'LED pattern to play when the doors were opened without bypass (i.e. without password)')

class SafetyConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("domeAccess", ns, SafetyDomeAccessConfig, 'Some configuration values of the Dome Access')


# === FBs ===

class SM_Safety(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, SafetyConfig, 'Editable configuration of the Safety subsystem')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("config", ns, SafetyConfig, 'Active configuration of the Safety subsystem')
        self.__addInstance__("statuses", ns, SafetyStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, SafetyParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, SafetyProcesses, 'Processes of the state machine')

class Safety(SM_Safety):
    def __init__(self, parent, name, ns, info):
        SM_Safety.__init__(self, parent, name, ns, info)

class SM_SafetyIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, SafetyIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, SafetyIOParts, 'Parts of the state machine')

class SafetyIO(SM_SafetyIO):
    def __init__(self, parent, name, ns, info):
        SM_SafetyIO.__init__(self, parent, name, ns, info)

class SM_SafetyHydraulicsAndSafetyIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, SafetyHydraulicsAndSafetyIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, SafetyHydraulicsAndSafetyIOParts, 'Parts of the state machine')

class SafetyHydraulicsAndSafetyIO(SM_SafetyHydraulicsAndSafetyIO):
    def __init__(self, parent, name, ns, info):
        SM_SafetyHydraulicsAndSafetyIO.__init__(self, parent, name, ns, info)

class SM_SafetyDomeAccessIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addInstance__("statuses", ns, SafetyDomeAccessIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, SafetyDomeAccessIOParts, 'Parts of the state machine')

class SafetyDomeAccessIO(SM_SafetyDomeAccessIO):
    def __init__(self, parent, name, ns, info):
        SM_SafetyDomeAccessIO.__init__(self, parent, name, ns, info)

class SM_SafetyHydraulics(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("groupComError", ns, 'TwinSAFE group communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupFbError", ns, 'TwinSAFE group function block error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupOutError", ns, 'TwinSAFE group output error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsPowered", ns, 'TRUE if the pumps are powered', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("returnFilterOverpressure", ns, 'TRUE if the oil return filter has an overpressure', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsMinFrequency", ns, 'TRUE if the pumps run at a minimum frequency (frequency &gt; QMin)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsFrequencyNotRising", ns, 'TRUE if the frequency of the pumps is not rising after a startup command', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pressureNotRising", ns, 'TRUE if the pressure is not rising after the frequency is rising', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("top1NoUnderpressure", ns, 'TRUE if there is no underpressure for Top pipe 1', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("top2NoUnderpressure", ns, 'TRUE if there is no underpressure for Top pipe 2', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("top3NoUnderpressure", ns, 'TRUE if there is no underpressure for Top pipe 3', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("top4NoUnderpressure", ns, 'TRUE if there is no underpressure for Top pipe 4', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bottom5NoUnderpressure", ns, 'TRUE if there is no underpressure for Bottom pipe 5', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bottom6NoUnderpressure", ns, 'TRUE if there is no underpressure for Bottom pipe 6', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bottom7NoUnderpressure", ns, 'TRUE if there is no underpressure for Bottom pipe 7', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bottom8NoUnderpressure", ns, 'TRUE if there is no underpressure for Bottom pipe 8', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("topNoOverpressure", ns, 'TRUE if there is no overpressure for the Top pipes', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bottomNoOverpressure", ns, 'TRUE if there is no overpressure for the Bottom pipes', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("topTripOK", ns, 'TRUE if there is no TRIP error for the top drive', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("bottomTripOK", ns, 'TRUE if there is no overpressure for the botton drive', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("noUnderpressure", ns, 'TRUE if there is no underpressure for all 8 pipes', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("noUnderpressureNoDelay", ns, 'TRUE if there is no underpressure for all 8 pipes (even momentarily, without delay)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("underpressureError", ns, 'TRUE if there is an underpressure problem (e.g. when the pumps are running and there is an underpressure)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("noOverpressure", ns, 'TRUE if there is no overpressure for all 8 pipes', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsStartingUp", ns, 'TRUE if the pumps are restarting', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsStopped", ns, 'TRUE if the pumps are stopped', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsRunning", ns, 'TRUE if the pumps are running', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("pumpsRelease", ns, 'TRUE if the pumps are released (RFR &#39;ReglerFreigabe&#39; high)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("allOK", ns, 'TRUE if the hydraulics are OK', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("restartPumpsOutput", ns, 'Output to restart the pumps', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("resetErrorsOutput", ns, 'Output to reset the errors', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("errorAcknowledge", ns, 'Output to restart the TwinSAFE group', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, SafetyHydraulicsStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, SafetyHydraulicsProcesses, 'Processes of the state machine')

class SafetyHydraulics(SM_SafetyHydraulics):
    def __init__(self, parent, name, ns, info):
        SM_SafetyHydraulics.__init__(self, parent, name, ns, info)

class SM_SafetyEmergencyStops(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("groupComError", ns, 'TwinSAFE group communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupFbError", ns, 'TwinSAFE group function block error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupOutError", ns, 'TwinSAFE group output error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("allOK", ns, 'TRUE if the emergency stops are OK', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("discrepancyError", ns, 'TRUE if there is a discrepancy time error between two contacts of an emergency stop', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("dome1NO", ns, 'TRUE if the make contact (NO) is conducting --&gt; button is pushed!', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("dome1NC", ns, 'TRUE if the break contact (NC) is conducting --&gt; button is not pushed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("dome2NO", ns, 'TRUE if the make contact (NO) is conducting --&gt; button is pushed!', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("dome2NC", ns, 'TRUE if the break contact (NC) is conducting --&gt; button is not pushed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("firstFloorNO", ns, 'TRUE if the make contact (NO) is conducting --&gt; button is pushed!', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("firstFloorNC", ns, 'TRUE if the break contact (NC) is conducting --&gt; button is not pushed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("controlRoomNO", ns, 'TRUE if the make contact (NO) is conducting --&gt; button is pushed!', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("controlRoomNC", ns, 'TRUE if the break contact (NC) is conducting --&gt; button is not pushed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("domeAccessNO", ns, 'TRUE if the make contact (NO) is conducting --&gt; button is pushed!', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("domeAccessNC", ns, 'TRUE if the break contact (NC) is conducting --&gt; button is not pushed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("restartOutput", ns, 'Output to restart the emergency buttons', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("errorAcknowledge", ns, 'Output to restart the TwinSAFE group', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, SafetyEmergencyStopsStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, SafetyEmergencyStopsProcesses, 'Processes of the state machine')

class SafetyEmergencyStops(SM_SafetyEmergencyStops):
    def __init__(self, parent, name, ns, info):
        SM_SafetyEmergencyStops.__init__(self, parent, name, ns, info)

class SM_SafetyDomeAccess(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("groupComError", ns, 'TwinSAFE group communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupFbError", ns, 'TwinSAFE group function block error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupOutError", ns, 'TwinSAFE group output error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey1", ns, 'TRUE if keypad key 1 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey2", ns, 'TRUE if keypad key 2 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey3", ns, 'TRUE if keypad key 3 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey4", ns, 'TRUE if keypad key 4 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey5", ns, 'TRUE if keypad key 5 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey6", ns, 'TRUE if keypad key 6 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey7", ns, 'TRUE if keypad key 7 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey8", ns, 'TRUE if keypad key 8 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKey9", ns, 'TRUE if keypad key 9 is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("keypadKeyStar", ns, 'TRUE if keypad key * is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("door1Closed", ns, 'TRUE if door 1 is closed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("door2Closed", ns, 'TRUE if door 2 is closed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("personHasLeftButtonPressed", ns, 'TRUE if the unblock button is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("returnButtonPressed", ns, 'TRUE if the return button is being pressed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("errorAcknowledge", ns, 'Output to restart the TwinSAFE group', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("personHasEntered", ns, 'TRUE if the doors were opened without bypass/password', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("enteredLedOn", ns, 'TRUE if the yellow led should be on', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("movingLedOn", ns, 'TRUE if the red led should be on', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("awakeLedOn", ns, 'TRUE if the yellow led should be on', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("sleepingLedOn", ns, 'TRUE if the orange led should be on', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("buzzerSounding", ns, 'TRUE if the green is being sounded', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("sensorsBeingBypassed", ns, 'TRUE if the sensors are currently being bypassed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("sensorsBypassedPermanently", ns, 'TRUE if the sensors are being bypassed permanently', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, SafetyDomeAccessStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, SafetyDomeAccessParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, SafetyDomeAccessProcesses, 'Processes of the state machine')

class SafetyDomeAccess(SM_SafetyDomeAccess):
    def __init__(self, parent, name, ns, info):
        SM_SafetyDomeAccess.__init__(self, parent, name, ns, info)

class SM_SafetyMotionBlocking(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("groupComError", ns, 'TwinSAFE group communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupFbError", ns, 'TwinSAFE group function block error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("groupOutError", ns, 'TwinSAFE group output error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("telescopeAzimuthReleaseOK", ns, 'TRUE if the telescope azimuth axis is released', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("telescopeElevationReleaseOK", ns, 'TRUE if the telescope elevation axis is released', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("telescopeRotationReleaseOK", ns, 'TRUE if the telescope rotation axes are released', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("motionAllowed", ns, 'TRUE if motion is allowed', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("errorAcknowledge", ns, 'Output to restart the TwinSAFE group', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, SafetyMotionBlockingStatuses, 'Statuses of the state machine')
        self.__addInstance__("processes", ns, SafetyMotionBlockingProcesses, 'Processes of the state machine')

class SafetyMotionBlocking(SM_SafetyMotionBlocking):
    def __init__(self, parent, name, ns, info):
        SM_SafetyMotionBlocking.__init__(self, parent, name, ns, info)



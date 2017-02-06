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
import mtcs_common


# This file (mtcs.py) was automatically generated at 2016-06-06T21:13:41.288481 -- do not edit manually!
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
        self.__addInstance__("changeInstrument", ns, MTCSChangeInstrumentProcess, 'Change the instrument')

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

class MTCSConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("instruments", ns, MTCSInstrumentsConfig, 'Configure the instruments')

class MTCSChangeInstrumentProcessArgs(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("name", ns, 'Name of the instrument', datatype=pyuaf.util.primitives.String, permissions='')


# === FBs ===

class SM_MTCS(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, MTCSConfig, 'Editable configuration of the MTCS')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
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




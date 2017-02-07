# === imports ===

import mtcs_common


# This file (mtcs_dome.py) was automatically generated at 2017-02-06T16:56:39.700842 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====


# === STRUCTS ===

class DomeParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("shutter", ns, DomeShutter, 'Shutter mechanism')
        self.__addInstance__("rotation", ns, DomeRotation, 'Rotation mechanism')
        self.__addInstance__("io", ns, DomeIO, 'EtherCAT devices')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class DomeShutterParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("pumpsRelay", ns, mtcs_common.SimpleRelay, 'Relay to start the pumps motors')
        self.__addInstance__("upperOpenRelay", ns, mtcs_common.SimpleRelay, 'Relay to open the upper shutter panel')
        self.__addInstance__("upperCloseRelay", ns, mtcs_common.SimpleRelay, 'Relay to close the upper shutter panel')
        self.__addInstance__("lowerOpenRelay", ns, mtcs_common.SimpleRelay, 'Relay to open the upper shutter panel')
        self.__addInstance__("lowerCloseRelay", ns, mtcs_common.SimpleRelay, 'Relay to close the upper shutter panel')

class DomeRotationParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("masterAxis", ns, mtcs_common.AngularAxis, 'Master axis')
        self.__addInstance__("slaveAxis", ns, mtcs_common.AngularAxis, 'Slave axis')
        self.__addInstance__("drive", ns, mtcs_common.AX52XXDrive, 'Dual axis drive')

class DomeIOParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("coupler", ns, mtcs_common.EtherCatDevice, 'Coupler')
        self.__addInstance__("slot1", ns, mtcs_common.EtherCatDevice, 'Slot 1')
        self.__addInstance__("slot2", ns, mtcs_common.EtherCatDevice, 'Slot 2')
        self.__addInstance__("slot3", ns, mtcs_common.EtherCatDevice, 'Slot 3')
        self.__addInstance__("slot4", ns, mtcs_common.EtherCatDevice, 'Slot 4')
        self.__addInstance__("slot5", ns, mtcs_common.EtherCatDevice, 'Slot 5')
        self.__addInstance__("slot6", ns, mtcs_common.EtherCatDevice, 'Slot 6')
        self.__addInstance__("slot7", ns, mtcs_common.EtherCatDevice, 'Slot 7')
        self.__addInstance__("slot8", ns, mtcs_common.EtherCatDevice, 'Slot 8')

class DomeProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the cover')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the cover')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset any errors')
        self.__addInstance__("powerOn", ns, mtcs_common.Process, 'Power on the dome')
        self.__addInstance__("powerOff", ns, mtcs_common.Process, 'Power off the dome')
        self.__addInstance__("syncWithAxes", ns, mtcs_common.Process, 'Synchronize the dome once with the axes')
        self.__addInstance__("trackAxes", ns, mtcs_common.Process, 'Start tracking the axes')
        self.__addInstance__("stop", ns, mtcs_common.Process, 'Stop the rotation movement and/or tracking')

class DomeShutterProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset errors')
        self.__addInstance__("open", ns, mtcs_common.Process, 'Open both panels')
        self.__addInstance__("close", ns, mtcs_common.Process, 'Close both panels')
        self.__addInstance__("stop", ns, mtcs_common.Process, 'Stop the panels')
        self.__addInstance__("lowerOpen", ns, mtcs_common.Process, 'Open the lower panel')
        self.__addInstance__("lowerClose", ns, mtcs_common.Process, 'Close the lower panel')
        self.__addInstance__("upperOpen", ns, mtcs_common.Process, 'Open the upper panel')
        self.__addInstance__("upperClose", ns, mtcs_common.Process, 'Close the upper panel')

class DomeRotationProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset errors')
        self.__addInstance__("stop", ns, mtcs_common.Process, 'Stop the rotation')

class DomeStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, '')

class DomeShutterStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("apertureStatus", ns, mtcs_common.ApertureStatus, 'Combined aperture status (i.e. of both panels)')
        self.__addInstance__("lowerApertureStatus", ns, mtcs_common.ApertureStatus, 'Aperture status of the lower panel')
        self.__addInstance__("upperApertureStatus", ns, mtcs_common.ApertureStatus, 'Aperture status of the upper panel')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Health status')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Busy status')

class DomeRotationStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Health status')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Busy status')
        self.__addInstance__("poweredStatus", ns, mtcs_common.PoweredStatus, 'Powered status')

class DomeIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class DomeConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("shutter", ns, DomeShutterConfig, 'The config of the shutter mechanism')
        self.__addInstance__("rotation", ns, DomeRotationConfig, 'The config of the bottom panel set')
        self.__addVariable__("maxTrackingDistance", ns, 'The maximum distance between telescope and dome while tracking', datatype=pyuaf.util.primitives.Double, permissions='')

class DomeShutterConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("wirelessPolling", ns, 'Polling frequency of the wireless I/O, in seconds. Negative value = no polling.', datatype=pyuaf.util.primitives.Double, permissions='')

class DomeRotationConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("maxMasterSlaveLag", ns, 'Below this lag value (in degrees), the lag is considered not an error', datatype=pyuaf.util.primitives.Double, permissions='')


# === FBs ===

class SM_Dome(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, DomeConfig, 'Editable configuration of the cover')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, DomeConfig, 'Active configuration of the cover')
        self.__addVariable__("isPoweredOffByPersonInDome", ns, 'True if the dome is powered off due to a person entering the dome', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("isTracking", ns, 'True if the dome is tracking the telescope', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, DomeStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, DomeParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, DomeProcesses, 'Processes of the state machine')

class Dome(SM_Dome):
    def __init__(self, parent, name, ns, info):
        SM_Dome.__init__(self, parent, name, ns, info)

class SM_DomeShutter(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("lowerOpenSignal", ns, 'False if the signal is not present OR if there is a communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("lowerClosedSignal", ns, 'False if the signal is not present OR if there is a communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("upperOpenSignal", ns, 'False if the signal is not present OR if there is a communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("upperClosedSignal", ns, 'False if the signal is not present OR if there is a communication error', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("wirelessTimeout", ns, 'True if the wireless communication to the shutter signals is timing out', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("wirelessError", ns, 'True if the wireless communication to the shutter signals is in error (other than timeout)', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("wirelessErrorId", ns, 'The error id if wirelessError is true', datatype=pyuaf.util.primitives.Int32, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, DomeShutterStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, DomeShutterParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, DomeShutterProcesses, 'Processes of the state machine')

class DomeShutter(SM_DomeShutter):
    def __init__(self, parent, name, ns, info):
        SM_DomeShutter.__init__(self, parent, name, ns, info)

class SM_DomeRotation(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("actPos", ns, mtcs_common.AngularPosition, 'The actual position (same as parts.masterAxis!)')
        self.__addInstance__("actVelo", ns, mtcs_common.AngularVelocity, 'The actual velocity (same as parts.masterAxis!)')
        self.__addInstance__("actAcc", ns, mtcs_common.AngularAcceleration, 'The actual acceleration (same as parts.masterAxis!)')
        self.__addInstance__("actTorqueMaster", ns, mtcs_common.Torque, 'The actual torque on the telescope axis by the master motor')
        self.__addInstance__("actTorqueSlave", ns, mtcs_common.Torque, 'The actual torque on the telescope axis by the slave motor')
        self.__addInstance__("masterSlaveLag", ns, mtcs_common.AngularPosition, 'masterAxis.actPos - slaveAxis.actPos')
        self.__addInstance__("masterSlaveLagError", ns, mtcs_common.AngularPosition, 'masterSlaveLag &gt;= config.maxMasterSlaveLag')
        self.__addVariable__("homingSensorSignal", ns, 'True = at home position', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("statuses", ns, DomeRotationStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, DomeRotationParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, DomeRotationProcesses, 'Processes of the state machine')

class DomeRotation(SM_DomeRotation):
    def __init__(self, parent, name, ns, info):
        SM_DomeRotation.__init__(self, parent, name, ns, info)

class SM_DomeIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, DomeIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, DomeIOParts, 'Parts of the state machine')

class DomeIO(SM_DomeIO):
    def __init__(self, parent, name, ns, info):
        SM_DomeIO.__init__(self, parent, name, ns, info)



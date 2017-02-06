# === imports ===

import mtcs_common


# This file (mtcs_cover.py) was automatically generated at 2017-02-03T09:55:17.523168 -- do not edit manually!
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


# === ENUMs ====

class CoverApertureProcedureStates:
        IDLE = 0
        ABORTED = 1
        PREPARE_PROCESS = 2
        ENABLING_RELAYS = 3
        ENABLING_MOTORS = 4
        ENABLING_MAGNETS = 5
        DISABLING_RELAYS = 6
        DISABLING_MOTORS = 7
        DISABLING_MAGNETS = 8
        OPENING_TOP_PANELS = 9
        OPENING_BOTH_PANELS = 10
        CLOSING_BOTTOM_PANELS = 11
        CLOSING_BOTH_PANELS = 12
        ERROR = 13
        RESETTING = 14
        ABORTING = 15


# === STRUCTS ===

class CoverParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("top", ns, CoverPanelSet, 'TOP panels')
        self.__addInstance__("bottom", ns, CoverPanelSet, 'BOTTOM panels')
        self.__addInstance__("io", ns, CoverIO, 'I/O modules')
        self.__addInstance__("apertureProcedure", ns, CoverApertureProcedure, 'The closing/opening/... procedure')
        self.__addInstance__("configManager", ns, mtcs_common.ConfigManager, 'The config manager (to load/save/activate configuration data)')

class CoverPanelSetParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("p1", ns, CoverPanel, 'Panel 1')
        self.__addInstance__("p2", ns, CoverPanel, 'Panel 2')
        self.__addInstance__("p3", ns, CoverPanel, 'Panel 3')
        self.__addInstance__("p4", ns, CoverPanel, 'Panel 4')
        self.__addInstance__("magnetsRelay", ns, mtcs_common.SimpleRelay, 'Relay for the magnets of this panelset')

class CoverPanelParts(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("axis", ns, mtcs_common.AngularAxis, 'NC Axis')
        self.__addInstance__("motorRelay", ns, mtcs_common.SimpleRelay, 'Relay for the motor')

class CoverIOParts(OpcUaNode):

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
        self.__addInstance__("slot9", ns, mtcs_common.EtherCatDevice, 'Slot 9')
        self.__addInstance__("slot10", ns, mtcs_common.EtherCatDevice, 'Slot 10')
        self.__addInstance__("slot11", ns, mtcs_common.EtherCatDevice, 'Slot 11')
        self.__addInstance__("slot12", ns, mtcs_common.EtherCatDevice, 'Slot 12')
        self.__addInstance__("slot13", ns, mtcs_common.EtherCatDevice, 'Slot 13')

class CoverProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initialize", ns, mtcs_common.Process, 'Start initializing')
        self.__addInstance__("lock", ns, mtcs_common.Process, 'Lock the cover')
        self.__addInstance__("unlock", ns, mtcs_common.Process, 'Unlock the cover')
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset any errors')
        self.__addInstance__("changeOperatingState", ns, mtcs_common.ChangeOperatingStateProcess, 'Change the operating state (e.g. AUTO, MANUAL, ...)')
        self.__addInstance__("open", ns, mtcs_common.Process, 'Start opening the cover (only enabled in AUTO mode!)')
        self.__addInstance__("close", ns, mtcs_common.Process, 'Start closing the cover (only enabled in AUTO mode!)')
        self.__addInstance__("abort", ns, mtcs_common.Process, 'Abort opening/closing the cover (only enabled in AUTO mode!)')

class CoverPanelSetProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("reset", ns, mtcs_common.Process, 'Reset any errors')

class CoverPanelProcesses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("startOpening", ns, mtcs_common.Process, 'Start opening the panel')
        self.__addInstance__("startClosing", ns, mtcs_common.Process, 'Start closing the panel')

class CoverStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("initializationStatus", ns, mtcs_common.InitializationStatus, '')
        self.__addInstance__("apertureStatus", ns, mtcs_common.ApertureStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')
        self.__addInstance__("operatingStatus", ns, mtcs_common.OperatingStatus, '')

class CoverApertureProcedureStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the CoverApertureProcedure in a busy state?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the CoverApertureProcedure in a healthy state?')

class CoverPanelSetStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("apertureStatus", ns, mtcs_common.ApertureStatus, '')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, '')
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, '')

class CoverPanelStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("busyStatus", ns, mtcs_common.BusyStatus, 'Is the panel in a busy state?')
        self.__addInstance__("apertureStatus", ns, mtcs_common.ApertureStatus, 'Is the panel open or closed?')
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the panel in a healthy state?')
        self.__addInstance__("openingStatus", ns, mtcs_common.OpeningStatus, 'Is the panel opening or closing or standing still?')

class CoverIOStatuses(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("healthStatus", ns, mtcs_common.HealthStatus, 'Is the I/O in a healthy state?')

class CoverConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("top", ns, CoverPanelSetConfig, 'The config of the top panel set')
        self.__addInstance__("bottom", ns, CoverPanelSetConfig, 'The config of the bottom panel set')
        self.__addVariable__("openingVelocity", ns, 'The opening velocity of the panels in degrees per second (always positive!)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("closingVelocity", ns, 'The closing velocity of the panels in degrees per second (always positive!)', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("magnetRemanentTime", ns, 'How many seconds should be waited after disabling a magnet, before a panel may move?', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("targetDistanceBetweenPanelSets", ns, 'The minimum distance in degrees between both panelsets', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("minDistanceBetweenPanelSets", ns, 'The minimum distance in degrees between both panelsets', datatype=pyuaf.util.primitives.Double, permissions='')

class CoverPanelSetConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("p1", ns, CoverPanelConfig, 'The config of the first panel of this set')
        self.__addInstance__("p2", ns, CoverPanelConfig, 'The config of the second panel of this set')
        self.__addInstance__("p3", ns, CoverPanelConfig, 'The config of the third panel of this set')
        self.__addInstance__("p4", ns, CoverPanelConfig, 'The config of the fourth panel of this set')
        self.__addVariable__("name", ns, 'The name of the panel set', datatype=pyuaf.util.primitives.String, permissions='')

class CoverPanelConfig(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("closedPosition", ns, 'The closed position of the panel in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("openPosition", ns, 'The open position of the panel in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("openTolerance", ns, 'The tolerance for opening, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("closedTolerance", ns, 'The tolerance for closing, in degrees', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("standstillTolerance", ns, 'Tolerance in degrees per second: if smaller than ABS(this value), then the cover panel is considered to be standing still', datatype=pyuaf.util.primitives.Double, permissions='')
        self.__addVariable__("name", ns, 'The name of the panel', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("offset", ns, 'The offset of the panel w.r.t. north', datatype=pyuaf.util.primitives.Double, permissions='')


# === FBs ===

class SM_Cover(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addInstance__("editableConfig", ns, CoverConfig, 'Editable configuration of the cover')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("config", ns, CoverConfig, 'Active configuration of the cover')
        self.__addInstance__("currentMeasurement", ns, mtcs_common.CurrentMeasurement, 'The current measurement of the selected panels')
        self.__addInstance__("statuses", ns, CoverStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, CoverParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, CoverProcesses, 'Processes of the state machine')

class Cover(SM_Cover):
    def __init__(self, parent, name, ns, info):
        SM_Cover.__init__(self, parent, name, ns, info)

class SM_CoverApertureProcedure(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("state", ns, 'New state, to be set by the manual implementation', datatype=CoverApertureProcedureStates, permissions='')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addVariable__("opening", ns, 'Is the procedure busy with opening?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("closing", ns, 'Is the procedure busy with closing?', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addInstance__("distance", ns, mtcs_common.AngularPosition, 'The closest distance between the top and bottom panels')
        self.__addInstance__("statuses", ns, CoverApertureProcedureStatuses, 'Statuses of the state machine')

class CoverApertureProcedure(SM_CoverApertureProcedure):
    def __init__(self, parent, name, ns, info):
        SM_CoverApertureProcedure.__init__(self, parent, name, ns, info)

class SM_CoverPanelSet(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, CoverPanelSetStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, CoverPanelSetParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, CoverPanelSetProcesses, 'Processes of the state machine')

class CoverPanelSet(SM_CoverPanelSet):
    def __init__(self, parent, name, ns, info):
        SM_CoverPanelSet.__init__(self, parent, name, ns, info)

class SM_CoverPanel(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("encoderErrorSignal", ns, 'Externally read error signal', datatype=pyuaf.util.primitives.Boolean, permissions='r')
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, CoverPanelStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, CoverPanelParts, 'Parts of the state machine')
        self.__addInstance__("processes", ns, CoverPanelProcesses, 'Processes of the state machine')

class CoverPanel(SM_CoverPanel):
    def __init__(self, parent, name, ns, info):
        SM_CoverPanel.__init__(self, parent, name, ns, info)

class SM_CoverIO(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__addVariable__("actualStatus", ns, 'Current status description', datatype=pyuaf.util.primitives.String, permissions='r')
        self.__addVariable__("previousStatus", ns, 'Previous status description', datatype=pyuaf.util.primitives.String, permissions='')
        self.__addInstance__("statuses", ns, CoverIOStatuses, 'Statuses of the state machine')
        self.__addInstance__("parts", ns, CoverIOParts, 'Parts of the state machine')

class CoverIO(SM_CoverIO):
    def __init__(self, parent, name, ns, info):
        SM_CoverIO.__init__(self, parent, name, ns, info)



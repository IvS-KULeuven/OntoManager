"""
Callback functions for the views of the 'elec' category.
"""

from triplestore import QUERY, INFO
import generic


# ======================================================== CONFIGURATIONS ===================================================


def getMainConfigurations(cache):
    """
    Expand the configurations of a node, that are not contained by another configuration.
    """
    INFO("elec.getMainConfigurations()")
    return generic.getInstances(cache = cache, className = "elec:Configuration", filterNotExists = "?x cont:contains ?instance")


def getConfigurations(cache):
    """
    Expand the configurations of a node.
    """
    INFO("elec.getConfigurations()")
    return generic.getInstances(cache = cache, className = "elec:Configuration")


def show_configuration(node, args=None):
    """
    Show the 'configuration' view of the 'elec' category.
    """
    INFO("elec.show_configuration(%s)" %node['qname'])

    node.expand("elec", "configuration")

    for expansion in ["I/O modules",
                      "circuit breakers",
                      "power supplies",
                      "motors",
                      "drives",
                      "terminals",
                      "wires",
                      "connectors",
                      "sensors",
                      "actuators",
                      "switches",
                      "cables",
                      "cable assemblies",
                      "sub-configurations",
                      "other devices"]:
        for item in node[expansion]:
            node.cache[item].show("elec")


def getSubConfigurations(cache, qname):
    """
    Expand the subconfigurations of a node.
    """
    INFO("elec.getSubConfigurations(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:Configuration")


def getOwningConfigurations(cache, qname):
    """
    Expand the owning configurations of a node.
    """
    INFO("elec.getOwningConfigurations(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="((^sys:realizes)|(sys:isRealizedBy))/((^cont:contains|cont:isContainedBy)+)", restriction="elec:Configuration", filterNotExists = "?x cont:contains ?result")


# ======================================================== TERMINALS ===================================================


def getTerminals(cache, qname):
    """
    Expand the terminals of a node.
    """
    INFO("elec.getTerminals(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasTerminal", restriction="elec:Terminal")


def show_Terminal(node, args=None):
    """
    Show the 'Terminal' view of the 'elec' category.
    """
    INFO("elec.show_Terminal(%s)" %node['qname'])

    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasTerminal' })

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")

    node.expand("elec", "Terminal")

    for connection in node["connections"]:
        node.cache[connection].show("elec")


def show_TerminalInstance(node, args=None):
    """
    Show the 'TerminalInstance' view of the 'elec' category.
    """
    INFO("elec.elec.show_TerminalInstance(%s)" %node['qname'])

    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol' , 'owner' : '^elec:hasTerminal' , 'realizes' : 'sys:realizes' })

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")
    if node['realizes'] is not None:
        generic.getDefaultNode(node.cache, node['realizes']).show("elec")

    node.expand("elec", "TerminalInstance")

    for connection in node["connections"]:
        node.cache[connection].show("elec")


# ====================================================== CONNECTIONS ===================================================


def getConnections(cache, qname):
    """
    Expand the "direct" connections of a node.
    """
    INFO("elec.getConnections(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="elec:isConnectedTo|^elec:isConnectedTo")

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames


def getAllConnections(cache, qname):
    """
    Expand the (in)direct connections of a node.
    """
    INFO("elec.getAllConnections(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="elec:isConnectedTo+|^elec:isConnectedTo+")

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames


# ======================================================= FITS ===================================================


def getFits(cache, qname):
    """
    Expand the fitting connectors of a node.
    """
    INFO("elec.getFits(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="elec:isJoinedWith|^elec:isJoinedWith")


# ======================================================= CONNECTORS ===================================================


def show_Gender(node, args=None):
    """
    Show the 'Gender' view of the 'elec' category.
    """
    pass


def show_Channel(node, args=None):
    """
    Show the 'Channel' view of the 'elec' category.
    """
    pass


def getConnectors(cache, qname):
    """
    Expand the connectors of a node.
    """
    INFO("soft.getConnectors(%s)" %(qname))

    return generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasConnector", restriction="elec:Connector")


def show_ConnectorType(node, args=None):
    """
    Show the 'ConnectorType' view of the 'elec' category.
    """
    INFO("elec.show_ConnectorType(%s)" %node['qname'])

    node.expand("elec", "ConnectorType")

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' },
                             optionals= { 'gender' : 'elec:hasGender' })

    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    if node['gender'] is not None:
        generic.getDefaultNode(node.cache, node['gender']).show()

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for pin in node["pins"]:
        node.cache[pin].show("elec")
    for fit in node["fits"]:
        node.cache[fit].show("elec")


def show_ConnectorInstance(node, args=None):
    """
    Show the 'ConnectorInstance' view of the 'elec' category.
    """
    INFO("elec.show_ConnectorInstance(%s)" %node['qname'])

    node.expand("elec", "ConnectorInstance")

    generic.fillFields(node, mandatories={'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol' })
    generic.getDefaultNode(node.cache, node['man_type']).show("elec")

    for pin in node["pins"]:
        node.cache[pin].show("elec")
    for wire in node["wires"]:
        node.cache[wire].show("elec")


# =========================================================== PINS =====================================================


def getPins(cache, qname):
    """
    Expand the pins of a node.
    """
    INFO("soft.getPins(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasPin", restriction="elec:Pin")

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

def show_Pin(node, args=None):
    """
    Show the 'Pin' view of the 'elec' category.
    """
    INFO("elec.show_Pin(%s)" %node['qname'])

    node.expand("elec", "Pin")

    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasPin' })
    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")

    node.expand("elec", "Pin")

    for connection in node["connections"]:
        node.cache[connection].show("elec")

def show_PinInstance(node, args=None):
    """
    Show the 'PinInstance' view of the 'elec' category.
    """
    INFO("elec.show_PinInstance(%s)" %node['qname'])

    node.expand("elec", "PinInstance")

    generic.fillFields(node, mandatories= { 'realizes' : 'sys:realizes' }, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasPin' })

    print "[[[[[[[[[[[[[[[[[[" + str(node['symbol'])+"]]]]]]]]]]]]]]]]]]]]"

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")
    if node['realizes'] is not None:
        generic.getDefaultNode(node.cache, node['realizes']).show("elec")

    node.expand("elec", "PinInstance")

    for connection in node["connections"]:
        node.cache[connection].show("elec")



# =========================================================== WIRES =====================================================


def getWires(cache, qname):
    """
    Expand the wires of a node.
    """
    INFO("soft.getWires(%s)" %(qname))

    # unsorted list:
    resultQNames =  generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasWire", restriction="elec:Wire", sortedByNumber=True)
    resultQNames += generic.getRelated(cache, subject=qname, property="(cont:contains|elec:hasTerminal|elec:hasPin)/(^elec:connectsTo|^elec:connectsFrom)", restriction="elec:Wire", sortedByNumber=True)

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

def show_Wire(node, args=None):
    """
    Show the 'Wire' view of the 'elec' category.
    """
    INFO("elec.show_Wire(%s)" %node['qname'])

    node.expand("elec", "Wire")

    for color in node["colors"]:
        node.cache[color].show("colors")
    for connection in node["connections"]:
        node.cache[connection].show("elec")

    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasWire', 'connectsFrom' : 'elec:connectsFrom', 'connectsTo' : 'elec:connectsTo'  })

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")
    if node['connectsFrom'] is not None:
        generic.getDefaultNode(node.cache, node['connectsFrom']).show("elec")
    if node['connectsTo'] is not None:
        generic.getDefaultNode(node.cache, node['connectsTo']).show("elec")


def show_WireInstance(node, args=None):
    """
    Show the 'WireInstance' view of the 'elec' category.
    """
    INFO("elec.show_WireInstance(%s)" %node['qname'])

    node.expand("elec", "WireInstance")

    generic.fillFields(node, mandatories= { 'realizes' : 'sys:realizes' }, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasWire', 'connectsFrom' : 'elec:connectsFrom', 'connectsTo' : 'elec:connectsTo'  })

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")
    if node['realizes'] is not None:
        generic.getDefaultNode(node.cache, node['realizes']).show("elec")
    if node['connectsFrom'] is not None:
        generic.getDefaultNode(node.cache, node['connectsFrom']).show("elec")
    if node['connectsTo'] is not None:
        generic.getDefaultNode(node.cache, node['connectsTo']).show("elec")

    for color in node["colors"]:
        node.cache[color].show("colors")
    for connection in node["connections"]:
        node.cache[connection].show("elec")



# ======================================================= CABLES ===================================================


def getCables(cache, qname):
    """
    Expand the cables of a node.
    """
    INFO("soft.getCables(%s)" %(qname))

    return generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasCable", restriction="elec:Cable")

def show_CableType(node, args=None):
    """
    Show the 'CableType' view of the 'elec' category.
    """
    INFO("elec.show_CableType(%s)" %node['qname'])

    node.expand("elec", "CableType")

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' }, optionals={'symbol' : 'elec:hasSymbol'})

    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for wire in node["wires"]:
        node.cache[wire].show("elec")

def show_CableInstance(node, args=None):
    """
    Show the 'CableInstance' view of the 'elec' category.
    """
    INFO("elec.show_CableInstance(%s)" %node['qname'])

    node.expand("elec", "CableInstance")

    generic.fillFields(node, mandatories={'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show("elec")

    for wire in node["wires"]:
        node.cache[wire].show("elec")


# ======================================================== CHANNELS ===================================================


def getChannels(cache, qname):
    """
    Expand the channels of a node.
    """
    INFO("soft.getChannels(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasChannel", restriction="elec:Channel", sortedByNumber=True)

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

def show_Channel(node, args=None):
    """
    Show the 'Channel' view of the 'elec' category.
    """
    INFO("elec.show_Channel(%s)" %node['qname'])

    node.expand("elec", "Channel")

    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")


# ======================================================== I/O ===================================================


def getIoModuleInstances(cache, qname):
    """
    Expand the I/O module instances of a node.
    """
    INFO("soft.getIOModuleInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:IoModuleInstance")

    #for resultQName in resultQNames:
    #    resultNode = cache[resultQName]
    #    resultNode.show("elec")

    # return the sorted list of expressions:
    return resultQNames

def show_IoModuleInstance(node, args=None):
    """
    Show the 'IoModuleInstance' view of the 'elec' category.
    """
    INFO("elec.show_IoModuleInstance(%s)" %node['qname'])

    generic.fillFields(node,
                       mandatories={ 'man_type' : 'man:hasType' },
                       optionals   = { 'interface'    : 'sys:hasInterface', 'symbol' : 'elec:hasSymbol' })

    generic.getDefaultNode(node.cache, node['man_type']).show('elec')
    if node['interface'] is not None:
        generic.getDefaultNode(node.cache, node['interface']).show('soft')

    node.expand("elec", "IoModuleInstance")

    for qname in node["channels"]:
        node.cache[qname].show("elec")
    for qname in node["terminals"]:
        node.cache[qname].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for qname in node["satisfies"]:
        node.cache[qname].show("sys")


# ======================================================== I/O ===================================================


def getIoModuleTypes(cache, qname):
    """
    Expand the I/O module types of a node.
    """
    INFO("soft.getIOModuleTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:IoModuleType")

    # return the sorted list of expressions:
    return resultQNames


def show_IoModuleType(node, args=None):
    """
    Show the 'IoModuleType' view of the 'elec' category.
    """
    INFO("elec.show_IoModuleType(%s)" %node['qname'])

    generic.fillFields(node,
                       mandatories = { 'id'           : 'man:hasId',
                                       'manufacturer' : 'man:isManufacturedBy' },
                       optionals   = { 'interface'    : 'sys:hasInterface' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()
    generic.getDefaultNode(node.cache, node['interface']).show()

    node.expand("elec", "IoModuleType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")

# ======================================================== Drives ===================================================


def getDriveInstances(cache, qname):
    """
    Expand the drive instances of a node.
    """
    INFO("soft.getDriveInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DriveInstance")

    # return the sorted list of expressions:
    return resultQNames


def show_DriveInstance(node, args=None):
    """
    Show the 'DriveInstance' view of the 'elec' category.
    """
    INFO("elec.show_DriveInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'} )
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "DriveInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Drive types ===================================================


def getDriveTypes(cache, qname):
    """
    Expand the drive types of a node.
    """
    INFO("soft.getDriveTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DriveType")

    # return the sorted list of expressions:
    return resultQNames


def show_DriveType(node, args=None):
    """
    Show the 'DriveType' view of the 'elec' category.
    """
    INFO("elec.show_DriveType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "DriveType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Sensors ===================================================


def getSensorInstances(cache, qname):
    """
    Expand the sensor instances of a node.
    """
    INFO("soft.getSensorInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SensorInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_SensorInstance(node, args=None):
    """
    Show the 'SensorInstance' view of the 'elec' category.
    """
    INFO("elec.show_SensorInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "SensorInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Sensor types ===================================================


def getSensorTypes(cache, qname):
    """
    Expand the sensor types of a node.
    """
    INFO("soft.getSensorTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SensorType")

    # return the sorted list of expressions:
    return resultQNames


def show_SensorType(node, args=None):
    """
    Show the 'SensorType' view of the 'elec' category.
    """
    INFO("elec.show_SensorType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "SensorType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Actuators ===================================================


def getActuatorInstances(cache, qname):
    """
    Expand the actuator instances of a node.
    """
    INFO("soft.getActuatorInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:ActuatorInstance")

    # return the sorted list of expressions:
    return resultQNames


def show_ActuatorInstance(node, args=None):
    """
    Show the 'ActuatorInstance' view of the 'elec' category.
    """
    INFO("elec.show_ActuatorInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "ActuatorInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Actuator types ===================================================


def getActuatorTypes(cache, qname):
    """
    Expand the actuator types of a node.
    """
    INFO("soft.getActuatorTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:ActuatorType")

    # return the sorted list of expressions:
    return resultQNames


def show_ActuatorType(node, args=None):
    """
    Show the 'ActuatorType' view of the 'elec' category.
    """
    INFO("elec.show_ActuatorType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "ActuatorType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")



# ======================================================== PowerSupplies ===================================================


def getPowerSupplyInstances(cache, qname):
    """
    Expand the power supply instances of a node.
    """
    INFO("soft.getPowerSupplyInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:PowerSupplyInstance")

    # return the sorted list of expressions:
    return resultQNames


def show_PowerSupplyInstance(node, args=None):
    """
    Show the 'PowerSupplyInstance' view of the 'elec' category.
    """
    INFO("elec.show_PowerSupplyInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "PowerSupplyInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== PowerSupply types ===================================================


def getPowerSupplyTypes(cache, qname):
    """
    Expand the power supply types of a node.
    """
    INFO("soft.getPowerSupplyTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:PowerSupplyType")

    # return the sorted list of expressions:
    return resultQNames


def show_PowerSupplyType(node, args=None):
    """
    Show the 'PowerSupplyType' view of the 'elec' category.
    """
    INFO("elec.show_PowerSupplyType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "PowerSupplyType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Cable assembly instances ===================================================


def getCableAssemblyInstances(cache, qname):
    """
    Expand the cable assembly instances of a node.
    """
    INFO("soft.getCableAssemblyInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CableAssemblyInstance")

    # return the sorted list of expressions:
    return resultQNames


def show_CableAssemblyInstance(node, args=None):
    """
    Show the 'CableAssemblyInstance' view of the 'elec' category.
    """
    INFO("elec.show_CableAssemblyInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "CableAssemblyInstance")

    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")


# ======================================================== Cable assembly types ===================================================


def getCableAssemblyTypes(cache, qname):
    """
    Expand the cable assembly types of a node.
    """
    INFO("soft.getCableAssemblyTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CableAssemblyType")

    # return the sorted list of expressions:
    return resultQNames


def show_CableAssemblyType(node, args=None):
    """
    Show the 'CableAssemblyType' view of the 'elec' category.
    """
    INFO("elec.show_CableAssemblyType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "CableAssemblyType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")

# ======================================================== Motors ===================================================


def getMotorInstances(cache, qname):
    """
    Expand the motor instances of a node.
    """
    INFO("soft.getMotorInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:MotorInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_MotorInstance(node, args=None):
    """
    Show the 'MotorInstance' view of the 'elec' category.
    """
    INFO("elec.show_MotorInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "MotorInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Motor types ===================================================


def getMotorTypes(cache, qname):
    """
    Expand the motor types of a node.
    """
    INFO("soft.getMotorTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:MotorType")

    # return the sorted list of expressions:
    return resultQNames


def show_MotorType(node, args=None):
    """
    Show the 'MotorType' view of the 'elec' category.
    """
    INFO("elec.show_MotorType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "MotorType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Switches ===================================================


def getSwitchInstances(cache, qname):
    """
    Show the 'MotorType' view of the 'elec' category.
    """
    INFO("soft.getSwitchInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SwitchInstance")

    # return the sorted list of expressions:
    return resultQNames


def show_SwitchInstance(node, args=None):
    """
    Show the 'SwitchInstance' view of the 'elec' category.
    """
    INFO("elec.show_SwitchInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "SwitchInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Switch types ===================================================


def getSwitchTypes(cache, qname):
    """
    Expand the switch types of a node.
    """
    INFO("soft.getSwitchTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SwitchType")

    # return the sorted list of expressions:
    return resultQNames


def show_SwitchType(node, args=None):
    """
    Show the 'SwitchType' view of the 'elec' category.
    """
    INFO("elec.show_SwitchType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "SwitchType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== Switches ===================================================


def getOtherDeviceInstances(cache, qname):
    """
    Expand the device instances of a node.
    """
    INFO("soft.getDeviceInstances(%s)" %(qname))

    # unsorted list:
    otherDevices   = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DeviceInstance")


    for expansion in ["I/O modules", "circuit breakers", "power supplies", "motors", "drives", "terminals", "connectors", "sensors", "actuators", "switches", "cables", "sub-configurations"]:
        for device in cache[qname][expansion]:
            if device in otherDevices:
                otherDevices.remove(device)

    # return the sorted list of expressions:
    return otherDevices


def show_DeviceInstance(node, args=None):
    """
    Show the 'DeviceInstance' view of the 'elec' category.
    """
    INFO("elec.show_DeviceInstance(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "DeviceInstance")

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")



# ======================================================== Device types ===================================================


def getDeviceTypes(cache, qname):
    """
    Expand the device types of a node.
    """
    INFO("soft.getDeviceTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DeviceType")

    # return the sorted list of expressions:
    return resultQNames


def show_DeviceType(node, args=None):
    """
    Show the 'DeviceType' view of the 'elec' category.
    """
    INFO("elec.show_DeviceType(%s)" %node['qname'])

    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "DeviceType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")
    for cableAssembly in node["cable assemblies"]:
        node.cache[cableAssembly].show("elec")


# ======================================================== I/O ===================================================


def getCircuitBreakerInstances(cache, qname):
    """
    Expand the circuit breaker instances of a node.
    """
    INFO("soft.getCircuitBreakerInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CircuitBreakerInstance")

    # return the sorted list of expressions:
    return resultQNames


def show_CircuitBreakerInstance(node, args=None):
    """
    Show the 'CircuitBreakerInstance' view of the 'elec' category.
    """
    INFO("elec.show_CircuitBreakerInstance(%s)" %node['qname'])

    generic.fillFields(node,
                       mandatories={ 'man_type' : 'man:hasType' },
                       optionals   = { 'interface'    : 'sys:hasInterface', 'symbol' : 'elec:hasSymbol' })

    generic.getDefaultNode(node.cache, node['man_type']).show('elec')
    if node['interface'] is not None:
        generic.getDefaultNode(node.cache, node['interface']).show('soft')

    node.expand("elec", "CircuitBreakerInstance")

    for qname in node["channels"]:
        node.cache[qname].show("elec")
    for qname in node["terminals"]:
        node.cache[qname].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")
    for qname in node["satisfies"]:
        node.cache[qname].show("sys")


# ======================================================== I/O ===================================================


def getCircuitBreakerTypes(cache, qname):
    """
    Expand the circuit breaker types of a node.
    """
    INFO("soft.getCircuitBreakerTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CircuitBreakerType")

    # return the sorted list of expressions:
    return resultQNames


def show_CircuitBreakerType(node, args=None):
    """
    Show the 'CircuitBreakerType' view of the 'elec' category.
    """
    INFO("elec.show_CircuitBreakerType(%s)" %node['qname'])

    generic.fillFields(node,
                       mandatories = { 'id'           : 'man:hasId',
                                       'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "CircuitBreakerType")

    node["owning_configurations_counts"] = []

    for cfg in node["owning_configurations"]:
        #node.cache[cfg].show("elec")
        # let's count the number of instances
        results = QUERY("""
            SELECT DISTINCT ?instance
            WHERE {
                %s ((^sys:realizes)|(sys:isRealizedBy)) ?instance .
                ?instance ((^cont:contains|cont:isContainedBy)+) %s .
            }""" %(node['qname'], cfg))
        node["owning_configurations_counts"].append(len(results))

    for channel in node["channels"]:
        node.cache[channel].show("elec")
    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")
    for qname in node["wires"]:
        node.cache[qname].show("elec")

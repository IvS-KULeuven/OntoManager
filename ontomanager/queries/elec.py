from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, IS_LITERAL, LOG, os
import generic
import pprint


# ========================================================= LIBRARY ====================================================

def getMainConfigurations(cache):
    return generic.getInstances(cache = cache, className = "elec:Configuration", filterNotExists = "?x cont:contains ?instance")

def getConfigurations(cache):
    return generic.getInstances(cache = cache, className = "elec:Configuration")


def show_configuration(node, args=None):
    node.expand("elec", "configuration", visible=False)

    for expansion in ["I/O modules", "circuit breakers", "power supplies", "motors", "drives", "terminals", "wires", "connectors", "sensors", "actuators", "switches", "cables", "cable assemblies", "sub-configurations", "other devices" ]:
        for item in node[expansion]:
            node.cache[item].show("elec")


def getSubConfigurations(cache, qname):
    LOG("getSubConfigurations(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:Configuration")

# ======================================================== CONFIGURATIONS ===================================================


def getOwningConfigurations(cache, qname):
    LOG("getOwningConfigurations(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="((^sys:realizes)|(sys:isRealizedBy))/((^cont:contains|cont:isContainedBy)+)", restriction="elec:Configuration", filterNotExists = "?x cont:contains ?result")

# ======================================================== TERMINALS ===================================================


def getTerminals(cache, qname):
    LOG("getTerminals(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasTerminal", restriction="elec:Terminal")

def show_Terminal(node, args=None):
    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasTerminal' })

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")

    node.expand("elec", "Terminal", visible=False)

    for connection in node["connections"]:
        node.cache[connection].show("elec")

def show_TerminalInstance(node, args=None):
    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol' , 'owner' : '^elec:hasTerminal' , 'realizes' : 'sys:realizes' })

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")
    if node['realizes'] is not None:
        generic.getDefaultNode(node.cache, node['realizes']).show("elec")

    node.expand("elec", "TerminalInstance", visible=False)

    for connection in node["connections"]:
        node.cache[connection].show("elec")


# ====================================================== CONNECTIONS ===================================================


def getConnections(cache, qname):
    LOG("getConnections(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="elec:isConnectedTo|^elec:isConnectedTo")

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames


def getAllConnections(cache, qname):
    LOG("getAllConnections(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="elec:isConnectedTo+|^elec:isConnectedTo+")

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

# ======================================================= FITS ===================================================

def getFits(cache, qname):
    LOG("getFits(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="elec:isJoinedWith|^elec:isJoinedWith")

# ======================================================= CONNECTORS ===================================================

def show_Gender(node, args=None):
    pass

def show_Channel(node, args=None):
    pass


def getConnectors(cache, qname):
    LOG("getConnectors(%s)" %(qname))

    return generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasConnector", restriction="elec:Connector")

def show_ConnectorType(node, args=None):

    node.expand("elec", "ConnectorType", visible=False)

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

    node.expand("elec", "ConnectorInstance", visible=False)

    generic.fillFields(node, mandatories={'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol' })
    generic.getDefaultNode(node.cache, node['man_type']).show("elec")

    for pin in node["pins"]:
        node.cache[pin].show("elec")
    for wire in node["wires"]:
        node.cache[wire].show("elec")

# =========================================================== PINS =====================================================


def getPins(cache, qname):

    LOG("getPins(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasPin", restriction="elec:Pin")

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

def show_Pin(node, args=None):

    node.expand("elec", "Pin", visible=False)

    generic.fillFields(node, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasPin' })
    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")

    node.expand("elec", "Pin", visible=False)

    for connection in node["connections"]:
        node.cache[connection].show("elec")

def show_PinInstance(node, args=None):

    node.expand("elec", "PinInstance", visible=False)

    generic.fillFields(node, mandatories= { 'realizes' : 'sys:realizes' }, optionals={ 'symbol' : 'elec:hasSymbol', 'owner' : '^elec:hasPin' })

    print "[[[[[[[[[[[[[[[[[[" + str(node['symbol'])+"]]]]]]]]]]]]]]]]]]]]"

    if node['owner'] is not None:
        generic.getDefaultNode(node.cache, node['owner']).show("elec")
    if node['realizes'] is not None:
        generic.getDefaultNode(node.cache, node['realizes']).show("elec")

    node.expand("elec", "PinInstance", visible=False)

    for connection in node["connections"]:
        node.cache[connection].show("elec")



# =========================================================== WIRES =====================================================


def getWires(cache, qname):

    LOG("getWires(%s)" %(qname))

    # unsorted list:
    resultQNames =  generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasWire", restriction="elec:Wire", sortedByNumber=True)
    resultQNames += generic.getRelated(cache, subject=qname, property="(cont:contains|elec:hasTerminal|elec:hasPin)/(^elec:connectsTo|^elec:connectsFrom)", restriction="elec:Wire", sortedByNumber=True)

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

def show_Wire(node, args=None):

    node.expand("elec", "Wire", visible=False)

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

    node.expand("elec", "WireInstance", visible=False)

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
    LOG("getCables(%s)" %(qname))

    return generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasCable", restriction="elec:Cable")

def show_CableType(node, args=None):

    node.expand("elec", "CableType", visible=False)

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

    node.expand("elec", "CableInstance", visible=False)

    generic.fillFields(node, mandatories={'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show("elec")

    for wire in node["wires"]:
        node.cache[wire].show("elec")


# ======================================================== CHANNELS ===================================================


def getChannels(cache, qname):
    LOG("getChannels(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains|elec:hasChannel", restriction="elec:Channel", sortedByNumber=True)

    for resultQName in resultQNames:
       cache[resultQName].show("elec")

    return resultQNames

def show_Channel(node, args=None):

    node.expand("elec", "Channel", visible=False)

    for terminal in node["terminals"]:
        node.cache[terminal].show("elec")


# ======================================================== I/O ===================================================


def getIoModuleInstances(cache, qname):
    LOG("getIOModuleInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:IoModuleInstance")

    #for resultQName in resultQNames:
    #    resultNode = cache[resultQName]
    #    resultNode.show("elec")

    # return the sorted list of expressions:
    return resultQNames

def show_IoModuleInstance(node, args=None):
    generic.fillFields(node,
                       mandatories={ 'man_type' : 'man:hasType' },
                       optionals   = { 'interface'    : 'sys:hasInterface', 'symbol' : 'elec:hasSymbol' })

    generic.getDefaultNode(node.cache, node['man_type']).show('elec')
    if node['interface'] is not None:
        generic.getDefaultNode(node.cache, node['interface']).show('soft')

    node.expand("elec", "IoModuleInstance", visible=False)

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
    LOG("getIOModuleTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:IoModuleType")

    #for resultQName in resultQNames:
    #    resultNode = cache[resultQName]
    #    resultNode.show("elec")

    # return the sorted list of expressions:
    return resultQNames

def show_IoModuleType(node, args=None):
    generic.fillFields(node,
                       mandatories = { 'id'           : 'man:hasId',
                                       'manufacturer' : 'man:isManufacturedBy' },
                       optionals   = { 'interface'    : 'sys:hasInterface' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()
    generic.getDefaultNode(node.cache, node['interface']).show()

    node.expand("elec", "IoModuleType", visible=False)

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
    LOG("getDriveInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DriveInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_DriveInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'} )
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "DriveInstance", visible=False)

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
    LOG("getDriveTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DriveType")

    # return the sorted list of expressions:
    return resultQNames

def show_DriveType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "DriveType", visible=False)

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
    LOG("getSensorInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SensorInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_SensorInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "SensorInstance", visible=False)

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
    LOG("getSensorTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SensorType")

    # return the sorted list of expressions:
    return resultQNames

def show_SensorType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "SensorType", visible=False)

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
    LOG("getActuatorInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:ActuatorInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_ActuatorInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "ActuatorInstance", visible=False)

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
    LOG("getActuatorTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:ActuatorType")

    # return the sorted list of expressions:
    return resultQNames

def show_ActuatorType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "ActuatorType", visible=False)

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
    LOG("getPowerSupplyInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:PowerSupplyInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_PowerSupplyInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "PowerSupplyInstance", visible=False)

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
    LOG("getPowerSupplyTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:PowerSupplyType")

    # return the sorted list of expressions:
    return resultQNames

def show_PowerSupplyType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "PowerSupplyType", visible=False)

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
    LOG("getCableAssemblyInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CableAssemblyInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_CableAssemblyInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "CableAssemblyInstance", visible=False)

    for cable in node["cables"]:
        node.cache[cable].show("elec")
    for connector in node["connectors"]:
        node.cache[connector].show("elec")


# ======================================================== Cable assembly types ===================================================


def getCableAssemblyTypes(cache, qname):
    LOG("getCableAssemblyTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CableAssemblyType")

    # return the sorted list of expressions:
    return resultQNames

def show_CableAssemblyType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "CableAssemblyType", visible=False)

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
    LOG("getMotorInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:MotorInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_MotorInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "MotorInstance", visible=False)

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
    LOG("getMotorTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:MotorType")

    # return the sorted list of expressions:
    return resultQNames

def show_MotorType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "MotorType", visible=False)

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
    LOG("getSwitchInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SwitchInstance")

    # return the sorted list of expressions:
    return resultQNames

def show_SwitchInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "SwitchInstance", visible=False)

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
    LOG("getSwitchTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:SwitchType")

    # return the sorted list of expressions:
    return resultQNames

def show_SwitchType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "SwitchType", visible=False)

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
    LOG("getDeviceInstances(%s)" %(qname))

    # unsorted list:
    otherDevices   = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DeviceInstance")


    for expansion in ["I/O modules", "circuit breakers", "power supplies", "motors", "drives", "terminals", "connectors", "sensors", "actuators", "switches", "cables", "sub-configurations"]:
        for device in cache[qname][expansion]:
            if device in otherDevices:
                otherDevices.remove(device)

    # return the sorted list of expressions:
    return otherDevices

def show_DeviceInstance(node, args=None):
    generic.fillFields(node, mandatories={ 'man_type' : 'man:hasType' }, optionals={'symbol' : 'elec:hasSymbol'})
    generic.getDefaultNode(node.cache, node['man_type']).show('elec')

    node.expand("elec", "DeviceInstance", visible=False)

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
    LOG("getDeviceTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:DeviceType")

    # return the sorted list of expressions:
    return resultQNames

def show_DeviceType(node, args=None):
    generic.fillFields(node, mandatories={ 'id'           : 'man:hasId',
                                           'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "DeviceType", visible=False)

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
    LOG("getCircuitBreakerInstances(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CircuitBreakerInstance")

    #for resultQName in resultQNames:
    #    resultNode = cache[resultQName]
    #    resultNode.show("elec")

    # return the sorted list of expressions:
    return resultQNames

def show_CircuitBreakerInstance(node, args=None):
    generic.fillFields(node,
                       mandatories={ 'man_type' : 'man:hasType' },
                       optionals   = { 'interface'    : 'sys:hasInterface', 'symbol' : 'elec:hasSymbol' })

    generic.getDefaultNode(node.cache, node['man_type']).show('elec')
    if node['interface'] is not None:
        generic.getDefaultNode(node.cache, node['interface']).show('soft')

    node.expand("elec", "CircuitBreakerInstance", visible=False)

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
    LOG("getCircuitBreakerTypes(%s)" %(qname))

    # unsorted list:
    resultQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="elec:CircuitBreakerType")

    #for resultQName in resultQNames:
    #    resultNode = cache[resultQName]
    #    resultNode.show("elec")

    # return the sorted list of expressions:
    return resultQNames

def show_CircuitBreakerType(node, args=None):
    generic.fillFields(node,
                       mandatories = { 'id'           : 'man:hasId',
                                       'manufacturer' : 'man:isManufacturedBy' })
    generic.getDefaultNode(node.cache, node['manufacturer']).show()

    node.expand("elec", "CircuitBreakerType", visible=False)

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

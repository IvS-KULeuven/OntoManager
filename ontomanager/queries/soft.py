from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, IS_LITERAL, LOG, os
import generic
import pprint



def GET_FILEPATH(dir, library, ext):
    return os.path.join(dir, "%s.%s" %(library.split(':',1)[1].lower(), ext))


def getCode(library, filePath, busyUpdating):
    # library = a Qname

    ret = {}
    ret["contents"] = None
    ret["status"] = "File has not been read yet"

    f = None
    filePathExists = False

    libName = library.split(":",1)[1]

    if busyUpdating:
        ret["status"] = "Busy updating ..."

    else:

        if filePath is not None:
            filePathExists = os.path.exists(filePath)
            if filePathExists:
                ret["status"] = "File exists"
            else:
                ret["status"] = "File does not exist!"

        if filePathExists:
            ret["status"] = "Opening file..."
            try:
                f = open(filePath, 'r')
                ret["status"] = "File has been opened"
            except Exception, e:
                ret["status"] = "Could not open the file: %s" %e

        if f is not None:
            ret["status"] = "Reading file..."
            try:
                ret["contents"] = f.read().decode(u'utf-8')
                ret["status"] = "File has been read"
            except Exception, e:
                ret["status"] = "Could not read the file: %s" %e

        if f is not None:
            try:
                f.close()
            except Exception, e:
                LOG("Could not close the file: %s" %e)


    return ret


def writeCode(code, library, filePath):
    # library = a Qname

    f = None
    filePathExists = False

    libName = library.split(":",1)[1]


    if filePath is not None:
        try:
            f = open(filePath, 'w')
        except Exception, e:
            raise Exception("Could not open the file: %s" %e)

    if f is not None:
        try:
            f.write(code.encode('utf-8'))
        except Exception, e:
            raise Exception("Could not write the file: %s" %e)

    if f is not None:
        try:
            f.close()
        except Exception, e:
            LOG("Could not close the file: %s" %e)




# ========================================================= LIBRARY ====================================================

def getLibraries(cache): # returns: list of Nodes
    return generic.getInstances(cache = cache, className = "soft:Library")


def show_library(node, args=None):
    node.expand("soft", "library", visible=False)

    for ns in node["namespaces"]:
        node.cache[ns].show("soft")
    for fb in node["FBs"]:
        node.cache[fb].show("soft")
    for struct in node["STRUCTs"]:
        node.cache[struct].show("soft")
    for enum in node["ENUMs"]:
        node.cache[enum].show("soft")


# ======================================================== NAMESPACE ===================================================

def getNamespaces(cache, qname):
    return generic.getRelated(cache, qname, "cont:contains|(^cont:isContainedBy)", restriction="soft:Namespace")


def show_namespace(node, args=None):
    node.expand("soft", "namespace", visible=False)

    for ns in node["namespaces"]:
        node.cache[ns].show("soft")
    for fb in node["FBs"]:
        node.cache[fb].show("soft")
    for struct in node["STRUCTs"]:
        node.cache[struct].show("soft")
    for enum in node["ENUMs"]:
        node.cache[enum].show("soft")


# ========================================================= LINKS =====================================================

def getLinks(cache, qname):
    return generic.getRelated(cache, qname, "sys:isInterfacedWith | ^sys:isInterfacedWith")


# ========================================================= METHOD =====================================================


def getMemberOf(cache, qname):
    return generic.getRelated(cache, qname, "(^soft:hasVariable) | (^soft:hasAttribute) | (^iec61131:hasInputVariable) | (^iec61131:hasOutputVariable) | (^iec61131:hasInOutVariable) | (^iec61131:hasLocalVariable) | (^soft:hasCallable) | (^iec61131:hasMethod) | (^iec61131:hasMethodInstance)")


def show_plc_method(node, args=None):
    show_type(node)
    node.expand("soft", "plc_method", visible=False)

    node["this"] = generic.getRelated(node.cache, node["qname"], "(^iec61131:hasMethod) | (^iec61131:hasMethodInstance)")[0]
    node.cache[node["this"]].show("soft")

    if node["implementation"] is not None:
        node.cache[node["implementation"]].show("soft")

    for memberOf in node["member_of"]:
        node.cache[memberOf].show("soft")

    for kind in ["var_in", "var_out", "var_inout", "var_local"]:
        for qname in node[kind]:
            node.cache[qname].show("soft")


# ===================================================== FUNCTION BLOCK =================================================


def getFBs(cache, qname):
    return generic.getRelated(cache, qname, "cont:contains|(^cont:isContainedBy)", restriction="iec61131:FunctionBlock")

def show_fb(node, args=None):
    show_type(node)
    node.expand("soft", "fb", visible=False)

    if node["implementation"] is not None:
        node.cache[node["implementation"]].show("soft")

    for kind in ["var_in", "var_out", "var_inout", "var_local", "methods"]:
        for qname in node[kind]:
            node.cache[qname].show("soft")

# ======================================================== STRUCT ======================================================


def getStructs(cache, qname):
    return generic.getRelated(cache, qname, "cont:contains|(^cont:isContainedBy)", restriction="iec61131:Struct")

def show_struct(node, args=None):
    show_type(node)
    node.expand("soft", "struct", visible=False)

    for attr in node["attributes"]:
        node.cache[attr].show("soft")

# ========================================================= ENUM =======================================================


def getEnums(cache, qname):
    return generic.getRelated(cache, qname, "cont:contains|(^cont:isContainedBy)", restriction="soft:Enumeration")

def show_enum(node, args=None):
    show_type(node)
    node.expand("soft", "enum", visible=False)

    for ns in node["items"]:
        node.cache[ns].show("soft", "enum_item")



# ====================================================== ENUM ITEM =====================================================


def getEnumItems(cache, qname):
    return generic.getRelated(cache, qname, "cont:contains", restriction="soft:EnumerationItem")

def show_enum_item(node, args=None):
    generic.fillNumber(node, optional=True)
    node["item_of"] = generic.getRelated(node.cache, node["qname"], "(^cont:contains)|(cont:isContainedBy)")[0]
    node.cache[node["item_of"]].show("soft", "enum")


# ====================================================== ATTRIBUTE =====================================================

def getAttributes(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasAttribute")


def show_attribute(node, args=None):
    node.expand("soft", "attribute", visible=False)

    show_variable(node)

# ====================================================== ARGUMENTS =====================================================

def getArguments(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasArgument")


def show_argument(node, args=None):
    node.expand("soft", "argument", visible=False)

    show_variable(node)



# ====================================================== INTERFACE =====================================================

def getInterfaceVariables(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasVariable")


def show_Interface(node, args=None):
    node.expand("soft", "Interface", visible=False)

    for v in node["variables"]:
        node.cache[v].show("soft")

# ====================================================== INTERFACE INSTANCE =====================================================

def getInterfaceInstanceVariables(cache, qname):
    return generic.getRelated(cache, qname, "sys:hasElement")


def show_InterfaceInstance(node, args=None):
    node.expand("soft", "InterfaceInstance", visible=False)

    for v in node["variables"]:
        node.cache[v].show()


# ====================================================== PRIMITIVE =====================================================


def show_primitive(node, args=None):

    results = QUERY("""
        SELECT DISTINCT ?value
        WHERE {
            %s expr:hasValue|expr:hasNumericValue ?value .
        }
        """ %node["qname"])

    node["value"] = None

    for (value,) in results:
        if value is not None:
            node["value"] = getExpressionString(value)


# ====================================================== VARIABLE ======================================================

def getInputVariables(cache, qname):
    return generic.getRelated(cache, qname, "iec61131:hasInputVariable", remove="(soft:extends+)/iec61131:hasInputVariable")

def getOutputVariables(cache, qname):
    return generic.getRelated(cache, qname, "iec61131:hasOutputVariable", remove="(soft:extends+)/iec61131:hasOutputVariable")

def getInOutVariables(cache, qname):
    return generic.getRelated(cache, qname, "iec61131:hasInOutVariable", remove="(soft:extends+)/iec61131:hasInOutVariable")

def getLocalVariables(cache, qname):
    return generic.getRelated(cache, qname, "iec61131:hasLocalVariable", remove="(soft:extends+)/iec61131:hasLocalVariable")

def getMethods(cache, qname):
    return generic.getRelated(cache, qname, "iec61131:hasMethod | iec61131:hasMethodInstance", remove="(soft:extends+)/(iec61131:hasMethod | iec61131:hasMethodInstance)")


def show_variable(node, args=None):
    LOG("show_variable(%s)" %(node["qname"]))

    node["type"]            = None
    node["points_to_type"]  = None
    node["initial_value"]   = None
    node["address"]         = None
    node["value"]           = None

    results = QUERY("""
        SELECT DISTINCT ?type ?pointsToType ?initialValue ?address ?link ?value
        WHERE {
            OPTIONAL { %s soft:hasType | (^soft:isTypeOf) ?type . } .
            OPTIONAL { %s soft:pointsToType ?pointsToType .} .
            OPTIONAL { %s soft:hasInitialValue ?initialValue . } .
            OPTIONAL { %s soft:hasAddress ?address . } .
            OPTIONAL { %s expr:hasValue | expr:hasNumericValue ?value . } .
        }
        """ %((node["qname"],)*5))

    for type, pointsToType, initialValue, address, link, value in results:

        if type is not None:
            typeQName = URI_TO_QNAME(type.toPython())
            node["type"] = typeQName
            generic.getDefaultNode(node.cache, typeQName).show("soft", "type")

        if pointsToType is not None:
            pointsToTypeQName = URI_TO_QNAME(pointsToType.toPython())
            node["points_to_type"] = pointsToTypeQName
            generic.getDefaultNode(node.cache, pointsToTypeQName).show("soft", "type")

        if initialValue is not None:
            node["initial_value"] = initialValue.toPython()

        if address is not None:
            node["address"] = address.toPython()

        if value is not None:
            node["value"] = getExpressionString(value)

    node.expand("soft", "variable", visible=False)

    for memberOf in node["member_of"]:
        node.cache[memberOf].show("soft")

    for l in node["links"]:
        node.cache[l].show("soft")

    for qualifier in node["qualifiers"]:
        node.cache[qualifier].show("soft")

    #for member in node["members"]:
    #    node.cache[member].show("soft")



# ===================================================== QUALIFIER ======================================================


def getQualifiers(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasQualifier")


def show_qualifier(node, args=None):
    results = QUERY("""
        SELECT DISTINCT ?symbol ?value
        WHERE {
            OPTIONAL { %s iec61131:hasSymbol ?symbol . } .
            OPTIONAL { %s expr:hasValue ?value . } .
        }
        """ %((node["qname"],)*2))

    node["plc_symbol"] = None
    node["value"]  = None

    for symbol, value in results:

        if symbol is not None:
            node["plc_symbol"] = symbol.toPython()

        if value is not None:
            node["value"] = value.toPython()

# ===================================================== OPERATOR ======================================================


def show_operator(node, args=None):
    results = QUERY("""
        SELECT DISTINCT ?symbol
        WHERE {
            OPTIONAL { %s iec61131:hasSymbol ?symbol . } .
        }
        """ %((node["qname"],)*1))

    node["plc_symbol"] = None

    for (symbol,) in results:

        if symbol is not None:
            node["plc_symbol"] = symbol.toPython()



# ===================================================== TYPE ======================================================


def getTypes(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasType | (^soft:isTypeOf)")


def show_type(node, args=None):
    results = QUERY("""
        SELECT DISTINCT ?implementation ?symbol ?extends ?returnType
        WHERE {
            OPTIONAL { %s soft:hasImplementation ?implementation . } .
            OPTIONAL { ?implementation soft:isImplementationOf %s . } .
            OPTIONAL { %s (^owl:sameAs)/iec61131:hasSymbol | iec61131:hasSymbol ?symbol . } .
            OPTIONAL { %s soft:extends ?extends } .
            OPTIONAL { %s soft:hasReturnType ?returnType . } .
        }
        """ %((node["qname"],)*5))

    node["implementation"] = None
    node["plc_symbol"] = None
    node["extends"] = None
    node["returnType"] = None

    for implementation, symbol, extends, returnType in results:

        if implementation is not None:
            implementationQName = URI_TO_QNAME(implementation.toPython())
            node["implementation"] = implementationQName
            generic.getDefaultNode(node.cache, implementationQName)
            # don't show it here

        if symbol is not None:
            node["plc_symbol"] = symbol.toPython()
        if extends is not None:
            extendsQName = URI_TO_QNAME(extends.toPython())
            node["extends"] = extendsQName
            generic.getDefaultNode(node.cache, extendsQName).show("soft")
        if returnType is not None:
            returnTypeQName = URI_TO_QNAME(returnType.toPython())
            node["returnType"] = returnTypeQName
            generic.getDefaultNode(node.cache, returnTypeQName).show("soft")

# ====================================================== INSTANCE ======================================================


def getInstances(cache, qname):
    return generic.getRelated(cache, qname, "soft:isTypeOf", restriction="soft:Type")

# ====================================================== MEMBER ======================================================


def getMembers(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasVariable")

def getAllMembers(cache, qname):
    return generic.getRelated(cache, qname, "soft:hasVariable*")

# ====================================================== IMPLEMENTATION ================================================



def show_implementation(node, args=None):
    node.expand("soft", "implementation", visible=False)

    for expr in node["expressions"]:
        node.cache[expr].show("soft")


# ======================================================== CALL ========================================================


def show_call(node, args=None):
    node.expand("soft", "call", visible=False)

    calls = generic.getRelated(node.cache, node["qname"], "soft:calls")

    if len(calls) != 1:
        raise Exception("Error in show_call: expected one result for '%s soft:calls ...' but we received: %s" %(node["qname"], calls))

    node["calls"] = calls[0]
    node.cache[calls[0]].show("soft")

    for ass in node["assignments"]:
        node.cache[ass].show("soft")


def getAssignments(cache, qname):
    return generic.getRelated(cache, qname, "expr:hasAssignment", sortedByNumber=True)



# ==================================================== EXPRESSIONS =====================================================


class ContextItem:
    def __init__(self, entry, uri):
        self.entry = entry
        self.uri = str(uri)
    def __str__(self):
        if self.entry is None:
            return "ContextItem(entry=%s, uri='%s')" %(self.entry,self.uri)
        else:
            return "ContextItem(entry='%s', uri='%s')" %(self.entry,self.uri)
    def __repr__(self):
        return self.__str__()


def getImplementationExpressions(cache, qname):
    LOG("getImplementationExpressions(%s)" %(qname))

    # unsorted list:
    itemQNames = generic.getRelated(cache, subject=qname, property="cont:contains", sortedByNumber=True)

    for itemQName in itemQNames:
        itemNode = cache[itemQName]
        itemNode.show("soft") # the view priority (defined by allviews.py) will determine which show_ function will be called!

    # return the sorted list of expressions:
    return itemQNames

def getExpressions(cache, qname):
    LOG("getPlcExpressions(%s)" %(qname))

    # unsorted list:
    expressionQNames = generic.getRelated(cache, subject=qname, property="cont:contains", restriction="expr:Expression", sortedByNumber=True)

    for expressionQName in expressionQNames:
        expressionNode = cache[expressionQName]
        expressionNode.show("soft") # the view priority (defined by allviews.py) will determine which show_ function will be called!

    # return the sorted list of expressions:
    return expressionQNames

# ======================================================= IF THEN ======================================================



def show_if_then(node, args=None):

    results = QUERY("""
        SELECT DISTINCT ?if ?then ?else
        WHERE {
            %s soft:if ?if .
            %s soft:then ?then .
            OPTIONAL { %s soft:else ?else . }
        }
        """ %((node["qname"],)*3))

    if len(results) != 1:
        raise Exception("Invalid specification of IfThen operation %s" %node["qname"])

    node["if"] = None
    node["then"] = None
    node["else"] = None

    for (i,t,e) in results:
        iNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(i))
        tNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(t))

        node["if"]   = iNode["qname"]
        node["then"] = tNode["qname"]

        iNode.show("soft")
        tNode.show("soft")

        if e is not None:
            eNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(e))
            node["else"] = eNode["qname"]
            eNode.show("soft")


# ================================================== BINARY OPERATION ==================================================

def show_binary_op(node, args=None):

    results = QUERY("""
        SELECT DISTINCT ?operator ?left ?right
        WHERE {
            %s expr:hasOperator ?operator .
            %s expr:hasLeftOperand ?left .
            %s expr:hasRightOperand ?right .
        }
        """ %((node["qname"],)*3))

    if len(results) == 0:
        raise Exception("Invalid specification of binary operation %s.\n\nNode=%s" %(node["qname"],pprint.pformat(node)))

    for (operatorUri, leftUri, rightUri) in results:

        oNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(operatorUri))
        lNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(leftUri))
        rNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(rightUri))

        node["operator"] = oNode["qname"]
        node["left"]     = lNode["qname"]
        node["right"]    = rNode["qname"]

        oNode.show("soft")
        lNode.show("soft")
        rNode.show("soft")


def show_unary_op(node, args=None):

    results = QUERY("""
        SELECT DISTINCT ?operator ?operand
        WHERE {
            %s expr:hasOperator ?operator .
            %s expr:hasOperand ?operand .
        }
        """ %((node["qname"],)*2))

    if len(results) == 0:
        raise Exception("Invalid specification of unary operation %s.\n\nNode=%s" %(node["qname"],pprint.pformat(node)))

    for (operatorUri, operandUri) in results:

        operatorNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(operatorUri))
        operandNode = generic.getDefaultNode(node.cache, URI_TO_QNAME(operandUri))

        node["operator"] = operatorNode["qname"]
        node["operand"]  = operandNode["qname"]

        operatorNode.show("soft")
        operandNode.show("soft")




def getMemberPath(startUri, endUri):
    LOG("getMemberPath(%s, %s)" %(startUri,endUri))
    startUri = str(startUri)
    endUri = str(endUri)

    if startUri == endUri:
        return []
    else:
        results = QUERY("""
            SELECT DISTINCT ?member ?label
            WHERE {
                <%s> soft:hasVariable ?member .
                ?member (soft:hasVariable)* <%s> .
                OPTIONAL { <%s> rdfs:label ?label . }
            }
            """ %(startUri,endUri,startUri))
        if len(results) == 0:
            raise Exception("%s has no member that owns %s!" %(startUri,endUri))

        for (memberUri, label) in results:
            if label is None:
                raise Exception("%s has no label!" %(startUri))

            return [label.toPython()] + getMemberPath(str(memberUri), endUri)



def getCommonVariablesOfContext(variableUri, contextUri):
    LOG("getCommonVariablesOfContext(%s, %s)" %(variableUri,contextUri))
    ret = []
    results = QUERY("""
        SELECT DISTINCT ?member
        WHERE {
            <%s> soft:hasVariable ?member .
            ?member (soft:hasVariable)* <%s> .
        }
        """ %(contextUri, variableUri))
    for (member, ) in results:
        ret.append(member.toPython())
    return ret


# def getCommonVariablesOfType(variableUri, contextUris):
#     LOG("getCommonVariablesOfType(%s, %s)" %(variableUri,contextUris))
#     ret = []
#     for contextUri in contextUris:
#         results = QUERY("""
#             SELECT DISTINCT ?member
#             WHERE {
#                 ?type soft:hasCallable <%s> .
#                 ?type soft:hasVariable ?member .
#                 ?member (soft:hasVariable)* <%s> .
#             }
#             """ %(contextUri, variableUri))
#         for (member, ) in results:
#             ret.append(member.toPython())
#     return ret

def getEnumPath(variableUri):
    LOG("getEnumOfEnumItem(%s)" %variableUri)
    results = QUERY("""
        SELECT DISTINCT ?enum ?label
        WHERE {
            ?enum soft:hasEnumerationItem <%s> .
            ?enum rdfs:label ?label .
        }
        """ %(variableUri))

    if len(results) == 0:
        return None
    elif len(results) > 1:
        raise Exception("Multiple enum definitions were found for item %s!" %variableUri)
    else:
        for (enumUri, enumLabel) in results:
            return { "path" : [ enumLabel.toPython() ]}


def getExpressionString(ex):
    if IS_LITERAL(ex):
        v = ex.toPython()
        if isinstance(v, str) or isinstance(v, unicode):
            return "'%s'" %v
        elif str(v).lower() == "false":
            return "FALSE"
        elif str(v).lower() == "true":
            return "TRUE"
        else:
            return str(v)
    else:
        return str(ex)




def isPlcFb(type):
    result = QUERY("""
        ASK WHERE {
            %s rdf:type/rdfs:subClassOf* iec61131:FunctionBlock .
        }
        """ %type)
    return bool(result)


def isPlcStruct(type):
    result = QUERY("""
        ASK WHERE {
            %s rdf:type/rdfs:subClassOf* iec61131:Struct .
        }
        """ %type)
    return bool(result)

def isPlcEnum(type):
    result = QUERY("""
        ASK WHERE {
            %s rdf:type/rdfs:subClassOf* iec61131:Enum .
        }
        """ %type)
    return bool(result)




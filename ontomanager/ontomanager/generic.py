__author__ = 'wimpe'
from .triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, IS_URI
from .util import Node
from .logging import INFO, DEBUG, LOG
from pyparsing import ParseException


def getDefaultNode(cache, qname):
    """
    Get a Node with default information, or get the node from the cache if available.

    The default information of a node includes:
     - its qname
     - its label
     - its uri
     - its comment
     - its ontoscript counter
     - its RDF classes (a list of qnames)

    All nodes contain the default information
     + optional other slots (filled by the show_... callbacks mentioned in allviews.py)
     + optional expansions (filled by the get... callbacks mentioned in allviews.py)
    """
    try:   
        node = cache[qname]
    except:
        INFO("    Get default node for %s" %qname)

        results = QUERY("""
            SELECT DISTINCT ?label ?comment ?counter ?rdfClass
            WHERE {
                OPTIONAL { %s rdfs:label ?label } .
                OPTIONAL { %s rdfs:comment ?comment } .
                OPTIONAL { %s ontoscript:counter ?counter } .
                OPTIONAL { %s a/(rdfs:subClassOf*) ?rdfClass . FILTER (!isBlank(?rdfClass)) } .

            }
            """ %(qname,qname,qname,qname))

        node = Node(
                qname           = qname,
                uri             = QNAME_TO_URI(qname),
                cache           = cache)

        rdfClasses = [] # only for logging

        for label, comment, counter, rdfClass in results:
            if label is not None:
                node["label"] = label.toPython()
            if comment is not None:
                node["comment"] = comment.toPython()
            if counter is not None:
                node["counter"] = int(counter.toPython())
            if rdfClass is not None:
                rdfClassQName = URI_TO_QNAME(rdfClass)
                node.registerClass(rdfClassQName)
                rdfClasses.append(rdfClassQName)

        INFO("     --> label '%s', counter %d, rdfClasses %s" %(node["label"], node["counter"], rdfClasses))

        node.registerClass("rdfs:Resource")

        node.registerKnownViews()

        cache[qname] = node

    return node


def getInstances(cache, className, filterNotExists=None):
    """
    Get the instances of a class.
    """
    INFO("    Get instances of %s" %className)

    if filterNotExists is None:
        filterNotExistsLine = ""
    else:
        filterNotExistsLine = "FILTER NOT EXISTS { %s }" %filterNotExists

    results = QUERY("""
        SELECT DISTINCT ?instance ?label ?comment ?counter ?rdfClass
        WHERE {
            ?instance rdf:type/rdfs:subClassOf* %s .
            OPTIONAL { ?instance rdfs:label ?label } .
            OPTIONAL { ?instance rdfs:comment ?comment } .
            OPTIONAL { ?instance ontoscript:counter ?counter } .
            OPTIONAL { ?instance a/(rdfs:subClassOf*) ?rdfClass . FILTER (!isBlank(?rdfClass)) } .
            %s
        }
        """ %(className, filterNotExistsLine))

    d = {}
    for uri, label, comment, counter, rdfClass in results:
        qname = URI_TO_QNAME(uri)

        if qname not in d:
            d[qname] = Node(
                        qname           = qname,
                        uri             = uri.toPython(),
                        cache           = cache)

        if label is not None:
            d[qname]["label"] = label.toPython()
        if comment is not None:
            d[qname]["comment"] = comment.toPython()
        if counter is not None:
            d[qname]["counter"] = int(counter.toPython())
        if rdfClass is not None:
            d[qname].registerClass(URI_TO_QNAME(rdfClass.toPython()))

    keysStr = ""
    for key in list(d.keys()):
        keysStr += (key + " ")

    INFO("     --> " + keysStr)

    for qname, node in list(d.items()):

        node.registerKnownViews()

        if qname not in cache:
            DEBUG("Caching %s" %qname)
            cache[qname] = node

    # return a list of QNames
    ret = [] # list of qnames
    resultNodes =  sorted(list(d.values()), key=lambda x: x["counter"])
    for resultNode in resultNodes:
        ret.append(resultNode['qname'])
    return ret


def getRelated(cache, subject, property, restriction=None, remove=None,  sortedByNumber=False, filterNotExists=None):
    """
    Get the related individuals of an individual.
    """
    INFO("    Get related %s of %s" %(property, subject))

    extraVariables = ""

    if restriction is None:
        restrictionLine = ""
    else:
        restrictionLine = "\n            ?result rdf:type/rdfs:subClassOf* %s ." %restriction

    if remove is None:
        removeLine = ""
    else:
        removeLine = "\n            FILTER NOT EXISTS { %s %s ?result }" %(subject, remove)

    if sortedByNumber:
        numberLine = "\n            OPTIONAL { ?result (cont:isItemOf|(^sys:hasItem))/cont:hasNumber ?number }"
        extraVariables += "?number"
    else:
        numberLine = ""

    if filterNotExists is None:
        filterNotExistsLine = ""
    else:
        filterNotExistsLine = "FILTER NOT EXISTS { %s }" %filterNotExists

    results = QUERY("""
        SELECT DISTINCT ?result ?label ?comment ?counter ?rdfClass %s
        WHERE {
            %s %s ?result . %s%s%s
            OPTIONAL { ?result rdfs:label ?label } .
            OPTIONAL { ?result rdfs:comment ?comment } .
            OPTIONAL { ?result ontoscript:counter ?counter } .
            OPTIONAL { ?result a/(rdfs:subClassOf*) ?rdfClass . FILTER (!isBlank(?rdfClass)) } .
            %s
        }
        """ %(extraVariables, subject,  property, restrictionLine, removeLine, numberLine, filterNotExistsLine))

    d = {}
    for result in results:
        resultQName = URI_TO_QNAME(result[0])

        if resultQName not in list(d.keys()):
            d[resultQName] = Node(uri             = result[0].toPython(),
                                  qname           = resultQName,
                                  cache           = cache)

        if result[1] is not None:
            d[resultQName]["label"] = result[1].toPython()
        if result[2] is not None:
            d[resultQName]["comment"] = result[2].toPython()
        if result[3] is not None:
            d[resultQName]["counter"] = int(result[3].toPython())
        if result[4] is not None:
            d[resultQName].registerClass(URI_TO_QNAME(result[4].toPython()))

        if sortedByNumber:
            if result[5] is not None:
                d[resultQName]["number"] = int(result[5].toPython())
            else:
                d[resultQName]["number"] = None

    keysStr = ""
    for key in list(d.keys()):
        keysStr += (key + " ")

    INFO("     --> " + keysStr)

    for resultQName, resultNode in list(d.items()):
        resultNode.registerKnownViews()
        if resultQName not in cache:
            cache[resultQName] = d[resultQName]

    # return a list of QNames
    ret = [] # list of qnames

    # first sort by 'counter' key:
    resultNodes =  sorted(list(d.values()), key=lambda x: x['counter'])  # entries with None will be put first in the sorted list

    # then, if necessary, sort by number:
    if sortedByNumber:
        resultNodes =  sorted(resultNodes, key=lambda x: x['number'])

    for resultNode in resultNodes:
        ret.append(resultNode['qname'])

    return ret


def fillFields(node, mandatories={}, optionals={}):
    """
    Fill some mandatory and/or optional fields of a node.
    """
    subject = node['qname']

    INFO("    Fill these fields of %s: mandatories=%s, optionals=%s" %(subject, list(mandatories.keys()), list(optionals.keys())))

    selectLine = ""
    wherePart = ""

    for key,value in list(mandatories.items()):
        selectLine += " ?%s" %key
        wherePart += "%s %s ?%s .\n" %(subject, value, key)

    for key,value in list(optionals.items()):
        selectLine += " ?%s" %key
        wherePart += "OPTIONAL { %s %s ?%s } .\n" %(subject, value, key)

    query = """
        SELECT DISTINCT %s
        WHERE {
            %s
        }
        """ %(selectLine, wherePart)

    results = QUERY(query)

    if len(results) == 0:
        raise Exception("No results for query:\n%s" %query)


    infoStr = "     --> mandatories ["

    for result in results:
        # the mandatories
        for i in range(len(mandatories)):
            key = list(mandatories.keys())[i]
            try:
                if IS_URI(result[i]):
                    node.cache[subject][key] = URI_TO_QNAME(result[i].toPython())
                else:
                    node.cache[subject][key] = result[i].toPython()
            except:
                node.cache[subject][key] = None

            if i > 0: infoStr += ","
            infoStr += str(node.cache[subject][key])

        infoStr += "], optionals ["

        for i in range(len(optionals)):
            key = list(optionals.keys())[i]
            try:
                j = len(mandatories) + i
                if IS_URI(result[j]):
                    node.cache[subject][key] = URI_TO_QNAME(result[j].toPython())
                else:
                    node.cache[subject][key] = result[j].toPython()
            except:
                node.cache[subject][key] = None

            if i > 0: infoStr += ","
            infoStr += str(node.cache[subject][key])

        infoStr += "]"

    INFO(infoStr)


def fillNumber(node, optional=False):
    """
    Fill out the number of a container item (according to the containers ontology).
    """
    INFO("    Fill number of %s")

    node["number"] = None

    results = QUERY("""
        SELECT DISTINCT ?number
        WHERE {
            %s (cont:isItemOf|(^cont:hasItem))/cont:hasNumber ?number .
        }
        """ %node["qname"])


    for (number,) in results:
        node["number"] = int(number.toPython())

    INFO("     --> %s" %node["number"])

__author__ = 'wimpe'

import os
import rdflib
import fnmatch

#from rdflib import plugin
#from rdflib.parser import Parser
#from rdflib.serializer import Serializer
#plugin.register("rdf-json", Parser    , "rdflib_jsonld.jsonld_parser"    , "JsonLDParser")

import pprint
PPRINTER = pprint.PrettyPrinter(depth=6)

__global_graph__ = None

def GET_GRAPH():
    return __global_graph__

def CREATE_GRAPH():
    global __global_graph__
    try:
        __global_graph__ = rdflib.ConjunctiveGraph()
    except:
        __global_graph__ = rdflib.graph.ConjunctiveGraph()






def FIND_FILES(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename




def CLEAR_GRAPH():
    global __global_graph__
    print "CLEARING (%d)" %len(__global_graph__)
    CREATE_GRAPH()
    print "CLEARED (%d)" %len(__global_graph__)



def CONTEXT():
    global __global_graph__
    d = {}
    for prefix, uri in __global_graph__.namespace_manager.namespaces():
        d[prefix] = uri
    return d

def LOG_CONTEXT():
    global __global_graph__
    LOG("CONTEXT:")
    c = CONTEXT()
    for prefix, uri in c.items():
        LOG("  %s : %s" %(prefix, uri))
    LOG("TRIPLES LOADED: %d" %len(__global_graph__))

def LOG(text=""):
    print("-- %s" %str(text))

def ERROR(text=""):
    print("!! %s" %text)

def QUERY(text):
    global PPRINTER
    strippedText = text.strip()
    LOG("Processing query:")
    for line in strippedText.split('\n'):
        LOG("   %s" %line)
    results = __global_graph__.query(strippedText)
    LOG("Results:")
    if len(results) >0:
        for result in results:
            LOG(result) #PPRINTER.pprint(result)
    else:
        LOG("   0 found")
    LOG()
    if results is None:
        results = []
    return results

def URI_TO_QNAME(uri):
    try:
        if str(uri).find("://"):
            return __global_graph__.namespace_manager.qname(unicode(str(uri)))
        else:
            raise Exception("Doesn't appear to be a valid URI!")
    except Exception, e:
        raise Exception("Couldn't convert '%s' to a QName: %s" %(uri,e))

def URI_TO_IDENTIFIER(uri):
    separator = str(uri).find('#')
    if separator > 0:
        return str(uri)[separator + 1:]
    else:
        raise Exception("URI %s doesn't contain an identifier" %uri)


def QNAME_TO_URI(qname):
    for prefix, uri in __global_graph__.namespace_manager.namespaces():
        if qname.find(prefix + ":") == 0:
            return uri + qname[len(prefix)+1:]
    else:
        raise Exception("QName %s is unknown" %qname)

def IS_QNAME(x):
    return len(x.split(':')) == 2

def IS_URI(x):
    return isinstance(x, rdflib.URIRef)

def IS_LITERAL(x):
    return isinstance(x, rdflib.Literal)

def PARSE_FOR_URI(s):

    # max 10 iterations:
    for i in xrange(10):
        httpStart = s.find("http://")
        if httpStart > 0:
            httpEnd = s.find(" ", httpStart)
            if httpEnd < 0:
                httpEnd = len(s)

            uri = s[httpStart:httpEnd]
            qname = URI_TO_QNAME(uri)
            html = "<a href=browse?browse=%s>%s</a>" %(qname,qname)
            s = s.replace(uri, html)
        else:
            break

    return s

"""
Module containing some functions related to the triple store (the global graph).
"""

import os
import rdflib
import fnmatch
from . import context
from .logging import DEBUG, INFO, ERROR

import pprint
PPRINTER = pprint.PrettyPrinter(depth=6)


###################################################################################################
# the global instance of the graph. Should not be accessed directly outside this module.
__global_graph__ = None
###################################################################################################


def GET_GRAPH():
    """
    Get a reference to the global graph.
    """
    return __global_graph__


def CREATE_GRAPH():
    """
    Create the global graph.
    """
    global __global_graph__
    try:
        __global_graph__ = rdflib.ConjunctiveGraph()
    except:
        __global_graph__ = rdflib.graph.ConjunctiveGraph()


def CLEAR_GRAPH():
    """
    Clear the global graph.
    """
    global __global_graph__
    INFO("CLEARING (triples: %d)" %len(__global_graph__))
    CREATE_GRAPH()
    INFO("CLEARED (triples: %d)" %len(__global_graph__))


def LOAD_MINIMAL_CONTEXT():
    """
    Load the minimal context, so that the queries defined in the templates get a meaning
    (and don't raise exceptions because of unknown namespaces"

    An example of a context item is:
        prefix "sys" = Namespace("http://www.mercator.iac.es/onto/metamodels/systems"))
    """
    global __global_graph__
    for (prefix,uri) in list(context.MINIMAL_CONTEXT.items()):
        __global_graph__.namespace_manager.bind(prefix, rdflib.namespace.Namespace(uri))


def FIND_FILES(directory, pattern):
    """
    Find the files that match a given pattern, in a given directory.
    """
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def CONTEXT():
    """
    Get the context of the global graph, as a dictionary of key=prefix and value=URI.
    """
    global __global_graph__
    d = {}
    for prefix, uri in __global_graph__.namespace_manager.namespaces():
        d[prefix] = uri
    return d


def LOG_CONTEXT():
    """
    Log the context as INFO.
    """
    global __global_graph__
    INFO("CONTEXT:")
    c = CONTEXT()
    for prefix, uri in list(c.items()):
        INFO("  %s : %s" %(prefix, uri))
    INFO("TRIPLES LOADED: %d" %len(__global_graph__))


def QUERY(text):
    """
    Execute a query.
    """
    strippedText = text.strip()


    for line in strippedText.split('\n'):
        DEBUG("   %s" %line)

    results = __global_graph__.query(strippedText)
    DEBUG("Results:")
    if len(results) >0:
        for result in results:
            DEBUG(result)
    else:
        DEBUG("   0 found")

    if results is None:
        results = []

    return results


def URI_TO_QNAME(uri):
    """
    Convert the given URI to a qname, using the context of the global graph.
    """
    try:
        if str(uri).find("://"):
            return __global_graph__.namespace_manager.qname(str(str(uri)))
        else:
            raise Exception("Doesn't appear to be a valid URI!")
    except Exception as e:
        raise Exception("Couldn't convert '%s' to a QName: %s" %(uri,e))


def URI_TO_IDENTIFIER(uri):
    """
    Return the identifier part of an URI (e.g. return 'b' for 'http://blabla.com/bla#b').
    """
    separator = str(uri).find('#')
    if separator > 0:
        return str(uri)[separator + 1:]
    else:
        raise Exception("URI %s doesn't contain an identifier" %uri)


def QNAME_TO_URI(qname):
    """
    Convert the given qname to an URI, based on the context of the global graph.
    """
    for prefix, uri in __global_graph__.namespace_manager.namespaces():
        if qname.find(prefix + ":") == 0:
            return uri + qname[len(prefix)+1:]
    else:
        raise Exception("QName %s is unknown" %qname)


def IS_QNAME(x):
    """
    Check if the given string is a qname.
    """
    return len(x.split(':')) == 2


def IS_URI(x):
    """
    Check if the given string is an URI.
    """
    return isinstance(x, rdflib.URIRef)


def IS_LITERAL(x):
    """
    Check if the given string is a literal.
    """
    return isinstance(x, rdflib.Literal)


def PARSE_FOR_URI(s):
    """
    Convert URI occurrences in a string to an HTML hyperlink for the browse view.
    """
    # max 10 iterations:
    for i in range(10):
        httpStart = s.find("http://")
        if httpStart > 0:
            httpEnd = s.find(" ", httpStart)
            if httpEnd < 0:
                httpEnd = len(s)

            uri = s[httpStart:httpEnd]
            qname = URI_TO_QNAME(uri)
            html = "<a href=browse?show;qname=%s>%s</a>" %(qname,qname)
            s = s.replace(uri, html)
        else:
            break

    return s

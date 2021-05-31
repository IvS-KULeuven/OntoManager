"""
Callback functions for the views of the 'browse' category.
"""

from .triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, INFO
import rdflib


def show_browse(node, args=None):
    """
    Show the 'browse' view of the 'browse' category.
    """
    INFO("browse.show_browse(%s)" %node['qname'])

    results = QUERY("""
        SELECT DISTINCT ?predicate ?object
        WHERE {
            %s ?predicate ?object .
        }
        """ %node["qname"])

    d = {}

    for predicateUri, ob in results:
        predicate = URI_TO_QNAME(predicateUri)

        if type(ob) == rdflib.term.URIRef:
            object = { "type"    : "uri",
                       "content" : { "uri"   : ob.toPython(),
                                     "qname" : URI_TO_QNAME(ob) } }


        elif type(ob) == rdflib.term.BNode:
            object = { "type"    : "bnode",
                       "content" : { "id" : ob } }
        elif type(ob) == rdflib.term.Literal:
            object = { "type"    : "literal",
                       "content" : ob.toPython() }
        else:
            object = { "type"    : "unknown",
                       "content" : ob }

        if predicate not in list(d.keys()):
            d[predicate] = { "uri"     : predicateUri,
                             "qname"   : predicate,
                             "objects" : [ object ] }

        else:
            d[predicate]["objects"].append( object )

    node["results"] = sorted(list(d.values()), key=lambda x: x["qname"])

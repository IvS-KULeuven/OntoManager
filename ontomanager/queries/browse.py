from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI
import rdflib
import pprint
from util import Node
from register import REGISTRY

#from rdflib.extras.infixowl import Class, Individual, manchesterSyntax, classOrIdentifier


def show_browse(node, args=None):

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

        if predicate not in d.keys():
            d[predicate] = { "uri"     : predicateUri,
                             "qname"   : predicate,
                             "objects" : [ object ] }

            # # in case of some known types, add the manchester syntax
            # uri = rdflib.term.URIRef(QNAME_TO_URI(node['qname']))
            # if predicate == "rdf:type":
            #     d[predicate]["manchester"] = [manchesterSyntax(classOrIdentifier(s), GRAPH) for s in Individual( uri , graph=GRAPH).type ]
            # elif predicate == "owl:equivalentClass":
            #     d[predicate]["manchester"] = [manchesterSyntax(classOrIdentifier(s), GRAPH) for s in Class( uri , graph=GRAPH).equivalentClass ]
            # elif predicate == "rdfs:subClassOf":
            #     d[predicate]["manchester"] = [manchesterSyntax(classOrIdentifier(s), GRAPH) for s in Class( uri , graph=GRAPH).subClassOf]
        else:
            d[predicate]["objects"].append( object )


    node["results"] = sorted(d.values(), key=lambda x: x["qname"])


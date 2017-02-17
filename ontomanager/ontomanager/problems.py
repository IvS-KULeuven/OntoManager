"""
Functions to read the constraint violations from the knowledge base.
"""

from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, URI_TO_IDENTIFIER
import pprint

def getAllConstraintViolations():
    """
    Get a list of all constraint violations.

    @return: a list of dictionaries.
    """
    results = QUERY("""
        SELECT DISTINCT ?root ?rootLabel ?rootCounter ?value ?level ?label
        WHERE {
            ?violation rdf:type/rdfs:subClassOf* spin:ConstraintViolation .
            ?violation spin:violationRoot ?root .
            ?root rdfs:label ?rootLabel .
            OPTIONAL { ?root ontoscript:counter ?rootCounter } .
            OPTIONAL { ?violation spin:violationValue ?value } .
            OPTIONAL { ?violation spin:violationLevel ?level } .
            ?violation rdfs:label ?label .
        }
        """)
    d = {}
    for rootUri, rootLabel, rootCounter, value, level, label in results:
        root = URI_TO_QNAME(rootUri)
        hash = "%s-%s" %(root, label)

        if hash not in d.keys():

            d[hash] = {  "root" : { "uri"     : rootUri.toPython(),
                                    "qname"   : root,
                                    "counter" : -1,
                                    "label"   : rootLabel.toPython() },
                         "label" : label.toPython(),
                         "value" : value,
                         "level" : level}

            if rootCounter is not None:
                d[hash]["root"]["counter"] = int(rootCounter.toPython())

            if value is not None:
                try:
                    d[hash]["value"] = value.toPython()
                except:
                    pass

            if level is not None:
                try:
                    d[hash]["level"] = level.toPython()
                except:
                    pass

    return sorted(d.values(), key=lambda x: x["root"]["counter"])

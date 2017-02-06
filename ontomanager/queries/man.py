from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, IS_LITERAL, LOG, os
import generic
import pprint


# ====================================================== Manufactured ==================================================


def getManufactured(cache, qname):
    LOG("getConnectors(%s)" %(qname))

    return generic.getRelated(cache, subject=qname, property="^man:isManufacturedBy")

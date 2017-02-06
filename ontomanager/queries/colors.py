__author__ = 'wimpe'
from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, IS_LITERAL, LOG, os
import generic
import pprint




def getColors(cache, qname):
    LOG("getColors(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="colors:hasColor")

def show_Color(node, args=None):
    generic.fillFields(node, mandatories={ 'hexValue' : 'colors:hasHexValue' })


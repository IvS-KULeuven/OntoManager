"""
Callback functions for the views of the 'colors' category.
"""

__author__ = 'wimpe'
from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI, IS_LITERAL, INFO
import generic


def getColors(cache, qname):
    """
    Expand the colors of a node.
    """
    INFO("colors.getColors(%s)" %qname)
    return generic.getRelated(cache, subject=qname, property="colors:hasColor")


def show_Color(node, args=None):
    """
    Show the 'Color' view of the 'colors' category.
    """
    INFO("colors.show_Color(%s)" %node['qname'])
    generic.fillFields(node, mandatories={ 'hexValue' : 'colors:hasHexValue' })

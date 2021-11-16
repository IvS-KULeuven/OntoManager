"""
Callback functions for the views of the 'man' category.
"""
from .triplestore import INFO
from . import generic


# ====================================================== Manufactured ==================================================


def getManufactured(cache, qname):
    """
    Expand the manufactured items of a node.
    """
    INFO("man.getManufactured(%s)" %(qname))
    return generic.getRelated(cache, subject=qname, property="^man:isManufacturedBy")

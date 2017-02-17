"""
Callback functions for the views of the 'org' category.
"""
import generic
from triplestore import QUERY, INFO


# ====================================================== Manufacturer ==================================================


def show_Manufacturer(node, args=None):
    """
    Show the 'Manufacturer' view of the 'org' category.
    """
    INFO("org.show_Manufacturer(%s)" %node['qname'])

    node.expand("org", "Manufacturer")

    generic.fillFields(node, mandatories={ 'long_name'    : 'org:hasLongName',
                                           'short_name'   : 'org:hasShortName' })

    for manufactured in node["manufactured"]:
        node.cache[manufactured].show()


# ====================================================== Organization ==================================================


def show_Organization(node, args=None):
    """
    Show the 'Organization' view of the 'org' category.
    """
    INFO("org.show_Organization(%s)" %node['qname'])

    node.expand("org", "Organization")

    generic.fillFields(node, mandatories={ 'long_name'    : 'org:hasLongName',
                                           'short_name'   : 'org:hasShortName' })

    for manufactured in node["manufactured"]:
        node.cache[manufactured].show()

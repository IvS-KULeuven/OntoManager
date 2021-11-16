"""
Callback functions for the views of the 'sys' category.
"""

from .logging import INFO
from . import generic


# ========================================================= PROJECT ====================================================


def getProjects(cache): # returns: list of Nodes
    """
    Get the projects in the KB.
    """
    INFO("sys.getProjects()")

    return generic.getInstances(cache = cache, className = "dev:Project")


def show_project(node, args=None):
    """
    Show the 'project' view of the 'sys' category.
    """
    INFO("sys.show_project(%s)" %node['qname'])

    node.expand("sys", "project")


# ========================================================= REALIZES ====================================================


def getRealizes(cache, qname):
    """
    Expand the list of nodes that the given node realizes.
    """
    INFO("sys.getRealizes(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:realizes")


def show_Realization(node, args=None):
    """
    Show the 'Realization' view of the 'sys' category.
    """
    INFO("sys.show_Realization(%s)" %node['qname'])

    node.expand("sys", "Realization")
    for r in node["realizes"]:
        node.cache[r].show()


# ========================================================= CONCEPT ====================================================


def getConcepts(cache, qname):
    """
    Expand the concepts of a node.
    """
    INFO("sys.getConcepts(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:hasPart|^sys:isPartOf", restriction="dev:Concept")


def show_concept(node, args=None):
    """
    Show the 'concept' view of the 'sys' category.
    """
    INFO("sys.show_concept(%s)" %node['qname'])

    node.expand("sys", "concept")

    for expansion in [ "requirements", "states", "properties", "constraints", "tests", "designs" ]:
        for qname in node[expansion]:
            node.cache[qname].show("sys")


# ====================================================== REQUIREMENTS ==================================================


def getRequirements(cache, qname):
    """
    Expand the requirements of a node.
    """
    INFO("sys.getRequirements(%s)" %(qname))

    return generic.getRelated(cache, qname, "dev:hasRequirement")


def getRealizedRequirements(cache, qname):
    """
    Expand the realized requirements of a node.
    """
    INFO("sys.getRealizedRequirements(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:realizes/dev:hasRequirement")


def show_requirement(node, args=None):
    """
    Show the 'requirement' view of the 'sys' category.
    """
    INFO("sys.show_requirement(%s)" %node['qname'])

    node.expand("sys", "requirement")

    for derived in node["derives"]:
        node.cache[derived].show()
    for derivedFrom in node["derived_from"]:
        node.cache[derivedFrom].show()
    for d in node["declared_by"]:
        node.cache[d].show("sys")
    for s in node["satisfied_by"]:
        node.cache[s].show("sys")


# ======================================================== DECLARED BY =====================================================


def getDeclaredBy(cache, qname):
    """
    Expand the list of nodes which declare this node.
    """
    INFO("sys.getDeclaredBy(%s)" %(qname))

    return generic.getRelated(cache, qname, "^dev:hasRequirement")

# ======================================================== SATISFIES =====================================================

def getSatisfies(cache, qname):
    """
    Expand the list of nodes which this node satisfies.
    """
    INFO("sys.getSatisfies(%s)" %(qname))

    return generic.getRelated(cache, qname, "(^dev:isSatisfiedBy)|dev:satisfies")


def getSatisfiedBy(cache, qname):
    """
    Expand the list of nodes that are satisfied by this node.
    """
    INFO("sys.getSatisfiedBy(%s)" %(qname))

    return generic.getRelated(cache, qname, "(^dev:satisfies)|dev:isSatisfiedBy")


# ======================================================== DERIVES =====================================================


def getDerives(cache, qname):
    """
    Expand the list of nodes which this node derives.
    """
    INFO("sys.getDerives(%s)" %(qname))

    return generic.getRelated(cache, qname, "dev:derives|^dev:isDerivedFrom")


def getDerivedFrom(cache, qname):
    """
    Expand the list of nodes that are derived from this node.
    """
    INFO("sys.getDerivedFrom(%s)" %(qname))

    return generic.getRelated(cache, qname, "dev:isDerivedFrom|^dev:derives")


# ======================================================== DESIGNS =====================================================


def getDesigns(cache, qname):
    """
    Expand the designs of this node.
    """
    INFO("sys.getDesigns(%s)" %(qname))

    return generic.getRelated(cache, qname, "^sys:realizes")


def show_design(node, args=None):
    """
    Show the 'design' view of the 'sys' category.
    """
    INFO("sys.show_design(%s)" %node['qname'])

    node.expand("sys", "design")

    for expansion in [ "realizes", "realized_requirements", "requirements", "states", "properties", "constraints", "tests", "parts" ]:
        for qname in node[expansion]:
            node.cache[qname].show("sys")


# ======================================================== STATES ======================================================


def getStates(cache, qname):
    """
    Expand the states of this node.
    """
    INFO("sys.getStates(%s)" %(qname))

    return generic.getRelated(cache, qname, "fsm:hasState")


# ====================================================== PROPERTIES ====================================================


def getProperties(cache, qname):
    """
    Expand the properties of this node.
    """
    INFO("sys.getProperties(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:hasProperty")


# ===================================================== CONSTRAINTS ====================================================


def getConstraints(cache, qname):
    """
    Expand the constraints of this node.
    """
    INFO("sys.getConstraints(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:hasProperty", restriction="dev:Constraint")


# ======================================================== TESTS =======================================================


def getTests(cache, qname):
    """
    Expand the tests of this node.
    """
    INFO("sys.getTests(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:hasProperty", restriction="dev:Test" )


def show_test(node, args=None):
    """
    Show the 'test' view of the 'sys' category.
    """
    INFO("sys.show_test(%s)" %node['qname'])

    node.expand("sys", "test")

    for verifies in node["verifies"]:
        node.cache[verifies].show()
    for t in node["tests"]:
        node.cache[t].show()


def getVerifies(cache, qname):
    """
    Expand the list of nodes which this node verifies.
    """
    INFO("sys.getVerifies(%s)" %(qname))

    return generic.getRelated(cache, qname, "dev:verifies")


def getTested(cache, qname):
    """
    Expand the list of nodes which this node tests.
    """
    INFO("sys.getTested(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:tests")


# ======================================================== PARTS =======================================================


def getParts(cache, qname):
    """
    Expand the parts of this node..
    """
    INFO("sys.getParts(%s)" %(qname))

    return generic.getRelated(cache, qname, "sys:hasPart")


def show_part(node, args=None):
    """
    Show the 'part' view of the 'sys' category.
    """
    INFO("sys.show_part(%s)" %node['qname'])

    node.expand("sys", "part")


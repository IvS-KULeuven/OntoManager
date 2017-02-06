from triplestore import QUERY, URI_TO_QNAME, QNAME_TO_URI
from util import Node
import generic
import pprint



# ========================================================= PROJECT ====================================================


def getProjects(cache): # returns: list of Nodes
    return generic.getInstances(cache = cache, className = "dev:Project")


def show_project(node, args=None):
    node.expand("sys", "project", visible=False)



# ========================================================= REALIZES ====================================================

def getRealizes(cache, something):
    return generic.getRelated(cache, something, "sys:realizes")


def show_Realization(node, args=None):
    node.expand("sys", "Realization", visible=False)
    for r in node["realizes"]:
        node.cache[r].show()



# ========================================================= CONCEPT ====================================================

def getConcepts(cache, project):
    return generic.getRelated(cache, project, "sys:hasPart|^sys:isPartOf", restriction="dev:Concept")


def show_concept(node, args=None):
    node.expand("sys", "concept", visible=False)

    for expansion in [ "requirements", "states", "properties", "constraints", "tests", "designs" ]:
        for qname in node[expansion]:
            node.cache[qname].show("sys")


# ====================================================== REQUIREMENTS ==================================================


def getRequirements(cache, concept):
    return generic.getRelated(cache, concept, "dev:hasRequirement")

def getRealizedRequirements(cache, concept):
    return generic.getRelated(cache, concept, "sys:realizes/dev:hasRequirement")


def show_requirement(node, args=None):
    node.expand("sys", "requirement", visible=False)

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
    return generic.getRelated(cache, qname, "^dev:hasRequirement")

# ======================================================== SATISFIES =====================================================

def getSatisfies(cache, qname):
    return generic.getRelated(cache, qname, "(^dev:isSatisfiedBy)|dev:satisfies")


def getSatisfiedBy(cache, qname):
    return generic.getRelated(cache, qname, "(^dev:satisfies)|dev:isSatisfiedBy")


# ======================================================== DERIVES =====================================================

def getDerives(cache, qname):
    return generic.getRelated(cache, qname, "dev:derives|^dev:isDerivedFrom")


def getDerivedFrom(cache, qname):
    return generic.getRelated(cache, qname, "dev:isDerivedFrom|^dev:derives")



# ======================================================== DESIGNS =====================================================


def getDesigns(cache, project):
    return generic.getRelated(cache, project, "^sys:realizes")


def show_design(node, args=None):
    node.expand("sys", "design", visible=False)

    for expansion in [ "realizes", "realized_requirements", "requirements", "states", "properties", "constraints", "tests", "parts" ]:
        for qname in node[expansion]:
            node.cache[qname].show("sys")


# ======================================================== STATES ======================================================

def getStates(cache, qname):
    return generic.getRelated(cache, qname, "fsm:hasState")

# ====================================================== PROPERTIES ====================================================

def getProperties(cache, qname):
    return generic.getRelated(cache, qname, "sys:hasProperty")


# ===================================================== CONSTRAINTS ====================================================

def getConstraints(cache, qname):
    return generic.getRelated(cache, qname, "sys:hasProperty", restriction="dev:Constraint")


# ======================================================== TESTS =======================================================

def getTests(cache, qname):
    return generic.getRelated(cache, qname, "sys:hasProperty", restriction="dev:Test" )



def show_test(node, args=None):
    node.expand("sys", "test", visible=False)

    for verifies in node["verifies"]:
        node.cache[verifies].show()
    for t in node["tests"]:
        node.cache[t].show()


def getVerifies(cache, qname):
    return generic.getRelated(cache, qname, "dev:verifies")


def getTested(cache, qname):
    return generic.getRelated(cache, qname, "sys:tests")

# ======================================================== PARTS =======================================================


def getParts(cache, qname):
    return generic.getRelated(cache, qname, "sys:hasPart")

def show_part(node, args=None):
    node.expand("sys", "part", visible=False)




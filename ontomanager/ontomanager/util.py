"""
Module containing some utility functions.
"""

from logging import DEBUG, INFO
from register import REGISTRY
import pprint


###################################################################################################
# a global instance of a pretty printer
PPRINTER = pprint.PrettyPrinter(depth=6)
###################################################################################################


def getFromDict(dataDict, mapList):
    """
    Get a value in a dictionary.
    """
    try:
        return reduce(lambda d, k: d[k], mapList, dataDict)
    except KeyError, e:
        pprint.pprint("dataDict:")
        pprint.pprint(dataDict)
        pprint.pprint("mapList:")
        pprint.pprint(mapList)
        raise

def setInDict(dataDict, mapList, value):
    """
    Set a value in a dictionary.
    """
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value



###################################################################################################
# example of a Node
__example__ = """
Node "cover:concept"
 |_qname
 |_uri
 |_label
 |_counter
 |_comment
 |_classes                         = [ 'sys:Concept', 'owl:Thing' ]
 |_views_order                     = [ ['sys','concept'], ['browse', 'all'] ]
 |_views
 |  |_sys
 |  |  |_concept
 |  |      |_shown_before          = True
 |  |      |_view_priority         = 14
 |  |      |_expansions            = [ "requirements", "tests" ]
 |  |      |_expanded              = True
 |  |      |_expanded_requirements = True
 |  |      |_expanded_tests        = True
 |  |_browse
 |     |_all
 |         |_view_priority         = 1
 |         |_expansions            = []
 |         |_expanded              = False
 |
 |_requirements                    = [ cover:concept.req1, cover:concept.req2 ]
 |_tests                           = [ cover:concept.test1 ]
 |_conceptualizes                  = cover:project
 |_browse_results                  = [ ... ]
"""

###################################################################################################


class Node(dict):
    """
    A Node represents a node in the graph: an RDF resource.
    """

    def __init__(self, qname, uri, label="", counter=-1, comment="", cache={}):
        """
        Create a new node using its qname, uri, label, counter, and comment.
        """
        dict.__init__(self)
        self["qname"]       = qname
        self["uri"]         = str(uri)
        self["label"]       = label
        self["counter"]     = counter
        self["comment"]     = comment
        self["classes"]     = []
        self["views_order"] = []
        self["default_views"] = {}
        self["views"]       = {}
        self.cache = cache


    def log(self, msg):
        """
        Simple low-level log function.
        """
        DEBUG("%s : %s" %(self['qname'], msg))


    def updateDefaultViews(self):
        """
        Set the default view, based on the views order.
        """
        for category in self["views"].keys():
            for orderedCategory, orderedType in self["views_order"]:
                if orderedCategory == category:
                    self["default_views"][category] = orderedType
                    break


    def updateViewsOrder(self):
        """
        Re-order the views.
        """
        self.log("Updating the views order")
        viewsOrder = []

        fullViews = []
        for category, categoryRest in self["views"].items():
            for type, rest in categoryRest.items():
                fullViews.append([category, type, rest])

        fullViews.sort(key = lambda item : item[2]["view_priority"], reverse=True)

        for fullView in fullViews:
            viewsOrder.append([fullView[0], fullView[1]])

        self["views_order"] = viewsOrder
        self.log("New views order: %s" %viewsOrder)
        self.updateDefaultViews()


    def registerClass(self, qname):
        """
        Register a new RDF class.
        """
        self.log("Registering class %s" %qname)

        if qname not in self["classes"]:
            self["classes"].append(qname)


    def registerKnownViews(self):
        """
        Register a known view for this node.
        """
        for view in REGISTRY.getViewsForClasses(self['classes']):
            self.registerViewIfNeeded(view["category"], view["type"], view["priority"])


    def registerViewIfNeeded(self, category, type, priority=-1):
        """
        Register a known view for this node, if it wasn't already registered.
        """
        self.log("Registering view %s/%s with priority=%d" %(category, type, priority))
        alreadyRegistered = False
        if self["views"].has_key(category):
            if self["views"][category].has_key(type):
                alreadyRegistered = True
        else:
            self["views"][category] = {}

        if alreadyRegistered:
            self.log("The view was already registered")
        else:
            self["views"][category][type] = {
                "view_priority" : priority,
                "expansions"    : [],
                "expandable"    : True,
                "expanded"      : False,
                "expanded_before" : False,
                "shown_before"    : False
            }

            self.log("The view has been registered")

            self.updateViewsOrder()


    def show(self, category=None, type=None, args=None):
        """
        Show the node (call the show_... callback function if needed).
        """
        if (category is None) or (category == ''):
            self.log("Showing default view")

            # determine the default view
            if self["views_order"] > 0:
                defaultCategory, defaultType = self["views_order"][0]
            else:
                raise Exception("Cannot show default view: no view registered!")

            # show it
            return self.show(category = defaultCategory, type = defaultType, args = args)
        else:
            if (type is None) or (type == ''):
                self.log("Showing default view for %s" %category)
                for currentCategory, currentType in self["views_order"]:
                    if category == currentCategory:
                        return self.show(category = category, type = currentType, args = args)
            else:
                self.log("Showing %s : %s (args=%s)" %(category, type, args))
                self.registerViewIfNeeded(category, type) # lowest priority if it didnt exist yet
                if not self["views"][category][type]["shown_before"]:
                    self["views"][category][type]["shown_before"] = True
                    REGISTRY.callViewIfNeeded(category, type, self, args)

                return category, type


    def writeToStdOut(self):
        """
        Simply write the node to the stdout, as a nicely formatted string.
        """
        PPRINTER.pprint(self)


    def expand(self, category=None, type=None, expansion=None):
        """
        Expand the expansion(s) of the node.

        If the category is not given, then the default view will be expanded.
        If the category is given but the type is not given, then the first
        view of the given category is expanded.
        If both category and type is given, but a specific expansion is not
        given, then all expansions of the given view are expanded.
        Else, expand the given expansion of the given view type of the given
        view category.
        """
        if (category is None) or (category == ""):
            self.log("Expanding default view")

            # determine the default view
            if self["views_order"] > 0:
                defaultCategory, defaultType = self["views_order"][0]
            else:
                raise Exception("Cannot expand default view: no view registered!")

            # expand it
            self.expand(category=defaultCategory, type=defaultType, expansion=expansion)
        else:
            if not self["views"].has_key(category):
                raise Exception("Cannot expand category %s: unknown category!" %category)

            if (type is None) or (type == ""):
                self.log("Expanding default view for %s" %category)
                for currentCategory, currentType in self["views_order"]:
                    if category == currentCategory:
                        return self.expand(category = currentCategory, type = currentType, expansion=expansion)
            else:
                if not self["views"][category].has_key(type):
                    self.writeToStdOut()
                    raise Exception("Cannot expand %s/%s: type %s is unknown!" %(category, type, type))

                if (expansion is None) or (expansion == ''):
                    self.log("Now fully expanding %s/%s" %(category,type))

                    if REGISTRY.expansions[category].has_key(type):
                        # add all expansions
                        for expansion in REGISTRY.expansions[category][type].keys():
                            if not (expansion in self["views"][category][type]["expansions"]):
                                self["views"][category][type]["expansions"].append(expansion)
                                self["views"][category][type]["expanded_%s" %expansion] = False
                                self["views"][category][type]["expanded_%s_before" %expansion] = False
                                self[expansion] = []

                        # set the top-level expansion,
                        self["views"][category][type]["expanded"] = True

                        # expand all expansions without showing;
                        if not self["views"][category][type]["expanded_before"]:
                            for currentExpansion in self["views"][category][type]["expansions"]:
                                self.expand(category=category, type=type, expansion=currentExpansion)
                            self["views"][category][type]["expanded_before"] = True
                    else:
                        self.log("%s/%s is not expandable" %(category,type))
                        self["views"][category][type]["expandable"] = False
                else:
                    self.log("Now expanding %s/%s[%s]" %(category,type,expansion))

                    if not self.has_key(expansion):
                        raise Exception("Cannot expand %s/%s[%s]: expansion %s is unknown!" %(category, type, expansion, expansion))

                    if not self["views"][category][type]["expanded_%s_before" %expansion]:
                        self["views"][category][type]["expanded_%s_before" %expansion] = True
                        REGISTRY.callExpansionIfNeeded(category, type, expansion, self)

                    self["views"][category][type]["expanded_%s" %expansion] = True


        self.log("Expansion is finished.")


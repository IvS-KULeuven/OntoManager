__author__ = 'wimpe'

from collections import OrderedDict


# =================================================================================================
class RegAND:
    """
    Represents a logical AND of 2 RDF classes, to be used in Registry::registerView.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right


# =================================================================================================
class Registry:
    """
    A class that registers all views.

    Its global instance (REGISTRY, created below) is populated in allviews.py.
    """

    def __init__(self):
        """
        Create a registry instance.
        """
        self.views = {}
        self.expansions = {}
        self.currentPriority = 0


    def registerView(self, category, type, expression, callback, expansions=None):
        """
        Register a new view.

        @param category: the category of the view (e.g. 'elec', 'soft', 'sys', ...
        @param type: the type of the view (e.g. 'MotorInstance' and 'Consumer' for category elec, 'Variable' for category soft, ...
        @param expression: the expression to associate the view with, either an RDF class or a logical AND of RDF classes.
                           e.g. 'elec:IoModule'                       --> view is available for all individuals with rdf:type=elec:IoModule
                           e.g. RegAND('elec:IoModule', 'sys:Design') --> view is available for all individuals with rdf:type=elec:IoModule AND rdf:type=sys:Design
        @param callback: the callback function to execute before showing the view. Executing this function will result in queries
                         (unless these queries were already executed and stored in the cache before!)
        @param expansions: a list of [expansionName, expansionFunction] (thus: a list of lists of 2 items).
        """
        if category not in self.views:
            self.views[category] = OrderedDict()
        if type in self.views[category]:
            raise Exception("Trying to register view %s/%s twice!" %(category, type))

        self.views[category][type] = { "category"   : category,
                                       "type"       : type,
                                       "expression" : expression,
                                       "priority"   : self.currentPriority,
                                       "callback"   : callback }

        self.currentPriority += 1

        if expansions is not None:
            for expansionName, expansionCallback in expansions:
                self.addExpansion(category, type, expansionName, expansionCallback)


    def getViewsForClasses(self, classes):
        """
        Get a list of views (dictionaries with query results) for specific classes.
        """
        ret = []
        for category in list(self.views.keys()):
            for view in list(self.views[category].values()):
                expression = view["expression"]
                if isinstance(expression, str):
                    # expression is a qname
                    if expression in classes:
                        ret.append(view)
                elif isinstance(expression, RegAND):
                    if (expression.left in classes) and (expression.right in classes):
                        ret.append(view)
                else:
                    raise NotImplementedError("This kind of expression is not implemented")
        return ret


    def addExpansion(self, category, type, expansion, callback):
        """
        Add an expansion.

        @param category: the category of the view (e.g. 'elec', 'soft', 'sys', ...
        @param type: the type of the view (e.g. 'MotorInstance' and 'Consumer' for category elec, 'Variable' for category soft, ...
        @param expansion: the name of the expansion (e.g. 'members' for soft:Type, 'wires' for elec:Cable, ...
        @param callback: the callback function to execute to expand (i.e. to get the members for the soft:Type individual,
                         to get the wires for the elec:Cable individual, ...)
        """
        if category not in self.expansions:
            self.expansions[category] = OrderedDict()

        if type not in self.expansions[category]:
            self.expansions[category][type] = OrderedDict()

        self.expansions[category][type][expansion] = callback


    def __str__(self):
        """
        Get a string representation of the registry, only for debugging purposes...
        """
        s = "Views:\n"
        for category, categoryRest in list(self.views.items()):
            s += "  %s:\n" %category
            for type, view in list(categoryRest.items()):
                s += "    %s : { expression=%s priority=%d callback=%s.%s }\n" %(type,
                                                                                 view["expression"],
                                                                                 view["priority"],
                                                                                 view["callback"].__module__,
                                                                                 view["callback"].__name__)
        s += "Expansions:\n"
        for category, remaining in list(self.expansions.items()):
            s += "  %s:\n" %category
            for type, rest in list(remaining.items()):
                s += "    %s:\n" %type
                for expansion, callback in list(rest.items()):
                    s += "      %s : %s\n" %(expansion, callback)
        return s


    def callExpansionIfNeeded(self, category, type, expansion, node):
        """
        Call the callback function to expand a given expansion of a given type of a given category.
        """
        node[expansion] = self.expansions[category][type][expansion](node.cache, node['qname'])


    def callViewIfNeeded(self, category, type, node, args=None):
        """
        Call the callback function to show a given view type of a given view category for a given Node.
        """
        self.views[category][type]["callback"](node, args)


###################################################################################################
# a global instance of the registry
REGISTRY = Registry()
###################################################################################################


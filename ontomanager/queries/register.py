__author__ = 'wimpe'

from collections import OrderedDict

class RegAND:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Registry:
    def __init__(self):
        self.views = {}
        self.expansions = {}
        self.currentPriority = 0


    def registerView(self, category, type, expression, callback, expansions=None):
        """
         expression: e.g. 'elec:IoModule'                       --> view is available for all individuals with rdf:type=elec:IoModules
                     e.g. RegAND('elec:IoModule', 'sys:Design') --> view is available for all individuals with rdf:type=elec:IoModules AND rdf:type=sys:Design
        """
        if not self.views.has_key(category):
            self.views[category] = OrderedDict()
        if self.views[category].has_key(type):
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
        ret = []
        for category in self.views.keys():
            for view in self.views[category].values():
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

    #
    # def getViewForClass(self, qname):
    #     for category in self.views.keys():
    #         for view in self.views[category].values():
    #             if view["views"] == qname:
    #                 return view
    #
    #     return None


    def addExpansion(self, category, type, expansion, callback):
        if not self.expansions.has_key(category):
            self.expansions[category] = OrderedDict()

        if not self.expansions[category].has_key(type):
            self.expansions[category][type] = OrderedDict()

        self.expansions[category][type][expansion] = callback

    def __str__(self):
        s = "Views:\n"
        for category, categoryRest in self.views.items():
            s += "  %s:\n" %category
            for type, view in categoryRest.items():
                s += "    %s : { expression=%s priority=%d callback=%s.%s }\n" %(type,
                                                                                 view["expression"],
                                                                                 view["priority"],
                                                                                 view["callback"].__module__,
                                                                                 view["callback"].__name__)
        s += "Expansions:\n"
        for category, remaining in self.expansions.items():
            s += "  %s:\n" %category
            for type, rest in remaining.items():
                s += "    %s:\n" %type
                for expansion, callback in rest.items():
                    s += "      %s : %s\n" %(expansion, callback)
        return s





    def callExpansionIfNeeded(self, category, type, expansion, node):
        node[expansion] = self.expansions[category][type][expansion](node.cache, node['qname'])

    def callViewIfNeeded(self, category, type, node, args=None):
        self.views[category][type]["callback"](node, args)

REGISTRY = Registry()



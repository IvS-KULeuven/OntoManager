"""
This module is required for running the generated PyUAF code.
"""

from opcua import ua
import mocsopcua


class OpcUaNode:
    """
    An OpcUaNode represents an OPC UA Node, as generated from the models.
    """

    def __init__(self, parent, name, ns, info=None):
        self.__opcua_parent__ = parent
        self.__opcua_name__ = name
        self.__opcua_ns__ = ns
        self.__opcua_info__ = info

    def __addVariable__(self, name, ns, info, datatype, permissions):
        setattr(self, name, OpcUaVariable(
            self, name, ns, info, datatype, permissions))

    def __addInstance__(self, name, ns, Type, info):
        setattr(self, name, Type(self, name, ns, info))

    def ADR(self):
        if isinstance(self.__opcua_parent__, mocsopcua.models.opcuanode.OpcUaNode):
            parentAddress = self.__opcua_parent__.ADR() + '.' + self.__opcua_name__
        else:
            if (self.__opcua_name__ == "maia"):
                parentAddress = 'ns=4;s=.' + self.__opcua_name__
            else:
                parentAddress = 'ns=4;s=GLOBAL.' + self.__opcua_name__

        return parentAddress

    def INFO(self):
        return self.__opcua_info__

    def __str__(self):
        return self.__opcua_name__ + " : " + self.INFO()


class OpcUaVariable(OpcUaNode):
    """
    An OpcUaNode represents an OPC UA Variable, as generated from the models.
    """

    def __init__(self, parent, name, ns, info=None, datatype=None, permissions=None):
        OpcUaNode.__init__(self, parent, name, ns, info)
        self.__opcua_permissions__ = permissions
        self.__opcua_datatype__ = datatype

    def PERMISSIONS(self):
        return self.__opcua_permissions__

    def DATATYPE(self):
        return self.__opcua_datatype__

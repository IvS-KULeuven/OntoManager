
<%def name="pyuaf_module(node)">\
<%
    libName = node['label'].lower()
    import datetime
    timeNow = datetime.datetime.now().isoformat()

    def getTypes(kind, parent):
        ret = parent[kind][:]

        for childQName in parent['namespaces']:
            child = CACHE[childQName]
            ret += getTypes(kind, child)
        return ret

    fbQNames     = getTypes('FBs', node)
    structQNames = getTypes('STRUCTs', node)
    enumQNames   = getTypes('ENUMs', node)

    fbs     = [ CACHE[qname] for qname in fbQNames      ]
    structs = [ CACHE[qname] for qname in structQNames  ]
    enums   = [ CACHE[qname] for qname in enumQNames    ]
    imported = [] # keep a list of the imported library names
%>\
# This file (${libName}.py) was automatically generated at ${timeNow} -- do not edit manually!
import mocsopcua.models.opcuanode
from mocsopcua.models.opcuanode import OpcUaNode
from opcua import ua

# === ENUMs ====

%for enum in enums:
${pyuaf_enum(enum, libName, imported)}
%endfor

# === STRUCTS ===

%for struct in structs:
${pyuaf_struct(struct, libName, imported)}
%endfor

# === FBs ===

%for fb in fbs:
${pyuaf_fb(fb, libName, imported)}
%endfor

# === imports ===

% for im in imported:
from . import ${im | n}
% endfor


</%def>


<%def name="pyuaf_enum(node, libName, imported)">\
class ${node['label']}:
%for itemQName in node["items"]:
    <% item = CACHE[itemQName] %>\
    ${item['label']} = ${item['number']}
%endfor
</%def>


<%def name="pyuaf_struct(node, libName, imported)">\
class ${node['label']}(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
%for attrQName in node["attributes"]:
<% attr = CACHE[attrQName] %>\
${pyuaf_addAttribute(attr, libName, imported)}\
%endfor
</%def>

<%def name="pyuaf_fb(node, libName, imported)">\
<%
    if "var_in" in node:
    	var_in    = [ CACHE[v] for v in node["var_in"] ]
    else:
        var_in    = []
    endif
    if "var_out" in node:
        var_out   = [ CACHE[v] for v in node["var_out"] ]
    else:
        var_out   = []
    endif
    if "var_local" in node:
        var_local = [ CACHE[v] for v in node["var_local"] ]
    else:
        var_local = []
    endif
    #methods   = [ CACHE[m] for m in node["methods"] ]
%>\
% if "extends" not in node or node["extends"] is None:
class ${node['label']}(OpcUaNode):

    def __init__(self, parent, name, ns, info):
        OpcUaNode.__init__(self, parent, name, ns, info)
% else:
class ${node['label']}(${pyuaf_getQualifiedName(CACHE[node["extends"]], libName, imported)}):

    def __init__(self, parent, name, ns, info):
        ${pyuaf_getQualifiedName(CACHE[node["extends"]], libName, imported)}.__init__(self, parent, name, ns, info)
% endif
%for vars in [var_in, var_out, var_local]:
    %for var in vars:
${pyuaf_addAttribute(var, libName, imported)}\
    %endfor
%endfor

## just like the PLC development, we still have to create a superclass of the SM_... statemachines manually:
% if node['label'][:3] == 'SM_':
class ${node['label'][3:]}(${node['label']}):
    def __init__(self, parent, name, ns, info):
        ${node['label']}.__init__(self, parent, name, ns, info)
% endif
</%def>


<%def name="pyuaf_getQualifiedName(node, libName, imported)">\
<%
    # extract the library name:
    leftCharNumber = node['qname'].find(':')+1
    rightCharNumber = node['qname'].find('.', leftCharNumber)
    if rightCharNumber < 0:
        typeLibName = node['qname'][leftCharNumber:].lower()
    else:
        typeLibName = node['qname'][leftCharNumber:rightCharNumber].lower()
    if typeLibName != libName and typeLibName not in imported:
        imported.append(typeLibName)
%>\
% if typeLibName == libName:
${node['label']}\
% else:
${typeLibName}.${node['label']}\
% endif
</%def>

<%def name="pyuaf_getDataType(node, libName, imported)">\
<%
    conversion = {
        u'expr:t_string'    : 'ua.VariantType.String',
        u'expr:t_bool'      : 'ua.VariantType.Boolean',
        u'expr:t_uint8'     : 'ua.VariantType.Byte',
        u'expr:t_int8'      : 'ua.VariantType.SByte',
        u'expr:t_uint16'    : 'ua.VariantType.Int16',
        u'expr:t_int16'     : 'ua.VariantType.UInt16',
        u'expr:t_uint32'    : 'ua.VariantType.Int32',
        u'expr:t_int32'     : 'ua.VariantType.UInt32',
        u'expr:t_uint64'    : 'ua.VariantType.Int64',
        u'expr:t_int64'     : 'ua.VariantType.UInt64',
        u'expr:t_float'     : 'ua.VariantType.Float',
        u'expr:t_double'    : 'ua.VariantType.Double',
        u'iec61131:STRING'    : 'ua.VariantType.String',
        u'iec61131:BOOL'      : 'ua.VariantType.Boolean',
        u'iec61131:BYTE'     : 'ua.VariantType.Byte',
        u'iec61131:SINT'      : 'ua.VariantType.SByte',
        u'iec61131:INT'    : 'ua.VariantType.Int16',
        u'iec61131:WORD'     : 'ua.VariantType.UInt16',
        u'iec61131:UINT'     : 'ua.VariantType.UInt16',
        u'iec61131:DINT'    : 'ua.VariantType.Int32',
        u'iec61131:UDINT'     : 'ua.VariantType.UInt32',
        u'iec61131:DWORD'     : 'ua.VariantType.UInt32',
        u'iec61131:LINT'    : 'ua.VariantType.Int64',
        u'iec61131:ULINT'     : 'ua.VariantType.UInt64',
        u'iec61131:REAL'     : 'ua.VariantType.Float',
        u'iec61131:LREAL'    : 'ua.VariantType.Double'
    }
%>\
% if node['qname'] in conversion:
${conversion[node['qname']]}\
% else:
${pyuaf_getQualifiedName(node, libName, imported)}\
%endif
</%def>


<%def name="pyuaf_addAttribute(node, libName, imported)">\
% if 'type' in node and node['type'] is not None:
<% typeNode = CACHE[node['type']] %>\
    %if (typeNode["plc_symbol"] is not None) or (u'soft:Enumeration' in typeNode['classes']): ## check for trivial type
<%
    if 'qualifiers' in node:
        # activated = u'beckhoff:OPC_UA_ACTIVATE' in node['qualifiers']
        if u'beckhoff:OPC_UA_ACCESS_R' in node['qualifiers']:
            permissions = 'r'
        elif u'beckhoff:OPC_UA_ACCESS_W' in node['qualifiers']:
            permissions = 'w'
        elif u'beckhoff:OPC_UA_ACCESS_RW' in node['qualifiers']:
            permissions= 'rw'
        else:
            permissions = ''
    else:
        # activated = False
        permissions = ''
%>\
##        % if activated:
        self.__addVariable__("${node['label']}", ns, '${node['comment']}', datatype=${pyuaf_getDataType(typeNode, libName, imported)}, permissions='${permissions}')
##        % endif
    % else:
        self.__addInstance__("${node['label']}", ns, ${pyuaf_getQualifiedName(typeNode, libName, imported)}, '${node['comment']}')
    % endif
% endif
</%def>

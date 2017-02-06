
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
import opcuanode
import pyuaf
from opcuanode import OpcUaNode


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
import ${im | n}
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
    var_in    = [ CACHE[v] for v in node["var_in"] ]
    var_out   = [ CACHE[v] for v in node["var_out"] ]
    var_local = [ CACHE[v] for v in node["var_local"] ]
    #methods   = [ CACHE[m] for m in node["methods"] ]
%>\
% if node["extends"] is None:
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
        u'expr:t_string'    : 'pyuaf.util.primitives.String',
        u'expr:t_bool'      : 'pyuaf.util.primitives.Boolean',
        u'expr:t_uint8'     : 'pyuaf.util.primitives.Byte',
        u'expr:t_int8'      : 'pyuaf.util.primitives.SByte',
        u'expr:t_uint16'    : 'pyuaf.util.primitives.Int16',
        u'expr:t_int16'     : 'pyuaf.util.primitives.UInt16',
        u'expr:t_uint32'    : 'pyuaf.util.primitives.Int32',
        u'expr:t_int32'     : 'pyuaf.util.primitives.UInt32',
        u'expr:t_uint64'    : 'pyuaf.util.primitives.Int64',
        u'expr:t_int64'     : 'pyuaf.util.primitives.UInt64',
        u'expr:t_float'     : 'pyuaf.util.primitives.Float',
        u'expr:t_double'    : 'pyuaf.util.primitives.Double',
        u'iec61131:STRING'    : 'pyuaf.util.primitives.String',
        u'iec61131:BOOL'      : 'pyuaf.util.primitives.Boolean',
        u'iec61131:BYTE'     : 'pyuaf.util.primitives.Byte',
        u'iec61131:SINT'      : 'pyuaf.util.primitives.SByte',
        u'iec61131:INT'    : 'pyuaf.util.primitives.Int16',
        u'iec61131:WORD'     : 'pyuaf.util.primitives.UInt16',
        u'iec61131:UINT'     : 'pyuaf.util.primitives.UInt16',
        u'iec61131:DINT'    : 'pyuaf.util.primitives.Int32',
        u'iec61131:UDINT'     : 'pyuaf.util.primitives.UInt32',
        u'iec61131:DWORD'     : 'pyuaf.util.primitives.UInt32',
        u'iec61131:LINT'    : 'pyuaf.util.primitives.Int64',
        u'iec61131:ULINT'     : 'pyuaf.util.primitives.UInt64',
        u'iec61131:REAL'     : 'pyuaf.util.primitives.Float',
        u'iec61131:LREAL'    : 'pyuaf.util.primitives.Double'
    }
%>\
% if conversion.has_key(node['qname']):
${conversion[node['qname']]}\
% else:
${pyuaf_getQualifiedName(node, libName, imported)}\
%endif
</%def>


<%def name="pyuaf_addAttribute(node, libName, imported)">\
% if node['type'] is not None:
<% typeNode = CACHE[node['type']] %>\
    %if (typeNode["plc_symbol"] is not None) or (u'soft:Enumeration' in typeNode['classes']): ## check for trivial type
<%
    if node.has_key('qualifiers'):
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
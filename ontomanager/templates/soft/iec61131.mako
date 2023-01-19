
<%def name="render_implementation(node, scope, html=True, indent='', more='    ')">\
%if "expressions" in node:
${layoutExpressions(node["expressions"], scope, html=html, indent=indent)}\
%endif
</%def>


<%def name="layoutExpressions(expressions, scope, html=True, indent='', more='    ')">\
    %if isinstance(expressions, list):
        %for e in expressions:
            % if not loop.first:
${indent}\
            % endif
${layoutExpressions(CACHE[e], scope, html=html, indent=indent)};
        %endfor
    %else:
${layoutExpression(expressions, scope, html=html, indent=indent)}\
    %endif
</%def>


<%def name="layoutExpression(e, scope, html=True, indent='', more='    ')">\
    %if "soft:IfThen" in e["classes"]:
${layoutIfThen(e, scope, html=html, indent=indent)}\
    %elif "expr:BinaryOperation" in e["classes"]:
${layoutBinaryOperation(e, scope, html=html, indent=indent)}\
    %elif "expr:UnaryOperation" in e["classes"]:
${layoutUnaryOperation(e, scope, html=html, indent=indent)}\
    %elif "soft:Variable" in e["classes"]:
${layoutVariable(e, scope, html=html, indent=indent)}\
    %elif "iec61131:Method" in e["classes"]:
${layoutMethod(e, scope, html=html, indent=indent)}\
    %elif "expr:Primitive" in e["classes"]:
${render_value(e, scope, html=html, indent=indent)}\
    %elif "soft:Call" in e["classes"]:
${layoutCall(e, scope, html=html, indent=indent)}\
    %elif "soft:Implementation" in e["classes"]:
${render_implementation(e, scope, html=html, indent=indent)}\
    %else:
<%
    import pprint
    raise Exception("ERROR in layoutExpression(%s)\n\nFull node:\n%s" %(e['qname'], pprint.pformat(e)))
%>
    %endif
</%def>


<%def name="render_value(node, scope, html=True, indent='')">\
<%
    import pprint
    if "value" not in node:
        raise Exception("Error in render_value(%s): no 'value' key found!\n\nFull node:\n%s" %(node['qname'], pprint.pformat(node)))
    if node["value"] is None:
        raise Exception("Error in render_value(%s): value is None!\n\nFull node:\n%s" %(node['qname'], pprint.pformat(node)))
%>\
${node['value']}\
</%def>


<%!
    import pprint

    def getPrefixAndPath(cache, dest, scope = []):

        e = None

        scopeLine = [ item['qname'] for item in scope ]

        for head in scope:

            destQName = dest["qname"]

            if "soft:EnumerationItem" in dest["classes"]:
                return None, [ dest["item_of"], destQName ]


            if "extends" in head and "points_to_type" in dest:
                if head["extends"] == dest["points_to_type"] != None:
                    return "SUPER", []

            try:
                if "iec61131:FunctionBlock" in head['classes']:
                    ## only explicitely mention THIS^ if there can be confusion (i.e. when the scope is > 1)
                    if len(scope) > 1:
                        return "THIS^", getPathToSubVariable(cache, dest, head)
                    else:
                        return None, getPathToSubVariable(cache, dest, head)
                elif "iec61131:Method" in head['classes']:
                    ## within the scope of a IEC61131-3 Method, the method itself is reachable via the method name
                    if dest['qname'] == head['qname']:
                        return dest['label'], []
                    else:
                        return None, getPathToSubVariable(cache, dest, head)


            except EOFError as eof:
                e = eof



        if e is not None:
            raise e

    def getPathToSubVariable(cache, dest, head):

        destQName = dest["qname"]
        headQName = head["qname"]

        if 'soft:GlobalVariable' in dest['classes']:
            return [destQName]

        if destQName == headQName:
            return []

        if "member_of" not in dest:
            raise EOFError()

        memberOfQNames = dest["member_of"]

        p = None
        for memberOfQName in memberOfQNames:
            memberOf = cache[memberOfQName]
            try:
                p =  getPathToSubVariable(cache, memberOf, head) + [ destQName  ]
                break
            except EOFError as e:
                pass

        if p is not None:
            return p

        raise EOFError( "Destination %s was not found as a subvariable of %s" %(destQName,headQName)
                        + "\n\n"
                        + "Destination:\n"
                        + pprint.pformat(dest)
                        + "\n\n"
                        + "Head:\n"
                        + pprint.pformat(head))




%>



<%def name="render_path(dest, scope, html=True)">\
<% prefix, path = getPrefixAndPath(CACHE, dest, scope) %>\
    %if prefix is not None:
${prefix}\
        % if len(path) > 0:
.\
        % endif
    %endif
    %for qname in path:
        % if not loop.first:
.\
        % endif
        % if html:
<a href="browse?show;qname=${qname}">\
        % endif
${CACHE[qname]["label"]}\
        % if html:
</a>\
        % endif
    %endfor
</%def>


<%def name="layoutVariable(v,scope,html=True,indent='',more='    ')">\
${render_path(v, scope, html=html)}\
</%def>


<%def name="layoutMethod(m,scope,html=True,indent='',more='    ')">\
${render_path(m, scope, html=html)}\
</%def>

<%def name="render_assignment(ass, scope, html=True)">\
<%
    left  = CACHE[ass["left"]]
    right = CACHE[ass["right"]]
%>\
    % if html:
<a href="soft?show;qname=${left['qname']}">${left['label']}</a>\
    % else:
${left['label']}\
    % endif
 := ${layoutExpression(right, scope=scope, html=html)}\
</%def>


<%def name="layoutCall(node, scope, html=True, indent='', more='    ')">\
<%
    assignments = [ CACHE[a] for a in node["assignments"] ]
    calls = CACHE[node["calls"]]
%>\
% if "expr:UnaryOperation" in calls["classes"]:
${layoutUnaryOperation(calls, scope, html=html, indent=indent)}\
% else:
${render_path(calls, scope, html=html)}\
% endif
(\
    % if len(node["assignments"]) == 0:
)\
    % elif len(node["assignments"]) == 1:
 ${render_assignment(assignments[0], scope, html=html)} )\
    % else:

        % for assignment in assignments:
${indent+more}${render_assignment(assignment, scope, html=html)}\
            % if loop.last:
)\
            % else:
,
            % endif
        % endfor
    % endif
</%def>

<%def name="layoutIfThen(node, scope, html=True, indent='', more='    ')">\
<%
    IF   = CACHE[node["if"]]
    THEN = CACHE[node["then"]]
    if node["else"] is None:
        ELSE = None
    else:
        ELSE = CACHE[node["else"]]
%>\
IF ${layoutExpression(IF, scope, html=html)} THEN
${indent+more}${layoutExpressions(THEN, scope, html=html, indent=indent+more)}\
    %if ELSE is not None:
${indent}ELSE
${indent+more}${layoutExpressions(ELSE, scope, html=html, indent=indent+more)}\
    %endif
${indent}END_IF\
</%def>


<%def name="layoutBinaryOperation(node, scope, html=True, indent='', more='    ')">\
<%
    operator = CACHE[node["operator"]]
    left = CACHE[node["left"]]
    right = CACHE[node["right"]]

    useBracketsForLeft  = not (("soft:Variable" in left["classes"])  or ("expr:Primitive" in left["classes"]))
    useBracketsForRight = not (("soft:Variable" in right["classes"]) or ("expr:Primitive" in right["classes"]))

    if operator["plc_symbol"] is None:
        raise Exception("Unknown symbol in layoutBinaryOperation(%s) for operator %s" %(node['qname']), operator['qname'])
%>\
    %if operator["plc_symbol"] in [":="]:
${layoutExpression(left, scope, html=html)} ${operator["plc_symbol"]} ${layoutExpression(right, scope, html=html)}\
    %else:
        %if useBracketsForLeft:
(${layoutExpression(left, scope, html=html)})\
        %else:
${layoutExpression(left, scope, html=html)}\
        %endif
 ${operator["plc_symbol"]} \
        %if useBracketsForRight:
(${layoutExpression(right, scope, html=html)})\
        %else:
${layoutExpression(right, scope, html=html)}\
        %endif
    %endif
</%def>


<%def name="layoutUnaryOperation(node, scope, html=True, indent='', more='    ')">\
<%
    operator = CACHE[node["operator"]]
    operand  = CACHE[node["operand"]]

    if operator["plc_symbol"] is None:
        raise Exception("Unknown symbol in layoutUnaryOperation(%s) for operator %s" %(node['qname']), operator['qname'])
%>\
    %if operator["plc_symbol"] == '^':
${layoutExpression(operand, scope, html=html)}^\
    %else:
${operator["plc_symbol"]}(${layoutExpression(operand, scope, html=html)})\
    %endif
</%def>



<%def name="xml_project(node)">\
<%
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

%>\
<?xml version="1.0" encoding="utf-8"?>
<project xmlns="http://www.plcopen.org/xml/tc6_0200">
  <fileHeader companyName="Institute of Astronomy" productName="OntoManager" productVersion="0.0.1" creationDateTime="${timeNow}" />
  <contentHeader name="${node['label']}" modificationDateTime="${timeNow}">
    <coordinateInfo>
      <fbd>
        <scaling x="1" y="1" />
      </fbd>
      <ld>
        <scaling x="1" y="1" />
      </ld>
      <sfc>
        <scaling x="1" y="1" />
      </sfc>
    </coordinateInfo>
    <addData>
      <data name="http://www.3s-software.com/plcopenxml/projectinformation" handleUnknown="implementation">
        <ProjectInformation />
      </data>
    </addData>
  </contentHeader>
  <types>
    <dataTypes>
    % for enum in enums:
      ${xml_enum(enum, '      ')}
    % endfor
    % for struct in structs:
      ${xml_struct(struct, '      ')}
    % endfor
    </dataTypes>
    <pous>
    % for fb in fbs:
      ${xml_pou_functionBlock(fb, '      ')}
    % endfor
    </pous>
  </types>
  <instances>
    <configurations />
  </instances>
  <addData>
    <data name="http://www.3s-software.com/plcopenxml/projectstructure" handleUnknown="discard">
      <ProjectStructure>
        ${xml_folder(node, '        ')}
      </ProjectStructure>
    </data>
  </addData>
</project>\
</%def>



<%def name="xml_enum(node,indent='')">\
<dataType name="${node['label']}">
${indent}  <baseType>
${indent}    <enum>
${indent}      <values>
                 %for itemQName in node["items"]:
<% item = CACHE[itemQName] %>\
${indent}        <value name="${item['label']}" value="${item['number']}" />
                 %endfor
${indent}      </values>
${indent}    </enum>
${indent}  </baseType>
${indent}</dataType>\
</%def>

<%def name="xml_struct(node,indent='')">\
<dataType name="${node['label']}">
${indent}  <baseType>
${indent}    <struct>
             %for attrQName in node["attributes"]:
<% attr = CACHE[attrQName] %>\
${indent}      ${xml_variable(attr,indent+'      ')}
             %endfor
${indent}    </struct>
${indent}  </baseType>
${indent}</dataType>\
</%def>

<%def name="xml_pou_functionBlock(node, indent='')">\
<%
    label  = node['label']
    if "var_in" in node:
        var_in    = [ CACHE[v] for v in node["var_in"] ]
    else:
        var_in    = [ ]
    endif
    if "var_out" in node:
        var_out   = [ CACHE[v] for v in node["var_out"] ]
    else:
        var_out   = [ ]
    endif
    if "var_inout" in node:
        var_inout = [ CACHE[v] for v in node["var_inout"] ]
    else:
        var_inout = [ ]
    endif
    if "var_local" in node:
        var_local = [ CACHE[v] for v in node["var_local"] ]
    else:
        var_local = [ ]
    endif
    if "methods" in node:
        methods   = [ CACHE[m] for m in node["methods"] ]
    else:
        methods   = [ ]
    endif
    if node["extends"] is None:
        extends = None
    else:
        extends = CACHE[node["extends"]]
    if node["implementation"] is None:
        implementation = None
    else:
        implementation = CACHE[node["implementation"]]

%>\
<pou name="${label}" pouType="functionBlock">
${indent}  <interface>
${indent}    ${xml_variables("input" , var_in    , indent+'    ')}
${indent}    ${xml_variables("output", var_out   , indent+'    ')}
${indent}    ${xml_variables("inOut" , var_inout , indent+'    ')}
${indent}    ${xml_variables("local" , var_local , indent+'    ')}
% if extends is not None:
${indent}    ${xml_pou_extends(extends, indent+'    ')}
% endif
${indent}  </interface>
${indent}  <body>
${indent}    <ST>
% if implementation is not None:
${indent}      ${xml_implementation(implementation, [ node ], indent+'      ')}
% endif
${indent}    </ST>
${indent}  </body>
${indent}  <addData>
% if len(methods) > 0:
${indent}    ${xml_methods(methods, node, indent+'    ')}
% endif
${indent}  </addData>
${indent}</pou>\
</%def>

<%def name="xml_implementation(implementation, scope, indent='')">\
<xhtml xmlns="http://www.w3.org/1999/xhtml">${render_implementation(implementation, scope, False)}</xhtml>\
</%def>


<%def name="xml_pou_extends(node, indent='')">\
<addData>
${indent}  <data name="http://www.3s-software.com/plcopenxml/pouinheritance" handleUnknown="implementation">
${indent}    <Inheritance>
${indent}      <Extends>${node["label"]}</Extends>
${indent}    </Inheritance>
${indent}  </data>
${indent}</addData>\
</%def>

<%def name="xml_types(types,indent='')">\
<types>
${indent}  <dataTypes>
   % for t in types:
       % if (t["plc_enum"] is not None):
${indent}    ${xml_enum(t,indent+'    ')}
       % elif (t["plc_struct"] is not None):
${indent}    ${xml_struct(t,indent+'    ')}
       % endif
   % endfor
${indent}  </dataTypes>
${indent}  <pous>
   % for t in types:
       % if (t["fb"] is not None):
${indent}    ${xml_pou_functionBlock(t,indent+'    ')}
       % endif
   % endfor
${indent}  </pous>
${indent}</types>\
</%def>

<%def name="xml_variables(kind, variables,indent='')">\
<${kind}Vars>
           % for v in variables:
${indent}  ${xml_variable(v, indent+'  ')}
           % endfor
${indent}</${kind}Vars>\
</%def>

<%def name="xml_variable(node, indent='')">\
\
% if address not in node:
<variable name="${node["label"]}">
% else:
% if node["address"] is not None:
<variable name="${node["label"]}" address="${node["address"]}">
% else:
<variable name="${node["label"]}">
% endif
% endif
${indent}  ${xml_type(node)}
        % if initial_value in node and node["initial_value"] is not None:
${indent}  <initialValue><simpleValue value="${str(node['initial_value']).upper()}" /></initialValue>
        % endif
        % if qualifiers in node and node["qualifiers"] is not None:
${indent}  <addData>
${indent}    <data name="http://www.3s-software.com/plcopenxml/attributes" handleUnknown="implementation">
${indent}      <Attributes>
               % for qualifierQName in node["qualifiers"]:
<% qualifier = CACHE[qualifierQName] %>\
${indent}        <Attribute Name="${qualifier['plc_symbol']}" Value="${qualifier['value']}" />
               % endfor
${indent}      </Attributes>
${indent}    </data>
${indent}  </addData>
        % endif
        % if node["comment"] is not None:
${indent}  <documentation>
${indent}    <xhtml xmlns="http://www.w3.org/1999/xhtml">${node["comment"]}</xhtml>
${indent}  </documentation>
        % endif
${indent}</variable>\
</%def>


<%def name="xml_type(node)">\
<type>${xml_type_contents(node)}</type>\
</%def>


<%def name="xml_type_element(node)">\
  %if node["plc_symbol"] is not None:
##for some reason, STRING must be rendered lowercase, otherwise you cannot import the file in TwinCAT !!!
    % if node["plc_symbol"] == 'STRING':
<string />\
    % else:
<${node["plc_symbol"]} />\
    % endif
  %else:
<derived name="${node["label"]}" />\
  % endif
</%def>

<%def name="xml_type_contents(node)">\
    %if type in node and node["type"] is not None:
<% typeNode = CACHE[node['type']] %>\
${xml_type_element(typeNode)}\
    %elif points_to_type in node and node["points_to_type"] is not None:
<% typeNode = CACHE[node['points_to_type']] %>\
        %if typeNode["plc_symbol"] is not None:
<pointer><baseType>${xml_type_element(typeNode)}</baseType></pointer>\
        %else:
<pointer><baseType>${xml_type_element(typeNode)}</baseType></pointer>\
        %endif
    %endif
</%def>

<%def name="xml_return_type(node)">\
<returnType>${xml_type_element(node)}</returnType>\
</%def>

<%def name="xml_methods(methods, scope, indent='')">\
    %for method in methods:
        % if not loop.first:
${indent}\
        % endif
${xml_method(method, scope, indent)}\
        % if not loop.last:

        % endif
    %endfor
</%def>


<%def name="xml_method(node, owner, indent='')">\
<%
    label     = node['label']
    var_in    = [ CACHE[v] for v in node["var_in"] ]
    var_out   = [ CACHE[v] for v in node["var_out"] ]
    var_inout = [ CACHE[v] for v in node["var_inout"] ]
    var_local = [ CACHE[v] for v in node["var_local"] ]
    if node["returnType"] is None:
        returnType = None
    else:
        returnType = CACHE[node["returnType"]]
    if node["implementation"] is None:
        implementation = None
    else:
        implementation = CACHE[node["implementation"]]
%>\
<data name="http://www.3s-software.com/plcopenxml/method" handleUnknown="implementation">
${indent}  <Method name="${label}">
${indent}    <interface>
% if returnType is not None:
${indent}      ${xml_return_type(returnType)}
% endif
${indent}      ${xml_variables("input" , var_in     , indent+'      ')}
${indent}      ${xml_variables("output", var_out    , indent+'      ')}
${indent}      ${xml_variables("inOut" , var_inout  , indent+'      ')}
${indent}      ${xml_variables("local" , var_local  , indent+'      ')}
${indent}      <addData>
${indent}        <data name="http://www.3s-software.com/plcopenxml/attributes" handleUnknown="implementation">
${indent}          <Attributes>
##${indent}            <Attribute Name="object_name" Value="${label}" />
${indent}            <Attribute Name="TcRpcEnable" Value="1" />
${indent}          </Attributes>
${indent}        </data>
${indent}      </addData>
${indent}    </interface>
${indent}    <body>
${indent}      <ST>
% if implementation is not None:
${indent}        ${xml_implementation(implementation, [ node, owner ], indent+'        ')}
% endif
${indent}      </ST>
${indent}    </body>
${indent}  </Method>
${indent}</data>\
</%def>


<%def name="xml_object(obj, indent='')">\
<Object Name="${obj['label']}">
    % if 'iec61131:FunctionBlock' in obj['classes']:
        % if 'methods' in obj:
            % for methodQName in obj['methods']:
<% method = CACHE[methodQName] %>\
${indent}  <Object Name="${method['label']}" />
            % endfor
        % endif
    % endif
${indent}</Object>\
</%def>

<%def name="xml_folder(node, indent='')">\
<%
    fbs      = [ CACHE[qname] for qname in node['FBs'] ]
    structs  = [ CACHE[qname] for qname in node['STRUCTs'] ]
    enums    = [ CACHE[qname] for qname in node['ENUMs'] ]
    types    = fbs + structs + enums
    children = [ CACHE[qname] for qname in node['namespaces'] ]
%>\
<Folder Name="${node['label']}">
  % for child in children:
${indent}  ${xml_folder(child, indent+'  ')}
  % endfor
  % for type in types:
${indent}  ${xml_object(type, indent+'  ')}
  % endfor
${indent}</Folder>\
</%def>

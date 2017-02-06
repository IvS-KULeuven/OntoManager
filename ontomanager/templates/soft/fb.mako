<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>
<%namespace name="util" file="util.mako"/>
<%namespace name="impl" file="implementation.mako"/>


<%
    TRIANGLE = "&#9655;"

    qname           = U["soft"]["show"]["qname"]
    node            = CACHE[qname]
    label           = node["label"]

    if node["extends"] is None:
        extends = None
    else:
        extends = CACHE[node["extends"]]

    inArgs          = [ CACHE[v] for v in node["var_in"] ]
    inCount         = len(inArgs)
    inOutArgs       = [ CACHE[v] for v in node["var_inout"] ]
    inOutCount      = len(inOutArgs)
    outArgs         = [ CACHE[v] for v in node["var_out"] ]
    outCount        = len(outArgs)
    localArgs       = [ CACHE[v] for v in node["var_local"] ]
    localCount      = len(localArgs)
    methods         = [ CACHE[m] for m in node["methods"] ]

    if node["implementation"] is None:
        implementation = None
    else:
        implementation = CACHE[node["implementation"]]

%>

<h1>FunctionBlock ${misc.render_view_link(node, "title")}</h1>


########################################################################################################################
## Jump to
########################################################################################################################

<div class="jump-to">
Jump to:
<ul>
    <li><a href="">Variables</a></li>
    <li><a href="">Methods</a></li>
    <li><a href="">Implementation</a></li>
    <li><a href="">PLCopen XML serialization</a></li>
</ul>
</div>

########################################################################################################################
## Function block visualization
########################################################################################################################

<link rel="stylesheet" href="${request.static_url('ontomanager:templates/soft/functionblock.css')}" />

<table class="functionblock">
    <tr>
        <td></td>
        <th colspan="2" class="functionblock">${misc.render_view_link(node, "visu")}<br /></th>
        <td></td>
        <td></td>
    </tr>
    % if extends is not None:
    <tr>
        <td></td>
        <td colspan="2" class="functionblock-extends">EXTENDS ${misc.render_view_link(extends, "visu")}</td>
        <td></td>
    </tr>
    % endif
    % for i in xrange(max(inCount + inOutCount, outCount + localCount) ):
    <tr>
        ## left side
        % if i < inCount:
            <td><div class="functionblock-bar"></div></td>
            <td class="functionblock-input">${misc.render_view_link(inArgs[i], "visu")}</td>
        % elif i < inCount + inOutCount:
            <td><div class="functionblock-bar"></div></td>
            <td class="functionblock-input">${misc.render_view_link(inOutArgs[i-inCount], "visu")} ${TRIANGLE | n}</td>
        % else:
            <td></td>
            <td class="functionblock-input"></td>
        % endif
        ## right side
        % if i < outCount:
            <td class="functionblock-output">${misc.render_view_link(outArgs[i], "visu")}</td>
            <td><div class="functionblock-bar"></div></td>
        % elif i < outCount + localCount:
            % if localCount == 1:
              <td class="functionblock-local single">
            % elif i == outCount:
              <td class="functionblock-local first">
            % elif i == outCount + localCount - 1:
              <td class="functionblock-local last">
            % else:
              <td class="functionblock-local">
            % endif
                ${misc.render_view_link(localArgs[i-outCount], "visu")}
              </td>
            <td><div class="functionblock-bar-small"></div></td>
        % else:
            <td class="functionblock-output"></td>
            <td class="functionblock"></td>
        % endif
        <td></td>
    </tr>
    % endfor
    % for method in methods:
    <tr>
        <td></td>
        <td class="functionblock-method" colspan="2">${render_method_signature(method, "visu")}</td></td>
        <td><div class="functionblock-bar"></div></td>
        <td><div class="functionblock-half-circle"></div></td>
    </tr>
    % endfor
    <tr>
        <td></td>
        <td colspan="2" class="functionblock-below"></td>
        <td></td>
        <td></td>
    </tr>
</table>

########################################################################################################################
## Variables table
########################################################################################################################

<h5 class="extraspace">Variables</h5>
<table class="gridtable">
${util.render_variables(inArgs, inOutArgs, outArgs, localArgs, firstColumn=None, id="vartable")}
</table>


<%def name="render_method_signature(method, id)">\
<% varIn = [ CACHE[qname] for qname in method["var_in"] ] %>\
${misc.render_view_link(method, id)}(\
        % for v in varIn:
${misc.render_view_link(v, id)}\
            % if not loop.last:
, \
            % endif
        % endfor
)\
</%def>


########################################################################################################################
## Methods
########################################################################################################################
<h5 class="extraspace">Methods</h5>

% for method in methods:
    <%
        method_in       = [ CACHE[v] for v in method["var_in"] ]
        method_inout    = [ CACHE[v] for v in method["var_inout"] ]
        method_out      = [ CACHE[v] for v in method["var_out"] ]
        method_local    = [ CACHE[v] for v in method["var_local"] ]
        if node["implementation"] is None:
            method_imp = None
        else:
            method_imp = CACHE[method["implementation"]]
    %>
    <ul>
        <li>
            <h3>${render_method_signature(method, "methodtable")}</h3>
            <table class="gridtable align-left">
                <tr>
                    <!-- Comment -->
                    <th>Comment</th>
                    % if method["comment"] is None:
                        <td colspan="7"></td>
                    % else:
                        <td colspan="7">${method["comment"]}</td>
                    % endif
                </tr>
                <tr>
                    <!-- Return type -->
                    <th>Return type</th>
                    % if method["returnType"] is None:
                        <td colspan="7"></td>
                    % else:
                        <% method_returnType = CACHE[method["returnType"]] %>
                        <td colspan="7">${misc.render_view_link(method_returnType, "methodTable")}</td>
                    % endif
                </tr>
                    ${util.render_variables(method_in, method_inout, method_out, method_local, firstColumn="Interface", id="methodTable")}
                <tr>
                    <!-- Implementation -->
                    <th>Implementation</th>
                    % if method["implementation"] is None:
                        <td colspan="7"></td>
                    % else:
                        <td colspan="7">
                            <pre>${iec61131.render_implementation(method_imp, [method, node])}</pre>
                        </td>
                    % endif
                </tr>
            </table>
            <br>
        </li>
    </ul>
% endfor

########################################################################################################################
## Implementation
########################################################################################################################

<h5>Implementation</h5>
    % if implementation is not None:
        <table class="gridtable">
            <tr>
                <td>
                    <pre>${iec61131.render_implementation(implementation, [ node ] )}</pre>
                </td>
            </tr>
        </table>
    % endif



########################################################################################################################
## PLCopen XML
########################################################################################################################

<h5 class="extraspace">PLCopen XML serialization</h5>
<div id="hidden"><xmp id="xmlcontent">${iec61131.xml_pou_functionBlock(node)}</xmp></div>

${misc.render_xml_editor()}



${misc.render_debug(node)}

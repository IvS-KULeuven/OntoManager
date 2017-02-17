<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    moduleType = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>I/O Module type ${misc.render_view_link(moduleType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

${elec_misc.render_device_type_summary(moduleType)}

<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(moduleType)}


<!-- =============================================== INTERFACE =======================================================  -->


<h3>Interface</h3>

% if moduleType['interface'] is not None:

    <%
        interface = CACHE[moduleType['interface']]
        variables = [ CACHE[variableQName] for variableQName in interface['variables'] ]
    %>

    <table class="gridtable">
        <tr>
            <th>Variable</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
        % for variable in variables:
            <tr>
                <td>${misc.render_view_link(variable)}</td>
                ## type
                % if variable["type"] is not None:
                    <%
                        typeNode = CACHE[variable["type"]]
                        try:
                            typeName = typeNode["plc_symbol"]
                            if typeName is None: raise Exception()
                        except:
                            typeName = typeNode["label"]
                    %>
                    <td>${misc.render_view_link(CACHE[variable["type"]], id='${variable["label"]}_type', contents=typeName)}</td>
                % elif variable["points_to_type"] is not None:
                    <%
                        typeNode = CACHE[variable["points_to_type"]]
                        try:
                            typeName = typeNode["plc_symbol"]
                            if typeName is None: raise Exception()
                        except:
                            typeName = typeNode["label"]
                    %>
                    <td>POINTER TO ${misc.render_view_link(CACHE[variable["points_to_type"]], contents=typeName)}</td>
                % else:
                    <td></td>
                % endif
                <td>${variable['comment']}</td>
            </tr>
        % endfor
    </table>
% endif

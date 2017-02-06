<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>
<%namespace name="elec_CableType" file="CableType.mako"/>
<%namespace name="elec_CableInstance" file="CableInstance.mako"/>
<%namespace name="elec_ConnectorInstance" file="ConnectorInstance.mako"/>
<%namespace name="elec_ConnectorType" file="ConnectorType.mako"/>

<%
    cableAssemblyType = CACHE[U["elec"]["show"]["qname"]]
%>




<h1>Cable assembly type ${misc.render_view_link(cableAssemblyType, "title")}</h1>

${misc.render_comment_below_title(cableAssemblyType)}
<!-- ============================================== SUMMARY =======================================================  -->

<h2>Summary</h2>


<%def name="render_summary(node, anchors=True)">
    <%
        manufacturer = CACHE[node['manufacturer']]
    %>

    <table class="lefttable">
        <tr>
            <th>ID</th>
            <td>${misc.render_view_link(node, id="summary_id", contents=node['id'])}</td>
        </tr>
        <tr>
            <th>Manufacturer</th>
            <td>${misc.render_view_link(manufacturer, id="summary_manufacturer", contents=manufacturer['long_name'])}</td>
        </tr>
        <tr>
            <th>Description</th>
            <td>${node['comment']}</td>
        </tr>
        <tr>
            <th>Used in</th>
            <td>${elec_misc.render_owning_configurations(node)}</td>
        </tr>
        <tr>
            <th>Cables</th>
            <td>
                <ul>
                    % for cableQName in node['cables']:
                        <%
                            cable = CACHE[cableQName]
                            cableType = CACHE[cable['man_type']]
                        %>
                        <li>
                            % if anchors:
                                <a href="#${cable['label']}">\
                            % endif
                            ${cable['label']}
                            % if anchors:
                                </a>\
                            % endif
                            (${misc.render_view_link(cableType, id="summary_id", contents=cableType['id'])})</li>
                    % endfor
                </ul>
            </td>
        </tr>
        <tr>
            <th>Connectors</th>
            <td>
                <ul>
                    % for connectorQName in node['connectors']:
                        <%
                            connector = CACHE[connectorQName]
                            connectorType = CACHE[connector['man_type']]
                        %>
                        <li>
                            % if anchors:
                                <a href="#${connector['label']}">\
                            % endif
                            ${connector['label']}
                            % if anchors:
                                </a>\
                            % endif
                            (${misc.render_view_link(connectorType, id="summary_id", contents=connectorType['id'])})</li>
                    % endfor
                </ul>
            </td>
        </tr>
    </table>
</%def>

${render_summary(cableAssemblyType)}


<h2>Cables</h2>

<%def name="render_cables(cableAssemblyType, anchors=True)">

    <ul>
    % for cableQName in cableAssemblyType['cables']:
        <%
            cable = CACHE[cableQName]
            cableType = CACHE[cable['man_type']]
        %>
        <li> <h3><a name="${cable['label']}"></a>${cable['label']}</h3>
        ${misc.render_comment_below_title(cable)}
        ${elec_CableType.render_summary(cableType)}
        ${elec_CableInstance.render_cable(cable, cableType)}
        </li>
    % endfor
    </ul>
</%def>

${render_cables(cableAssemblyType)}


<h2>Connectors</h2>

<%def name="render_connectors(cableAssemblyType, anchors=True)">


<ul>

% for connectorQName in cableAssemblyType['connectors']:

    <%
        connector = CACHE[connectorQName]
        connectorType = CACHE[connector['man_type']]
    %>
    <li> <h3><a name="${connector['label']}"></a>${connector['label']}</h3>
    ${misc.render_comment_below_title(connector)}
    ${elec_ConnectorType.render_summary(connectorType)}
    ${elec_ConnectorInstance.render_ConnectorInstance(connector, connectorType)}

% endfor
</ul>
</%def>
${render_connectors(cableAssemblyType)}
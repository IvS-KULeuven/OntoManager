<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>
<%namespace name="ConnectorType" file="ConnectorType.mako"/>

<%
    connector = CACHE[U["elec"]["show"]["qname"]]
    connectorType = CACHE[connector["man_type"]]
%>


<h1>Connector instance ${misc.render_view_link(connector, "title")}</h1>

${misc.render_comment_below_title(connector)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Connector type summary</h5>

${ConnectorType.render_summary(connectorType)}


<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>


<%def name="render_ConnectorInstance(connector, connectorType)">
    <table class="gridtable">
        <tr>
            <th colspan="3">Type (${misc.render_view_link(connectorType, id="connections_type_id", contents=connectorType['id'])})</th>
            <th colspan="3">Instance</th>
        </tr>
        <tr>
            <th>Pin</th>
            <th>Symbol</th>
            <th>Description</th>
            <th>Symbol</th>
            <th>Description</th>
            <th>Connected to</th>
        </tr>
            <%
                pins = [ CACHE[pinQName] for pinQName in connectorType['pins'] ]
            %>
            % for pin in pins:
                <%
                    for instanceQName in connector["pins"]:
                        instance = CACHE[instanceQName]
                        if instance['realizes'] == pin['qname']:
                            break
                    else:
                        raise Exception("Pin %s doesn't have a matching pin instance of connector %s" %(pin['qname'], connector['qname']))
                %>
                <tr>
                    <td>${pin['label']}</td>
                    <td>${pin['symbol']}</td>
                    <td>${pin['comment']}</td>
                    % if instance['symbol'] is None:
                    <td></td>
                    % else:
                    <td>${instance['symbol']}</td>
                    % endif
                    <td>${instance['comment']}</td>
                    <td>
                        ${elec_misc.render_connections(instance, connector['wires'])}
                    </td>
                </tr>
            % endfor

    </table>

</%def>

${render_ConnectorInstance(connector, connectorType)}


<%def name="render_connectors(connectors)">
    <ul>
    % for connectorQName in connectors:
        <%
            connector = CACHE[connectorQName]
            connectorType = CACHE[connector['realizes']]
        %>
        <li> <h3>${connector['label']}</h3>
        ${misc.render_comment_below_title(connector)}
        ${ConnectorType.render_summary(connectorType)}
        ${render_ConnectorInstance(connector, connectorType)}
        </li>
    % endfor
    </ul>
</%def>
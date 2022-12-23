<%namespace name="misc" file="../misc.mako"/>


<%def name="render_pin_or_terminal(node)">\
<%
    kind = ''
    label = ''
    symbol = ''
    ownerNode = None
    ownerKind = ''
    ownerLabel = ''
    # if the node is a realization, fill the label and symbol (if present) and substitute the node for the realized node
    if 'elec:Pin' in node['classes']:
        kind = "pin"
    elif 'elec:Terminal' in node['classes']:
        kind = 'terminal'
    elif 'elec:Wire' in node['classes']:
        kind = 'wire'
    else:
        kind = '???'

    if 'label' in node: label = node['label']
    if 'symbol' in node: symbol = node['symbol']
    if node['owner'] is not None:
        ownerNode = CACHE[node['owner']]

    # now get some info about the owner node
    if ownerNode is not None:
        ownerLabel = ownerNode['label']
        if 'elec:Connector' in ownerNode['classes'] or 'elec:ConnectorInstance' in ownerNode['classes']:
            ownerKind = 'Connector'
        elif 'elec:IoModule' in ownerNode['classes']:
            ownerKind = 'I/O module'
        elif 'elec:Drive' in ownerNode['classes']:
            ownerKind = 'Drive'
        elif 'elec:Actuator' in ownerNode['classes']:
            ownerKind = 'Actuator'
        elif 'elec:Sensor' in ownerNode['classes']:
            ownerKind = 'Sensor'
        elif 'elec:PowerSupply' in ownerNode['classes']:
            ownerKind = 'PowerSupply'
        elif 'elec:Switch' in ownerNode['classes']:
            ownerKind = 'Switch'
        elif 'elec:CircuitBreaker' in ownerNode['classes']:
            ownerKind = 'Circuit breaker'
        elif 'elec:Device' in ownerNode['classes']:
            ownerKind = 'Device'
        elif 'elec:Configuration' in ownerNode['classes']:
            ownerKind = 'Configuration'
        else:
            ownerKind = ''

    pinContents = label
    if symbol != '' and symbol != label and symbol is not None:
        pinContents += ' (' + symbol + ')'

%>
% if ownerNode is not None:
${ownerKind} ${misc.render_view_link(ownerNode, id='pin_or_terminal_${ownerNode["qname"]}', contents=ownerLabel)} : \
% endif
${kind} ${misc.render_view_link(node, id='pin_or_terminal_${node["qname"]}', contents=pinContents)}\
</%def>


<%def name="render_connections(pinNode, wires)">\
<%
    connections = [ CACHE[connectionQName] for connectionQName in pinNode['connections'] ]
%>
% if len(connections) == 1:
    ${render_connection(pinNode, connections[0], wires)}
% else:
    <ul>
    % for connection in connections:
        <li>${render_connection(pinNode, connection, wires)}</li>
    % endfor
    </ul>
% endif
</%def>


<%def name="render_connection(pinNode, connectionNode, wires)">\
 <%
    colors = []
    for wireQName in wires:
        wire = CACHE[wireQName]
        if wire['connectsFrom'] == pinNode['qname']:
            colors = wire['colors']
            break
%>
${misc.render_colorbox(colors)} ${render_pin_or_terminal(connectionNode)}
</%def>


<%def name="render_direct_connections(node)">\
<%
    directConnections = []
    for connectionQName in node['connections']:
        directConnections.append( CACHE[connectionQName] )
%>
  % if len(directConnections) >= 0:
      ${render_connections(node,[])}
  % else:
<ul>
      <li>(no direct connections)</li>
</ul>
  % endif
</%def>


<%def name="render_indirect_connections(node)">\
<%
    indirectConnections = []
    for connectionQName in node['all_connections']:
        if not ( (connectionQName in node['connections']) or (connectionQName == node['qname']) ):
            indirectConnections.append( CACHE[connectionQName] )
%>
<ul>
  % if len(indirectConnections) > 0:
      % for connection in indirectConnections:
        <li>${render_pin_or_terminal(connection)}</li>
      % endfor
  % else:
      <li>(no indirect connections)</li>
  % endif
</ul>
</%def>


<%def name="render_terminal_info_or_from_connection(node, key, connections)">\
    % if node[key] is not None and node[key] != '':
        ${node[key]}
    % elif len(connections) > 0:
        % if connections[0][key] is not None:
            % if connections[0]['owner'] is not None:
                <% ownerNode = CACHE[connections[0]['owner']] %>
                ${misc.render_view_link(ownerNode, contents=connections[0][key])}
            % else:
                ${connections[0][key]}
            % endif
        % endif
    % endif
</%def>



<%def name="render_terminals_table(node, typeNode)">\
<table class="gridtable">
    <tr>
        <th colspan="4">Type (${misc.render_view_link(typeNode, id="connections_type_id", contents=typeNode['id'])})</th>
        <th colspan="3">Instance</th>
    </tr>
    <tr>
        <th>Channel</th>
        <th>Terminal</th>
        <th>Symbol</th>
        <th>Description</th>
        <th>Symbol</th>
        <th>Description</th>
        <th>Connected to</th>
    </tr>
    <%
        channels       = [ CACHE[channelQName] for channelQName in typeNode['channels'] ]
        allTerminals   = [ CACHE[terminalQName] for terminalQName in typeNode['terminals'] ]
        shownTerminalQNames = []
    %>
    % for channel in channels:
        <%
            terminals = [ CACHE[terminalQName] for terminalQName in channel['terminals'] ]
            shownTerminalQNames += channel['terminals']
        %>
        % for terminal in terminals:
            <%
                for instanceQName in node["terminals"]:
                    instance = CACHE[instanceQName]
                    if instance['realizes'] == terminal['qname']:
                        break
                else:
                    raise Exception("Terminal %s doesn't have a matching instance" %terminal['qname'])
                connections = [  CACHE[connectionQName] for connectionQName in instance['connections'] ]
            %>
            <tr>
                % if loop.first:
                    <td rowspan="${len(terminals)}">${channel['label']}</td>
                % endif
                <td>${terminal['label']}</td>
                <td>${terminal['symbol']}</td>
                <td>${terminal['comment']}</td>
                <td>${render_terminal_info_or_from_connection(instance, 'symbol', connections)}</td>
                <td>${render_terminal_info_or_from_connection(instance, 'comment', connections)}</td>
                <td>
${render_connections(instance, node['wires'])}
                </td>
            </tr>
        % endfor
    % endfor
    ## also add the remaining terminals
    <% grayColumnWritten = False %>\
    % for remainingTerminal in allTerminals:
        % if not remainingTerminal['qname'] in shownTerminalQNames:
            <%
                for instanceQName in node["terminals"]:
                    instance = CACHE[instanceQName]
                    if instance['realizes'] == remainingTerminal['qname']:
                        break
                else:
                    raise Exception("Terminal %s doesn't have a matching instance" %remainingTerminal['qname'])
                connections = [  CACHE[connectionQName] for connectionQName in instance['connections'] ]
            %>
            <tr>
                % if not grayColumnWritten:
                <th rowspan="${len(allTerminals) - len(shownTerminalQNames)}"></th>
                <% grayColumnWritten = True %>\
                % endif
                <td>${remainingTerminal['label']}</td>
                <td>${remainingTerminal['symbol']}</td>
                <td>${remainingTerminal['comment']}</td>


                <td>${render_terminal_info_or_from_connection(instance, 'symbol', connections)}</td>
                <td>${render_terminal_info_or_from_connection(instance, 'comment', connections)}</td>

                <td>
${render_connections(instance, node['wires'])}
                </td>
            </tr>
        % endif
    % endfor

</table>
</%def>







<%def name="render_interface_table(instanceQName, typeQName)">\

    <%
        if instanceQName is None:
            instanceNode = None
        else:
            instanceNode = CACHE[instanceQName]

        if typeQName is None:
            typeNode = None
        else:
            typeNode = CACHE[typeQName]
    %>


    <table class="gridtable">

        <tr>
##            <th colspan="3">I/O Module</th>
##            <th colspan="2">Linked variable</th>
        </tr>

        <tr>
            <th>Variable</th>
            <th>Type</th>
            <th>Description</th>
            <th>Linked variable</th>
##            <th>Description</th>
        </tr>


        % if typeNode is not None:

            <%
                variables = [ CACHE[variableQName] for variableQName in typeNode['variables'] ]
            %>

            % for variable in variables:

                <%
                    links = []
                    for vQName in instanceNode['variables']:
                        vNode = CACHE[vQName]
                        if variable['qname'] in vNode['realizes']:
                            links = vNode['links']
                    if len(links) > 1:
                        noOfRows = len(links)
                    else:
                        noOfRows = 1
                %>


                <tr>
                    <td rowspan="${noOfRows}">${misc.render_view_link(variable)}</td>
                    ## variable type
                    % if variable["type"] is not None:
                        <%
                            varTypeNode = CACHE[variable["type"]]
                            try:
                                varTypeName = varTypeNode["plc_symbol"]
                                if varTypeName is None: raise Exception()
                            except:
                                varTypeName = varTypeNode["label"]
                        %>
                        <td rowspan="${noOfRows}">${misc.render_view_link(CACHE[variable["type"]], id='${variable["label"]}_type', contents=varTypeName)}</td>
                    % elif variable["points_to_type"] is not None:
                        <%
                            varTypeNode = CACHE[variable["points_to_type"]]
                            try:
                                varTypeName = varTypeNode["plc_symbol"]
                                if varTypeName is None: raise Exception()
                            except:
                                varTypeName = varTypeNode["label"]
                        %>
                        <td rowspan="${noOfRows}">POINTER TO ${misc.render_view_link(CACHE[variable["points_to_type"]], contents=varTypeName)}</td>
                    % else:
                        <td rowspan="${noOfRows}"></td>
                    % endif
                    <td rowspan="${noOfRows}">${variable['comment']}</td>

                    % for linkQName in links:
                        <%
                            linkNode = CACHE[linkQName]
                        %>
                        <td>${render_interface_link(linkNode)}</td>
##                        <td>${linkNode['comment']}</td>
                    % endfor

                    % if len(links) == 0:
                        <th colspan="2"></th>
                    % endif
                </tr>
            % endfor


        % endif
    </table>

</%def>



<%def name="render_interface_link(node)">\
<%
    try:
        typeNode = CACHE[node["type"]]
    except:
        typeNode = None
    try:
        pointToTypeNode = CACHE[node["points_to_type"]]
    except:
        pointToTypeNode = None

%>\
% if 'member_of' in node:
   % if node['member_of'] is not None:
       % if len(node['member_of']) > 0:
${render_interface_link(CACHE[node['member_of'][0]])}.\
       % endif
   % endif
% endif
% if typeNode is not None:
<%
    try:
        typeName = typeNode["plc_symbol"]
        if typeName is None: raise Exception()
    except:
        typeName = typeNode["label"]
%>\
${misc.render_view_link(typeNode, id='${node["label"]}_type', contents=node["label"])}\
% elif pointToTypeNode is not None:
<%
    try:
        typeName = pointToTypeNode["plc_symbol"]
        if typeName is None: raise Exception()
    except:
        typeName = pointToTypeNode["label"]
%>\
${misc.render_view_link(pointToTypeNode, contents=node["label"])}\
% else:
${node['label']}\
% endif
</%def>


<%def name="render_owning_configurations(node)">\
<%
    configs = [ CACHE[configQName] for configQName in node['owning_configurations'] ]
%>
% for config in configs:
    % if loop.index > 0:
, \
    % endif
${misc.render_view_link(config)} (${node['owning_configurations_counts'][loop.index]})\
% endfor
</%def>



<%def name="render_device_type_summary(node)">
    <%
        manufacturer = CACHE[node['manufacturer']]
        imgUrl = request.static_url("ontomanager:static/models/external/%s/%s.png" %(manufacturer['short_name'],node['qname'].split(':')[1]))
    %>
<style>
IMG.MaxSized
{
max-width: 1000px;
max-height: 1000px;
}
</style>

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
            <td>${render_owning_configurations(node)}</td>
        </tr>
        % if "cables" in node:
            % if len(node['cables']) > 0:
                <tr>
                    <th>Cables</th>
                    <td>
                        <ul>
                        % for cableQName in node['cables']:
                            <%
                                cable     = CACHE[cableQName]
                                cableType = CACHE[cable['man_type']]
                            %>
                            <li>${misc.render_view_link(cable, id="summary_cable")} (${misc.render_view_link(cableType, id="summary_cabletype")})</li>
                        % endfor
                        </ul>
                    </td>
                </tr>
            % endif
        % endif
        % if "connectors" in node:
            % if len(node['connectors']) > 0:
                <tr>
                    <th>Connectors</th>
                    <td>
                        <ul>
                        % for connectorQName in node['connectors']:
                            <%
                                connector     = CACHE[connectorQName]
                                connectorType = CACHE[connector['man_type']]
                            %>
                            <li>${misc.render_view_link(connector, id="summary_connector")} (${misc.render_view_link(connectorType, id="summary_connectortype", contents=connectorType['id'])})</li>
                        % endfor
                        </ul>
                    </td>
                </tr>
            % endif
        % endif
    </table>
    <a href="${imgUrl}"><img src='${imgUrl}' class="MaxSized"/></a>
</%def>


<%def name="render_device_type_layout(node)">
    <table class="gridtable">
        <tr>
            <th>Channel</th>
            <th>Terminal</th>
            <th>Symbol</th>
            <th>Description</th>
        </tr>
        <%
            channels       = [ CACHE[channelQName] for channelQName in node['channels'] ]
            allTerminals   = [ CACHE[terminalQName] for terminalQName in node['terminals'] ]
            shownTerminalQNames = []
        %>
        % for channel in channels:
            <%
                terminals = [ CACHE[terminalQName] for terminalQName in channel['terminals'] ]
                shownTerminalQNames += channel['terminals']
            %>
            % for terminal in terminals:
                <tr>
                    % if loop.first:
                        <td rowspan="${len(terminals)}">${channel['label']}</td>
                    % endif
                    <td>${terminal['label']}</td>
                    <td>${terminal['symbol']}</td>
                    <td>${terminal['comment']}</td>
                </tr>
            % endfor
        % endfor
        ## also add the remaining terminals
        <% grayColumnWritten = False %>\
        % for remainingTerminal in allTerminals:
            % if not remainingTerminal['qname'] in shownTerminalQNames:
                <tr>
                    % if not grayColumnWritten:
                    <th rowspan="${len(allTerminals) - len(shownTerminalQNames)}"></th>
                    <% grayColumnWritten = True %>\
                    % endif
                    <td>${remainingTerminal['label']}</td>
                    <td>${remainingTerminal['symbol']}</td>
                    <td>${remainingTerminal['comment']}</td>
                </tr>
            % endif
        % endfor

    </table>
</%def>


<%def name="render_summary(title, items, shown=[])">
    <%
        for item in items:
            shown.append(item)
    %>

    % if len(items) > 0:
        <h3>${title} (${len(items)})</h3>

        <table class="gridtable">

            <tr>
                <th>ID</th>
                <th>Manufacturer</th>
                <th>Type</th>
                <th>Type comment</th>
                <th>Instance comment</th>
            </tr>

            % for qname in items:

                 <%
                     instance = CACHE[qname]
                     realizes = CACHE[instance['man_type']]
                     if 'manufacturer' in realizes:
                        manufacturer = CACHE[realizes['manufacturer']]
                     else:
                        manufacturer = None
                 %>

                <tr>
                    <td>${misc.render_view_link(instance, "io_id")}</td>
                    % if manufacturer is None:
                        <td></td>
                    % else:
                        <td>${misc.render_view_link(manufacturer, "io_man", contents=manufacturer['long_name'])}</td>
                    % endif
                    % if id in realizes:
                        <td>${misc.render_view_link(realizes, "io_type_id", contents=realizes['id'])}
                    % else:
                        <td>${misc.render_view_link(realizes, "io_type_id")}
                    % endif
                    <td>${realizes['comment']}</td>
                    <td>${instance['comment']}</td>
                </tr>

            % endfor

        </table>
    % endif
</%def>

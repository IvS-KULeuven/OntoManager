<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>
<%namespace name="CableType" file="CableType.mako"/>

<%
    cable = CACHE[U["elec"]["show"]["qname"]]

    cableType = CACHE[cable["man_type"]]
%>


<h1>Cable instance ${misc.render_view_link(cable, "title", contents=cable['symbol'])}</h1>

${misc.render_comment_below_title(cable)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Cable type summary</h5>

${CableType.render_summary(cableType)}


<!-- ============================================ WIRES =====================================================  -->

<h5>Wires</h5>



<%def name="render_cable(cable, cableType)">

    <table class="gridtable">
        <tr>
            <th colspan="3">Type (${misc.render_view_link(cableType, id="wires_type_id", contents=cableType['id'])})</th>
            <th colspan="3">Instance</th>
        </tr>
        <tr>
            <th>Wire</th>
            <th>Color(s)</th>
            <th>Description</th>
            <th>Connects from</th>
            <th>Connects to</th>
            <th>Description</th>
        </tr>
            <%
                wires = [ CACHE[wireQName] for wireQName in cableType['wires'] ]
            %>
            % for wire in wires:
                <%
                    for instanceQName in cable["wires"]:
                        instance = CACHE[instanceQName]
                        if instance['realizes'] == wire['qname']:
                            break
                    else:
                        raise Exception("Wire %s doesn't have a matching wire instance of cable %s" %(wire['qname'], wire['qname']))
                    try:
                        connectsFrom = CACHE[instance['connectsFrom']]
                    except:
                        connectsFrom = None
                    try:
                        connectsTo = CACHE[instance['connectsTo']]
                    except:
                        connectsTo = None
                %>
                <tr>
                    <td>${wire['label']}</td>
                    <td>${CableType.render_colors(wire['colors'])}</td>
                    <td>${wire['comment']}</td>

                    % if instance['connectsFrom'] is None:
                    <td></td>
                    % else:
                    <td>${elec_misc.render_pin_or_terminal(CACHE[instance['connectsFrom']])}</td>
                    % endif
                    % if instance['connectsTo'] is None:
                        <td>
                        % if len(instance['connections']) > 0:
                            ${elec_misc.render_direct_connections(instance)}
                        % endif
                        </td>
                    % else:
                    <td>${elec_misc.render_pin_or_terminal(CACHE[instance['connectsTo']])}</td>
                    % endif
                    <td>${instance['comment']}</td>
                </tr>
            % endfor

    </table>
</%def>

${render_cable(cable,cableType)}

<%def name="render_cables(cables)">
    <ul>
    % for cableQName in cables:
        <%
            cable = CACHE[cableQName]
            cableType = CACHE[cable['realizes']]
        %>
        <li> <h3>${cable['label']}</h3>
        ${misc.render_comment_below_title(cable)}
        ${CableType.render_summary(cableType)}
        ${render_cable(cable, cableType)}
        </li>
    % endfor
    </ul>
</%def>
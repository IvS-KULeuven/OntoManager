<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    cableType = CACHE[U["elec"]["show"]["qname"]]
%>




<h1>Cable type ${misc.render_view_link(cableType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

<%def name="render_summary(node)">
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
    </table>
</%def>

${render_summary(cableType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

<%def name="render_colors(colorQNames)">
    <%
        colors = [ CACHE[qname] for qname in colorQNames ]
    %>
    % if len(colors) > 0:
        ${misc.render_colorbox(colorQNames)}
        % for color in colors:
${color['label']}\
            % if not loop.last:
, \
            % endif
        % endfor
    % else:
        (color(s) not specified)
    % endif
</%def>


<table class="gridtable">
    <tr>
        <th>Wire</th>
        <th>Color(s)</th>
        <th>Comment</th>
    </tr>
    <%
        wires = [ CACHE[wireQName] for wireQName in cableType['wires'] ]
    %>
    % for wire in wires:
        <%
        %>
        <tr>
            <td>${wire['label']}</td>
            <td>${render_colors(wire['colors'])}</td>
            <td>${wire['comment']}</td>
        </tr>
    % endfor

</table>






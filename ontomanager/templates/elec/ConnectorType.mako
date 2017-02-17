<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    connectorType = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Connector type ${misc.render_view_link(connectorType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

<%def name="render_summary(node)">
    <%
        manufacturer = CACHE[node['manufacturer']]
        imgUrl = request.static_url("ontomanager:static/models/external/%s/%s.png" %(manufacturer['short_name'],node['qname'].split(':')[1]))
        fits = [ CACHE[fit] for fit in node['fits'] ]
    %>

    <table class="lefttable">
        <tr>
            <th>ID</th>
            <td>${misc.render_view_link(node, id="summary_id", contents=node['id'])}</td>
        </tr>
    % if node['gender'] is not None:
        <tr>
                <th>Gender</th>
                <td>${misc.render_view_link(CACHE[node['gender']], id="summary_gender")}</td>
        </tr>
    % endif
        <tr>
            <th>Manufacturer</th>
            <td>${misc.render_view_link(manufacturer, id="summary_manufacturer", contents=manufacturer['long_name'])}</td>
        </tr>
        <tr>
            <th>Description</th>
            <td>${node['comment']}</td>
        </tr>
        <tr>
            <th>Fits to</th>
            <td>${render_fits(fits)}</td>
        </tr>
        <tr>
            <th>Used in</th>
            <td>${elec_misc.render_owning_configurations(node)}</td>
        </tr>
    </table>
    <img src='${imgUrl}'/>
</%def>

${render_summary(connectorType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>


<table class="gridtable">
    <tr>
        <th>Pin</th>
        <th>Symbol</th>
        <th>Description</th>
    </tr>
    <%
        pins = [ CACHE[pinQName] for pinQName in connectorType['pins'] ]
    %>
    % for pin in pins:
        <tr>
            <td>${pin['label']}</td>
            <td>${pin['symbol']}</td>
            <td>${pin['comment']}</td>
        </tr>
    % endfor

</table>


<!-- =============================================== LAYOUT =======================================================  -->

<%def name="render_fits(fits)">
    % if len(fits) > 1:
<ul>
        % for fit in fits:
     <li>${misc.render_view_link(fit, id="fit", contents=fit['id'])}</li>
        % endfor
</ul>
    % else:
        % for fit in fits:
${misc.render_view_link(fit, id="fit", contents=fit['id'])}
        % endfor
    % endif
</%def>




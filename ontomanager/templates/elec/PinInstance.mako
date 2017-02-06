<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    pin = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Pin ${misc.render_view_link(pin, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Summary</h5>

<table class="gridtable">
    <tr>
        <th>Name</th>
        <th>Symbol</th>
        <th>Connector</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>${pin['label']}</td>
        % if pin['symbol'] is not None:
           <td>${pin['symbol']}</td>
        % else:
           <td></td>
        % endif
        % if pin['owner'] is not None:
           <td>${misc.render_view_link(CACHE[pin['owner']], id='summary_connector')}</td>
        % else:
           <td></td>
        % endif
        <td>${pin['comment']}</td>
    </tr>

</table>


<h5>Direct connections</h5>
${elec_misc.render_direct_connections(pin)}

<br />

<h5>Indirect connections</h5>
${elec_misc.render_indirect_connections(pin)}
<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    terminal = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Terminal ${misc.render_view_link(terminal, "title")}</h1>

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
        <td>${terminal['label']}</td>
        % if terminal['symbol'] is not None:
           <td>${terminal['symbol']}</td>
        % else:
           <td></td>
        % endif
        % if terminal['owner'] is not None:
           <td>${misc.render_view_link(CACHE[terminal['owner']], id='summary_owner')}</td>
        % else:
           <td></td>
        % endif
        <td>${terminal['comment']}</td>
    </tr>

</table>


<h5>Direct connections</h5>
${elec_misc.render_direct_connections(terminal)}

<br />

<h5>Indirect connections</h5>
${elec_misc.render_indirect_connections(terminal)}
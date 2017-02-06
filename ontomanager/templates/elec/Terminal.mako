<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    terminal = CACHE[U["elec"]["show"]["qname"]]
%>




<h1>Terminal ${misc.render_view_link(terminal, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

<%def name="render_summary(node)">

    <table class="gridtable">
        <tr>
            <th>Name</th>
            <td>${misc.render_view_link(node, id="summary_id", contents=node['label'])}</td>
        </tr>
        <tr>
            <th>Description</th>
            <td>${node['comment']}</td>
        </tr>
    </table>
</%def>

${render_summary(terminal)}


<h5>Direct connections</h5>
${elec_misc.render_direct_connections(terminal)}

<br />

<h5>Indirect connections</h5>
${elec_misc.render_indirect_connections(terminal)}
<%namespace name="misc" file="../misc.mako"/>

<%
    channel = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Channel ${misc.render_view_link(channel, "title")}</h1>

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

${render_summary(channel)}

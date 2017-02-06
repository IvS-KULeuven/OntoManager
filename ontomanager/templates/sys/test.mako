<%namespace name="misc" file="../misc.mako"/>

<%
    node        = CACHE[U['sys']["show"]["qname"]]
    tests       = [ CACHE[d] for d in node["tests"] ]
    verifies    = [ CACHE[d] for d in node["verifies"] ]
%>

<h1>Requirement ${misc.render_view_link(node, "title")}</h1>

${misc.render_comment_below_title(node)}


<h3>Properties</h3>
<table class="lefttable">
    <tr>
        <th>Tests</th>
        <td>
            <ul>
            % for t in tests:
                <li>${misc.render_view_link(t, t['label']+"_tests", contents=t['qname'])}</li>
            % endfor
            </ul>
        </td>
    </tr>
    <tr>
        <th>Verifies</th>
        <td>
            <ul>
            % for d in verifies:
                <li>${misc.render_view_link(d, d['label']+"_verifies", contents=d['qname'])}</li>
            % endfor
            </ul>
        </td>
    </tr>
</table>


<%def name="render_one_table_row(test, header=False)">
    % if header:
        <tr>
            <th>Description</th>
            <th>Verifies requirement:</th>
            <th>Tests constraint:</th>
        </tr>
    % else:
        <%
            tests       = [ CACHE[d] for d in test["tests"] ]
            verifies    = [ CACHE[d] for d in test["verifies"] ]
        %>
        <tr>
            <td>
                ${test['comment']}
            </td>
            <td>
                <ul>
                % for t in tests:
                    <li>${misc.render_view_link(t, t['label']+"_tests", contents=t['qname'])}</li>
                % endfor
                </ul>
            </td>
            <td>
                <ul>
                % for d in verifies:
                    <li>${misc.render_view_link(d, d['label']+"_verifies", contents=d['qname'])}</li>
                % endfor
                </ul>
            </td>
        </tr>
    % endif
</%def>
<%namespace name="misc" file="../misc.mako"/>

<%
    company = CACHE[U["org"]["show"]["qname"]]
    imgUrl = request.static_url("ontomanager:static/models/org/Company/%s.png" %(company['short_name']))

    manufactured = [ CACHE[m] for m in company['manufactured'] ]
%>


<h1>Company ${misc.render_view_link(company, "title", contents=company['short_name'])}</h1>

<!-- ============================================== Logo =======================================================  -->

<h3>Logo</h3>

<img src='${imgUrl}'/>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

<%def name="render_summary(node)">

    <table class="lefttable">
        <tr>
            <th>Short name</th>
            <td>${node['short_name']}</td>
        </tr>
        <tr>
            <th>Long name</th>
            <td>${node['long_name']}</td>
        </tr>
        <tr>
            <th>Description</th>
            <td>${node['comment']}</td>
        </tr>
    </table>
</%def>

${render_summary(company)}

<!-- ============================================== Manufactured ======================================================  -->

<h3>Products</h3>

<%def name="render_manufactured(manufactured)">
    <table class="gridtable">
        <tr>
            <th>ID</th>
            <th>Description</th>
            <th>Used in</th>
        </tr>
        % for m in manufactured:
        <tr>
            <td>${misc.render_view_link(m, "item", contents=m['id'])}</td>
            <td>${m['comment']}</td>
            <td>
            % if m.has_key('owning_configurations'):
                <%
                    configs = [ CACHE[configQName] for configQName in m['owning_configurations'] ]
                %>
                % for config in configs:
                    % if loop.index > 0:
, \
                    % endif
${misc.render_view_link(config)} (${m['owning_configurations_counts'][loop.index]})\
                % endfor
            % endif
            </td>
        </tr>
        % endfor
    </table>
</%def>

${render_manufactured(manufactured)}
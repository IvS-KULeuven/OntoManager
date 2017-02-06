<%namespace name="misc" file="../misc.mako"/>

<%
    node        = CACHE[U['sys']["show"]["qname"]]
    derives     = [ CACHE[d] for d in node["derives"] ]
    derivedFrom = [ CACHE[d] for d in node["derived_from"] ]
    satisfiedBy = [ CACHE[s] for s in node["satisfied_by"] ]
    declaredBy  = [ CACHE[d] for d in node["declared_by"] ]
%>

<h1>Requirement ${misc.render_view_link(node, "title")}</h1>

${misc.render_comment_below_title(node)}


<h3>Properties</h3>
<table class="lefttable">
    <tr>
        <th>Derives</th>
        <td>
            <ul class="arrow_forward">
            % for d in derives:
                <li>${misc.render_view_link(d, d['label']+"_derives", contents=d['qname'])}</li>
            % endfor
            </ul>
        </td>
    </tr>
    <tr>
        <th>Derived from</th>
        <td>
            <ul class="arrow_backward gray">
            % for d in derivedFrom:
                <li>${misc.render_view_link(d, d['label']+"_derived_from", contents=d['qname'])}</li>
            % endfor
            </ul>
        </td>
    </tr>
    <tr>
        <th>Satisfied by</th>
        <td>
            <ul>
            % for s in satisfiedBy:
                <li>${misc.render_view_link(s, s['label']+"_satisfied_by", contents=s['qname'])}</li>
            % endfor
            </ul>
        </td>
    </tr>
    <tr>
        <th>Declared by</th>
        <td>
            <ul>
            % for d in declaredBy:
                <li>${misc.render_view_link(d, d['label']+"_declared_by", contents=d['qname'])}</li>
            % endfor
            </ul>
        </td>
    </tr>
</table>



<%def name="render_one_table_row(req, header=False)">
    % if header:
            <tr>
                <th>Label</th>
                <th>Description</th>
                <th>Derives</th>
                <th>Derived from</th>
                <th>Satisfied by</th>
                <th>Declared by</th>
            </tr>
    % else:

        <%
        derives     = [ CACHE[d] for d in req["derives"] ]
        derivedFrom = [ CACHE[d] for d in req["derived_from"] ]
        satisfiedBy = [ CACHE[s] for s in req["satisfied_by"] ]
        declaredBy  = [ CACHE[d] for d in req["declared_by"] ]
        %>

        <tr>
            <td>
                ${req['label']}
            </td>
            <td>
                ${req['comment']}
            </td>
            <td>
                <ul class="arrow_forward">
                % for d in derives:
                    <li>${misc.render_view_link(d, d['label']+"_derives", contents=d['qname'])}</li>
                % endfor
                </ul>
            </td>
            <td>
                <ul class="arrow_backward gray">
                % for d in derivedFrom:
                    <li>${misc.render_view_link(d, d['label']+"_derived_from", contents=d['qname'])}</li>
                % endfor
                </ul>
            </td>
            <td>
                <ul>
                % for s in satisfiedBy:
                    <li>${misc.render_view_link(s, s['label']+"_satisfied_by", contents=s['qname'])}</li>
                % endfor
                </ul>
            </td>
            <td>
                <ul>
                % for d in declaredBy:
                    <li>${misc.render_view_link(d, d['label']+"_declared_by", contents=d['qname'])}</li>
                % endfor
                </ul>
            </td>
        </tr>

    % endif
</%def>
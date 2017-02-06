<%inherit file="base_layout.mako"/>
<%namespace name="misc" file="misc.mako"/>

<%block name="contents">

    <%
        browseQName = U["browse"]["show"]["qname"]

        if browseQName is None:
            browseQName = ''
        try:
            node = CACHE[browseQName]
        except:
            node = None
    %>

    <h1>QName to browse:</h1>

    <form  action="/browse" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <input name="qname" class="browsing" type="text" value="${browseQName}"/>
        <input name="submit" type="submit" value="Submit" />
    </form>


##    <h3>Summary:</h3>
##    <div class="box">
##        % for result in node["results"]:
##            % if result.has_key("manchester"):
##                % if result["qname"] == "rdf:type":
##                    <h4>Types:</h4>
##                % elif result["qname"] == "owl:equivalentClass":
##                    <h4>Equivalent classes:</h4>
##                % elif result["qname"] == "rdfs:subClassOf":
##                    <h4>Subclasses:</h4>
##                % else:
##                    <h4>${result["qname"]}:</h4>
##                % endif
##                <ul>
##                    % for s in result["manchester"]:
##                        <li>${s}</li>
##                    % endfor
##                </ul>
##            % endif
##        % endfor
##    </div>

% if node is not None:

    <p>
    <h1>Facts for ${node["qname"]}</h1>
    <table class="gridtable">
        <tr>
            <th>Predicate</th>
            <th>Object</th>
        </tr>

        % for result in node["results"]:
            % for object in result["objects"]:
                <tr>
                % if loop.first:
                        <td rowspan="${len(result["objects"])}">${result["qname"]}</td>
                % endif
                % if object["type"] == "uri":
                    <td><a href="browse?show;qname=${object["content"]["qname"]}">${object["content"]["qname"]}</a></td>
                % elif object["type"] == "bnode":
                    <td>${object["content"]["id"]}</td>
                % elif object["type"] == "literal":
                    <td>${object["content"]}</td>
                % else:
                    <td>${object["content"]}</td>
                % endif
                </tr>

            % endfor

        % endfor

    </table>
    </p>


    ${misc.render_debug(node)}

% endif
</%block>

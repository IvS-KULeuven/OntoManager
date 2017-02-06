<%inherit file="base_layout.mako"/>

<%!
    #import sys
    #import os
    #sys.path.append("../queries")
    #print os.path.abspath("../queries")
    #from triplestore import PARSE_FOR_URI
    #${PARSE_FOR_URI(label)}
%>

<%block name="contents">

    <% violations = M['problems']['violations'] %>

    <h1>Constraint violations (${len(violations)})</h1>


    <table class="gridtable">
        <tr>
            <th>Level</th>
            <th>Root</th>
            <th>Label</th>
            <th>Value</th>
        </tr>

        % for violation in violations:

            <%
                try:
                    level = M['functions']["URI_TO_QNAME"](violation["level"])
                except:
                    level = None
                root = violation["root"]
                label = M['functions']["PARSE_FOR_URI"](violation["label"])
                try:
                    value = M['functions']["URI_TO_QNAME"](violation["value"])
                except:
                    value = None


            %>

            <tr>
                %if level != None:

                 % if level == "spin:Warning":
                  <td class="orange">
                 %elif level == "spin:Error":
                  <td class="red">
                 %else:
                  <td>
                 % endif
                   <a href="browse?show;qname=${level}">${level}</a>
                  </td>
                %else:
                  <td></td>
                %endif
                <td><a href="browse?show;qname=${root["qname"]}">${root["qname"]}</a></td>
                <td>${label | n}</td>
                %if value != None:
                  <td><a href="browse?show;qname=${value}">${value}</a></td>
                %else:
                  <td></td>
                %endif
            </tr>
        % endfor
    </table>

</%block>

<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>

<%
    struct = CACHE[U["soft"]["show"]["qname"]]
%>


<h1>Struct ${misc.render_view_link(struct, "title")}</h1>


<h5>Attributes</h5>
<table class="gridtable">
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Initial value</th>
        <th>Description</th>
    </tr>
    % for attrQName in struct["attributes"]:
        <% attr = CACHE[attrQName] %>
        <tr>
            <td>${misc.render_view_link(attr, "table")}</td>
            % if (attr["type"] is not None):
                <%
                    attrType = CACHE[attr["type"]]
                    if attrType["plc_symbol"] is not None:
                        contents = attrType["plc_symbol"]
                    else:
                        contents = attrType["label"]
                %>
                <td>${misc.render_view_link(attrType, id="table", contents=contents)}</td>
            % else:
                <td></td>
            % endif

            % if attr["initial_value"] is not None:
            <td>${attr["initial_value"]}</td>
            % else:
            <td></td>
            % endif

            % if attr["comment"] is not None:
            <td>${attr["comment"]}</td>
            % else:
            <td></td>
            % endif
        </tr>
    % endfor
</table>



<h5 class="extraspace">PLCopen XML serialization</h5>
<div id="hidden"><xmp id="xmlcontent">${iec61131.xml_struct(struct)}</xmp></div>

${misc.render_xml_editor()}
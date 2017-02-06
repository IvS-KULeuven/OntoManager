<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>

<%
    enum = CACHE[U["soft"]["show"]["qname"]]
%>


<h1>Enum ${misc.render_view_link(enum, "title")}</h1>

<h5>Items</h5>
<table class="gridtable">
    <tr>
        <th>#</th>
        <th>Name</th>
    </tr>
    % for itemQName in enum["items"]:
        <%
            item = CACHE[itemQName]
        %>
        <tr>

            <td>${item["number"]}</td>
            <td>${misc.render_view_link(item, "table1")}</td>
        </tr>
    % endfor
</table>


<h5 class="extraspace">PLCopen XML serialization</h5>
<div id="hidden"><xmp id="xmlcontent">${iec61131.xml_enum(enum)}</xmp></div>

${misc.render_xml_editor()}
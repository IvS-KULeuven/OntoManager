<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>

<%
    ns = CACHE[U["soft"]["show"]["qname"]]
%>


<h1>Namespace ${misc.render_view_link(ns, "title")}</h1>

<h5>Sub-namespaces</h5>
<ul>
% for itemQName in ns["namespaces"]:
    <%
        item = CACHE[itemQName]
    %>
  <li>${misc.render_view_link(item, "ns_")}</li>
% endfor
</ul>

<h5>ENUMs</h5>

<ul>
% for itemQName in ns["ENUMs"]:
    <%
        item = CACHE[itemQName]
    %>
  <li>${misc.render_view_link(item, "enum_")}</li>
% endfor
</ul>

<h5>Structs</h5>

<ul>
% for itemQName in ns["STRUCTs"]:
    <%
        item = CACHE[itemQName]
    %>
  <li>${misc.render_view_link(item, "struct_")}</li>
% endfor
</ul>

<h5>Function blocks</h5>

<ul>
% for itemQName in ns["FBs"]:
    <%
        item = CACHE[itemQName]
    %>
  <li>${misc.render_view_link(item, "fb_")}</li>
% endfor
</ul>
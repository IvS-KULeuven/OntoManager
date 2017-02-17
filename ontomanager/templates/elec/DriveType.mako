<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    driveType = CACHE[U["elec"]["show"]["qname"]]

%>


<h1>Drive type ${misc.render_view_link(driveType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

${elec_misc.render_device_type_summary(driveType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(driveType)}
<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    motorType = CACHE[U["elec"]["show"]["qname"]]

%>




<h1>Motor type ${misc.render_view_link(motorType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

${elec_misc.render_device_type_summary(motorType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(motorType)}

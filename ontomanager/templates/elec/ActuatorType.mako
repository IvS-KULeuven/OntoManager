<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    actuatorType = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Actuator type ${misc.render_view_link(actuatorType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>


${elec_misc.render_device_type_summary(actuatorType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(actuatorType)}

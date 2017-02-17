<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    sensorType = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Sensor type ${misc.render_view_link(sensorType, "title")}</h1>

${misc.render_comment_below_title(sensorType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>


${elec_misc.render_device_type_summary(sensorType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(sensorType)}

<!-- ============================================== Cables =======================================================  -->

${elec_misc.render_summary("Cables", sensorType['cables'])}

<!-- ============================================== Connectors =======================================================  -->

${elec_misc.render_summary("Connectors", sensorType['connectors'])}
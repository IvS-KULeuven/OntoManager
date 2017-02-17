<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>
<%namespace name="elec_CableInstance" file="CableInstance.mako"/>
<%namespace name="elec_ConnectorInstance" file="ConnectorInstance.mako"/>

<%
    deviceType = CACHE[U["elec"]["show"]["qname"]]

%>


<h1>Device type ${misc.render_view_link(deviceType, "title")}</h1>

${misc.render_comment_below_title(deviceType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

${elec_misc.render_device_type_summary(deviceType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(deviceType)}


<!-- ============================================== Cables =======================================================  -->


${elec_CableInstance.render_cables(deviceType['cables'])}


<!-- ============================================== Connectors =======================================================  -->

${elec_ConnectorInstance.render_connectors(deviceType['connectors'])}
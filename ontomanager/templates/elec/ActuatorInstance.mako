<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    actuator = CACHE[U["elec"]["show"]["qname"]]
    actuatorType = CACHE[actuator["man_type"]]
%>


<h1>Actuator ${misc.render_view_link(actuator, "title")}</h1>

${misc.render_comment_below_title(actuatorType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Actuator type summary</h5>

${elec_misc.render_device_type_summary(actuatorType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(actuator, actuatorType)}
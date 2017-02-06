<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    motor = CACHE[U["elec"]["show"]["qname"]]
    motorType = CACHE[motor["man_type"]]
%>


<h1>Motor ${misc.render_view_link(motor, "title")}</h1>

${misc.render_comment_below_title(motorType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Motor type summary</h5>

${elec_misc.render_device_type_summary(motorType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(motor, motorType)}
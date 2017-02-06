<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    sensor = CACHE[U["elec"]["show"]["qname"]]
    sensorType = CACHE[sensor["man_type"]]
%>


<h1>Sensor ${misc.render_view_link(sensor, "title")}</h1>

${misc.render_comment_below_title(sensorType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>sensor type summary</h5>

${elec_misc.render_device_type_summary(sensorType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

% if len(sensorType['terminals']) > 0:

<h5>Connections</h5>

${elec_misc.render_terminals_table(sensor, sensorType)}

% endif
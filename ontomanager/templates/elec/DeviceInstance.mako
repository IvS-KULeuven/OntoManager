<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    device = CACHE[U["elec"]["show"]["qname"]]
    deviceType = CACHE[device["man_type"]]
%>


<h1>Device ${misc.render_view_link(device, "title")}</h1>

${misc.render_comment_below_title(device)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Device type summary</h5>

${elec_misc.render_device_type_summary(deviceType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

% if len(deviceType['terminals']) > 0:
<h5>Connections</h5>

${elec_misc.render_terminals_table(device, deviceType)}
% endif



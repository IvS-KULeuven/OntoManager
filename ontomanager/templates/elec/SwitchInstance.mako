<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    switch = CACHE[U["elec"]["show"]["qname"]]
    switchType = CACHE[switch["man_type"]]
%>


<h1>Switch ${misc.render_view_link(switch, "title")}</h1>

${misc.render_comment_below_title(switchType)}

% if 'symbol' in switch:
<h5>Symbol</h5>
<p>${switch['symbol']}</p>
% endif

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Switch type summary</h5>

${elec_misc.render_device_type_summary(switchType)}


<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(switch, switchType)}

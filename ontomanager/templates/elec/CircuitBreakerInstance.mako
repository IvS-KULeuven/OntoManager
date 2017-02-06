<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    cb = CACHE[U["elec"]["show"]["qname"]]
    cbType = CACHE[cb["man_type"]]
%>


<h1>Circuit breaker ${misc.render_view_link(cb, "title")}</h1>

${misc.render_comment_below_title(cbType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Circuit breaker type summary</h5>

${elec_misc.render_device_type_summary(cbType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(cb, cbType)}
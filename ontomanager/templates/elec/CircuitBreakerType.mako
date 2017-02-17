<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    cbType = CACHE[U["elec"]["show"]["qname"]]

%>


<h1>Circuit breaker type ${misc.render_view_link(cbType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

${elec_misc.render_device_type_summary(cbType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(cbType)}

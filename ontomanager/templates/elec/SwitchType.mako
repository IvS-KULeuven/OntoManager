<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    switchType = CACHE[U["elec"]["show"]["qname"]]

%>




<h1>Switch type ${misc.render_view_link(switchType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>


${elec_misc.render_device_type_summary(switchType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>

${elec_misc.render_device_type_layout(switchType)}

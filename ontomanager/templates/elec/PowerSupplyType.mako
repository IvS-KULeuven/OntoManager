<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    powerSupplyType = CACHE[U["elec"]["show"]["qname"]]
%>


<h1>Power supply type ${misc.render_view_link(powerSupplyType, "title")}</h1>

<!-- ============================================== SUMMARY =======================================================  -->

<h3>Summary</h3>

${elec_misc.render_device_type_summary(powerSupplyType)}


<!-- =============================================== LAYOUT =======================================================  -->

<h3>Layout</h3>


${elec_misc.render_device_type_layout(powerSupplyType)}

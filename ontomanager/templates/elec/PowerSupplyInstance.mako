<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    powerSupply = CACHE[U["elec"]["show"]["qname"]]
    powerSupplyType = CACHE[powerSupply["man_type"]]
%>


<h1>Power supply ${misc.render_view_link(powerSupply, "title")}</h1>

${misc.render_comment_below_title(powerSupplyType)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>powerSupply type summary</h5>

${elec_misc.render_device_type_summary(powerSupplyType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(powerSupply, powerSupplyType)}
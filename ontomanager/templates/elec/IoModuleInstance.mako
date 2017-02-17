<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>
<%namespace name="IoModuleType" file="IoModuleType.mako"/>

<%
    module = CACHE[U["elec"]["show"]["qname"]]
    moduleType = CACHE[module["man_type"]]
%>


<h1>I/O Module instance ${misc.render_view_link(module, "title")}</h1>

${misc.render_comment_below_title(module)}

<!-- ============================================== SYSTEM PROPERTIES =======================================================  -->

<h5>System properties</h5>
${misc.render_system_properties(module)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Module type summary</h5>

${elec_misc.render_device_type_summary(moduleType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(module, moduleType)}

<!-- ============================================ INTERFACE =====================================================  -->

<h5>Interface</h5>

${elec_misc.render_interface_table(module['interface'], moduleType['interface'])}
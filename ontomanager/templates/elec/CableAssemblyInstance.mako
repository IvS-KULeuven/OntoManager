<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>
<%namespace name="elec_CableType" file="CableType.mako"/>
<%namespace name="elec_CableInstance" file="CableInstance.mako"/>
<%namespace name="elec_ConnectorInstance" file="ConnectorInstance.mako"/>
<%namespace name="elec_ConnectorType" file="ConnectorType.mako"/>
<%namespace name="elec_CableAssemblyType" file="CableAssemblyType.mako"/>


<%
    cableAssembly = CACHE[U["elec"]["show"]["qname"]]
    cableAssemblyType = CACHE[cableAssembly["man_type"]]
%>


<h1>Cable assembly instance ${misc.render_view_link(cableAssembly, "title")}</h1>

${misc.render_comment_below_title(cableAssembly)}

<!-- ============================================== SUMMARY =======================================================  -->

<h2>Cable assembly type summary</h2>

${elec_CableAssemblyType.render_summary(cableAssemblyType)}



<h2>${misc.render_view_link(cableAssemblyType, id="view_layout", contents="Cable assembly type")} layout:</h2>


<h3>Cables</h3>
${elec_CableAssemblyType.render_cables(cableAssemblyType)}



<h3>Connectors</h3>
${elec_CableAssemblyType.render_connectors(cableAssemblyType)}
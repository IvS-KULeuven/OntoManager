<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    drive = CACHE[U["elec"]["show"]["qname"]]
    driveType = CACHE[drive["man_type"]]
%>


<h1>Drive ${misc.render_view_link(drive, "title")}</h1>

${misc.render_comment_below_title(drive)}

<!-- ============================================== SUMMARY =======================================================  -->

<h5>Drive type summary</h5>

${elec_misc.render_device_type_summary(driveType)}

<!-- ============================================ CONNECTIONS =====================================================  -->

<h5>Connections</h5>

${elec_misc.render_terminals_table(drive, driveType)}

<%namespace name="iec61131" file="iec61131.mako"/>\
<%
    node = CACHE[project]
%>\
${iec61131.xml_project(node)}
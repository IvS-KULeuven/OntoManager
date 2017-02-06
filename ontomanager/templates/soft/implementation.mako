<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>



<%def name="render(node)">\
<%
    expressions = [ CACHE[e] for e in node["expressions"] ]
%>\
${expressions}
</%def>
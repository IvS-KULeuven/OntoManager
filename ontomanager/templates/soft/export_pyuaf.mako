<%namespace name="pyuaf" file="pyuaf.mako"/>\
<%
    node = CACHE[project]
%>\
${pyuaf.pyuaf_module(node)}
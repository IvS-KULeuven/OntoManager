<%inherit file="../base_layout.mako"/>

<%block name="contents">

<%
    show_type = U["org"]["show"]["type"]
%>

%if show_type == "Manufacturer":
    <%include file="Manufacturer.mako"/>
%elif show_type == "Organization":
    <%include file="Organization.mako"/>
%elif show_type is None:
    ## nothing to show
%else:
    <p>No view defined for ${show_type}</p>
%endif


</%block>

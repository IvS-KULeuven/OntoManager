<%inherit file="base_layout.mako"/>

<%block name="contents">

    <h1>CACHE</h1>

    <%
        import pprint
        fullCache = pprint.pformat(CACHE)
    %>

    <pre>${fullCache}</pre>


</%block>

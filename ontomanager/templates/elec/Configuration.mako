<%namespace name="misc" file="../misc.mako"/>
<%namespace name="elec_misc" file="misc.mako"/>

<%
    elecConfig = CACHE[U["elec"]["show"]["qname"]]
%>


<%def name="render_config(cfg, parents=[])">
    <%
        import pprint
        pp = pprint.PrettyPrinter(indent=4)

        shown = []

        pngPath = "static/models/elec/%s.png" %cfg["qname"]
        pdfPath = "static/models/elec/%s.pdf" %cfg["qname"]
        dxfPath = "static/models/elec/%s.dxf" %cfg["qname"]

        import pkg_resources
        pngExists = pkg_resources.resource_exists('ontomanager', pngPath)
        pdfExists = pkg_resources.resource_exists('ontomanager', pdfPath)
        dxfExists = pkg_resources.resource_exists('ontomanager', dxfPath)

        pngUrl = request.static_url("ontomanager:%s" %pngPath)
        pdfUrl = request.static_url("ontomanager:%s" %pdfPath)
        dxfUrl = request.static_url("ontomanager:%s" %dxfPath)
    %>

    % if len(parents) == 0:
        <h1>Configuration ${misc.render_view_link(cfg, "title")}</h1>
    % else:

        <h2>Sub-configuration
            % for parent in parents:
                ${misc.render_view_link(parent, "subtitle")} / \
            % endfor
             ${misc.render_view_link(cfg, "title")}</h2>
    % endif

    ${misc.render_comment_below_title(cfg)}


    <!-- ============================================== Circuit breakers =======================================================  -->
    % if pngExists or pdfExists or dxfExists:
        <h3>Overview</h3>
    % endif
    % if pngExists:
        <style>
        IMG.MaxSized
        {
        max-width: 800px;
        max-height: 800px;
        }
        </style>
        <a href="${pngUrl}"><img src='${pngUrl}' class="MaxSized"/></a>
        <br />
    % endif

    % if pdfExists:
        <a href="${pdfUrl}">[PDF]</a>
    % endif

    % if dxfExists:
        <a href="${dxfUrl}">[DXF]</a>
    % endif

    % if pngExists or pdfExists or dxfExists:
        <br />
        <br />
    % endif

    <%
        try:
            cb = cfg['circuit breakers']
        except Exception as e:
            s = pp.pformat(cfg)
            raise Exception(s)
    %>

    <!-- ============================================== Circuit breakers =======================================================  -->

    ${elec_misc.render_summary("Circuit breakers", cb, shown)}

    <!-- ============================================== Power supplies =======================================================  -->

    ${elec_misc.render_summary("Power supplies", cfg['power supplies'], shown)}

    <!-- ============================================== Terminals =======================================================  -->

    % if len(cfg['terminals']) > 0:
        <h3>Terminals (${len(cfg['terminals'])})</h3>

        <table class="gridtable">

            <tr>
                <th>Symbol</th>
                <th># connections</th>
                <th>Comment</th>
            </tr>

            % for qname in cfg['terminals']:
                <%
                    terminal = CACHE[qname]
                %>
                <tr>
                    % if 'symbol' in terminal:
                        <td>${misc.render_view_link(terminal, "term_symbol", contents=terminal['symbol'])}</td>
                    % else:
                        <td>${misc.render_view_link(terminal, "term_symbol")}</td>
                    % endif
                    <td>${len(terminal['connections'])}</td>
                    <td>${terminal['comment']}</td>
                </tr>

            % endfor

        </table>
    % endif

    <!-- ============================================== I/O modules =======================================================  -->

    ${elec_misc.render_summary("I/O modules", cfg['I/O modules'], shown)}

    <!-- ============================================== Drives =======================================================  -->

    ${elec_misc.render_summary("Drives", cfg['drives'], shown)}

    <!-- ============================================== Connectors =======================================================  -->

    ${elec_misc.render_summary("Connectors", cfg['connectors'], shown)}

    <!-- ============================================== Switches =======================================================  -->

    ${elec_misc.render_summary("Switches", cfg['switches'], shown)}


    <!-- ============================================== Sensors =======================================================  -->

    ${elec_misc.render_summary("Sensors", cfg['sensors'], shown)}

    <!-- ============================================== Cables =======================================================  -->

    ${elec_misc.render_summary("Cables", cfg['cables'], shown)}

    <!-- ============================================== Cable assemblies =======================================================  -->

    ${elec_misc.render_summary("Cable assemblies", cfg['cable assemblies'], shown)}



    <!-- ============================================== Other actuators =======================================================  -->

    <%
        otherActuators = []
        for device in cfg['actuators']:
            if not device in shown:
                otherActuators.append(device)
    %>

    % if len(otherActuators) > 0:
    ${elec_misc.render_summary("Other actuators", otherActuators, shown)}
    % endif
    <!-- ============================================== Other devices =======================================================  -->

    ${elec_misc.render_summary("Other devices", cfg['other devices'], shown)}


    <!-- ============================================== Sub-configurations =======================================================  -->

    <br />
    % if len(cfg['sub-configurations']) > 0:
        ##<h3>Sub-configurations (${len(cfg['sub-configurations'])})</h3>
        <br/>
    <ul>
        <%
            parents.append(cfg)
        %>
        % for subCfg in cfg['sub-configurations']:
            <li>
                ${render_config(CACHE[subCfg], parents)}
            </li>
        % endfor
    </ul>

    % endif



</%def>

${render_config(elecConfig)}

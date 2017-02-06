<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>

<%
    qname = U["soft"]["show"]["qname"]
    node  = CACHE[qname]
    label = node['label']
    xmlCode  = node['xml_code']
    pyuafCode  = node['pyuaf_code']

    xmlPath = M["functions"]['SOFT_GET_FILEPATH'](M["config"]['plcopen_dir'], qname, 'xml')
    pyPath = M["functions"]['SOFT_GET_FILEPATH'](M["config"]['pyuaf_dir'], qname, 'py')
%>


<h1>Library ${misc.render_view_link(node, "title")}</h1>


<h5 class="extraspace">PLCopen XML serialization

</h5>

<table class="gridtable">
    <tr>
        <th>File</th>
        <td>${xmlPath}</td>
    </tr>
    <tr>
        <th>Status</th>
        <td>${xmlCode["status"]}</td>
    </tr>
    <tr>
        <th>Code generation</th>
        % if node["xml_process_busy"]:
            <td>RUNNING</td>
        % else:
            <td>Not running</td>
        % endif
    </tr>
</table>

<form  action="/soft" method="post" accept-charset="utf-8" enctype="multipart/form-data">
    <input name="ns"        type="hidden" value="${qname}" />
    <input name="submit"    type="submit" value="Generate PLCopen XML" />
    <input name="submit"    type="submit" value="Download PLCopen XML" />
</form>




<h5 class="extraspace">PyUAF serialization</h5>

<table class="gridtable">
    <tr>
        <th>File</th>
        <td>${pyPath}</td>
    </tr>
    <tr>
        <th>Status</th>
        <td>${pyuafCode["status"]}</td>
    </tr>
    <tr>
        <th>Code generation</th>
        % if node["pyuaf_process_busy"]:
            <td>RUNNING</td>
        % else:
            <td>Not running</td>
        % endif
    </tr>
</table>

<form  action="/soft" method="post" accept-charset="utf-8" enctype="multipart/form-data">
    <input name="ns"        type="hidden" value="${qname}" />
    <input name="submit"    type="submit" value="Generate pyUAF code" />
    <input name="submit"    type="submit" value="Download pyUAF code" />
</form>


% if node["xml_process_busy"] or node["pyuaf_process_busy"]:

    <script>
        setTimeout(function () {
            window.location.reload(1);
        }, 1000);  // After 1 secs
    </script>

% else:




    <h5 class="extraspace">File contents:</h5>

    % if xmlCode['contents'] is None:
        <div id="hidden"><xmp id="xmlcontent"></xmp></div>
    % else:
        <div id="hidden"><xmp id="xmlcontent">${xmlCode['contents'] | n}</xmp></div>
    % endif

    % if pyuafCode['contents'] is None:
        <div id="hidden"><xmp id="pyuafcontent"></xmp></div>
    % else:
        <div id="hidden"><xmp id="pyuafcontent">${pyuafCode['contents'] | n}</xmp></div>
    % endif

    <button name="show_plcopen">Show PLCopen XML code</button>
    <button name="show_pyuaf">Show PyUAF code</button>


    <div id="xmleditor"></div>

    <script src="${request.static_url('ontomanager:static/ace/src-min-noconflict/ace.js')}" type="text/javascript" charset="utf-8"></script>
    <script>
      var xmleditor = ace.edit("xmleditor");
      xmleditor.setTheme("ace/theme/tomorrow_night_blue");
      xmleditor.setReadOnly(true);
      xmleditor.getSession().setMode("ace/mode/xml")
      xmleditor.getSession().setValue($("#xmlcontent").text());

      $(document).ready(function(){
        $('button[name="show_plcopen"]').click(function(){
              xmleditor.getSession().setMode("ace/mode/xml")
              xmleditor.getSession().setValue($("#xmlcontent").text());
        });
        $('button[name="show_pyuaf"]').click(function(){
              xmleditor.getSession().setMode("ace/mode/python")
              xmleditor.getSession().setValue($("#pyuafcontent").text());
        });
      });
    </script>

% endif
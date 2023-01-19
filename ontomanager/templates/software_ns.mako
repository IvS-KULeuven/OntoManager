<%
    ns = show["content"]["ns"]
    nsName = ns['qname'].split(":",1)[1]
    code = show["content"]["code"]
    process = show["content"]["process"]
%>

<%namespace name="iec61131" file="iec61131.mako"/>

<h1>Namespace <a href="browse?browse=${ns["qname"]}">${nsName}</a></h1>


<h5 class="extraspace">PLCopen XML serialization

</h5>

<table class="gridtable">
    <tr>
        <th>File</th>
        % if nsName in config["files"]["generated_xml_library"]:
            <td>${config["files"]["generated_xml_library"][nsName]}</td>
        % else:
            <td></td>
        % endif
    </tr>
    <tr>
        <th>Status</th>
        <td>${code["status"]}</td>
    </tr>
    <tr>
        <th>Code generation</th>
        % if process["busy"]:
            <td>RUNNING</td>
        % else:
            <td>Not running</td>
        % endif
    </tr>
</table>

<form  action="/software" method="post" accept-charset="utf-8" enctype="multipart/form-data">
    <input name="ns"        type="hidden" value="${ns["qname"]}" />
    <input name="submit"    type="submit" value="Generate" />
    <input name="submit"    type="submit" value="Download" />
</form>


% if process["busy"]:

    <script>
        setTimeout(function () {
            window.location.reload(1);
        }, 1000);  // After 5 secs
    </script>

% else:


    <h5 class="extraspace">File contents:</h5>

    % if code["code"] is None:
        <div id="hidden"><xmp id="xmlcontent"></xmp></div>
    % else:
        <div id="hidden"><xmp id="xmlcontent">${code["code"] | n}</xmp></div>
    % endif


    <div id="xmleditor"></div>
    <script src="${request.static_url('ontomanager:static/ace/src-min-noconflict/ace.js')}" type="text/javascript" charset="utf-8"></script>
    <script>
      var xmleditor = ace.edit("xmleditor");
      xmleditor.setTheme("ace/theme/tomorrow_night_blue");
      xmleditor.setReadOnly(true);
      xmleditor.getSession().setMode("ace/mode/xml")
      xmleditor.getSession().setValue($("#xmlcontent").text());
    </script>

% endif

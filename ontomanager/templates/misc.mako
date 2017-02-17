


<%def name="render_debug(node)">
    <%
        if DEBUG and (node is not None):
            import pprint
            nodeDescription = pprint.pformat(node)
    %>
    %if DEBUG and (node is not None):
        <h3>Debugging info</h3>
        <div class="box"><pre>${nodeDescription}</pre></div>
    %endif
</%def>


<%def name="render_xml_editor()">
      <div id="xmleditor"></div>
      <script src="${request.static_url('ontomanager:static/ace/src-min-noconflict/ace.js')}" type="text/javascript" charset="utf-8"></script>
      <script>
          var xmleditor = ace.edit("xmleditor");
          xmleditor.setTheme("ace/theme/tomorrow_night_blue");
          xmleditor.setReadOnly(true);
          xmleditor.getSession().setMode("ace/mode/xml")
          xmleditor.getSession().setValue($("#xmlcontent").text());
      </script>
</%def>


<%def name="render_default_view_link(node, contents=None)">\
<%
    if len(node["views_order"]) > 0:
        viewCategory, viewType = node["views_order"][0]
    else:
        viewCategory = "browse"
        viewType     = "all"
    if contents is None:
        contents = node["label"]
%>\
<a href="${viewCategory}?show=${viewType};qname=${node['qname']}">${contents}</a>
</%def>

<%def name="render_complex_default_view_link(node, contents=None)">\
<%
    if len(node["views_order"]) > 0:
        viewCategory, viewType = node["views_order"][0]
    else:
        viewCategory = "browse"
        viewType     = "all"
    if contents is None:
        contents = node["label"]
%>\
##<a href="${viewCategory}?show=${viewType};qname=${node['qname']}">[${viewType[0]}] ${node['label']}</a>
<div class="viewddd">

            <a href="${viewCategory}?show=${viewType};qname=${node['qname']}"
                onmouseover="mopen('m_${node['qname']}')"
                ##onmouseout="mclosetime()">[${viewType[0]}] ${node['label']}</a>
                onmouseout="mclosetime()"> ${contents}</a>
                <div id='m_${node['qname']}'
                    onmouseover="mcancelclosetime()"
                    onmouseout="mclosetime()">
                % for viewCategory, viewType in node['views_order']:
                    <a href="${viewCategory}?show=${viewType};qname=${node['qname']}">[${viewType[0]}] ${viewType}</a></br>
                % endfor
                </div>
</div>
</%def>

<%def name="render_complex_view_link(node, id='', contents=None)">\
<%
    if len(node["views_order"]) > 0:
        viewCategory, viewType = node["views_order"][0]
    else:
        viewCategory = "browse"
        viewType     = "all"

    if contents is None:
        contents = node["label"]
%>\
<div class="viewddd">\
<a href="${viewCategory}?show=${viewType};qname=${node['qname']}" onmouseover="mopen('m_${node['qname']}_${id}')" onmouseout="mclosetime()">${contents}</a>\
<div id='m_${node['qname']}_${id}' onmouseover="mcancelclosetime()" onmouseout="mclosetime()">\
% for viewCategory, viewType in node['views_order']:
<a href="${viewCategory}?show=${viewType};qname=${node['qname']}">[${viewType[0]}] ${viewType}</a></br>\
% endfor
</div>\
</div>\
</%def>

<%def name="render_view_link(node, id='', contents=None)">\
<%
    if len(node["views_order"]) > 0:
        viewCategory, viewType = node["views_order"][0]
    else:
        viewCategory = "browse"
        viewType     = "thing"

    if contents is None:
        contents = node["label"]
%>\
<a href="${viewCategory}?show=${viewType};qname=${node['qname']}">${contents}</a>\
</%def>


<%def name="render_tree(qname, branch, category, path, firstItem=True, display='label')">\
<%

    node = CACHE[qname]
    try:
        type = node["default_views"][category]
        view = node["views"][category][type]
        expandable = node["views"][category][type]["expandable"]
        isOpened = branch['__opened__']
        hasView = True
    except:
        hasView = False
        isOpened = False
        expandable = False
    try:
        displayStr = node[display]
        if len(displayStr) == 0:
            raise Exception('empty display string')
    except:
        displayStr = node['label']

%>\
% if hasView and expandable:
    ${render_expand_icon(category, type, path, isOpened)} \
% endif
${render_default_view_link(node, contents=displayStr)} \
% if hasView:
    %if isOpened:
        <ul>
            % for expansion in view["expansions"]:
                % if len(node[expansion]) > 0 and expansion in branch.keys():
                    <%
                        isBranchOpened = branch[expansion]['__opened__']
                        unsortedChildren = branch[expansion].keys()
                        unsortedChildren.remove('__opened__')
                        unsortedChildren.remove('__opened_before__')
                        children = []
                        for item in node[expansion]:
                            if item in unsortedChildren:
                                children.append(item)
                        import urllib
                        expansionPath = path + '::' + urllib.quote(expansion, safe='')
                    %>
                        <li>${render_expand_icon(category, type, expansionPath, isBranchOpened)} <i>${expansion}</i>
                        % if len(children) > 0 and isBranchOpened:
                        <ul>
                            % for subitemQName in children:
                                <%
                                import urllib
                                childPath = expansionPath + '::' + urllib.quote(subitemQName, safe='')
                                %>
                                <li>${render_tree(subitemQName, branch[expansion][subitemQName], category, childPath, False, display)}</li>
                            % endfor
                        </ul>
                        % endif
                    </li>
                % endif
            % endfor
        </ul>
    %endif
% endif
</%def>



<%def name="render_expand_icon(category, type, path, isOpened)">\
<%
    if type is None:
        type = node["default_views"][category]
%>
%if isOpened:
<a href="${category}?close;path=${path}">${render_expand_icon_image(expanded=True)}</a>\
%else:
<a href="${category}?open=${type};path=${path}">${render_expand_icon_image(expanded=False)}</a>\
%endif
</%def>


<%def name="render_expand_icon_image(expanded=True)">\
<% size = 13 %>
% if expanded:
<img src="${request.static_url('ontomanager:static/collapse.gif')}" width="${size}" height="${size}">\
% else:
<img src="${request.static_url('ontomanager:static/expand.gif')}" width="${size}" height="${size}">\
% endif
</%def>


<%def name="render_comment_below_title(node)">\
% if (node['comment'] is not None):
    % if (node['comment'] != ''):
<p><blockquote>${node['comment']}</blockquote></p>
<br />
    % else:
        <br />
    % endif
% endif
</%def>


<%def name="render_colorbox(colorQNames, maxWidth=60)">
    <%
        colors = [ CACHE[qname] for qname in colorQNames ]
    %>
    % if len(colors) > 0:
        <%
            width = maxWidth / len(colors)
        %>
            <div class="colorBoxes">
        % for color in colors:
            <div title="${color['label']}" class="colorBox" style="width:${width}px; background-color:#${color['hexValue']}"></div>\
        % endfor
            </div>
    % endif
</%def>


<%def name="render_system_properties(node)">\
% if node.has_key('satisfies'):
    % if len(node['satisfies']) > 0:
        <table class="lefttable">
            <tr>
                <th rowspan="${len(node['satisfies'])}">Satisfies</th>
                % for satisfiesQName in node['satisfies']:
                    <td>${render_view_link(CACHE[satisfiesQName], "satisfies", contents=satisfiesQName)}</td>
                % endfor
            </tr>
        </table>
    % endif
% endif
</%def>

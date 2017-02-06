<%namespace name="misc" file="../misc.mako"/>

<%inherit file="../base_layout.mako"/>


<%block name="contents">


    <div id="freeleft">

        <ul class="tree">
          % for qname, branch in U["soft"]["tree"].items():
              <li>
                  ${misc.render_tree(qname, branch, "soft", qname)}
              </li>
          % endfor
        </ul>

    </div>

    <div id="freeright">

        <% show_type = U["soft"]["show"]["type"] %>

        %if show_type == "library":
            <%include file="library.mako"/>
        %elif show_type == "enum":
            <%include file="enum.mako"/>
        %elif show_type == "struct":
            <%include file="struct.mako"/>
        %elif show_type == "fb":
            <%include file="fb.mako"/>
        %elif show_type == "namespace":
            <%include file="namespace.mako"/>
        %elif show_type is None:
            ## nothing to show
        %else:
            <p>No '${show_type}' view defined for <a href="browse?show=thing;qname=${U['soft']['show']['qname']}">${U['soft']['show']['qname']}</a></p>
        %endif





    </div>

</%block>



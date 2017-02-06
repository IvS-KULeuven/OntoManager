<%namespace name="misc" file="../misc.mako"/>

<%inherit file="../base_layout.mako"/>



<%block name="contents">

    <div id="freeleft">


        <ul class="tree">
          % for qname, branch in U['sys']["tree"].items():
              <li>
                  ${misc.render_tree(qname, branch, "sys", qname)}
              </li>
          % endfor
        </ul>

    </div>

    <div id="freeright">

##        <div id="errormessagebox">Systems views are still under construction ...</div>


        <%
            show_type = U['sys']['show']['type']
        %>

        % if show_type == "projects":
            <%include file="projects.mako"/>
        % elif show_type == "project":
            <%include file="project.mako"/>
        % elif show_type == "concept":
            <%include file="concept.mako"/>
        % elif show_type == "design":
            <%include file="design.mako"/>
        % elif show_type == "requirement":
            <%include file="requirement.mako"/>
        % elif show_type == "test":
            <%include file="test.mako"/>
        % elif show_type is None:
            ## nothing to show
        % else:
            <p>No view defined for ${show_type}</p>
        % endif

    </div>

</%block>

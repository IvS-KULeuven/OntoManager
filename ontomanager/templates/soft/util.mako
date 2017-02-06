<%namespace name="misc" file="../misc.mako"/>
<%namespace name="iec61131" file="iec61131.mako"/>

##<%def name="layoutArgumentsList(qnames)">\
##<% args = [ CACHE[qname] for qname in qnames ] %>\
##        % for arg in args:
##${arg["label"]}\
##            % if not loop.last:
##, \
##            % endif
##        % endfor
##</%def>

<%def name="render_qualifiers(qnames, id='')">\
<% nodes = [ CACHE[qname] for qname in qnames ]%>\
        % for node in nodes:
${misc.render_view_link(node, contents=node["plc_symbol"] + '=' + node["value"], id=id+str(loop.index))}\
            % if not loop.last:
, \
            % endif
        % endfor
</%def>

<%def name="render_variables(varIn, varInOut, varOut, varLocal, firstColumn=None, id='')">
        <%
            allVars = [ [ "VAR_INPUT"  , varIn     ],
                        [ "VAR_IN_OUT" , varInOut  ],
                        [ "VAR_OUTPUT" , varOut    ],
                        [ "VAR"        , varLocal  ] ]
            noOfVars = 0
            for kind, vars in allVars:
                noOfVars += len(vars)
        %>

        <tr>
            %if firstColumn is not None:
                <th rowspan="${1+noOfVars}">${firstColumn}</th>
            %endif
            <th>Variable</th>
            <th>Name</th>
            <th>Type</th>
            <th>Initial value</th>
            <th>Address</th>
            <th>Description</th>
            <th>Qualifiers</th>
        </tr>
        % for kind, vars in allVars:
            % for arg in vars:
                % if loop.first:
                    <tr><td rowspan="${len(vars)}">${kind}</td>
                % else:
                    <tr>
                % endif
                        <td>${misc.render_view_link(arg, id=id)}</td>
                        % if arg["type"] is not None:
                            <%
                                typeNode = CACHE[arg["type"]]
                                try:
                                    typeName = typeNode["plc_symbol"]
                                    if typeName is None: raise Exception()
                                except:
                                    typeName = typeNode["label"]
                            %>
                            <td>${misc.render_view_link(CACHE[arg["type"]], id=id, contents=typeName)}</td>
                        % elif arg["points_to_type"] is not None:
                            <%
                                typeNode = CACHE[arg["points_to_type"]]
                                try:
                                    typeName = typeNode["plc_symbol"]
                                    if typeName is None: raise Exception()
                                except:
                                    typeName = typeNode["label"]
                            %>
                            <td>POINTER TO ${misc.render_view_link(CACHE[arg["points_to_type"]], id=id, contents=typeName)}</td>
                        % else:
                            <td></td>
                        % endif

                        % if arg["initial_value"] is not None:
                        <td>${arg["initial_value"]}</td>
                        % else:
                        <td></td>
                        % endif

                        % if arg["address"] is not None:
                        <td>${arg["address"]}</td>
                        % else:
                        <td></td>
                        % endif

                        % if arg["comment"] is not None:
                        <td>${arg["comment"]}</td>
                        % else:
                        <td></td>
                        % endif

                        % if arg["qualifiers"] is not None:
                        <td>${render_qualifiers(arg["qualifiers"], id=id)}</td>
                        % else:
                        <td></td>
                        % endif

                        % if not loop.first:
                            </tr>
                        % endif
                    </tr>
            % endfor
        % endfor
</%def>
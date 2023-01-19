
% if show["type"] is not None:

    <%
        TRIANGLE = "&#9655;"
    %>

    <%namespace name="iec61131" file="iec61131.mako"/>

    <%def name="layoutArgumentsList(args)">\
        % for arg in args:
${arg["label"]}\
            % if not loop.last:
, \
            % endif
        % endfor
    </%def>

    <%def name="layoutQualifierList(qualifiersDict)">\
        % for qualifierQname, details in qualifiersDict.items():
<a href="browse?browse=${qualifierQname}">${details["symbol"]}=${details["value"]}</a>\
            % if not loop.last:
, \
            % endif
        % endfor
    </%def>

    <%def name="layoutVariablesTable(dictArgs, firstColumn=None)">
            <%
                allArgs = [ [ "VAR_INPUT"  , dictArgs["in"]     ],
                            [ "VAR_IN_OUT" , dictArgs["in_out"] ],
                            [ "VAR_OUTPUT" , dictArgs["out"]    ],
                            [ "VAR"        , dictArgs["local"]  ] ]
                noOfArgs = 0
                for kind, args in allArgs:
                    noOfArgs += len(args)
            %>

            <tr>
                %if firstColumn is not None:
                    <th rowspan="${1+noOfArgs}">${firstColumn}</th>
                %endif
                <th>Variable</th>
                <th>Name</th>
                <th>Type</th>
                <th>Initial value</th>
                <th>Address</th>
                <th>Description</th>
                <th>Qualifiers</th>
            </tr>
            % for kind, args in allArgs:
                % for arg in args:
                    % if loop.first:
                        <tr><td rowspan="${len(args)}">${kind}</td>
                    % else:
                        <tr>
                    % endif
                            <td><a href="browse?browse=${arg["qname"]}">${arg["label"]}</a></td>
                            % if (arg["type"] is not None) and (arg["typeLabel"] is not None):
                                <td><a href="software?show_type=${arg["type"]}">${arg["typeLabel"]}</a></td>
                            % elif (arg["pointsToType"] is not None) and (arg["pointsToTypeLabel"] is not None):
                                <td>POINTER TO <a href="software?show_type=${arg['pointsToType']}">${arg["pointsToTypeLabel"]}</a></td>
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
                            <td>${layoutQualifierList(arg["qualifiers"])}</td>
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

    % if show["content"]["fb"] is not None:

        <%
            qname           = show["content"]["qname"]
            label           = show["content"]["label"]
            extends         = show["content"]["extends"]
            fb              = show["content"]["fb"]
            instances       = show["content"]["instances"]
            variables       = fb["variables"]
            inArgs          = variables["in"]
            inCount         = len(inArgs)
            inOutArgs       = variables["in_out"]
            inOutCount      = len(inOutArgs)
            outArgs         = variables["out"]
            outCount        = len(outArgs)
            localArgs       = variables["local"]
            localCount      = len(localArgs)
            methods         = fb["methods"]
            implementation  = fb["implementation"]

        %>

        <h1>FunctionBlock <a href="browse?browse=${qname}">${label}</a></h1>

        <table class="functionblock">
            <tr>
                <td></td>
                <th colspan="2" class="functionblock"><a href="browse?browse=${qname}">${label}</a><br /></th>
                <td></td>
                <td></td>
            </tr>
                    % if extends is not None:
            <tr>
                <td></td>
                <td colspan="2" class="functionblock-extends">EXTENDS <a href="software?show_type=${extends['qname']}">${extends['label']}</a></td>
                <td></td>
            </tr>
                    % endif
            % for i in range(max(inCount + inOutCount, outCount + localCount) ):
            <tr>
                ## left side
                % if i < inCount:
                    <td><div class="functionblock-bar"></div></td>
                    <td class="functionblock-input"><a href="browse?browse=${inArgs[i]["qname"]}">${inArgs[i]["label"]}</a></td>
                % elif i < inCount + inOutCount:
                    <td><div class="functionblock-bar"></div></td>
                    <td class="functionblock-input"><a href="browse?browse=${inOutArgs[i-inCount]["qname"]}">${inOutArgs[i-inCount]["label"]}</a> ${TRIANGLE | n}</td>
                % else:
                    <td></td>
                    <td class="functionblock-input"></td>
                % endif
                ## right side
                % if i < outCount:
                    <td class="functionblock-output"><a href="browse?browse=${outArgs[i]["qname"]}">${outArgs[i]["label"]}</a></td>
                    <td><div class="functionblock-bar"></div></td>
                % elif i < outCount + localCount:
                    % if localCount == 1:
                      <td class="functionblock-local single">
                    % elif i == outCount:
                      <td class="functionblock-local first">
                    % elif i == outCount + localCount - 1:
                      <td class="functionblock-local last">
                    % else:
                      <td class="functionblock-local">
                    % endif
                        <a href="browse?browse=${localArgs[i-outCount]["qname"]}">${localArgs[i-outCount]["label"]}</a>
                      </td>
                    <td><div class="functionblock-bar-small"></div></td>
                % else:
                    <td class="functionblock-output"></td>
                    <td class="functionblock"></td>
                % endif
                <td></td>
            </tr>
            % endfor
            % for method in methods:
            <tr>
                <td></td>
                <td class="functionblock-method" colspan="2"><a href="browse?browse=${method["qname"]}">${method["label"]}( ${layoutArgumentsList(method['variables']['in'])} )</a></td></td>
                <td><div class="functionblock-bar"></div></td>
                <td><div class="functionblock-half-circle"></div></td>
            </tr>
            % endfor
            <tr>
                <td></td>
                <td colspan="2" class="functionblock-below"></td>
                <td></td>
                <td></td>
            </tr>
        </table>

        <h5 class="extraspace">Variable declarations</h5>
        <table class="gridtable">
        ${layoutVariablesTable(dictArgs=fb["variables"])}
        </table>

        <h5 class="extraspace">Implementation</h5>
            % if implementation is not None:
                <table class="gridtable">
                    <tr>
                        <td>
                            <pre>${iec61131.layoutExpressions(implementation)}</pre>
                        </td>
                    </tr>
                </table>
            % endif


        <h5 class="extraspace">Method declarations</h5>


        % for method in methods:
            <ul>
                <li>
                    <h3><a href="browse?browse=${method["qname"]}">${method["label"]}( ${layoutArgumentsList(method['variables']['in'])} )</a></h3>
                    <table class="gridtable align-left">
                        <tr>
                            <!-- Comment -->
                            <th>Comment</th>
                            % if method["comment"] is None:
                                <td colspan="7"></td>
                            % else:
                                <td colspan="7">${method["comment"]}</td>
                            % endif
                        </tr>
                        <tr>
                            <!-- Return type -->
                            <th>Return type</th>
                            % if method["returnType"] is None:
                                <td colspan="7"></td>
                            % else:
                                <td colspan="7"><a href="browse?browse=${method["returnType"]["qname"]}">${method["returnType"]["label"]}</a></td>
                            % endif
                        </tr>
                        ${layoutVariablesTable(dictArgs=method["variables"], firstColumn="Interface")}
                        <tr>
                            <!-- Implementation -->
                            <th>Implementation</th>
                            % if method["implementation"] is None:
                                <td colspan="7"></td>
                            % else:
                                <td colspan="7">
                                    <pre>${iec61131.layoutExpressions(method["implementation"])}</pre>
                                </td>
                            % endif
                        </tr>
                    </table>
                    <br>
                </li>
            </ul>
        % endfor



        <h5 class="extraspace">Instances</h5>
        <table class="gridtable">
            % for instance in instances:
                <tr>
                    <td><a href="browse?browse=${instance["qname"]}">${instance["qname"]}</a></td>
                </tr>
            % endfor
        </table>


        <h5 class="extraspace">PLCopen XML serialization</h5>

            <div id="hidden"><xmp id="xmlcontent">${iec61131.xml_pou_functionBlock(show['content'])}</xmp></div>

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



% else:
    <p>ERROR</p>
% endif

% if show["project"] is not None:

    <%
        designs = show["content"]
    %>

    % for design in designs:

        <%
            specs = design["specs"]
        %>

        <h1>Requirements vs. design matrix for ${design["qname"]}</h1>

        <table class="gridtable">
            <tr>
                <th></th>
                % for spec in specs:
                    <th class="vertical">${spec["label"]}</th>
                % endfor
            </tr>
            <tr>
                <th class="align-left">STATES</th>
                % for spec in specs:
                    <th></th>
                % endfor
            </tr>
            % for state in design["states"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${state["qname"]}">${state["label"]}</a></th>
                    % for spec in specs:
                        % if (spec["qname"] in state["satisfies"]):
                            <td><div tooltip='${state["label"]} satisfies ${spec["label"]}'>S</div></td>
                        % else:
                            <td></td>
                        % endif
                    % endfor

                </tr>
            % endfor
            <tr>
                <th class="align-left">CONSTRAINTS</th>
                % for spec in specs:
                    <th></th>
                % endfor
            </tr>
            % for constraint in design["constraints"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${constraint["qname"]}">${constraint["label"]}</a></th>
                    % for spec in specs:
                        % if (spec["qname"] in constraint["satisfies"]):
                            <td><div tooltip='${constraint["label"]} satisfies ${spec["label"]}'>S</div></td>
                        % else:
                            <td></td>
                        % endif
                    % endfor

                </tr>
            % endfor
            <tr>
                <th class="align-left">PROPERTIES</th>
                % for spec in specs:
                    <th></th>
                % endfor
            </tr>
            % for property in design["properties"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${property["qname"]}">${property["label"]}</a></th>
                    % for spec in specs:
                        % if (spec["qname"] in property["satisfies"]):
                            <td><div tooltip='${property["label"]} satisfies ${spec["label"]}'>S</div></td>
                        % else:
                            <td></td>
                        % endif
                    % endfor

                </tr>
            % endfor

            <tr>
                <th class="align-left">PARTS</th>
                % for spec in specs:
                    <th></th>
                % endfor
            </tr>
            % for part in design["parts"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${part["qname"]}">${part["label"]}</a></th>
                    % for spec in specs:
                        % if (spec["qname"] in part["satisfies"]):
                            <td><div tooltip='${part["label"]} satisfies ${spec["label"]}'>S</div></td>
                        % else:
                            <td></td>
                        % endif
                    % endfor

                </tr>
            % endfor
        </table>

    % endfor

% else:
    <p>ERROR</p>
% endif
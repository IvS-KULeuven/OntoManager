% if show["project"] is not None:

    <%
        reqs     = show["content"]["reqs"]
        concepts = show["content"]["concepts"]
    %>

    % for concept in concepts:

        <h1>Requirements vs. concept matrix for ${concept["qname"]}</h1>

        <table class="gridtable">
            <tr>
                <th></th>
                % for req in reqs:
                    <th class="vertical">${req["label"]}</th>
                % endfor
            </tr>
            <tr>
                <th class="align-left">STATES</th>
                % for req in reqs:
                    <th></th>
                % endfor
            </tr>
            % for state in concept["states"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${state["qname"]}">${state["label"]}</a></th>
                    % for req in reqs:
                        % if (req["qname"] in state["satisfies"]):
                            <td><div tooltip='${state["label"]} satisfies ${req["label"]}'>S</div></td>
                        % else:
                            <td></td>
                        % endif
                    % endfor

                </tr>
            % endfor
            <tr>
                <th class="align-left">CONSTRAINTS</th>
                % for req in reqs:
                    <th></th>
                % endfor
            </tr>
            % for constraint in concept["constraints"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${constraint["qname"]}">${constraint["label"]}</a></th>
                    % for req in reqs:
                        % if (req["qname"] in constraint["satisfies"]):
                            <td><div tooltip='${constraint["label"]} satisfies ${req["label"]}'>S</div></td>
                        % else:
                            <td></td>
                        % endif
                    % endfor

                </tr>
            % endfor
            <tr>
                <th class="align-left">PROPERTIES</th>
                % for req in reqs:
                    <th></th>
                % endfor
            </tr>
            % for property in concept["properties"]:

                <tr class="align-center">

                    <th class="align-left"><a href="browse?browse=${property["qname"]}">${property["label"]}</a></th>
                    % for req in reqs:
                        % if (req["qname"] in property["satisfies"]):
                            <td><div tooltip='${property["label"]} satisfies ${req["label"]}'>S</div></td>
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
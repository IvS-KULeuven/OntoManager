
% if show["project"] is not None:

    % for design in show["content"]:

        <h1>System design specifications for ${design["qname"]}</h1>

        <table class="gridtable">
            <tr>
                <th>Label</th>
                <th>Description</th>
                <th>Derives (&#x2192;) / <div id="gray">Derived from (&#x2190;)</div></th>
            </tr>

        % for spec in design["specs"]:
            <tr>
                <td><a href="browse?browse=${spec["qname"]}">${spec["label"]}</a></td>
                <td>${spec["comment"]}</td>
                <td>
                    <ul class="arrow_forward">
                        % for derives in spec["derives"]:
                            <li><a href="browse?browse=${derives}">${derives}</a></li>
                        % endfor
                        </ul>
                        <ul class="arrow_backward gray">
                        % for derived_from in spec["derived_from"]:
                            <li><a href="browse?browse=${derived_from}" class="lightblue">${derived_from}</a></li>
                        % endfor
                    </ul>
                </td>
            </tr>
        % endfor
        </table>

    % endfor

% else:
    <p>ERROR</p>
% endif

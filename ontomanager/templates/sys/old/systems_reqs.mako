
% if show["project"] is not None:
    <h1>Requirements list for ${show["project"]["qname"]}</h1>

    <table class="gridtable">
        <tr>
            <th>Label</th>
            <th>Description</th>
            <th>Derives (&#x2192;) / <div id="gray">Derived from (&#x2190;)</div></th>
        </tr>
    % for req in show["content"]:
        <tr>
            <td><a href="browse?browse=${req["qname"]}">${req["label"]}</a></td>
            <td>${req["comment"]}</td>
            <td>
                <ul class="arrow_forward">
                % for derives in req["derives"]:
                    <li><a href="browse?browse=${derives}">${derives}</a></li>
                % endfor
                </ul>
                <ul class="arrow_backward gray">
                % for derived_from in req["derived_from"]:
                    <li><a href="browse?browse=${derived_from}" class="lightblue">${derived_from}</a></li>
                % endfor
                </ul>
            </td>
        </tr>
    % endfor
    </table>
% else:
    <p>ERROR</p>
% endif

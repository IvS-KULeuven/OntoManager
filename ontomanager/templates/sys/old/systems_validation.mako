
% if show["project"] is not None:
    <h1>Requirement tests for ${show["project"]["qname"]}</h1>


    <ol>
    % for test in show["content"]:
            <li> <h3><a href="browse?browse=${test["qname"]}">${test["label"]}</a></h3>
                <table class="gridtable align-left">
                    <tr>
                        <th>Description</th>
                        <td>${test["comment"]}</td>
                    </tr>
                    <tr>
                        <th>Asserts</th>
                        <td>
                            % for asserted in test["asserted"]:
                                <a href="browse?browse=${asserted}">${asserted}</a><br />
                            % endfor
                        </td>
                    </tr>
                    <tr>
                        <th>Validates</th>
                        <td>
                            % for validated in test["validated"]:
                                <a href="browse?browse=${validated}">${validated}</a><br />
                            % endfor
                        </td>
                    </tr>
                </table>
                <br>
            </li>
    % endfor
    </ol>


% else:
    <p>ERROR</p>
% endif

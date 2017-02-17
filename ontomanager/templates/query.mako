<%inherit file="base_layout.mako"/>
<%namespace name="misc" file="misc.mako"/>

<%block name="contents">

    <%
        query = U['query']
    %>

    <h1>Query</h1>

    <div id="show" align="center"></div>


    <form  action="/query" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <textarea rows="12" class="queries" name="query">${query['query']}</textarea>
        <input name="submit" type="submit" value="Submit" />
    </form>

    <br />

    <table class="lefttable">
        % if query['results'] is None:
            ${""}
        % elif isinstance(query['results'], Exception):
            ERROR:<br />
            <div id="errormessagebox">${str(query['results'])}</div>
        % else:
            % if query['results'].type == 'ASK':
                ${query['results'].askAnswer}
            % elif query['results'].type == 'SELECT':
                <tr>
                % for var in query['results'].vars:
                    <th>${var}</th>
                % endfor
                </tr>
                % for row in query['results']:
                <tr>
                    % for result in row:
                        % if M['functions']['IS_URI'](result):
                            <%
                                resultQname = M['functions']['URI_TO_QNAME'](result)
                            %>
                            % if CACHE.has_key(resultQname):

                                ##<td>---${CACHE[resultQname]}</td>
                                <td>${misc.render_view_link(CACHE[resultQname], contents=resultQname)}</td>
                            % else:
                                <td><a href="browse?show;qname=${resultQname}">${resultQname}</a></td>
                            % endif
                        % else:
                            <td>${str(result)}</td>
                        % endif
                    % endfor
                </tr>
                % endfor
            % else:
                type: ${query['results'].type} <br />
                results: ${query['results']} <br />
            % endif
        % endif
    </table>


</%block>

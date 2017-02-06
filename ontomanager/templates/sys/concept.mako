<%namespace name="misc" file="../misc.mako"/>
<%namespace name="requirement" file="requirement.mako"/>
<%namespace name="test" file="test.mako"/>

<%
    # define nodes
    concept = CACHE[U['sys']["show"]["qname"]]
    reqs =  [ CACHE[r] for r in concept["requirements"] ]
    tests =  [ CACHE[t] for t in concept["tests"] ]
    designs =  [ CACHE[d] for d in concept["designs"] ]
%>

<h1>Concept "${concept["label"]}"</h1>

${misc.render_comment_below_title(concept)}


########################################################################################################################
## Jump to
########################################################################################################################

<div class="jump-to">
Jump to:
<ul>
    <li><a href="#section-requirements">Requirements</a></li>
    <li><a href="#section-tests">Tests</a></li>
    <li><a href="#section-designs">Designs</a></li>
</ul>
</div>

########################################################################################################################
<a name="section-requirements"></a>
<h2>Requirements</h2>

<h4>Flat list:</h4>

<table class="lefttable">
    ${requirement.render_one_table_row(None, header=True)}
    % for req in reqs:
        ${requirement.render_one_table_row(req)}
    % endfor
</table>

<h4>Derivation matrix:</h4>

${render_req_vs_req(concept)}

<%def name="render_req_vs_req(concept)">
    <%
    requirements = []
    tests = []

    for qname in concept["requirements"]:
        requirements.append(CACHE[qname])

    for qname in concept["tests"]:
        tests.append(CACHE[qname])
    %>

    <table class="gridtable">
        <tr>
            <th></th>
            % for req in requirements:
                <th class="vertical">${req['label']}</th>
            % endfor
        </tr>
        % for hReq in requirements:
            <tr class="align-center">
                <th class="align-left"><div tooltip='${hReq["comment"]}'>${misc.render_view_link(hReq)}</div></th>
                % for vReq in requirements:
                    % if hReq["uri"] == vReq["uri"]:
                        <th></th>
                    % else:
                            % if (vReq["qname"] in hReq["derives"]) and (hReq["qname"] in vReq["derives"]):
                                <td><div tooltip='${vReq["label"]} derives ${hReq["label"]} and vice versa'>&#x2922;</div></td>
                            % elif vReq["qname"] in hReq["derives"]:
                                <td><div tooltip='${hReq["label"]} derives ${vReq["label"]}'>&#x2197;</div></td>
                            % elif hReq["qname"] in vReq["derives"]:
                                <td><div tooltip='${hReq["label"]} isDerivedBy ${vReq["label"]}'>&#x2199;</div></td>
                            % else:
                                <td></td>
                            % endif
                    % endif
                % endfor
            </tr>
        % endfor
    </table>
</%def>




<br/>
########################################################################################################################
<a name="section-tests"></a>
<h2>Tests</h2>


<table class="lefttable">
    ${test.render_one_table_row(None, header=True)}
    % for t in tests:
        ${test.render_one_table_row(t)}
    % endfor
</table>




<br/>
########################################################################################################################
<a name="section-designs"></a>
<h2>Designs</h2>

% if len(designs) == 0:
    <h2>&#8627; NO DESIGNS DEFINED!</h2>
% elif len(designs) == 1:
    <h2>&#8627; design defined for this concept: ${misc.render_view_link(designs[0])}</h2>
% else:
    %for i in xrange(len(designs)):
        &#8627; design ${i}: ${misc.render_view_link(designs[i])}
    %endfor
% endif

<br/>
<br/>
<br/>
<br/>
<%namespace name="misc" file="../misc.mako"/>
<%namespace name="requirement" file="requirement.mako"/>
<%namespace name="test" file="test.mako"/>

<%
    import collections

    # define nodes
    design = CACHE[U['sys']["show"]["qname"]]

    reqs   = [ CACHE[qname] for qname in design["requirements"] ]
    rreqs  = [ CACHE[qname] for qname in design["realized_requirements"] ]
    tests  = [ CACHE[qname] for qname in design["tests"] ]
    parts  = [ CACHE[qname] for qname in design["parts"] ]
    realizes  = [ CACHE[qname] for qname in design["realizes"] ]

    externalReqs = []
    for req in reqs:
        for kind in ['derives', 'derived_from']:
            for d in req[kind]:
                if (d not in design["requirements"]) and (d not in externalReqs):
                    externalReqs.append(d)
    externalReqsPerSystem = collections.OrderedDict()

    for rreq in rreqs:

        for declaredBy in rreq['declared_by']:

            externalReqsPerSystem[declaredBy] = CACHE[declaredBy]["requirements"]

%>


<h1>Design ${misc.render_view_link(design, "title")}</h1>

% if len(realizes) == 0:
    <h2>&#8627; NOT REALIZING ANY CONCEPT!</h2>
% elif len(realizes) == 1:
    <h2>&#8627; realizes: ${misc.render_view_link(realizes[0])}</h2>
% else:
    %for i in range(len(realizes)):
        &#8627; realizes ${i}: ${misc.render_view_link(realizes[i])}
    %endfor
% endif

${misc.render_comment_below_title(design)}

########################################################################################################################
## Jump to
########################################################################################################################

<div class="jump-to">
Jump to:
<ul>
    <li><a href="#section-requirements">Requirements</a></li>
    <li><a href="#section-parts">Parts</a></li>
</ul>
</div>
########################################################################################################################


########################################################################################################################
<a name="section-requirements"></a>
<h2>Requirements</h2>

<table class="lefttable">
    ${requirement.render_one_table_row(None, header=True)}
    % for req in reqs:
        ${requirement.render_one_table_row(req)}
    % endfor
</table>

<h4>Realized requirements:</h4>

<table class="lefttable">
    % for req in rreqs:
        % if loop.index != 0:
,
        % endif
${misc.render_view_link(req)}\
    % endfor
</table>

<h4>Derivation matrix:</h4>

<table class="gridtable">
    <tr>
        <th rowspan="2"></th>
        <th colspan="${len(reqs)}">${misc.render_view_link(design, "table_firstrow")}</th>
        ## add the systems containing the external requirements
        % for (sysQName, reqQNames) in externalReqsPerSystem.items():
            <th colspan="${len(reqQNames)}">${misc.render_view_link(CACHE[sysQName], "table_firstrow")}</th>
        % endfor
    </tr>
    <tr>
        ## headers
        % for req in reqs:
            <th class="vertical">${req['label']}</th>
        % endfor
        % for (sysQName, vReqQNames) in externalReqsPerSystem.items():
            % for vReqQName in vReqQNames:
                <th class="vertical">${CACHE[vReqQName]['label']}</th>
            % endfor
        % endfor
    </tr>
    % for hReq in reqs:
        <tr class="align-center">
            <th class="align-left"><div tooltip='${hReq["comment"]}'><a href="sys?show=design;qname=${hReq["qname"]}">${hReq["label"]}</a></div></th>
            % for vReq in reqs:
                ${render_requirements_cell(hReq, vReq)}
            % endfor
            % for (sysQName, vReqQNames) in externalReqsPerSystem.items():
                % for vReqQName in vReqQNames:
                    ${render_requirements_cell(hReq, CACHE[vReqQName])}
                % endfor
            % endfor
        </tr>
    % endfor
</table>




<%def name="render_requirements_cell(hReq, vReq)">\
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
                <td>
                % for deriv in hReq["derived_from"]:
                    % if "realizes" in CACHE[deriv]:
                        % if vReq["qname"] in CACHE[deriv]['realizes']:
                            &#x2199;
                        % endif
                    % endif
                % endfor
                </td>
            % endif
    % endif
</%def>


<br/>
########################################################################################################################
<a name="section-parts"></a>
<h2>Parts</h2>

<ul>
%for i in range(len(parts)):
   <li> <h4>&#8627; Part: ${misc.render_view_link(parts[i])} </h4></li>
%endfor
</ul>

<br/>
<br/>
<br/>
<br/>

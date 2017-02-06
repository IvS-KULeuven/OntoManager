<%namespace name="misc" file="../misc.mako"/>

<%
    project = CACHE[U['sys']["show"]["qname"]]
    concepts = [ CACHE[c] for c in project["concepts"] ]
%>


<h1>Project "${project["label"]}"</h1>

${misc.render_comment_below_title(project)}

% if len(concepts) == 0:
    <h2>&#8627; NO CONCEPTS DEFINED!</h2>
% elif len(concepts) == 1:
    <h2>&#8627; concept defined within this project: ${misc.render_view_link(concepts[0])}</h2>
% else:
    %for i in xrange(len(concepts)):
        &#8627; concept ${i}: ${misc.render_view_link(concepts[i])}
    %endfor
% endif
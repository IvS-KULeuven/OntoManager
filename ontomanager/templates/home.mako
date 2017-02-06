<%inherit file="base_layout.mako"/>

<%block name="contents">

<h1>Home for user '${user_id}'</h1>



<br />
<h3>Admin:</h3>
<div class="align-left">
    <form action="/logout" method="post">
        <div class="form-group">
          <button type="submit" name="logout.submitted" value="Log out" class="button">Log out</button>
        </div>
    </form>
</div>

<br />
<h3>Groups you belong to:</h3>
<ul>
% for group in user_groups:
    <li>${group}</li>
% endfor
</ul>

<br />
<h3>Files in your account folder:</h3>
<ul>
% for fileName in home_files:
    <%
        import os
        filePath = os.path.join('home', user_id, fileName)
        fileUrl = request.static_url("ontomanager:%s" %filePath)
    %>
    <li><a href="${fileUrl}">${fileName}</a></li>
% endfor
</ul>

</%block>

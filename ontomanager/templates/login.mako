<%inherit file="base_layout.mako"/>


<%block name="contents">

  <p></p>
  <p></p>
  <p></p>

  <div class="align-center">

  <div id="loginbox">


  <h1>Login required</h1>


  <div class="align-right">
  <form action="${authentication['url']}" method="post">

    <input type="hidden" name="came_from" value="${authentication['came_from']}">
    <div class="form-group">
      <label for="login">Username</label>
      <input type="text" name="login" value="${authentication['login']}">
    </div>
    <div class="form-group">
      <label for="password">Password</label>
      <input type="password" name="password" value="${authentication['password']}">
    </div>
    <div class="form-group">
      <button type="submit" name="form.submitted" value="Log In" class="button">Log In</button>
    </div>
  </form>
  </div>

  </div>

<br />
<br />
% if authentication['message'] is not None and authentication['message'] != '':
    <div id="errormessagebox">${authentication['message']}</div>
% endif


  </div>
</%block>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:metal="http://xml.zope.org/namespaces/metal"
      xml:lang="en">
<head>
  <title>${M['project']}</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />
  <link rel="shortcut icon" href="${request.static_url('ontomanager:static/favicon.ico')}" />
  <link rel="stylesheet" href="${request.static_url('ontomanager:static/pylons.css')}" type="text/css" media="screen" charset="utf-8" />
  <link rel="stylesheet" src="${request.static_url('ontomanager:static/popup.css')}" />
  <script src="${request.static_url('ontomanager:static/jquery-1.11.3.min.js')}"></script>
  <!-- add script to rotate the contents of a table cell -->
  <script type="text/javascript" src="${request.static_url('ontomanager:static/jquery.rotateTableCellContent.js')}"></script>

  <!-- jstree -->
  <link rel="stylesheet" href="${request.static_url('ontomanager:static/jstree/themes/default/style.min.css')}" />
  <script type="text/javascript" src="${request.static_url('ontomanager:static/jstree/jstree.js')}"></script>

    <!-- dd menu -->
    <script type="text/javascript">
            <!--
            var timeout         = 100;
            var closetimer		= 0;
            var ddmenuitem      = 0;

            // open hidden layer
            function mopen(id)
            {
                // cancel close timer
                mcancelclosetime();

                // close old layer
                if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';

                // get new layer and show it
                ddmenuitem = document.getElementById(id);
                ddmenuitem.style.visibility = 'visible';

            }
            // close showed layer
            function mclose()
            {
                if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
            }

            // go close timer
            function mclosetime()
            {
                closetimer = window.setTimeout(mclose, timeout);
            }

            // cancel close timer
            function mcancelclosetime()
            {
                if(closetimer)
                {
                    window.clearTimeout(closetimer);
                    closetimer = null;
                }
            }

            // close layer when click-out
            document.onclick = mclose;
            // -->
    </script>






</head>
<body>
  <div id="wrap">
    <div id="top">
      <div class="top">
          <div class="align-center">
            <div class="top-text">${M['project']}</div>
          </div>
##          <div class="logged-in">
##            ${user_id}
##          </div>
      </div>
    </div>
    <div id="middle">
      <div class="middle align-center">



##        <div id="menu_reset">
##            <a href="problems?reset"><img src="${request.static_url('ontomanager:static/refresh.png')}" width="20" height="20"></a>
####            <a href="#" class="html_popup"><img src="${request.static_url('ontomanager:static/refresh_green.png')}" width="20" height="20"></a>
##        </div>

        <ul class="menu">
          % for item in M['menu_items']:
            % if current_page == item["name"]:
                <li class="menu_item_current">
            % else:
                <li class="menu_item">
            % endif
            <a href=${item["target"]}>${item["name"]}</a></li>
          % endfor
        </ul>

      </div>
    </div>
    <div id="bottom">
      <div class="bottom">

        <%block name="contents"/>

      </div>
    </div>
  </div>

    <!-- add script to display popups -->
    <script type="text/javascript" src="${request.static_url('ontomanager:static/jquery.popup.js')}"></script>

    <script type="application/javascript" language="JavaScript">
        $(function(){
            $('a.popup').popup();
            $('.html_popup').popup({
                content : '<h1>This is some HTML</h1>',
                type : 'html'
            });
        });
    </script>

</body>
</html>

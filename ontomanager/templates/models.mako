<%inherit file="base_layout.mako"/>

<%block name="contents">

    <%
        import json
        jsonTree = json.dumps(M['models'])
        shown_file  = U['models']["shown_file"]
    %>

    <div id="left">

        <h2>Models</h2>

        <style media="screen" type="text/css">
            .folder>i.jstree-checkbox
            {
                display:none
            }
        </style>

        <div id="run_models_tree"></div>

        <script type="application/javascript" language="JavaScript">
        <%
        %>
        var restored = false;
        $('#run_models_tree')
        .jstree({
            'plugins':["types", "state"],
            'core' : {
                'data' : ${jsonTree | n}
            },
            "state" : { "key" : "state_of_the_model_tree" },
            "types" :
            {
               "file"   :  { 'icon' : "${request.static_url('ontomanager:static/document_16x16.png')}" },
               "folder" :  { 'icon' : "${request.static_url('ontomanager:static/folder_open_yellow_16x16.png')}" }
            }

        })
       .on('restore_state.jstree', function () {
           console.log("starting restoring jstree");
           restored = true;
           $('#run_models_tree').on( 'select_node.jstree',
               function(e, data) {
                    data.instance.save_state();
                    $.post("models", { "models_tree_clicked" : data.node.id } );
                    location.reload();
                });
       }).bind('ready.jstree', function(e, data) {
           if (!restored) {
               console.log("Not restored --> bind select_node");

               $('#run_models_tree').on( 'select_node.jstree',
                   function(e, data) {
                        data.instance.save_state();
                        $.post("models", { "models_tree_clicked" : data.node.id } );
                        location.reload();
                    });
           }
           else {
               console.log("finished restoring jstree");
           }
        });
        </script>



        </div>


        <div id="right">
          <div id="editor-container">
              % if shown_file is not None:
                  <h2>Model: ${shown_file["path"]}</h2>

                  <table class="gridtable">
                    <tr>
                        <th>Prefix</th>
                        <td>${shown_file['prefix']}</td>
                    </tr>
                    <tr>
                        <th>URI</th>
                        <td>${shown_file['uri']}</td>
                    </tr>
                  </table>

                 <div id="editor">${shown_file["contents"]}</div>
                  <script src="${request.static_url('ontomanager:static/ace/src-min-noconflict/ace.js')}" type="text/javascript" charset="utf-8"></script>
                  <script>
                      var editor = ace.edit("editor");
                      //editor.setTheme("ace/theme/tomorrow_night_blue");
                      editor.setTheme("ace/theme/textmate");
                      editor.getSession().setMode("ace/mode/coffee");
                  </script>
              % endif
          </div>


        </div>

</%block>

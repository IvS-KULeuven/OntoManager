<%inherit file="base_layout.mako"/>

<%block name="contents">

    <%
        dataset = M['dataset']
    %>


    <h1>DATASET</h1>

  <div id="freeleft">

    <h2>Select data source</h2>

    % for checkboxName in dataset["repository_checkboxes"]:
         <h3><input type="radio" id="checkbox_repo_${checkboxName}" name="repos" />${dataset[checkboxName]['comment']}</h3>
    % endfor

    <br/>

    <h2>Pre-process data</h2>

    <h3><input type="checkbox" id="checkbox_run_metamodels" /> Run metamodels</h3>

    <h3><input type="checkbox" id="checkbox_run_models" /> Run models</h3>

    <style media="screen" type="text/css">
        .folder>i.jstree-checkbox
        {
            display:none
        }
    </style>

        <div id="run_models_tree"></div>

        <script type="application/javascript" language="JavaScript">
        <%
            import json
            jsonTree = json.dumps(dataset["run_models"]["tree"])
        %>
        $('#run_models_tree')
        .jstree({
            'plugins':["checkbox", "types"],
            'core' : {
                'data' : ${jsonTree | n}
            },//"checkbox": { //"two_state": true, //"whole_node" : false //,//"keep_selected_style" : false},
            "types" :
            {
               "file"   :  { 'icon' : "${request.static_url('ontomanager:static/document_16x16.png')}" },
               "folder" :  { 'icon' : "${request.static_url('ontomanager:static/folder_open_yellow_16x16.png')}" }
            }

        })
        .on( 'select_node.jstree', function(e, data) { $.post("dataset", { "run_models_tree_checked" : data.node.id } ); })
        .on( 'deselect_node.jstree', function(e, data) { $.post("dataset", { "run_models_tree_unchecked" : data.node.id } ); });
        </script>


    <h3><input type="checkbox" id="checkbox_run_inferences" /> Run inferences</h3>

    <br/>


    <h2>Load data</h2>

    <h3><input type="checkbox" id="checkbox_load_asserted" /> Load asserted data</h3>

    <div id="load_asserted_tree"></div>

    <h3><input type="checkbox" id="checkbox_load_inferred" /> Load inferred data</h3>

    <br/>


    <h2>Post-process data (optional)</h2>

      % for fileType in ["plcopen", "pyuaf"]:

            <%
                if fileType == "plcopen":
                    fileTypeTitle = "PLCOpen"
                elif fileType == "pyuaf":
                    fileTypeTitle = "PyUAF"
                else:
                    fileTypeTitle = fileType
            %>

            <h3><input type="checkbox" id="checkbox_generate_${fileType}" /> Generate ${fileTypeTitle} files</h3>

            <style media="screen" type="text/css">
                .folder>i.jstree-checkbox
                {
                    display:none
                }
            </style>


            <div id="generate_${fileType}_tree"></div>

            <script type="application/javascript" language="JavaScript">
            <%
                import json
                jsonTree = json.dumps(dataset["generate_%s" %fileType]["tree"])
            %>
            $('#generate_${fileType}_tree')
            .jstree({
                'plugins':["checkbox", "types"],
                'core' : {
                    'data' : ${jsonTree | n}
                },//"checkbox": { //"two_state": true, //"whole_node" : false //,//"keep_selected_style" : false},
                "types" :
                {
                   "file"   :  { 'icon' : "${request.static_url('ontomanager:static/document_16x16.png')}" },
                   "folder" :  { 'icon' : "${request.static_url('ontomanager:static/folder_open_yellow_16x16.png')}" }
                }

            })
            .on( 'select_node.jstree', function(e, data) { $.post("dataset", { "generate_${fileType}_tree_checked" : data.node.id } ); })
            .on( 'deselect_node.jstree', function(e, data) { $.post("dataset", { "generate_${fileType}_tree_unchecked" : data.node.id } ); });
            </script>
      % endfor


    <h3><input type="checkbox" id="checkbox_save_cache" /> Save cache</h3>

    <br/>


    <form  action="/dataset" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <input name="submit" type="submit" value="Start processing" />
    </form>

    <br/>

    <script type="application/javascript" language="JavaScript">
    $(document).ready(function() {
        % for checkbox in dataset["main_checkboxes"]:
            // set initial state.
            $('#checkbox_${checkbox}').prop( "checked", ${str(dataset[checkbox]["checked"]).lower()} );
            // post on change
            $('#checkbox_${checkbox}').change(function() {
                %if checkbox in ["run_models", "generate_plcopen", "generate_pyuaf"]:
                    $.post("dataset",
                            { '${checkbox}_checked'    : $(this).is(':checked') },
                            // update visibility by success function:
                            function(){
                                if ($('#checkbox_${checkbox}').is(':checked')) {
                                    $('#${checkbox}_tree').show();
                                } else {
                                    $('#${checkbox}_tree').hide();
                                }
                            } );
                %else:
                    $.post("dataset", { '${checkbox}_checked'    : $(this).is(':checked') } );
                %endif

            });

            %if checkbox in ["run_models", "generate_plcopen", "generate_pyuaf"]:
                // set initial visibility
                if ($('#checkbox_${checkbox}').is(':checked')) {
                    $('#${checkbox}_tree').show();
                } else {
                    $('#${checkbox}_tree').hide();
                }
            %endif
        % endfor

        % for checkbox in dataset["repository_checkboxes"]:
            // set initial state.
            $('#checkbox_repo_${checkbox}').prop( "checked", ${str(dataset[checkbox]["checked"]).lower()} );
            // post on change
            $('#checkbox_repo_${checkbox}').change(function() {
            $.post("dataset", { '${checkbox}_checked'    : $(this).is(':checked') } );
            // sleep a few seconds, so that the python code has updated the tree, before reloading the page
            setTimeout(function() {
                window.location.reload();
            }, 3000);
            });
        % endfor
    });
    </script>


    <hr />


    <script language="JavaScript">
    function confirmSubmit(text) {
        var agree=confirm(text);
        if (agree)
            return true;
        else
            return false;
    }
    </script>

    <form  action="/dataset" method="post" accept-charset="utf-8" enctype="multipart/form-data">
        <input name="cache" type="submit" value="Load cache" onClick="return confirmSubmit('Are you sure that you want to load a previously saved cache from disk? \n\nOnly proceed if you\'re sure that the models or metamodels have not changed since the cache file was saved.')" />
        <input name="cache" type="submit" value="Save cache" onClick="return confirmSubmit('Are you sure that you want to save the current cache to disk?\n\nThis action will overwrite the existing saved cache file.')" />
    </form>



  </div>

  <div id="freeright">

    <div id="hidden"><xmp id="xmlcontent">${dataset['output'] | n}</xmp></div>

    <div id="xmleditor"></div>
    <script src="${request.static_url('ontomanager:static/ace/src-min-noconflict/ace.js')}" type="text/javascript" charset="utf-8"></script>
    <script>
      var editor = ace.edit("xmleditor");
      editor.setTheme("ace/theme/textmate");
      editor.setReadOnly(true);
      editor.getSession().setValue($("#xmlcontent").text());
      editor.renderer.setShowGutter(false);
      editor.setReadOnly(true);
      editor.resize(true); // needed for scrolling

      session = editor.getSession();
      count = session.getLength();
      //Go to end of the last line
      editor.gotoLine(count, session.getLine(count-1).length);
      editor.scrollToLine(count, true, true, function () {});

    % if dataset["thread_running"]:
            setTimeout(function () {
                window.location.reload(1);
            }, 1000);


    % endif

    </script>

  </div>

</%block>

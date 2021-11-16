============================
Modeling workflow help
============================

This guide assumes you have installed and configured:

- OntoManager_ : the OntoManager web-server
- Ontoscript_  : the DSL (domain-specific language) to model the Mercator Telescope Control System (TCS)
- MTCS-models_ : the models of the Mercator TCS
- MTCS_        : the TwinCAT 3 software of the Mercator Telescope Control System (TCS) (a private GitHub project)
- MOCS_        : the Python software of the Mercator Observatory Control System (OCS) (a private GitHub project)



-----------------------------
Step 1: check OntoManager
-----------------------------

Check if you can log into OntoManager:

#. Make a VPN connection

#. Surf to the OntoManager URL (e.g. http://machine:8080 )

#. Log in with your credentials. These credentials are specified in the ``ontomanager/config/config.ini`` file.

#. In the **Dataset** page, check if you can select your personal data source. If not, configure your data source in ``ontomanager/config/config.ini``.


If you cannot access OntoManager, then maybe OntoManager must be restarted:

.. code:: bash

   # log into the machine
   ssh administrator@machine

   # see if there is a screen that you can resume
   screen -r

   # if no screen was open, then start a new screen using the "screen" command

   # start the OntoManager application as explained in the README.md file
   cd /some/path/ontomanager
   export PYTHONPATH=/some/path/ontomanager/OntoManager/
   export NODE_PATH=/some/path/Ontoscript
   ./bin/pserve OntoManager/production.ini


-----------------------------
Step 2: Start modeling
-----------------------------

The models that you create or edit must be visible as a data source to OntoManager. You can do this in two ways:

- clone the MTCS-models_ project once on your laptop, and once on the host machine of OntoManager.
  Edit all files on your laptop, and push them from there to your personal github fork. Then, pull the
  changes in the clone at the host machine of OntoManager.

- clone the MTCS-models_ once on a shared directory, and mount this directory on your laptop and on
  the host machine of OntoManager.


If you want to create new models, simply create empty ``.coffee`` files, and add the following basic code (e.g. for a software model):

.. code:: coffeescript

    require "ontoscript"

    REQUIRE "models/mtcs/common/software.coffee"

    MODEL "http://www.mercator.iac.es/onto/models/mtcs/axes/software" : "axes_soft"

    axes_soft.IMPORT common_soft

    # add a library, function blocks, enumerations, ...

    axes_soft.WRITE "models/mtcs/axes/software.jsonld"

To know how to model, look at the existing examples and the REFERENCE_SOFTWARE.rst_ help file of the MTCS-models_ project.

Since we expect that all subsystems of the Mercator telescope are already defined, probably you just need to edit the existing models (and not create new ones). Just edit them in your favourite editor with coffeescript syntax highlighting.

-------------------------------------------------
Step 3: Run the models and generate source code
-------------------------------------------------

#. In the **Dataset** page of OntoManager, make sure that the correct data source is selected,
   so that your changes are visible to OntoManager. You can verify this by going to the **Models**
   page, and look at the models that you just created or edited.

#. In the **Dataset** page, **select the model(s) that you edited**. Almost always, you must select
   only one file. This is because the models represent a tree of models that REQUIRE ("import")
   each other. If you select the top of the tree, then all down-level (required) models will be run anyhow.    The top-level software model, for the Mercator TCS, is the ``models/mtcs/softaware.coffee`` file.

#. Click on the **"Start processing" button** to run the models. This takes a few minutes. If there is an error, execution will stop and you'll see some debugging info. Correct the models, and press the button again (it will re-read the models from disk).

#. If the models have been run successfully, you can now load them into memory: **select "Load asserted data"**. You can also select the source code files that you want to generate. Obviously, if you only changed the dome software model (``mtcs/dome/software.coffee``) then you only have to generate the ``mtcs_dome`` source code. Press the **"Start processing" button**.

#. When the data has been loaded into memory (and source has been generated), you can now click on the Systems, Mechanics, Electronic, and Software tab. To download the earlier generated source code, **go to the Software tab and click on the generated library** (e.g. ``mtcs_dome``). Note that if you click on another library which hasn't been generated yet, the web page will take a few minutes to open since many queries have to be executed. You can now download the PLC code (PLCopen XML) or python code (PyUAF).

-------------------------------------------------
Step 4: Import the PLC code in TwinCAT
-------------------------------------------------

#. In your Windows environment, open a web-browser, login to OntoManager, go to the Software tab, click on the libraries that you have changed, and then click on the "Download PLCopen XML" button each time.

#. In TwinCAT 3, open the MTCS_ project, and go to the correct subsystem. Right-click on the Generated directory, and import the PLCopen XML file that we just generated.

#. For more info about the software, see the HELP file of the MTCS project.

-------------------------------------------------
Step 5: Copy the Python code into MOCS
-------------------------------------------------

#. Download the file (e.g. ``mtcs_dome.py``) and copy it to ``$MHOME/python/mocsopcua/models/``.

#. Commit the changes to the MOCS repository.




.. _OntoManager: http://github.com/IvS-KULeuven/OntoManager
.. _Ontoscript:  http://github.com/IvS-KULeuven/Ontoscript
.. _MTCS-models: http://github.com/IvS-KULeuven/MTCS-models
.. _MTCS: http://github.com/IvS-KULeuven/MTCS
.. _MOCS: http://github.com/IvS-KULeuven/MOCS
.. _REFERENCE_SOFTWARE.rst: http://github.com/IvS-KULeuven/MTCS-models/blob/master/REFERENCE_SOFTWARE.rst

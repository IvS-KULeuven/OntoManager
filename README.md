OntoManager README
==================

OntoManager is a web-based application to facilitate ontology-based development of
industrial control systems (in particular, those of astronomical telescopes).

See ontomanager_introduction_paper_ICALEPCS_2015.pdf for a quick intro.


How to install:
---------------

    cd /some/path/
    mkdir ontomanager
    cd ontomanager
    sudo easy_install virtualenv
    virtualenv .
    git clone https://github.com/IvS-KULeuven/OntoManager.git
    ./bin/python OntoManager/setup.py install
    # setup.py may fail because the installation order of some dependencies
    # is incorrectly configured. Simply run it again, if needed:
    ./bin/python OntoManager/setup.py install


How to install other dependencies:
----------------------------------

To execute Ontoscript models, you need to install the following:

* Ontoscript

      cd /some/path
      git clone https://github.com/IvS-KULeuven/Ontoscript

* coffee-script

      sudo dnf install coffee-script
      # in the above line, dnf is the package manager for fedora
      # this should automatically install Node.js (package 'nodejs'), as well.

* (Optional) inference engine

  Download and install SPIN API
  (http://www.topquadrant.com/repository/spin/org/topbraid/spin/).

  You'll also need to install its main dependency: Apache Jena
  (http://jena.apache.org).

  SPIN API and Jena are only required to verify and analyze models.

  For common tasks (browsing the HTML web pages, generating PLCopen XML
  and PyUAF source code), the inference engine is not needed.


How to configure:
-----------------

    cd /some/path/ontomanager
    # make a directory to store all generated files:
    mkdir generated
    # create a configuration file by copying the example configuration file:
    cp OntoManager/ontomanager/config/example_config.ini OntoManager/ontomanager/config/config.ini

Then, edit the config.ini file.
Set the paths of the config file to the previously configured locations, such as:

    [general]
    coffee = /usr/bin/coffee

    [user_wim]
    ontologies_dir = /some/path/MTCS-models/ttl/metamodels
    coffee_dir     = /some/path/MTCS-models/coffee
    generated_dir  = /some/path/generated
    comment        = "Wim's home repo"


How to run:
-----------

    cd /some/path/ontomanager
    export PYTHONPATH=/some/path/ontomanager/OntoManager/
    export NODE_PATH=/some/path/Ontoscript
    ./bin/pserve OntoManager/production.ini

(optional flag: --reload to restart the server whenever one of the python files is changed)

Now open your web-browser and surf to http://localhost:8080


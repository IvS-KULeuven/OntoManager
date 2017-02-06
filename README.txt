OntoManager README
==================



How to install:
---------------

$ mkdir ontomanager
$ cd ontomanager
$ sudo easy_install virtualenv
$ virtualenv .
$ cp -R $REPOSITORY/OntoManager .
$ ./bin/python OntoManager/setup.py install



How to run:
-----------

$ cd OntoManager
$ ../bin/pserve production.ini

(optional flag: --reload to restart the server whenever one of the python files is changed)

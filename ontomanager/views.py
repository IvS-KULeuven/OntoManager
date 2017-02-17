# python system libraries
import subprocess
from collections import OrderedDict
import urllib
import threading
import pprint
import os
import pickle
import sys

# pyramid librariies
from pyramid.renderers import render
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.response import FileResponse
from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember, forget

# ontomanager libraries
import ontomanager
from ontomanager import ontologies, triplestore, soft, problems, util, generic, dataset, rdfconvert, elec, logging, configuration
from ontomanager.triplestore import GET_GRAPH, CREATE_GRAPH, FIND_FILES, CLEAR_GRAPH, LOAD_MINIMAL_CONTEXT, LOG_CONTEXT, IS_QNAME, IS_URI, URI_TO_QNAME, QUERY
from ontomanager.register import REGISTRY
from ontomanager.logging import INFO, DEBUG, LOG, ERROR, do_DEBUG
from ontomanager.configuration import USERS, HOMES
from tests import TESTQUERY

# since the config has been read, we can set the loglevel
logging.SET_LOGLEVEL(configuration.LOGLEVEL)

# some queries form a deep cascade of new queries, so therefore we set the recursion limit to a high number
sys.setrecursionlimit(sys.getrecursionlimit() * 10)
DEBUG("New recursion limit: %d" %sys.getrecursionlimit())


###################################################################################################
# the CACHE memory of our application is a global variable
CACHE = {}
###################################################################################################


# =================================================================================================
def buildResponse(request, currentPage):
    """
    Build a response (a dictionary) to a HTTP request.

    The contents of this response will be accessible from within the templates.
    """
    global M
    global U
    global CACHE

    # find out the user ID
    userId = request.authenticated_userid

    # we always require a user
    if userId is None:
        userId = "guest"

    # build the response structure
    d = dict(
        M = M,
        CACHE = CACHE,
        user_id = userId,
        user_groups = ontomanager.configuration.groupfinder(userId, request),
        current_page = currentPage,
        U = U[userId]
    )

    return d


# =================================================================================================
class Model(dict):
    """
    A Model in the Model-View-Controller paradigm holds all information that must be displayed.
    """

    def __init__(self):
        """
        Create the model.
        """
        # initialize the dictionary
        dict.__init__(self)

        # clear the cache
        global CACHE
        CACHE = {}

        # create the basic graph
        CREATE_GRAPH()

        # load a minimal context, so that we can already execute some queries
        LOAD_MINIMAL_CONTEXT()

        # reset the application
        self.reset()


    def reset(self):
        """
        Reset the application.

        Resetting means: put OntoManager in its initial state, before the user
        started clicking on things and before queries were executed by the user.
        The configuration file (config/config.ini) will be re-read.
        """
        LOG("Resetting...")

        # build the main structure of the dictionary
        self["logged_in"] = None
        self["authentication"] = None
        self["DEBUG"] = False
        self["functions"]    = { "PARSE_FOR_URI"        : triplestore.PARSE_FOR_URI,
                                 "IS_URI"               : triplestore.IS_URI,
                                 "URI_TO_QNAME"         : triplestore.URI_TO_QNAME,
                                 "SOFT_GET_FILEPATH"    : soft.GET_FILEPATH }
        self["project"]      = 'OntoManager @ Mercator Telescope'
        self["menu_items"]   = [ { 'name'   : 'Home',
                                   'target' : '/' },
                                 { 'name'   : 'Models',
                                   'target' : '/models' },
                                 { 'name'   : 'Dataset',
                                   'target' : '/dataset' },
                                 { 'name'   : 'Problems',
                                   'target' : '/problems' },
                                 { 'name'   : 'Browse',
                                   'target' : '/browse' },
                                 { 'name'   : 'Query',
                                   'target' : '/query' },
                                 { 'name'   : 'Systems',
                                   'target' : '/sys' },
                                 { 'name'   : 'Mechanics',
                                   'target' : '/mech' },
                                 { 'name'   : 'Electronics',
                                   'target' : '/elec' },
                                 { 'name'   : 'Software',
                                   'target' : '/soft' } ]
        self["dataset"] = {}
        self["dataset"]["output"] = ""
        self["dataset"]["thread_running"] = False
        self["dataset"]["main_checkboxes"] = [ "run_metamodels",
                                               "run_models",
                                               "run_inferences",
                                               "load_asserted",
                                               "load_inferred",
                                               "generate_plcopen",
                                               "generate_pyuaf",
                                               "save_cache"  ]
        self["config"] = {}
        self["problems"] = { "violations" : [] }


        # read contents from the files (coffee, jsonld, ...) that are inside the
        # directories of the configuration file
        self.updateDataset()

        # load the asserted data
        self.loadAsserted()

        LOG("Reset done.")


    def log(self, msg, newLine=True):
        """
        Log a message, both to OntoManager's logging system and to the
        ["dataset"]["output"] string, which can be displayed in the web browser.

        @param newLine: True if a newline must be added before the message
                        displayed in the web browser..
        """
        INFO(msg)
        if newLine:
            msg = b'\n%s' %msg.decode(u'utf-8')
        else:
            msg = b'%s' %msg.decode(u'utf-8')

        self["dataset"]["output"] += msg


    def loadAsserted(self):
        """
        Load the asserted data.

        The asserted data is the data that was entered by the user. It corresponds
        to the data of the jsonld files:
         - the metamodel jsonld files, created by converting the ontologies (in .ttl format)
           into jsonld
        """
        self.log("========================= Loading asserted data ========================= ")

        self.log("Clearing graph ...")
        CLEAR_GRAPH()

        self.log("Loading minimal context ...")
        LOAD_MINIMAL_CONTEXT()

        self.log("Loading asserted  data (in %s) ..." %self['config']['jsonld_dir'])

        # get the list of files to read (i.e. to "load" in memory)
        fileNames = FIND_FILES(self['config']['jsonld_dir'], '*.jsonld')

        # read each file
        for fileName in fileNames:
            self.log("Reading %s..." %fileName)
            f = file(fileName, mode='r')
            GET_GRAPH().parse(fileName, format="json-ld")
            f.close()

        # ok done!
        self.log("========================= All asserted data has been read ========================= ")


    def loadInferred(self):
        """
        Load the inferred data.

        Inferred data is produced by a reasoner (a rules engine).
        This step is not needed for showing the common views or for generating source code,
        it is only needed for verification and analaysis.
        """
        self.log("========================= Loading inferred data ========================= ")

        # get a list of the files to read
        fileNames = FIND_FILES(self['config']['inferred_dir'], '*.jsonld')

        # read each file
        for fileName in fileNames:
            self.log("Reading %s..." %fileName)
            f = file(fileName, mode='r')
            GET_GRAPH().parse(fileName, format="json-ld")
            f.close()

        self.log("========================= All inferred data has been read ========================= ")


    def updateDataset(self, repoName=None):
        """
        Update the dataset.

        This means:
         - update the used directories, based on the chosen repository name
         - list the useful files in those directories
         - re-create the trees (the expandable menus on the left side of the web pages)
         - reset the state of the checbboxes of the dataset page

        @param repoName: the name of the chosen repository, as determined by the config.ini.
        """
        # if no repoName is specified, then we use the default repository:
        if repoName is None:
            repo = configuration.DEFAULT_REPOSITORY
            self.log("Updating dataset to the default repository: %s" %(repo['comment']))
        else:
            repo = configuration.REPOSITORIES[repoName]
            self.log("Updating dataset to repository: %s" %(repo['comment']))

        # update the directories in the configuration
        self["config"]["ontologies_dir"] = repo["ontologies_dir"]
        self["config"]["coffee_dir"]     = repo["coffee_dir"]
        self["config"]["generated_dir"]  = repo['generated_dir']
        self["config"]["models_dir"]     = os.path.join(repo["coffee_dir"], "models")
        self["config"]["metamodels_dir"] = os.path.join(repo["coffee_dir"], "metamodels")
        self["config"]["jsonld_dir"]     = os.path.join(configuration.DEFAULT_REPOSITORY["generated_dir"], repo["name"], "jsonld")
        self["config"]["inferred_dir"]   = os.path.join(configuration.DEFAULT_REPOSITORY["generated_dir"], repo["name"], "inferred")
        self["config"]["plcopen_dir"]    = os.path.join(configuration.DEFAULT_REPOSITORY["generated_dir"], repo["name"], "plcopen")
        self["config"]["pyuaf_dir"]      = os.path.join(configuration.DEFAULT_REPOSITORY["generated_dir"], repo["name"], "pyuaf")
        self["config"]["cache_dir"]      = os.path.join(configuration.DEFAULT_REPOSITORY["generated_dir"], repo["name"], "cache")

        # create the generated dirs if they don't exist yet
        for key in ["jsonld_dir", "inferred_dir", "plcopen_dir", "pyuaf_dir"]:
            if not os.path.exists(self["config"][key]):
                os.makedirs(self["config"][key])

        # find the files in the directories
        self["dataset"]["ontologies"] = { "ttl"    : dataset.findFiles(self["config"]["ontologies_dir"], "*.ttl") }
        self["dataset"]["metamodels"] = { "coffee" : dataset.findFiles(self["config"]["metamodels_dir"], "*.coffee"),
                                          "jsonld" : dataset.findFiles(os.path.join(self["config"]["jsonld_dir"], "metamodels"), "*.jsonld") }
        self["dataset"]["models"]     = { "coffee" : dataset.findFiles(self["config"]["models_dir"], "*.coffee"),
                                          "jsonld" : dataset.findFiles(os.path.join(self["config"]["jsonld_dir"], "models"), "*.jsonld") }

        # deselect the main checkboxes
        for checkbox in self["dataset"]["main_checkboxes"]:
            self["dataset"][checkbox] = { "checked" : False }

        # create the tree menus
        self["dataset"]["run_models"]["tree"] = dataset.getJsTree(self["config"]["models_dir"], "*.coffee")
        self["dataset"]["generate_plcopen"]["tree"] = dataset.getJsTree(self["config"]["plcopen_dir"], "*.xml")
        self["dataset"]["generate_pyuaf"]["tree"] = dataset.getJsTree(self["config"]["pyuaf_dir"], "*.xml")
        self["models"] = dataset.getJsTree(self["config"]["models_dir"], "*.coffee")

        # create the repository checbboxes, and select the current one
        self["dataset"]["repository_checkboxes"] = []
        for (name,details) in configuration.REPOSITORIES.items():
            self["dataset"]["repository_checkboxes"].append(name)
            self["dataset"][name] = { "checked" : (name == repoName),
                                      "name"    : name,
                                      "comment" : details["comment"] }


    def datasetGetCheckedFilenames(self, jstree):
        """
        Get the filenames of the files that are selected (by their checkbox).

        @return: a list of filenames
        """
        ret = []
        for item in jstree:
            if item['type'] == 'file':
                if item['state']['selected']:
                    ret.append(item['_filename_'])
            else:
                ret += self.datasetGetCheckedFilenames(item['children'])
        return ret

    def datasetSetChecked(self, treeName, relPathString, checked):
        """
        Set the given relative path of the given tree to checked or unchecked.

        @param treeName: the tree name
        @param relPathString: the relative path of the element of the tree
        @param checked: either True to set checked, False to set unchecked.
        """
        # remove the leading /
        if relPathString[0] == '/':
            relPathString = relPathString[1:]

        relPathParts = relPathString.split('/')

        self.datasetSetJsTreeChecked( self["dataset"][treeName]["tree"], relPathParts, checked )


    def datasetSetJsTreeChecked(self, tree, relPath, checked):
        """
        Same as datasetSetChecked, only this time for a JsTree
        (a file tree based on a javascript extension).

        See datasetSetChecked.
        """
        currentText = relPath[0]
        remainingPath = relPath[1:]

        for item in tree:
            if item['text'] == currentText:
                if len(remainingPath) == 0:
                    item['state']['selected'] = checked
                    DEBUG( item['_filename_'] + " = " + str(checked) )
                else:
                    # go to child nodes
                    if item.has_key('children'):
                        self.datasetSetJsTreeChecked(item['children'], remainingPath, checked)

    def getCacheFileName(self):
        """
        Get the path of the cache file.
        """
        return os.path.join(self["config"]["cache_dir"], 'cache.pickle')

    def saveCache(self):
        """
        Save the CACHE (a dictionary) to disk.
        """
        global CACHE
        INFO("Now saving the cache...")
        f = open(self.getCacheFileName(), 'w')
        pickle.dump(CACHE, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        INFO("The cache has been saved.")


    def loadCache(self):
        """
        Read the CACHE (a dictionary) from disk.
        """
        global CACHE
        INFO("Now loading the cache...")
        f = open(self.getCacheFileName(), 'r')
        CACHE = pickle.load(f)
        f.close()
        INFO("The cache has been loaded.")


    def problems_show_violations(self, violations):
        """
        Store constraint violations (spin:Constraint instances) in the Model.
        """
        self["problems"]["violations"] = violations


###################################################################################################
# create a global instance of the Model, named M
M = Model()
###################################################################################################


# =================================================================================================
class UserSpaces(dict):
    """
    The UserSpaces class represents a dictionary that holds user-specific information such as
    the view currently shown, and the current state of the tree menus.
    """

    def __init__(self):
        """
        Create a new userspace.
        """
        dict.__init__(self)


    def addUser(self, userId):
        """
        Add a new user to the user spaces.
        """
        self[userId] = dict(
            models = dict(
                shown_file = None
            ),
            query = dict(
                query = TESTQUERY,
                results = None
            ),
            browse = dict(
                show  = dict(
                    type = None,
                    qname = None
                )
            ),
            org = dict(
                tree = OrderedDict(),
                show = dict( type = None, qname = None )
            ),
            sys = dict(
                tree = OrderedDict(),
                show = dict( type = None, qname = None )
            ),
            mech = dict(
                tree = OrderedDict(),
                show = dict( type = None, qname = None )
            ),
            elec = dict(
                tree = OrderedDict(),
                show = dict( type = None, qname = None )
            ),
            soft = dict(
                tree = OrderedDict(),
                show = dict( type = None, qname = None )
            )
        )

        projects = ontomanager.sys.getProjects(CACHE)
        for project in projects:
            self[userId]["sys"]["tree"][project] = { '__opened__'   : False,
                                                     '__opened_before__' : False }

        libs = soft.getLibraries(CACHE)
        for lib in libs:
            self[userId]["soft"]["tree"][lib] = { '__opened__'   : False,
                                                  '__opened_before__' : False }

        cfgs = elec.getMainConfigurations(CACHE)
        for cfg in cfgs:
            self[userId]["elec"]["tree"][cfg] = { '__opened__'   : False,
                                                  '__opened_before__' : False }


    def getUser(self, request):
        """
        Get the user id from a request.
        """
        return request.authenticated_userid


    def show(self, request, category):
        """
        Show a view for a particular user.

        A view can have a category, e.g. an electric motor instance can be shown
         - in the category 'elec' (resulting in the template elec/MotorInstance.mako)
         - or in the category 'sys' (resulting in the template sys/design.mako)
         - or in the category 'browse' (resulting in the template browse.mako).

        All categories can be seen in allviews.py.

        @param request: the HTTP request
        @param category: the name of the category ('elec', 'sys', 'soft', ...)
        """
        global M
        global CACHE

        user       = self.getUser(request)
        typeToShow = request.params.get('show')
        qname      = request.params.get('qname')

        if (qname is None) or (qname == ""):
            self[user][category]["show"]["type"]  = typeToShow
            self[user][category]["show"]["qname"] = None
        else:
            INFO("Showing %s/%s for %s" %(category, typeToShow, qname))
            try:
                node = generic.getDefaultNode(CACHE, qname)
                newCategory, newType = node.show(category, typeToShow)
                self[user][category]["show"]["type"]  = newType
                self[user][category]["show"]["qname"] = qname

                # handle special cases
                if category == "soft" and typeToShow == "library":
                    global BUSY_GenerateXmlNsThread
                    node["xml_code"] = soft.getCode(qname, soft.GET_FILEPATH(M["config"]["plcopen_dir"], qname, "xml"), busyUpdating=BUSY_GenerateXmlNsThread)
                    node["xml_process_busy"] = BUSY_GenerateXmlNsThread
                    global BUSY_generatePyuafNsThreadBusy
                    node["pyuaf_code"] = soft.getCode(qname,soft.GET_FILEPATH(M["config"]["pyuaf_dir"], qname, "py"), busyUpdating=BUSY_generatePyuafNsThreadBusy)
                    node["pyuaf_process_busy"] = BUSY_generatePyuafNsThreadBusy
            except Exception, e:
                LOG("Failed to show %s/%s for %s: %s %s" %(category, typeToShow, qname, type(e), str(e)))
                self[user][category]["show"]["type"]  = None
                self[user][category]["show"]["qname"] = None


    def models_show_file(self, request):
        """
        Show the contents of a file (e.g. a model or metamodel).
        """
        global M
        try:
            user   = self.getUser(request)
            relPathString = request.POST["models_tree_clicked"]
            INFO("models_show_file: %s" %relPathString)
            self[user]["models"]["shown_file"] = {  "path"     : relPathString,
                                                    "uri"      : "",
                                                    "prefix"   : "",
                                                    "contents" : "" }

            fullPathString = M['config']['models_dir'] + relPathString
            f = file(fullPathString)
            self[user]["models"]["shown_file"]["contents"] = f.read().decode(u'utf-8')

            try:
                uri, prefix = ontologies.extractUriAndPrefixFromCoffeeModel(self[user]["models"]["shown_file"]["contents"])
                self[user]["models"]["shown_file"]["uri"] = uri
                self[user]["models"]["shown_file"]["prefix"] = prefix
            except Exception, e:
                LOG("models_show_file: Could not extract URI and prefix: %s" %e)

            f.close()
        except Exception, e:
            LOG("models_show_file: %s" %e)
            self[user]["models"]["shown_file"] = None


    def models_show_ontology(self, request):
        """
        Show the contents of an ontology.
        """
        global M
        try:
            user   = self.getUser(request)
            number = request.params.get('show_ontology')
            self[user]["models"]["shown_ontology"] = {  "number"   : int(number),
                                                        "ontology" :  M["models"][int(number)] }
            # set a default source file:
            defaultSource = self[user]["models"]["shown_ontology"]["ontology"]["sources"][0]
            self[user]["models"]["shown_source"] = { "number"   : 0,
                                                     "source"   : defaultSource,
                                                     "contents" : ontologies.getSourceContents(defaultSource["file"]).decode(u'utf-8') }
        except Exception, e:
            LOG("models_show_ontology: %s" %e)
            self[user]["models"]["shown_ontology"] = None
            self[user]["models"]["shown_source"]   = None


    def models_show_source(self, request):
        """
        Show the contents of the source code of an ontology.
        """
        try:
            user   = self.getUser(request)
            number = request.params.get('show_source')
            source = self[user]["models"]["shown_ontology"]["ontology"]["sources"][int(number)]
            self[user]["models"]["shown_source"] = { "number"   : int(number),
                                                     "source"   : source,
                                                     "contents" : ontologies.getSourceContents(source["file"]).decode(u'utf-8') }
        except Exception, e:
            LOG("models_show_source: %s" %e)
            self[user]["models"]["shown_source"] = None


    def query_submit(self, request):
        """
        Submit a query.
        """
        global CACHE
        queryText = request.POST["query"]
        user      = self.getUser(request)

        self[user]['query']['query'] = queryText.strip()

        try:
            INFO("Executing free query '%s'" %queryText)

            self[user]['query']['results'] = QUERY(queryText)

            for row in self[user]['query']['results']:
                for result in row:
                    if IS_URI(result):
                        node = generic.getDefaultNode(CACHE, URI_TO_QNAME(result))

            INFO(" --> #results: %d" %len(self[user]['query']['results']))

        except Exception, e:
            self[user]['query']['results'] = e


    def open(self, request, category):
        """
        Open a tree branch.
        """
        global CACHE

        user = self.getUser(request)
        type = request.params.get('open')
        pathStr = request.params.get('path')

        DEBUG("pathStr: %s" %pathStr)
        path = pathStr.split('::')
        DEBUG("path: %s" %path)
        for i in xrange(len(path)):
            path[i] = urllib.unquote(path[i])
        subtree = util.getFromDict(self[user][category]["tree"], path)
        if subtree['__opened_before__']:
            subtree['__opened__'] = True
            util.setInDict(self[user][category]["tree"], path, subtree)
        else:
            newDict = { '__opened__' : True, '__opened_before__' : True }
            # first expand the node, then update the tree
            if len(path) == 0:
                raise Exception("Cannot expand empty path!")
            elif IS_QNAME(path[-1]):
                qname = path[-1]
                expansion = ''
                node = generic.getDefaultNode(CACHE, qname)
                node.expand(category, type, expansion, qname)
                DEBUG(node)
                for item in node['views'][category][type]["expansions"]:
                    newDict[item] = { '__opened__' : False, '__opened_before__' : False }
            elif len(path) > 1:
                if IS_QNAME(path[-2]) and not IS_QNAME(path[-1]):
                    qname = path[-2]
                    expansion = path[-1]
                    node = generic.getDefaultNode(CACHE, qname)
                    node.expand(category, type, expansion, qname)
                    for item in node[expansion]:
                        newDict[item] = { '__opened__' : False, '__opened_before__' : False }
                else:
                    raise Exception("Path %s does not hold a QName and an expansion!" %path)

            util.setInDict(self[user][category]["tree"], path, newDict)
        if do_DEBUG():
            pprint.pprint(self[user][category]["tree"])


    def close(self, request, category):
        """
        Close a tree branch.
        """
        user = self.getUser(request)
        pathStr = request.params.get('path')

        path = pathStr.split('::')
        for i in xrange(len(path)):
            path[i] = urllib.unquote(path[i])

        subtree = util.getFromDict(self[user][category]["tree"], path)
        subtree['__opened__'] = False
        util.setInDict(self[user][category]["tree"], path, subtree)
        if do_DEBUG():
            pprint.pprint(self[user][category]["tree"])


    def expand(self, category, type, expansion, qname):
        """
        Expand an "expansion" of a node.

        Expansions are lists of properties. E.g. a software class node may
        have expansions called 'variables' and 'methods'. Expanding may take
        quite some time, because queries will be executed (unless they were
        executed and cached before).

        @param category: name of the view category, e.g. 'elec', 'sys', 'soft'. See allviews.py.
        @param type: type of the view, e.g. 'Motor' (from category elec), 'Design' (from category sys), ...
        @param qname: qname of the node which expansions must be expanded.
        """
        global CACHE
        if (qname is None) or (qname == ""):
            raise Exception("Argument 'qname' needs to be provided!")
        else:
            DEBUG("Expanding %s/%s[%s] for %s" %(category, type, expansion, qname))
            node = generic.getDefaultNode(CACHE, qname)
            node.expand(category, type, expansion)


###################################################################################################
# create a global instance of the UserSpaces, named U, and add the users of the config.ini
U = UserSpaces()
for userName in USERS:
    U.addUser(userName)
###################################################################################################



@view_config(route_name='default', renderer='ontomanager:templates/home.mako', permission='view')
@view_config(route_name='home', renderer='ontomanager:templates/home.mako', permission='view')
# =================================================================================================
def home_view(request):
    """
    A user requested the home view.
    """
    INFO("VIEW: Home")
    global U

    if 'logout.submitted' in request.params:
        headers = forget(request)
        return HTTPFound(location = request.route_url('login'),
                         headers = headers)

    response = buildResponse(request, "Home")

    # find out which files of the user's home directory must be shown
    homeFiles = []
    try:
        homeDir = HOMES[response['user_id']]
        if os.path.exists(homeDir):
            INFO("Home directory found: %s" %homeDir)
            contents = os.listdir(homeDir)
            for item in contents:
                if os.path.isfile(item):
                    homeFiles.append(item)
            homeFiles.sort()
        else:
            INFO("Home directory %s does not exist!" %homeDir)
    except KeyError:
        INFO("No home directory configured")

    response['home_files'] = homeFiles

    return response



@view_config(route_name='models', renderer='ontomanager:templates/models.mako', permission='view')
# =================================================================================================
def models_view(request):
    """
    A user requested the Models view.
    """
    INFO("VIEW: Models")
    global U

    if request.params.get('show_ontology') is not None:
        U.models_show_ontology(request)

    if request.params.get('show_source') is not None:
        U.models_show_source(request)

    if request.POST.has_key("models_tree_clicked"):
        U.models_show_file(request)

    return buildResponse(request, "Models")


@view_config(route_name='cache', renderer='ontomanager:templates/cache.mako', permission='edit')
# =================================================================================================
def cache_view(request):
    """
    A user requested the Cache view.
    """
    INFO("VIEW: Cache")
    # the cache is already available via the global model, nothing to do
    global M
    return M


@view_config(route_name='config', renderer='ontomanager:templates/config.mako', permission='edit')
# =================================================================================================
def config_view(request):
    """
    A user requested the Config view.
    """
    INFO("VIEW: Config")
    return buildResponse(request, 'Config')


@view_config(route_name='dataset', renderer='ontomanager:templates/dataset.mako', permission='edit')
# =================================================================================================
def dataset_view(request):
    """
    A user requested the Dataset view.
    """
    INFO("VIEW: Dataset")
    global M

    if request.POST.has_key('opening'):
        INFO("OPENING")

    for checkbox in M["dataset"]["main_checkboxes"]:
        if request.POST.has_key("%s_checked" %checkbox):
            checked = ( str(request.POST["%s_checked" %checkbox]).lower() == 'true' )
            M["dataset"][checkbox]["checked"] = checked
            INFO("Checkbox %s state has changed to %s" %(checkbox, checked))

    for checkbox in M["dataset"]["repository_checkboxes"]:
        if request.POST.has_key("%s_checked" %checkbox):
            checked = ( str(request.POST["%s_checked" %checkbox]).lower() == 'true' )
            M["dataset"][checkbox]["checked"] = checked
            INFO("Checkbox %s state has changed to %s" %(checkbox, checked))
            # the other checkboxes must be the opposite
            for otherCheckbox in M["dataset"]["repository_checkboxes"]:
                if otherCheckbox != checkbox:
                    M["dataset"][otherCheckbox]["checked"] = not checked
                    INFO("Checkbox %s state has changed to %s" %(otherCheckbox, not checked))
            if checked:
                M.updateDataset(repoName=checkbox)
                url = request.route_url('dataset')
                return HTTPFound(location=url)


    for checkbox in ["run_models", 'generate_plcopen']:
        if request.POST.has_key("%s_tree_unchecked" %checkbox):
            relPathString = request.POST["%s_tree_unchecked" %checkbox]
            M.datasetSetChecked(checkbox, relPathString, False)
            INFO("%s%s is now unchecked" %(checkbox, relPathString))
        if request.POST.has_key("%s_tree_checked" %checkbox):
            relPathString = request.POST["%s_tree_checked" %checkbox]
            M.datasetSetChecked(checkbox, relPathString, True)
            INFO("%s%s is now checked" %(checkbox, relPathString))


    if request.POST.has_key("submit"):
        if request.POST["submit"] == "Start processing":

            global BUSY_processDatasetThreadBusy
            if not BUSY_processDatasetThreadBusy:
                t = ProcessDatasetThread(request, M)
                t.start()

            url = request.route_url('dataset')
            return HTTPFound(location=url)


    if request.POST.has_key("cache"):
        if request.POST["cache"] == "Load cache":
            M.loadCache()
        if request.POST["cache"] == "Save cache":
            M.saveCache()

        url = request.route_url('dataset')
        return HTTPFound(location=url)

    return buildResponse(request, "Dataset")


@view_config(route_name='problems', renderer='ontomanager:templates/problems.mako', permission='view')
# =================================================================================================
def problems_view(request):
    """
    A user requested the Problems view.
    """
    INFO("VIEW: Problems")
    global M

    if request.params.get('reset') is not None:
        M.reset()

    M.problems_show_violations(problems.getAllConstraintViolations())

    return buildResponse(request, 'Problems')


@view_config(route_name='browse', renderer='ontomanager:templates/browse.mako', permission='view')
# =================================================================================================
def browse_view(request):
    """
    A user requested the Browse view.
    """
    INFO("VIEW: Browse")
    global U

    if request.params.get('show') is not None:
        U.show(request  = request,
               category = "browse")

    if request.params.get('submit') is not None:
        return HTTPFound(location = '/browse?show;qname=%s' %request.params.get('qname'))

    return buildResponse(request, 'Browse')


@view_config(route_name='sys', renderer='ontomanager:templates/sys/sys.mako', permission='view')
# =================================================================================================
def sys_view(request):
    """
    A user requested the Sys view.
    """
    INFO("VIEW: Sys")

    global U
    if request.params.get('open') is not None:
        U.open(request, "sys")
    if request.params.get('close') is not None:
        U.close(request, "sys")

    if request.params.get('show') is not None:
        U.show(request = request, category = "sys")


    return buildResponse(request, 'Systems')



@view_config(route_name='mech', renderer='ontomanager:templates/mech/mech.mako', permission='view')
# =================================================================================================
def mech_view(request):
    """
    A user requested the Mech view.
    """
    INFO("VIEW: Mech")

    global M

    if request.params.get('reset') is not None:
        M.reset()
    if request.params.get('open') is not None:
        M.open("mech", request.params.get('open'), request.params.get('path'))
    if request.params.get('close') is not None:
        M.close("mech", request.params.get('path'))

    if request.params.get('show') is not None:
        M.show(category = "mech",
               type     = request.params.get('show'),
               qname    = request.params.get('qname'))

    return buildResponse(request, 'Mechanics')




@view_config(route_name='elec', renderer='ontomanager:templates/elec/elec.mako', permission='view')
# =================================================================================================
def electronics_view(request):
    """
    A user requested the Elec view.
    """
    INFO("VIEW: Elec")
    global U

    if request.params.get('show') is not None:
        U.show(request, "elec")
    if request.params.get('open') is not None:
        U.open(request, "elec")
    if request.params.get('close') is not None:
        U.close(request, "elec")

    return buildResponse(request, 'Electronics')



@view_config(route_name='soft', renderer='ontomanager:templates/soft/soft.mako', permission='view')
# =================================================================================================
def software_view(request):
    """
    A user requested the Soft view.
    """
    INFO("VIEW: Soft")
    global U
    global M

    if request.params.get('show') is not None:
        U.show(request, "soft")
    if request.params.get('open') is not None:
        U.open(request, "soft")
    if request.params.get('close') is not None:
        U.close(request, "soft")

    if request.POST.has_key("submit"):

        DEBUG(request.POST)

        ns = request.POST["ns"]

        if request.POST["submit"] == "Generate PLCopen XML":

            global BUSY_GenerateXmlNsThread
            if not BUSY_GenerateXmlNsThread:
                t = GenerateXmlNsThread(request, M)
                t.start()

            url = request.route_url('soft')
            return HTTPFound(location=url + "?show=library;qname=%s" %ns)

        if request.POST["submit"] == "Download PLCopen XML":

            nsName = ns.split(":",1)[1]

            filePath = soft.GET_FILEPATH(M["config"]["plcopen_dir"], ns, "xml")
            if os.path.exists(filePath):
                INFO("Sending file %s" %filePath)
                response = FileResponse(filePath, request=request, content_type="text/xml")
                response.content_disposition = 'attachment; filename="%s.xml"' %nsName
                return response
            else:
                INFO("File %s not found on server" %filePath)
                return HTTPNotFound("File %s not found on server" %filePath)


        if request.POST["submit"] == "Generate pyUAF code":

            global BUSY_generatePyuafNsThreadBusy
            if not BUSY_generatePyuafNsThreadBusy:
                t = GeneratePyuafNsThread(request, M)
                t.start()

            url = request.route_url('soft')
            return HTTPFound(location=url + "?show=library;qname=%s" %ns)

        if request.POST["submit"] == "Download pyUAF code":

            nsName = ns.split(":",1)[1]

            filePath = soft.GET_FILEPATH(M["config"]["pyuaf_dir"], ns, "py")
            if os.path.exists(filePath):
                INFO("Sending file %s" %filePath)
                response = FileResponse(filePath, request=request, content_type="text/plain")
                response.content_disposition = 'attachment; filename="%s.py"' %nsName
                return response
            else:
                INFO("File %s not found on server" %filePath)
                return HTTPNotFound("File %s not found on server" %filePath)

    return buildResponse(request, 'Software')


@view_config(route_name='query', renderer='ontomanager:templates/query.mako', permission='query')
# =================================================================================================
def query_view(request):
    """
    A user requested the Query view.
    """
    INFO("VIEW: Query")
    global U

    if request.POST.has_key("submit"):
        U.query_submit(request)

    return buildResponse(request, 'Query')

@view_config(route_name='org', renderer='ontomanager:templates/org/org.mako')
# =================================================================================================
def org_view(request):
    """
    A user requested the Org view.
    """
    INFO("VIEW: Org")
    global U

    if request.params.get('show') is not None:
        U.show(request, "org")

    return buildResponse(request, 'Org')



@view_config(route_name='login', renderer='ontomanager:templates/login.mako')
@forbidden_view_config(renderer='ontomanager:templates/login.mako')
# =================================================================================================
def login(request):
    """
    A user requested the Login view.
    """
    INFO("VIEW: Login")
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        if not (login in USERS.keys()):
            message = "Unknown username"
        elif USERS.get(login) == password:
            headers = remember(request, login)
            return HTTPFound(location = '/',
                             headers = headers)
        else:
            message = 'Invalid password'



    INFO("==========")
    INFO("Session created: %s" %request.session.created)
    INFO("Session new: %s" %request.session.new)
    INFO("Cookies: %s" %request.cookies)

    response = buildResponse(request, "")
    response['authentication'] = dict( message = message,
                                       url = request.application_url + '/login',
                                       came_from = came_from,
                                       login = login,
                                       password = password
                                      )
    return response


@view_config(route_name='logout')
# =================================================================================================
def logout(request):
    """
    A user requested the Logout view.
    """
    INFO("VIEW: Logout")
    headers = forget(request)
    return HTTPFound(location = request.route_url('login'),
                     headers = headers)




###################################################################################################
# create some global flags to see if a particular thread is running or not
# (quick and dirty implementation, should be replaced by locks, of course)
BUSY_GenerateXmlNsThread       = False
BUSY_generatePyuafNsThreadBusy = False
BUSY_processDatasetThreadBusy  = False
###################################################################################################


# =================================================================================================
class GenerateXmlNsThread(threading.Thread):
    """
    A thread to generate PLCOpen XML files.
    """

    def __init__(self, request, model):
        """
        Create a thread instance.
        """
        threading.Thread.__init__(self)
        self.request = request
        self.ns = request.POST["ns"] # qname
        self.model = model

    def run(self):
        """
        The overridden run() method.
        """
        global BUSY_GenerateXmlNsThread
        global CACHE

        # flag the thread as busy
        BUSY_GenerateXmlNsThread = True

        try:
            if self.ns is not None and self.request is not None:
                INFO("GenerateXmlNsThread Starting...")
                node = generic.getDefaultNode(CACHE, self.ns)
                soft.show_library(node)
                code = render('ontomanager:templates/soft/export_plcopen.mako', { 'project' : self.ns, 'CACHE' : CACHE } , request=self.request)
                soft.writeCode(code, self.ns, soft.GET_FILEPATH(self.model["config"]["plcopen_dir"], self.ns, "xml"))
        finally:
            INFO("GenerateXmlNsThread Done")

            # flag the thread as not busy anymore
            BUSY_GenerateXmlNsThread = False

        self.request.POST.clear()
        software_view(self.request)


# =================================================================================================
class GeneratePyuafNsThread(threading.Thread):
    """
    A thread to generate PyUAF python files.
    """

    def __init__(self, request, model):
        """
        Create a thread instance.
        """
        threading.Thread.__init__(self)
        self.request = request
        self.ns = request.POST["ns"] # qname
        self.model = model


    def run(self):
        """
        The overridden run() method.
        """
        global BUSY_generatePyuafNsThreadBusy
        global CACHE

        # flag the thread as busy
        BUSY_generatePyuafNsThreadBusy = True

        try:
            if self.ns is not None and self.request is not None:
                INFO("GeneratePyuafNsThread Starting...")
                node = generic.getDefaultNode(CACHE, self.ns)
                soft.show_library(node)
                code = render('ontomanager:templates/soft/export_pyuaf.mako', { 'project' : self.ns, 'CACHE' : CACHE } , request=self.request)

                importPartStart = code.find('# === imports ===')
                newCode = code[importPartStart:] + code[:importPartStart]

                soft.writeCode(newCode, self.ns, soft.GET_FILEPATH(self.model["config"]["pyuaf_dir"], self.ns, "py"))
        finally:
            INFO("GeneratePyuafNsThread Done")

            # flag the thread as not busy anymore
            BUSY_generatePyuafNsThreadBusy = False

        self.request.POST.clear()
        software_view(self.request)


# =================================================================================================
class ProcessDatasetThread(threading.Thread):

    def __init__(self, request, model):
        """
        Create a thread instance.
        """
        threading.Thread.__init__(self)
        global U
        self.request = request
        self.model = model
        self.user = U.getUser(request)

        self.ontologiesDir = self.model["config"]["ontologies_dir"]
        self.coffeeDir     = self.model["config"]["coffee_dir"]
        self.metamodelsDir = self.model["config"]["metamodels_dir"]
        self.jsonldDir     = self.model["config"]["jsonld_dir"]


    def log(self, msg, newLine=True):
        """
        Log a message to the logging system and to the web browser.
        """
        INFO(msg)
        if newLine:
            msg = b'\n%s' %msg.decode(u'utf-8')
        else:
            msg = b'%s' %msg.decode(u'utf-8')

        self.model["dataset"]["output"] += msg

    def logHeading(self, title, newLine=True):
        """
        Log a big header message
        """
        self.log("====================================================================================================", newLine=newLine)
        self.log(title)
        self.log("====================================================================================================")


    def logError(self, msg):
        """
        Log an error message
        """
        ERROR(msg)
        self.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", newLine=False)
        self.log(msg)
        self.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


    def run(self):
        """
        The overridden run() method.
        """
        global BUSY_processDatasetThreadBusy
        global CACHE
        global U

        self.logHeading("Processing is started", newLine=False)

        # flag the thread as busy
        BUSY_processDatasetThreadBusy = True

        self.model["dataset"]["thread_running"] = True

        try:
            INFO("ProcessDatasetThread Starting...")

            # erase the output
            self.model["dataset"]["output"] = u""

            if self.model["dataset"]["run_metamodels"]["checked"]:
                self.log("Running metamodels")

                outputDir = os.path.join(self.jsonldDir , "metamodels")

                # make sure the output directory exists
                if not os.path.exists(outputDir):
                    os.makedirs(outputDir)

                rdfconvert.convert(
                    inputFilesOrDirs = [ self.ontologiesDir ],
                    inputFormat      = "n3",
                    inputExtensions  = [".ttl"],
                    outputDir        = outputDir,
                    outputFormat     = "json-ld",
                    outputExt        = ".jsonld",
                    recursive        = True,
                    overwrite        = True,
                    loggingCb        = self.log)


            if self.model['dataset']['run_models']['checked']:
                filenames = self.model.datasetGetCheckedFilenames(self.model['dataset']['run_models']['tree'])
                for filename in filenames:
                    iPath = self.coffeeDir
                    IPath = self.jsonldDir
                    oPath = self.jsonldDir
                    command = "%s %s -s -a -t -i %s -I %s -o %s -f" %(configuration.COFFEE, filename, iPath, IPath, oPath)

                    self.log("============================ starting process ==========================")
                    self.log(command)
                    self.log("========================================================================")

                    popen = subprocess.Popen(command,
                                             stdout = subprocess.PIPE,
                                             stderr = subprocess.STDOUT,
                                             shell=True)

                    while True:
                        out = popen.stdout.readline()
                        if out == '' and popen.poll() != None:
                            break

                        if out != '':
                            self.log(out[:-1])
                            sys.stdout.flush()

                    if popen.returncode == 0:
                        self.log("============================ processes finished with exit code 0 ==========================")
                    else:
                        self.log("!!!!!!!!!!!!!!!!!!!!!!!!!!!! processes finished with exit code %d !!!!!!!!!!!!!!!!!!!!!!!!!!!!" %popen.returncode)


            if self.model['dataset']['load_asserted']['checked']:
                self.model.loadAsserted()
                global CACHE
                global U
                CACHE = {}
                U = UserSpaces()
                for userName in USERS:
                    U.addUser(userName)

            if self.model['dataset']['load_inferred']['checked']:
                self.model.loadInferred()

            if self.model["dataset"]["generate_plcopen"]["checked"]:
                filenames = self.model.datasetGetCheckedFilenames(self.model['dataset']['generate_plcopen']['tree'])

                self.log("============================ Generating libraries ==========================")
                for filePath in filenames:
                    # find the corresponding library
                    library = None
                    for lib in U[self.user]['soft']['tree'].keys():
                        if soft.GET_FILEPATH(self.model["config"]["plcopen_dir"], lib, "xml") == filePath:
                            library = lib
                            break

                    if library is None:
                        self.log("Skipping %s: no corresponding library found" %filePath)
                    else:
                        self.log("Generating %s..." %filePath)
                        node = generic.getDefaultNode(CACHE, lib)
                        soft.show_library(node)
                        code = render('ontomanager:templates/soft/export_plcopen.mako', { 'project' : lib, 'CACHE' : CACHE } , request=self.request)
                        soft.writeCode(code, lib, filePath)
                        self.log(" OK", newLine=False)


            if self.model["dataset"]["save_cache"]["checked"]:
                self.model.saveCache()

            self.logHeading("Processing is finished")

        except Exception, e:
            self.logError("Processing data ended with error: %s" %e)
        finally:
            INFO("ProcessDatasetThread Done")

            # flag the thread as not busy anymore
            BUSY_processDatasetThreadBusy = False
            self.model["dataset"]["thread_running"] = False

        self.request.POST.clear()
        dataset_view(self.request)


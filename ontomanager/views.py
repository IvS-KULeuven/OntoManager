from pyramid.response import Response
from pyramid.renderers import get_renderer, render
from pyramid.view import view_config, view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.response import FileResponse
from queries import ontologies, triplestore, browse, soft, problems, util, register, generic, dataset, rdfconvert, elec
from queries import sys as mercator_sys
from queries.triplestore import *
from queries.util import *
from queries.register import REGISTRY
import configuration
import subprocess

from collections import OrderedDict
import allviews

TESTQUERY = """SELECT ?company ?companyName ?m ?id ?comment (COUNT(?instance) AS ?count)
WHERE {
    ?m        rdf:type             elec:IoModuleType .
    ?m        man:hasId            ?id .
    ?m        man:isManufacturedBy ?company .
    ?company  org:hasLongName      ?companyName  .
    ?instance sys:realizes         ?m .
    OPTIONAL { ?m rdfs:comment ?comment }
}
GROUP BY ?id
ORDER BY ASC(?id)"""


from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    )

from .configuration import USERS, groupfinder


import urllib
import threading
import pprint
import os
import pickle
import sys



sys.setrecursionlimit(sys.getrecursionlimit() * 10)

print "New recursion limit: %d" %sys.getrecursionlimit()

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))


print "REGISTRY:"
print REGISTRY


def buildResponse(request, currentPage):
    global M
    global U
    global CACHE
    userId = request.authenticated_userid
    d = dict(
        M = M,
        CACHE = CACHE,
        user_id = userId,
        user_groups = groupfinder(userId, request),
        current_page = currentPage
    )

    if userId is None:
        userId = "guest"

    if userId is not None:
        d['U'] = U[userId]
    return d


CACHE = {}

class Model(dict):
    def __init__(self):
        dict.__init__(self)
        global CACHE
        CACHE = {}
        CREATE_GRAPH()
        self.reset()

    def test(self):
        QUERY("""
        SELECT DISTINCT ?instance ?view ?anything
        WHERE {
            ?instance rdf:type/rdfs:subClassOf* sys:Project .
            OPTIONAL { ?view ontoscript:views ?anything } .
        }
        """)


    def reset(self):
        LOG("Resetting...")

        self["logged_in"] = None
        self["authentication"] = None
        self["DEBUG"] = False
        self["functions"]    = { "PARSE_FOR_URI"        : triplestore.PARSE_FOR_URI,
                                 "IS_URI"               : triplestore.IS_URI,
                                 "URI_TO_QNAME"         : triplestore.URI_TO_QNAME,
                                 "SOFT_GET_FILEPATH"    : soft.GET_FILEPATH
                                 }
        self["project"]      = 'OntoManager @ Mercator Telescope'
        self["menu_items"]   = [ { 'name'   : 'Home',
                                   'target' : '/' },
                                 { 'name'   : 'Models',
                                   'target' : '/models' },
                                 # { 'name'   : 'Config',
                                 #   'target' : '/config' },
                                 { 'name'   : 'Dataset',
                                   'target' : '/dataset' },
                                 { 'name'   : 'Problems',
                                   'target' : '/problems' },
                                 { 'name'   : 'Browse',
                                   'target' : '/browse' },
                                 { 'name'   : 'Query',
                                   'target' : '/query' },
                                 # { 'name'   : 'Org',
                                 #   'target' : '/org' },
                                 { 'name'   : 'Systems',
                                   'target' : '/sys' },
                                 { 'name'   : 'Mechanics',
                                   'target' : '/mech' },
                                 { 'name'   : 'Electronics',
                                   'target' : '/elec' },
                                 { 'name'   : 'Software',
                                   'target' : '/soft' } ]

        self["config"] = {
            "ontologies_dir" : configuration.DEFAULT_REPOSITORY["location"],
            "jsonld_dir"     : os.path.join(PROJECT_DIR, "jsonld"),
            "inferred_dir"   : os.path.join(PROJECT_DIR, "rdf-inferred"),
            "plcopen_dir"    : os.path.join(PROJECT_DIR, "generated", "plcopen"),
            "pyuaf_dir"      : os.path.join(PROJECT_DIR, "generated", "pyuaf") }
        
        self["dataset"] = {}
        self.createDataset()

        self.loadAsserted()

        #self.loadInferred()

        self["models"] = dataset.getJsTree(os.path.join(self["config"]["ontologies_dir"], "coffee", "models"), "*.coffee")

        LOG("Reset done.")


    def log(self, msg, newLine=True):
        print msg
        if newLine:
            msg = b'\n%s' %msg.decode(u'utf-8')
        else:
            msg = b'%s' %msg.decode(u'utf-8')

        self["dataset"]["output"] += msg


    def loadAsserted(self):
        self.log("Clearing graph ...")

        CLEAR_GRAPH()

        self.log("Loading asserted ...")

        fileNames = FIND_FILES(self['config']['jsonld_dir'], '*.jsonld')

        global CACHE

        for fileName in fileNames:
            self.log("Reading %s..." %fileName)
            f = file(fileName, mode='r')
            GET_GRAPH().parse(fileName, format="json-ld")
            f.close()

        self.log("========================= All asserted data has been read ========================= ")

        LOG_CONTEXT()

        self["problems"] = { "violations" : [] }

        LOG("Load asserted done.")


    def loadInferred(self):
        LOG("Loading inferred ...")

        fileNames = FIND_FILES(self['config']['inferred_dir'], '*.jsonld')

        global CACHE

        for fileName in fileNames:
            self.log("Reading %s..." %fileName)
            f = file(fileName, mode='r')
            GET_GRAPH().parse(fileName, format="json-ld")
            f.close()

        self.log("========================= All inferred data has been read ========================= ")

        LOG_CONTEXT()

        self["problems"] = { "violations" : [] }

        LOG("Load inferred done.")


    def updateDataset(self, defaultRepoName):
        repo = configuration.REPOSITORIES[defaultRepoName]
        self.log("Updating dataset to %s (%s)" %(repo['comment'], repo['location']))
        self["config"]["ontologies_dir"] = repo['location']
        ontologiesDir = self["config"]["ontologies_dir"]
        jsonldDir = self["config"]["jsonld_dir"]
        self["dataset"]["metamodels"] = { "coffee" : dataset.findFiles(os.path.join(ontologiesDir, "coffee", "metamodels"), "*.coffee"),
                                          "ttl"    : dataset.findFiles(os.path.join(ontologiesDir, "ttl"   , "metamodels"), "*.ttl"),
                                          "jsonld" : dataset.findFiles(os.path.join(jsonldDir, "metamodels"), "*.jsonld") }
        self["dataset"]["models"]     = { "coffee" : dataset.findFiles(os.path.join(ontologiesDir, "coffee", "models")    , "*.coffee"),
                                          "jsonld" : dataset.findFiles(os.path.join(jsonldDir, "models")    , "*.jsonld") }
        self["dataset"]["run_models"]["tree"] = dataset.getJsTree(os.path.join(ontologiesDir, "coffee", "models")    , "*.coffee")

        self["models"] = dataset.getJsTree(os.path.join(ontologiesDir, "coffee", "models"), "*.coffee")


    def createDataset(self):
        self["dataset"]["output"] = ""
        self.log("Creating dataset")

        plcopenDir = self["config"]["plcopen_dir"]
        ontologiesDir = self["config"]["ontologies_dir"]
        jsonldDir = self["config"]["jsonld_dir"]

        self["dataset"]["thread_running"] = False
        self["dataset"]["metamodels"] = { "coffee" : dataset.findFiles(os.path.join(ontologiesDir, "coffee", "metamodels"), "*.coffee"),
                                          "ttl"    : dataset.findFiles(os.path.join(ontologiesDir, "ttl"   , "metamodels"), "*.ttl"),
                                          "jsonld" : dataset.findFiles(os.path.join(jsonldDir, "metamodels"), "*.jsonld") }
        self["dataset"]["models"]     = { "coffee" : dataset.findFiles(os.path.join(ontologiesDir, "coffee", "models")    , "*.coffee"),
                                          "jsonld" : dataset.findFiles(os.path.join(jsonldDir, "models")    , "*.jsonld") }


        self["dataset"]["main_checkboxes"] = [ "run_metamodels",
                                               "run_models",
                                               "run_inferences",
                                               "load_asserted",
                                               "load_inferred",
                                               "generate_plcopen",
                                               "save_cache"  ]

        for checkbox in self["dataset"]["main_checkboxes"]:
            self["dataset"][checkbox] = { "checked" : False }

        self["dataset"]["repository_checkboxes"] = []
        for (name,details) in configuration.REPOSITORIES.items():
            self["dataset"]["repository_checkboxes"].append(name)
            self["dataset"][name] = { "checked" : (name == configuration.DEFAULT_REPOSITORY["name"]),
                                      "name"    : name,
                                      "location": details["location"],
                                      "comment" : details["comment"] }


        self["dataset"]["run_models"]["tree"] = dataset.getJsTree(os.path.join(ontologiesDir, "coffee", "models")    , "*.coffee")
        self["dataset"]["generate_plcopen"]["tree"] = dataset.getJsTree(plcopenDir, "*.xml")

        #self["dataset"]["load_asserted"]["tree"] = dataset.getJsTree(os.path.join(ontologiesDir, "jsonld", "models")    , "*.jsonld")
        #for fileName in self["dataset"]["models"]["coffee"]:
        #    self["dataset"]["run_models"]["models"][fileName] = { "checked" : False }

    def datasetGetCheckedFilenames(self, jstree):
        # return: filenames
        ret = []
        for item in jstree:
            if item['type'] == 'file':
                if item['state']['selected']:
                    ret.append(item['_filename_'])
            else:
                ret += self.datasetGetCheckedFilenames(item['children'])
        return ret

    def datasetSetChecked(self, set, relPathString, checked):

        # remove the leading /
        if relPathString[0] == '/':
            relPathString = relPathString[1:]

        relPathParts = relPathString.split('/')

        self.datasetSetJsTreeChecked( self["dataset"][set]["tree"], relPathParts, checked )


    def datasetSetJsTreeChecked(self, tree, relPath, checked):
        currentText = relPath[0]
        remainingPath = relPath[1:]

        for item in tree:
            if item['text'] == currentText:
                if len(remainingPath) == 0:
                    item['state']['selected'] = checked
                    print item['_filename_'] + " = " + str(checked)
                else:
                    # go to child nodes
                    if item.has_key('children'):
                        self.datasetSetJsTreeChecked(item['children'], remainingPath, checked)

    def getCacheFileName(self):
        return os.path.join(PROJECT_DIR, 'cache', 'cache.pickle')

    def saveCache(self):
        global CACHE
        print("Now saving the cache...")
        f = open(self.getCacheFileName(), 'w')
        pickle.dump(CACHE, f, pickle.HIGHEST_PROTOCOL)
        f.close()
        print("The cache has been saved.")

    def loadCache(self):
        global CACHE
        print("Now loading the cache...")
        f = open(self.getCacheFileName(), 'r')
        CACHE = pickle.load(f)
        f.close()
        print("The cache has been loaded.")



    ####################################################### sys ########################################################

    def problems_show_violations(self, violations):
        self["problems"]["violations"] = violations



M = Model()


class UserSpaces(dict):
    def __init__(self):
        dict.__init__(self)

    def addUser(self, userId):
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

        for project in mercator_sys.getProjects(CACHE):
            self[userId]["sys"]["tree"][project] = { '__opened__'   : False,
                                                     '__opened_before__' : False }

        for lib in soft.getLibraries(CACHE):
            self[userId]["soft"]["tree"][lib] = { '__opened__'   : False,
                                                  '__opened_before__' : False }
        for cfg in elec.getMainConfigurations(CACHE):
            self[userId]["elec"]["tree"][cfg] = { '__opened__'   : False,
                                                  '__opened_before__' : False }




    def getUser(self, request):
        return request.authenticated_userid

    def show(self, request, category):
        global M
        global CACHE

        user       = self.getUser(request)
        typeToShow = request.params.get('show')
        qname      = request.params.get('qname')

        if (qname is None) or (qname == ""):
            self[user][category]["show"]["type"]  = typeToShow
            self[user][category]["show"]["qname"] = None
        else:
            print("Showing %s/%s for %s" %(category, typeToShow, qname))
            try:
                node = generic.getDefaultNode(CACHE, qname)
                newCategory, newType = node.show(category, typeToShow)
                self[user][category]["show"]["type"]  = newType
                self[user][category]["show"]["qname"] = qname

                # handle special cases
                if category == "soft" and typeToShow == "library":
                    global generateXmlNsThreadBusy
                    node["xml_code"] = soft.getCode(qname, soft.GET_FILEPATH(M["config"]["plcopen_dir"], qname, "xml"), busyUpdating=generateXmlNsThreadBusy)
                    node["xml_process_busy"] = generateXmlNsThreadBusy
                    global generatePyuafNsThreadBusy
                    node["pyuaf_code"] = soft.getCode(qname,soft.GET_FILEPATH(M["config"]["pyuaf_dir"], qname, "py"), busyUpdating=generatePyuafNsThreadBusy)
                    node["pyuaf_process_busy"] = generatePyuafNsThreadBusy
            except Exception, e:
                LOG("Failed to show %s/%s for %s: %s %s" %(category, typeToShow, qname, type(e), str(e)))
                self[user][category]["show"]["type"]  = None
                self[user][category]["show"]["qname"] = None

    def models_show_file(self, request):
        global M
        try:
            user   = self.getUser(request)
            relPathString = request.POST["models_tree_clicked"]
            print("models_show_file: %s" %relPathString)
            self[user]["models"]["shown_file"] = {  "path"     : relPathString,
                                                    "uri"      : "",
                                                    "prefix"   : "",
                                                    "contents" : "" }

            fullPathString = M['config']['ontologies_dir'] + "/coffee/models" + relPathString
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
        global CACHE
        queryText = request.POST["query"]
        user      = self.getUser(request)

        self[user]['query']['query'] = queryText.strip()
        try:
            self[user]['query']['results'] = QUERY(queryText)

            for row in self[user]['query']['results']:
                for result in row:
                    if IS_URI(result):
                        node = generic.getDefaultNode(CACHE, URI_TO_QNAME(result))


        except Exception, e:
            self[user]['query']['results'] = e


    def open(self, request, category):
        global CACHE

        user = self.getUser(request)
        type = request.params.get('open')
        pathStr = request.params.get('path')

        print "pathStr: %s" %pathStr
        path = pathStr.split('::')
        print "path: %s" %path
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
                print node
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
        pprint.pprint(self[user][category]["tree"])


    def close(self, request, category):

        user = self.getUser(request)
        pathStr = request.params.get('path')

        path = pathStr.split('::')
        for i in xrange(len(path)):
            path[i] = urllib.unquote(path[i])

        subtree = util.getFromDict(self[user][category]["tree"], path)
        subtree['__opened__'] = False
        util.setInDict(self[user][category]["tree"], path, subtree)
        pprint.pprint(self[user][category]["tree"])


    def expand(self, category, type, expansion, qname):
        global CACHE
        if (qname is None) or (qname == ""):
            raise Exception("Argument 'qname' needs to be provided!")
        else:
            print("Expanding %s/%s[%s] for %s" %(category, type, expansion, qname))
            node = generic.getDefaultNode(CACHE, qname)
            node.expand(category, type, expansion)

    def collapse(self, category, type, expansion, qname):
        global CACHE
        if (qname is None) or (qname == ""):
            raise Exception("Argument 'qname' needs to be provided!")
        else:
            print("Collapsing %s/%s[%s] for %s" %(category, type, expansion, qname))
            node = generic.getDefaultNode(CACHE, qname)
            node.collapse(category, type, expansion)


U = UserSpaces()
for userName in USERS:
    U.addUser(userName)



@view_config(route_name='default', renderer='ontomanager:templates/home.mako', permission='view')
@view_config(route_name='home', renderer='ontomanager:templates/home.mako', permission='view')
def home_view(request):

    if 'logout.submitted' in request.params:
        headers = forget(request)
        return HTTPFound(location = request.route_url('login'),
                         headers = headers)

    response = buildResponse(request, "Home")

    homeFolder = os.path.join(PROJECT_DIR, 'home', response['user_id'])
    if os.path.exists(homeFolder):

        homeFiles = os.listdir(homeFolder)
        homeFiles.sort()
    else:
        homeFiles = []

    response['home_files'] = homeFiles

    return response



@view_config(route_name='models', renderer='ontomanager:templates/models.mako', permission='view')
def models_view(request):
    global U

    if request.params.get('show_ontology') is not None:
        U.models_show_ontology(request)

    if request.params.get('show_source') is not None:
        U.models_show_source(request)

    if request.POST.has_key("models_tree_clicked"):
        U.models_show_file(request)

    return buildResponse(request, "Models")


@view_config(route_name='cache', renderer='ontomanager:templates/cache.mako', permission='edit')
def cache_view(request):
    global M
    return M

@view_config(route_name='config', renderer='ontomanager:templates/config.mako', permission='edit')
def config_view(request):
    return buildResponse(request, 'Config')

@view_config(route_name='dataset', renderer='ontomanager:templates/dataset.mako', permission='edit')
def dataset_view(request):
    global M

    if request.POST.has_key('opening'):
        print "OPENING"

    for checkbox in M["dataset"]["main_checkboxes"]:
        if request.POST.has_key("%s_checked" %checkbox):
            checked = ( str(request.POST["%s_checked" %checkbox]).lower() == 'true' )
            M["dataset"][checkbox]["checked"] = checked
            print("Checkbox %s state has changed to %s" %(checkbox, checked))

    for checkbox in M["dataset"]["repository_checkboxes"]:
        if request.POST.has_key("%s_checked" %checkbox):
            checked = ( str(request.POST["%s_checked" %checkbox]).lower() == 'true' )
            M["dataset"][checkbox]["checked"] = checked
            print("Checkbox %s state has changed to %s" %(checkbox, checked))
            # the other checkboxes must be the opposite
            for otherCheckbox in M["dataset"]["repository_checkboxes"]:
                if otherCheckbox != checkbox:
                    M["dataset"][otherCheckbox]["checked"] = not checked
                    print("Checkbox %s state has changed to %s" %(otherCheckbox, not checked))
            if checked:
                M.updateDataset(defaultRepoName=checkbox)
                url = request.route_url('dataset')
                return HTTPFound(location=url)


    for checkbox in ["run_models", 'generate_plcopen']:
        if request.POST.has_key("%s_tree_unchecked" %checkbox):
            relPathString = request.POST["%s_tree_unchecked" %checkbox]
            M.datasetSetChecked(checkbox, relPathString, False)
            print("%s%s is now unchecked" %(checkbox, relPathString))
        if request.POST.has_key("%s_tree_checked" %checkbox):
            relPathString = request.POST["%s_tree_checked" %checkbox]
            M.datasetSetChecked(checkbox, relPathString, True)
            print("%s%s is now checked" %(checkbox, relPathString))


    if request.POST.has_key("submit"):
        if request.POST["submit"] == "Start processing":

            global processDatasetThreadBusy
            if not processDatasetThreadBusy:
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
def problems_view(request):
    global M

    if request.params.get('reset') is not None:
        M.reset()

    M.problems_show_violations(problems.getAllConstraintViolations())

    return buildResponse(request, 'Problems')


@view_config(route_name='browse', renderer='ontomanager:templates/browse.mako', permission='view')
def browse_view(request):
    global U

    if request.params.get('show') is not None:
        U.show(request  = request,
               category = "browse")

    if request.params.get('submit') is not None:
        return HTTPFound(location = '/browse?show;qname=%s' %request.params.get('qname'))

    return buildResponse(request, 'Browse')


@view_config(route_name='sys', renderer='ontomanager:templates/sys/sys.mako', permission='view')
def sys_view(request):

    global U
    if request.params.get('open') is not None:
        U.open(request, "sys")
    if request.params.get('close') is not None:
        U.close(request, "sys")

    if request.params.get('show') is not None:
        U.show(request = request, category = "sys")


    return buildResponse(request, 'Systems')



@view_config(route_name='mech', renderer='ontomanager:templates/mech/mech.mako', permission='view')
def mech_view(request):

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


class GenerateXmlNsThread(threading.Thread):

    def __init__(self, request, model):
        threading.Thread.__init__(self)
        self.request = request
        self.ns = request.POST["ns"] # qname
        self.model = model

    def run(self):
        global generateXmlNsThreadBusy
        global CACHE
        generateXmlNsThreadBusy = True
        try:
            if self.ns is not None and self.request is not None:
                print("GenerateXmlNsThread Starting...")
                node = generic.getDefaultNode(CACHE, self.ns)
                soft.show_library(node)
                code = render('ontomanager:templates/soft/export_plcopen.mako', { 'project' : self.ns, 'CACHE' : CACHE } , request=self.request)
                print code
                soft.writeCode(code, self.ns, soft.GET_FILEPATH(self.model["config"]["plcopen_dir"], self.ns, "xml"))
        finally:
            print("GenerateXmlNsThread Done")
            generateXmlNsThreadBusy = False

        self.request.POST.clear()
        software_view(self.request)

generateXmlNsThreadBusy = False

class GeneratePyuafNsThread(threading.Thread):

    def __init__(self, request, model):
        threading.Thread.__init__(self)
        self.request = request
        self.ns = request.POST["ns"] # qname
        self.model = model

    def run(self):
        global generatePyuafNsThreadBusy
        global CACHE
        generatePyuafNsThreadBusy = True
        try:
            if self.ns is not None and self.request is not None:
                print("GeneratePyuafNsThread Starting...")
                node = generic.getDefaultNode(CACHE, self.ns)
                soft.show_library(node)
                code = render('ontomanager:templates/soft/export_pyuaf.mako', { 'project' : self.ns, 'CACHE' : CACHE } , request=self.request)


                importPartStart = code.find('# === imports ===')
                newCode = code[importPartStart:] + code[:importPartStart]



                soft.writeCode(newCode, self.ns, soft.GET_FILEPATH(self.model["config"]["pyuaf_dir"], self.ns, "py"))
        finally:
            print("GeneratePyuafNsThread Done")
            generatePyuafNsThreadBusy = False

        self.request.POST.clear()
        software_view(self.request)

generatePyuafNsThreadBusy = False


class ProcessDatasetThread(threading.Thread):

    def __init__(self, request, model):
        threading.Thread.__init__(self)
        global U
        self.request = request
        self.model = model
        self.user = U.getUser(request)

        self.ontologiesDir = self.model["config"]["ontologies_dir"]
        self.jsonldDir = self.model["config"]["jsonld_dir"]

    def log(self, msg, newLine=True):
        print msg
        if newLine:
            msg = b'\n%s' %msg.decode(u'utf-8')
        else:
            msg = b'%s' %msg.decode(u'utf-8')

        self.model["dataset"]["output"] += msg

    def logTitle(self, title):
        self.log("====================================================================================================", newLine=False)
        self.log(title)
        self.log("====================================================================================================")

    def run(self):
        global processDatasetThreadBusy
        global CACHE
        global U
        processDatasetThreadBusy = True
        self.model["dataset"]["thread_running"] = True
        try:
            print("ProcessDatasetThread Starting...")

            # erase the output
            self.model["dataset"]["output"] = u""

            # # update the ontologies_dir
            # for repoName in self.model["dataset"]["repository_checkboxes"]:
            #     if self.model["dataset"][repoName]["checked"]:
            #         location = configuration.REPOSITORIES[repoName]["location"]
            #         comment  = configuration.REPOSITORIES[repoName]["comment"]
            #         self.logTitle("Data source: %s (%s)" %(comment, location))
            #         self.model["config"]["ontologies_dir"] = location
            #         self.ontologiesDir = location
            #         break

            if self.model["dataset"]["run_metamodels"]["checked"]:
                self.logTitle("Running metamodels")
                rdfconvert.convert(
                    inputFilesOrDirs = [ os.path.join(self.ontologiesDir, "ttl"   , "metamodels") ],
                    inputFormat      = "n3",
                    inputExtensions  = [".ttl"],
                    outputDir        = os.path.join(self.jsonldDir , "metamodels"),
                    outputFormat     = "json-ld",
                    outputExt        = ".jsonld",
                    recursive        = True,
                    overwrite        = True,
                    loggingCb        = self.log,
                    logLevel         = rdfconvert.LOGLEVEL_INFO)


            if self.model['dataset']['run_models']['checked']:
                filenames = self.model.datasetGetCheckedFilenames(self.model['dataset']['run_models']['tree'])
                for filename in filenames:
                    iPath = os.path.join(self.ontologiesDir, "coffee")
                    IPath = os.path.join(self.jsonldDir)
                    oPath = os.path.join(self.jsonldDir)
                    command = "coffee %s -s -a -t -i %s -I %s -o %s -f" %(filename, iPath, IPath, oPath)

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


                    # while popen.poll() is None:
                    #     (stdout, stderr) = popen.communicate()
                    #     newLines = stdout.split('\n')
                    #     for line in newLines:
                    #         self.log(line)
            if self.model['dataset']['load_asserted']['checked']:
                self.model.loadAsserted()
                global CACHE
                CACHE = {}
                global U
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

        except Exception, e:
            print("ProcessDatasetThread ended with error: %s" %e)
        finally:
            print("ProcessDatasetThread Done")
            processDatasetThreadBusy = False
            self.model["dataset"]["thread_running"] = False

        self.request.POST.clear()
        dataset_view(self.request)


processDatasetThreadBusy = False




@view_config(route_name='elec', renderer='ontomanager:templates/elec/elec.mako', permission='view')
def electronics_view(request):
    global U

    if request.params.get('show') is not None:
        U.show(request, "elec")
    if request.params.get('open') is not None:
        U.open(request, "elec")
    if request.params.get('close') is not None:
        U.close(request, "elec")

    return buildResponse(request, 'Electronics')



@view_config(route_name='soft', renderer='ontomanager:templates/soft/soft.mako', permission='view')
def software_view(request):
    global U
    global M

    if request.params.get('show') is not None:
        U.show(request, "soft")
    if request.params.get('open') is not None:
        U.open(request, "soft")
    if request.params.get('close') is not None:
        U.close(request, "soft")

    if request.POST.has_key("submit"):

        print request.POST

        ns = request.POST["ns"]

        if request.POST["submit"] == "Generate PLCopen XML":

            global generateXmlNsThreadBusy
            if not generateXmlNsThreadBusy:
                t = GenerateXmlNsThread(request, M)
                t.start()

            url = request.route_url('soft')
            return HTTPFound(location=url + "?show=library;qname=%s" %ns)

        if request.POST["submit"] == "Download PLCopen XML":

            nsName = ns.split(":",1)[1]

            filePath = soft.GET_FILEPATH(M["config"]["plcopen_dir"], ns, "xml")
            if os.path.exists(filePath):
                print "Sending file %s" %filePath
                response = FileResponse(filePath, request=request, content_type="text/xml")
                response.content_disposition = 'attachment; filename="%s.xml"' %nsName
                return response
            else:
                print "File %s not found on server" %filePath
                return HTTPNotFound("File %s not found on server" %filePath)


        if request.POST["submit"] == "Generate pyUAF code":

            global generatePyuafNsThreadBusy
            if not generatePyuafNsThreadBusy:
                t = GeneratePyuafNsThread(request, M)
                t.start()

            url = request.route_url('soft')
            return HTTPFound(location=url + "?show=library;qname=%s" %ns)

        if request.POST["submit"] == "Download pyUAF code":

            nsName = ns.split(":",1)[1]

            filePath = soft.GET_FILEPATH(M["config"]["pyuaf_dir"], ns, "py")
            if os.path.exists(filePath):
                print "Sending file %s" %filePath
                response = FileResponse(filePath, request=request, content_type="text/plain")
                response.content_disposition = 'attachment; filename="%s.py"' %nsName
                return response
            else:
                print "File %s not found on server" %filePath
                return HTTPNotFound("File %s not found on server" %filePath)

    return buildResponse(request, 'Software')


@view_config(route_name='query', renderer='ontomanager:templates/query.mako', permission='query')
def query_view(request):
    global U

    if request.POST.has_key("submit"):
        U.query_submit(request)

    return buildResponse(request, 'Query')

@view_config(route_name='org', renderer='ontomanager:templates/org/org.mako')
def org_view(request):
    global U

    if request.params.get('show') is not None:
        U.show(request, "org")

    return buildResponse(request, 'Org')



@view_config(route_name='login', renderer='ontomanager:templates/login.mako')
@forbidden_view_config(renderer='ontomanager:templates/login.mako')
def login(request):
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



    print("==========")
    print request.session
    print request.session.created
    print request.session.new
    print request.cookies

    response = buildResponse(request, "")
    response['authentication'] = dict( message = message,
                                       url = request.application_url + '/login',
                                       came_from = came_from,
                                       login = login,
                                       password = password
                                      )
    return response

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('login'),
                     headers = headers)

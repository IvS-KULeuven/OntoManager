"""
Some helper functions to process the ontologies.
"""

import os
import fnmatch

from rdflib import Graph, RDF, OWL


def findFiles(directory, pattern):
    """
    Find files with the given pattern (e.g. '*.ttl') in the given directory.
    """
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def getSourceContents(fileName):
    """
    Read the contents of a source code file.
    """
    try:
        f = file(fileName)
        contents = f.read()
        f.close()
        return contents
    except Exception, e:
        return "Error: %s" %(fileName, e)


def getOntologies(dir):
    """
    Get all ontologies.
    """
    ret = []
    ret += getMetaModels(dir)
    ret += getModels(dir)
    return ret


def getMetaModels(dir):
    """
    Get all metamodels.
    """
    fileNames = findFiles(os.path.join(dir, "ttl", "metamodels"), "*.ttl")

    d = {}

    for fileName in fileNames:
        g = Graph()
        g.load(fileName, format="n3")
        ontologies = [x for x, y, z in g.triples((None, RDF.type, OWL.Ontology))]

        if len(ontologies) == 1:
            uri = str(ontologies[0])

            if not d.has_key(uri):
                d[uri] = { "type"     : "metamodel",
                           "uri"      : uri,
                           "sources"  : [],
                           "prefixes" : []}

            d[uri]["sources"].append( { "type" : "ttl",
                                        "file" : fileName } )

    return sorted(d.values(), key=lambda x: x["uri"])


def extractUriAndPrefixFromCoffeeModel(contents):
    """
    Read a coffeescript Model, and extract its URI and prefix.
    """
    lines = contents.split('\n')
    for line in lines:
        l = line.strip()
        if l[0:6] == 'MODEL ':
            split = l[6:].rsplit(":", 1)
            if len(split) == 2:
                uri    = split[0].strip().strip("'\"")
                prefix = split[1].strip().strip("'\"")

                return uri, prefix


def getModels(dir):
    """
    Get all models.
    """
    fileNames = findFiles(os.path.join(dir, "coffee", "models"), "*.coffee")

    d = {}

    for fileName in fileNames:
        print fileName
        f = file(fileName, mode='r')
        lines = f.readlines()
        for line in lines:
            l = line.strip()
            if l[0:6] == 'MODEL ':
                split = l[6:].rsplit(":", 1)
                print "-->", split
                if len(split) == 2:
                    uri    = split[0].strip().strip("'\"")
                    prefix = split[1].strip().strip("'\"")

                    if not d.has_key(uri):
                        d[uri] = { "type"     : "model",
                                   "uri"      : uri,
                                   "sources"  : [],
                                   "prefixes" : []}

                    d[uri]["sources"].append( { "type" : "coffee",
                                                "file" : fileName } )
                    d[uri]["prefixes"].append(prefix)
        f.close()

    return sorted(d.values(), key=lambda x: x["uri"])


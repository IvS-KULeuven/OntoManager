import rdflib

from rdflib import Graph, RDF, OWL, ConjunctiveGraph

import os, fnmatch
import json


class Ontology:
    def __init__(self, uri):
        self.uri = uri
        self.imports = []

    def addImport(self, uri):
        self.imports.append(uri)



def findFiles(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def getFileTree(dir, pattern):
    tree = []
    matches = False

    children = os.listdir(dir)

    dirChildren = []
    fileChildren = []

    for child in children:

        if os.path.isdir(os.path.join(dir, child)):
            dirChildren.append(child)
        else:
            fileChildren.append(child)

    dirChildren.sort()
    fileChildren.sort()

    for child in dirChildren:
        childMatches, childTree = getFileTree(os.path.join(dir, child), pattern)

        if childMatches:
            matches = True
            tree.append( { child : childTree } )

    for child in fileChildren:
        if fnmatch.fnmatch(child, pattern):
            matches = True
            tree.append(child)

    return matches, tree



def getJsTree(abspath, pattern):
    matches, tree = getFileTree(abspath, pattern)
    jsTree = convertToJsTree(abspath, '', tree)
    return jsTree



def convertToJsTree(abspath,relpath, tree):

    ret = []

    for item in tree:

        d = {}

        if isinstance(item, str):
            # the item is a file
            d['text'] = item
            d['type'] = 'file'
            #d['icon'] = "/static/document_16x16.png"
            d['id'] = relpath + "/" + item
            d['_filename_'] = os.path.join(abspath, item)
            d['state'] = { 'selected' : False }



        elif isinstance(item, dict):
            # the item is a folder with a single key:value pair

            folderName, folderContents = item.items()[0]

            d['text'] = folderName
            d['type'] = 'folder'
            d['id'] = relpath + "/" + folderName
            d['_filename_'] = os.path.join(abspath, folderName)
            d['children'] = convertToJsTree(d['_filename_'], d['id'], folderContents)
            d['state'] = { 'selected' : False, "checkbox_disabled": True, "disabled" : True }
            d['a_attr'] = { 'class': "folder" }

        ret.append(d)

    return ret


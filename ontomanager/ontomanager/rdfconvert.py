"""
This module contains a function to convert files (or a hierarchic tree of files) from
one RDF format to another.
"""

from logging import INFO, DEBUG
from rdflib import ConjunctiveGraph
import os
import fnmatch

# input formats (convert FROM this format)
INPUT_FORMAT_TO_EXTENSIONS = { "application/rdf+xml" : [".xml", ".rdf", ".owl"],
                               "text/html"           : [".html"],
                               "xml"                 : [".xml", ".rdf", ".owl"],
                               "json-ld"             : [".jsonld", ".json-ld"],
                               "ttl"                 : [".ttl"],
                               "nt"                  : [".nt"],
                               "nquads"              : [".nq"],
                               "trix"                : [".xml", ".trix"],
                               "rdfa"                : [".xhtml", ".html"],
                               "n3"                  : [".n3", ".ttl"] }

# output formats (convert TO this format)
OUTPUT_FORMAT_TO_EXTENSION = { "xml"        : ".xml",
                               "pretty-xml" : ".xml",
                               "json-ld"    : ".jsonld",
                               "nt"         : ".nt",
                               "nquads"     : ".nq",
                               "trix"       : ".xml",
                               "ttl"        : ".ttl",
                               "n3"         : ".n3" }


def convert(inputFilesOrDirs, inputFormat, inputExtensions, outputDir, outputFormat, outputExt, recursive=True, overwrite=True, loggingFunction=None):
    """
    Conversion function.

    @param inputFilesOrDirs : a list of paths (to a file or to a directory)
    @param inputFormat      : input files format (the keys of INPUT_FORMAT_TO_EXTENSIONS)
    @param inputExtensions  : a list of input files extensions (one or more values of INPUT_FORMAT_TO_EXTENSIONS)
    @param outputFormat     : output files format (the keys of OUTPUT_FORMAT_TO_EXTENSIONS)
    @param outputExt        : the output files extension (one of the values of OUTPUT_FORMAT_TO_EXTENSIONS)
    @param recursive        : if inputFilesOrDirs contains directories, descend into these directories to find all files
    @param overwrite        : True to overwrite any existing file.
    """
    if loggingFunction is None:
        loggingFunction = INFO

    # process each input file sequentially:
    for inputFileOrDir in inputFilesOrDirs:

        loggingFunction("Processing input file or directory '%s'" %inputFileOrDir)

        # check if the file exists, and if it's a directory or a file
        isdir = False
        if os.path.exists(inputFileOrDir):
            if os.path.isdir(inputFileOrDir):
                DEBUG("'%s' exists and is a directory" %inputFileOrDir)
                inputFileOrDir = os.path.abspath(inputFileOrDir)
                isdir = True
            else:
                DEBUG("'%s' exists and is a file" %inputFileOrDir)
        else:
            raise IOError("Input file '%s' was not found" %inputFileOrDir)

        DEBUG("Input format: %s" %inputFormat)
        DEBUG("Output format: %s" %outputFormat)

        # find out which extensions we should match
        if inputExtensions is None:
            inputExtensions = INPUT_FORMAT_TO_EXTENSIONS[inputFormat]

        DEBUG("Input extensions: %s" %inputExtensions)

        # find out which output extension we should write
        if outputExt:
            outputExtension = outputExt
        else:
            outputExtension = OUTPUT_FORMAT_TO_EXTENSION[outputFormat]

        DEBUG("Output extension: '%s'" %outputExtension)

        inputFiles = []

        if isdir:
            DEBUG("Now walking the directory (recursive = %s):" %recursive)
            for root, dirnames, filenames in os.walk(inputFileOrDir):
                DEBUG("   * Finding files in '%s'" %root)
                for extension in inputExtensions:
                    for filename in fnmatch.filter(filenames, "*%s" %extension):
                        DEBUG("     -> found '%s'" %filename)
                        inputFiles.append(os.path.join(root, filename))
                if not recursive:
                    break

        else:
            inputFiles.append(inputFileOrDir)

        # create the graph, and parse the input files

        for inputFile in inputFiles:

            g = ConjunctiveGraph()
            g.parse(inputFile, format=inputFormat)

            DEBUG("the graph was parsed successfully")

            # if no output directory is specified, just print the output to the stdout
            if outputDir is None:
                output = g.serialize(None, format=outputFormat)
                DEBUG("output:")
                print(output)
            # if an output directory was provided, but it doesn't exist, then exit the function
            elif not os.path.exists(outputDir):
                raise IOError("Output dir '%s' was not found" %outputDir)
            # if the output directory was given and it exists, then figure out the output filename
            # and write the output to disk
            else:
                head, tail = os.path.split(inputFile)
                DEBUG("head, tail: %s, %s" %(head, tail))

                # remove the common prefix from the head and the input directory
                # (otherwise the given input path will also be added to the output path)
                commonPrefix = os.path.commonprefix([head, inputFileOrDir])
                DEBUG("inputFileOrDir: %s" %inputFileOrDir)
                DEBUG("common prefix: %s" %commonPrefix)
                headWithoutCommonPrefix = head[len(commonPrefix)+1:]
                DEBUG("head without common prefix: %s" %headWithoutCommonPrefix)
                outputAbsPath = os.path.join(os.path.abspath(outputDir),
                                             headWithoutCommonPrefix)
                DEBUG("output absolute path: %s" %outputAbsPath)

                outputFileName = os.path.splitext(tail)[0] + outputExtension
                outputAbsFileName = os.path.join(outputAbsPath, outputFileName)

                DEBUG("output filename: '%s'" %outputAbsFileName)

                # for safety, check that we're not overwriting the input file
                if outputAbsFileName == os.path.abspath(inputFile):
                    IOError("Input file '%s' is the same as output file" %outputAbsFileName)
                else:
                    DEBUG("this file is different from the input filename")

                # check if we need to skip this file
                skipThisFile = os.path.exists(outputAbsFileName) and not overwrite

                if skipThisFile:
                    DEBUG("this file will be skipped")
                else:
                    dirName = os.path.dirname(outputAbsFileName)
                    if not os.path.exists(dirName):
                        DEBUG("Now creating %s since it does not exist yet" %dirName)
                        os.makedirs(dirName)

                    loggingFunction("Writing %s" %outputAbsFileName)
                    g.serialize(outputAbsFileName, auto_compact=True, format=outputFormat)

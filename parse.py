#!/usr/bin/python
# -*-coding: utf8 -*-
import sys, os
from LilyParser.Parser import Parser as LyParser

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Insufficient Argument! : No file path."
        exit(0)

    filepath = sys.argv[1]
    try:
        file_to_parse = file(filepath)
    except IOError:
        print "Invalid Argument! : No such file."

    lilydoc = file_to_parse.read()

    lily = LyParser(lilydoc).Parse()

    # header
    print "=== HEADER ==="
    for key, value in lily['header'].variables.iteritems():
        print key + " : " + value

    # version
    print "=== VERSION ==="
    print lily['version']

    # variables
    for key, value in lily.variables.iteritems():
        print "=== variable "+key+" ==="
        print value
        print "attributes : " + str(value.attributes)
        if value.name == "Music":
            print "relative : " + value.relative
            print "notes : " + str(value.notes)

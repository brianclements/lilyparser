#!/usr/bin/python
# -*-coding: utf8 -*-
import sys, os
from LilyParser.Parser import Parser as lp

DEBUG = True

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
    lilyparser = lp(lilydoc)

    if DEBUG:
        lilyparser._print_tokens()
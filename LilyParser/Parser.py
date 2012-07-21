#!/usr/bin/python
# -*- coding: utf8 -*-
from cStringIO import StringIO
from tokenize import generate_tokens

class Parser:
    def __init__(self, str):
        self._tokenize(str)

    def _tokenize(self, str):
        STRING = 1
        self.tokens = list(token[STRING] for token in generate_tokens(StringIO(str).readline) if token[STRING])

    def _print_tokens(self):
        for token in self.tokens:
            if token == " ":
                print "Space"
            elif token == "\n":
                print "nl"
            else:
                print token

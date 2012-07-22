#!/usr/bin/python
# -*- coding: utf8 -*-

# custom modules
from Data import LyData as Data
from Functions import RefineStringMargin
from Debug import DEBUG
from Unit import LyUnit

class Root(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Root"
        super(Root, self).__init__(string)

    def Parse(self):
        self._tokenize()
        self.data = Data('Root')

        for token in self.tokens:
            pass # todo

        return self.data

class String(LyUnit):
    def __init__(self, string):
        super(String, self).__init__(string)

    def Parse(self):
        self.data = RefineStringMargin(self.data, ['"', "'", " "])
        return self.data

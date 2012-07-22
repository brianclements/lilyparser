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

        token_index = 0
        while token_index < len(self.tokens):
            token = self.tokens[token_index]
            if token == "\header":
                self.data['header'] = Header(RefineStringMargin(self.tokens[token_index+1], ["{", "}"])).Parse()
                token_index += 2
            else:
                self.data.attributes.append(token)
                token_index += 1

        return self.data

class Header(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Header"
        super(Header, self).__init__(string)

    def Parse(self):
        self._tokenize()
        self.data = Data('Header')

        token_index = 0
        while token_index < len(self.tokens):
            token = self.tokens[token_index]
            if self.tokens[token_index+1] == "=":
                variable_key = token
                variable_value = self.tokens[token_index+2]
                self.data.variables[variable_key] = String(variable_value).Parse()
                token_index += 3
            else:
                self.data.attributes.append(token)
                token_index += 1

        return self.data

class String(LyUnit):
    def __init__(self, string):
        super(String, self).__init__(string)

    def Parse(self):
        self.data = RefineStringMargin(self.string, ['"', "'", " "])
        return self.data

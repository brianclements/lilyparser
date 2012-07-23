#!/usr/bin/python
# -*- coding: utf8 -*-

# custom modules
from Data import LyData as Data
from Functions import RefineStringMargin, IsGroup, IsString
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
        self.ProcessTokens()

        return self.data

    def ProcessTokens(self):
        token_index = 0
        while token_index < len(self.tokens):
            token = self.tokens[token_index]
            if token == "\\header":
                self.data['header'] = Header(RefineStringMargin(self.tokens[token_index+1], ["{", "}"])).Parse()
                token_index += 2
            else:
                next_token = self.tokens[token_index+1]
                if next_token == "=":
                    variable = self.tokens[token_index+2]
                    if IsGroup(variable):
                        self.data.variables[token] = Variable(variable).Parse()
                        token_index += 3
                    elif IsString(variable):
                        self.data.variables[token] = String(variable).Parse()
                        token_index += 3
                    else:
                        if variable == "\\relative":
                            relative = self.tokens[token_index+3]
                            variable = self.tokens[token_index+4]
                            self.data.variables[token] = Music(variable, relative).Parse()
                            token_index += 5
                        else:
                            pass # todo
                else:
                    self.data.attributes.append(token)
                    token_index += 1

class Header(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Header"
        super(Header, self).__init__(string)

    def Parse(self):
        self._tokenize()
        self.data = Data('Header')
        self.ProcessTokens()
        return self.data

    def ProcessTokens(self)
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

class Variable(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Variable"
        super(Variable, self).__init__(string)

    def Parse(self):
        self.string = RefineStringMargin(self.string, ['{', '}'])
        self._tokenize()
        self.data = Data('Variable')
        self.ProcessTokens()
        return self.data

    def ProcessTokens():
        token_index = 0
        while token_index < len(self.tokens):
            token = self.tokens[token_index]
            if token == "\\key":
                pass # todo

class Music(LyUnit):
    def __init__(self, string, relative):
        if DEBUG():
            pring "__init__ of Music"
        super(Music, self).__init__(string)
        self._relative = relative

    def Parse(self):
        self.string = RefineStringMargin(self.string, ['{', '}'])
        self._tokenize()
        self.data = Data('Music')
        self.data.relative = self._relative
        Variable.ProcessTokens(self)
        return self.data

class String(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Stirng"
        super(String, self).__init__(string)

    def Parse(self):
        self.data = RefineStringMargin(self.string, ['"', "'", " "])
        return self.data

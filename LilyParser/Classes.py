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
            elif token == "\\version":
                self.data['version'] = String(self.tokens[token_index+1]).Parse()
                token_index += 2
            elif token == "\\score":
                self.data['score'] = Score(RefineStringMargin(self.tokens[token_index+1], ["{", "}"])).Parse()
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
                            self.data.attributes.append(token)
                            token_index += 1
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

    def ProcessTokens(self):
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

    def ProcessTokens(self):
        token_index = 0
        while token_index < len(self.tokens):
            token = self.tokens[token_index]
            if token == "\\key":
                self.data['key'] = self.tokens[token_index+1]
                token_index += 2
            elif token == "\\major":
                self.data['major'] = True
                token_index += 1
            elif token == "\\time":
                self.data['time'] = self.tokens[token_index+1]
                token_index += 2
            elif token == "\\clef":
                self.data['clef'] = self.tokens[token_index+1]
                token_index += 2
            else:
                if token[0] in "cdefgab":
                    self.data.notes.append(token)
                else:
                    self.data.attributes.append(token)
                token_index += 1

class Music(Variable):
    def __init__(self, string, relative):
        if DEBUG():
            print "__init__ of Music"
        super(Music, self).__init__(string)
        self._relative = relative

    def Parse(self):
        self.string = RefineStringMargin(self.string, ['{', '}'])
        self._tokenize()
        self.data = Data('Music')
        self.data.relative = self._relative
        self.ProcessTokens()
        return self.data

class Score(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Score"
        super(Score, self).__init__(string)
    
    def Parse(self):
        self._tokenize()
        self.data = Data('Score')
        self.ProcessTokens()
        return self.data
    
    def ProcessTokens(self):
        token_index = 0
        while token_index < len(self.tokens):
            token = self.tokens[token_index]
            token_index += 1 # todo

class String(LyUnit):
    def __init__(self, string):
        if DEBUG():
            print "__init__ of Stirng"
        super(String, self).__init__(string)

    def Parse(self):
        self.data = RefineStringMargin(self.string, ['"', "'", " "])
        return self.data

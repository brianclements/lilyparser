#!/usr/bin/python
# -*- coding: utf8 -*-

# custom modules
from Data import LyData as Data, LyTokenWaitingQueue as WaitingQ
from Functions import RefineStringMargin, TokenizeString
from Debug import DEBUG

class LyUnit(object):
    spaces = [" ", "\n", "\t"]

    def __init__(self, string):
        self.string = string

    def _tokenize(self):
        self._raw_tokens = TokenizeString(self.string)

        if DEBUG():
            print "RAW TOKENS..."
            self._print_raw_tokens()

        self._refine_raw_tokens()

    def _print_raw_tokens(self):
        for token in self._raw_tokens:
            if token == " ":
                print "Space"
            elif token == "\n":
                print "nl"
            else:
                print token

    def _refine_raw_tokens(self):
        self.tokens = []

        _waiting_queue = WaitingQ()
        for rtoken in self._raw_tokens:
            if rtoken in self.spaces:
                continue

            if _waiting_queue.IsWaitingSomething():
                if _waiting_queue.IsWaiting(rtoken):
                    _include_rtoken = _waiting_queue.IncludeTokensWaited()
                    _exclude_rtoken = _waiting_queue.ExcludeTokensWaited()
                    if _include_rtoken:
                        _waiting_queue.Append(rtoken)
                    self.tokens.append(_waiting_queue.ToString())
                    _waiting_queue.Clear()
                    if _include_rtoken or _exclude_rtoken:
                        continue
                else:
                    if rtoken == "\n" or rtoken == "\t":
                        _waiting_queue.Append(" ")
                    else:
                        _waiting_queue.Append(rtoken)

            if not _waiting_queue.IsWaitingSomething():
                if rtoken == "{":
                    _waiting_queue.WillWaitAndInclude(['}'], check_nested=['{'])
                    _waiting_queue.Append(rtoken)
                elif rtoken == "(":
                    _waiting_queue.WillWaitAndInclude([')'], check_nested=['('])
                    _waiting_queue.Append(rtoken)
                elif rtoken == "<<":
                    _waiting_queue.WillWaitAndInclude(['>>'])
                    _waiting_queue.Append(rtoken)
                else:
                    self.tokens.append(rtoken)

        if DEBUG():
            print "REFINED TOKENS..."
            self._print_tokens()

    def _print_tokens(self):
        for token in self.tokens:
            print token

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

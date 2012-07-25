#!/usr/bin/python
# -*- coding: utf8 -*-

# custom modules
from Functions import RefineStringMargin, RefineStringSpaces
from Debug import DEBUG

# external modules
from collections import deque

class LyData(dict):
    def __init__(self, name):
        super(LyData, self).__init__()
        self.name = name
        self.attributes = list()
        self.variables = dict()
        self.notes = list()

    def SetName(self, name):
        self.name = name

class LyTokenWaitingQueue:
    def __init__(self):
        self._waiting_queue = deque()
        self._tokens_waited = []
        self._include_waited_tokens = False
        self._exclude_waited_tokens = False
        self._check_nested = []
        self._nested_count = 0

    def IsWaitingSomething(self):
        return len(self._tokens_waited) != 0

    def IsWaiting(self, rtoken):
        if rtoken in self._check_nested:
            self._nested_count += 1
        elif rtoken in self._tokens_waited:
            if self._nested_count == 0:
                return True
            else:
                self._nested_count -= 1
        return False

    def WillWait(self, tokens_waited, check_nested=[]):
        if DEBUG():
            print "Start waiting..." + str(tokens_waited)
        self._tokens_waited = tokens_waited
        self._check_nested = check_nested

    def WillWaitAndInclude(self, tokens_waited, check_nested=[]):
        self.WillWait(tokens_waited, check_nested)
        self._include_waited_tokens = True

    def WillWaitAndExclude(self, tokens_waited, check_nested=[]):
        self.WilWait(tokens_waited, check_nested)
        self._exclude_waited_tokens = True

    def IncludeTokensWaited(self):
        return self._include_waited_tokens

    def ExcludeTokensWaited(self):
        return self._exclude_waited_tokens

    def Clear(self):
        self._waiting_queue.clear()
        self._tokens_waited = []
        self._include_waited_tokens = False
        self._exclude_waited_tokens = False
        self._check_nested = []
        self._nested_count = 0

    def Append(self, el):
        self._waiting_queue.append(el)

    def ToString(self):
        result = " ".join(self._waiting_queue)
        result = RefineStringMargin(result, [" ", "\t", "\b"])
        result = RefineStringSpaces(result)
        return result

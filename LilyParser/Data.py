#!/usr/bin/python
# -*- coding: utf8 -*-

# custom modules
from Functions import RefineStringMargin

# external modules
from collections import deque

class LyData(dict):
    def __init__(self, name):
        super(LyData, self).__init__()
        self.name = name

    def SetName(self, name):
        self.name = name

class LyTokenWaitingQueue:
    def __init__(self, tokens_waited):
        self._waiting_queue = deque()
        self._tokens_waited = tokens_waited
        self._include_waited_tokens = False
        self._exclude_waited_tokens = False

    def IsWaitingSomething(self):
        return len(self._tokens_waited) != 0

    def IsWaiting(self, rtoken):
        return rtoken in self._tokens_waited

    def WillWait(self, tokens_waited):
        self._tokens_waited = tokens_waited

    def WillWaitAndInclude(self, tokens_waited):
        self.WillWait(tokens_waited)
        self._include_waited_tokens = True

    def WillWaitAndExclude(self, tokens_waited):
        self.WilWait(tokens_waited)
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

    def Append(self, el):
        self._waiting_queue.append(el)

    def ToString(self):
        result = ""
        for el in self._waiting_queue:
            try:
                result += str(el)
            except:
                pass

        return RefineStringMargin(result, [" ", "\t", "\b"])

#!/usr/bin/python
# -*- coding: utf8 -*-

# custom modules
from Classes import Root

class Parser:
    def __init__(self, _str):
        self.string = _str;

    def Parse(self):
        return Root(self.string).Parse()

#!/usr/bin/python
# -*- coding: utf8 -*-
from cStringIO import StringIO
from tokenize import generate_tokens

class LilyParser:
    def __init__(self, str):
        self._tokenize(str)

    def _tokenize(self, str):
        STRING = 1
        self.tokens = list(token[STRING] for token in generate_tokens(StringIO(str).readline) if token[STRING])

#!/usr/bin/python
# -*- encoding: utf8 -*-

# external modules
from cStringIO import StringIO
from tokenize import generate_tokens

def RefineStringMargin(string, margin_list):
    result = string
    while result[0] in margin_list:
        result = result[1:]
    while result[len(result)-1] in margin_list:
        result = result[:len(result)-1]
    return result

def TokenizeString(string):
    STRING = 1
    return list(token[STRING] for token in generate_tokens(StringIO(string).readline) if token[STRING])

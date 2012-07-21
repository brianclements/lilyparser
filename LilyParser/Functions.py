#!/usr/bin/python
# -*- encoding: utf8 -*-

# custom modules
from Debug import DEBUG

# external modules
import re

def RefineStringMargin(string, margin_list):
    result = string
    while result[0] in margin_list:
        result = result[1:]
    while result[len(result)-1] in margin_list:
        result = result[:len(result)-1]
    return result

def RefineStringSpaces(string):
    while "  " in string:
        string = string.replace("  ", " ")
    while "\t" in string:
        string = string.replace("\t", " ")
    return string

def TokenizeString(string):
    _string = string

    # prevent "string" from being tokenized
    string_list = []
    string_index = 0
    while True:
        m = re.search(r'(\".+\")', _string)
        if m:
            matched_str = m.group(0)
            if DEBUG():
                print "Tokenized String " + str(string_index) + " : " + matched_str
            _string = _string.replace(matched_str, "%%STRING_" + str(string_index) + "%%", 1)
            string_list.append(matched_str)
            string_index += 1
        else:
            break

    _string = _string.replace("\t", " ").replace("\n", " ")
    while "  " in _string:
        _string = _string.replace("  ", " ")
    _list = re.split('([{}()#\s])', _string)
    while "" in _list:
        _list.remove("")

    # replace %%STRING_(INDEX)%% with the real string
    string_index = 0
    for el in _list:
        if el == "%%STRING_" + str(string_index) + "%%":
            _list[_list.index(el)] = string_list[string_index]
            string_index += 1
    return _list 

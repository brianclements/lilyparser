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
    find_from = 0
    while True:
        if _string.find('"', find_from) >= 0:
            quote_start = _string.find('"', find_from)
            find_from = quote_start + 1
            while True:
                if _string.find('"', find_from) >= 0:
                    quote_end = _string.find('"', find_from)
                    if _string[quote_end-1] == "/" and _string[quote_end-2] != "/":
                        find_from = quote_end + 1
                    else:
                        _quote = _string[quote_start:quote_end+1]
                        string_list.append(_quote)
                        _string = _string.replace(_quote, "%%STRING_"+str(string_index)+"%%", 1)
                        if DEBUG():
                            print "STRING "+str(string_index)+" : "+_quote
                        string_index += 1
                        find_from = quote_end + 1
                        break
                else:
                    break
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

def IsGroup(string):
    return string.startswith("{") and string.endswith("}")

def IsString(string):
    return string.startswith('"') and string.endswith('"')

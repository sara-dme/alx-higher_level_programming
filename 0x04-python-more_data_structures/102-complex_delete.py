#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delkey = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delkey.append(key)
    for key in delkey:
        del a_dictionary[key]
    return a_dictionary

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = []
    for i in range(a_dictionary):
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary

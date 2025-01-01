#!/usr/bin/python3
def number_keys(a_dictionary):
    return len(list(map(lambda k: k, a_dictionary.keys())))

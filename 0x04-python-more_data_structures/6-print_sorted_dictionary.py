#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys(), key=lambda k: k)
    list(map(lambda k: print(f"{k}: {a_dictionary[k]}"), sorted_keys))

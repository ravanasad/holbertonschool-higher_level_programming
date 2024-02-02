#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for x in sorted_keys:
        print("{}: {}".format(x, a_dictionary[x]))

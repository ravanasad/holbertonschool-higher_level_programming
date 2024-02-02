#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    uniq_list = list(my_set)
    return sum(uniq_list)

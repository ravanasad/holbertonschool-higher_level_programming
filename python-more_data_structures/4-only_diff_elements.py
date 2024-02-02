#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    c_set = {x for x in set_1 if x in set_2}
    print(c_set)
    set_1.update(set_2)
    return {x for x in set_1 if x not in c_set}


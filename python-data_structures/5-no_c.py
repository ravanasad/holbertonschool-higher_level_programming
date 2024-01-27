#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x in ['c', 'C']:
            new_string += ' '
        else:
            new_string += x
    print("{}".format(new_string))

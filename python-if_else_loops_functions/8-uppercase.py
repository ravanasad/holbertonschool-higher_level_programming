#!/usr/bin/python3
def uppercase(c):
    for i in c:
        ord_num = ord(i)
        if ord_num >= 97 and ord_num <= 122:
            i = chr(ord_num - 32)
        print("{}".format(i), end='')
    print("")

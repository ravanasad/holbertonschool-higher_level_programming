#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    functions = {"+": add, "-": sub, "*": mul, "/": div}
    for op in functions:
        print("{} {} {} = {}".format(a, op, b, functions[op](a, b)))

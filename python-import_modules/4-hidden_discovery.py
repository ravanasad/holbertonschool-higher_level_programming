#!/usr/bin/python3

if __name__ == "__main__":
    names = dir("hidden_4")
    for x in sorted(names):
        if not x.startswith('__'):
            print(x)

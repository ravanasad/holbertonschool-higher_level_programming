#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = 0
    for x in range(1, len(argv)):
        result += int(argv[x])
    print(result)

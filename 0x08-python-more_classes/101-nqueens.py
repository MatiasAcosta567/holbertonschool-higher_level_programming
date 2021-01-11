#!/usr/bin/python3
from sys import argv

if argv == 2:
    number = argv[1]
    if (type(number) != int):
        print("N must be a number")
        sys.exit(1)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)
else:
    print("Usage: nqueens N")
    sys.exit(1)

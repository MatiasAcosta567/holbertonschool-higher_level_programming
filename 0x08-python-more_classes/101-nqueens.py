#!/usr/bin/python3
from sys import argv, exit

if len(argv) == 2:
    number = argv[1]
    if (number.isdigit()):
        number = int(number)
        if number < 4:
            print("N must be at least 4")
            exit(1)
    else:
        print("N must be a number")
        exit(1)
else:
    print("Usage: nqueens N")
    exit(1)
solution = False
while(

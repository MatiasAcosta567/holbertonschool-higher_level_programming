#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv) - 1
    res = 0
    if args != 0:
        for i in range(1, args + 1):
            res += int(sys.argv[i])
    print("{:d}".format(res))

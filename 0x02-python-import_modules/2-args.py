#!/usr/bin/python3
import sys
args = len(sys.argv) - 1
if args == 0:
    print("0 arguments.")
else:
    print("{:d} {}:".format(args, "argument" if args == 1 else "arguments"))
    for i in range(1, args + 1):
        print("{}".format(sys.argv[i]))
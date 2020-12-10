#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    ac = len(argv)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num1 = argv[1]
        op = argv[2]
        num2 = argv[3]
        if op != '+' and op != '-' and op != '*' and op != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        if op == '+':
            print("{:d} {} {:d} = {:d}".format(num1, op, num2, add(num1, num2)))
        if op == '-':
            print("{:d} {} {:d} = {:d}".format(num1, op, num2, sub(num1, num2)))
        if op == '*':
            print("{:d} {} {:d} = {:d}".format(num1, op, num2, mov(num1, num2)))
        if op == '/':
            print("{:d} {} {:d} = {:d}".format(num1, op, num2, div(num1, num2)))

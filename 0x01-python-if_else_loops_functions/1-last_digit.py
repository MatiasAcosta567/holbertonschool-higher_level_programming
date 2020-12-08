#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (last < 6 and last != 0) or number < 0:
    if number < 0:
        last *= -1
        print("Last digit of {:d} is {:d}".format(number, last), end="")
    else:
        print("Last digit of {:d} is {:d}".format(number, last), end="")
    print(" and is less than 6 and not 0")
elif last > 5:
    print("Last digit of {:d} is {:d}".format(number, last), end="")
    print(" and is greater than 5")
elif last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))

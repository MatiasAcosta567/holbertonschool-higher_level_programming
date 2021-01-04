#!/usr/bin/python3
import dis
def myfun(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            result += (a ** b) / i
        except:
            break
    result = b + a
    return result
dis.dis(myfun)

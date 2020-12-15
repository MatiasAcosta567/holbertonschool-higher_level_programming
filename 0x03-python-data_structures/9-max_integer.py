#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maxim = 0
        for i in my_list:
            if i > maxim:
                maxim = i
        return maxim
    else:
        return None

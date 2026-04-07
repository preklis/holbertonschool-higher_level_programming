#!/usr/bin/python3
def max_integer(my_list = []):
    maxz = - 2 ** 31 - 1
    for i in my_list:
        maxz = max(maxz,i)
    return maxz

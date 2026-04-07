#!/usr/bin/python3
def max_integer(my_list = []):
    if len(my_list) == 0:
        return None
    maxz = - 2 ** 31 - 1
    for i in my_list:
        if i > maxz:
            maxz=i
    return maxz

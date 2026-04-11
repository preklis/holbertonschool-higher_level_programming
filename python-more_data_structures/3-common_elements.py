#!/usr/bin/python3
def common_elements(s1={}, s2={}):
    result = []
    for i in s2:
        if i in s1:
            result.append(i)
    return result

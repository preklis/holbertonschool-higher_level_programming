#!/usr/bin/python3
def only_diff_elements(s1={}, s2={}):
    result = []
    for i in s2:
        if i not in result:
            result.append(i)
        else:
            del result[result.index(i)]
    for i in s1:
        if i not in result:
            result.append(i)
        else:
            del result[result.index(i)]
    return result

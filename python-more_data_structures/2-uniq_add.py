#!/usr/bin/python3
def uniq_add(list=[]):
    checker=[]
    sum=0
    for i in list:
        if i not in checker:
            sum+=i
            checker.append(i)
    return sum

#!/usr/bin/python3
def search_replace(list=[], val1=0, val2=0):
    listnew = []
    for i in range(0, len(list)):
        if list[i] == val1:
            listnew.append(val2)
        else:
            listnew.append(list[i])
    return listnew

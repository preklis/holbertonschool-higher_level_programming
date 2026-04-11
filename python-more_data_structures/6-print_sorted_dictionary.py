#!/usr/bin/python3
def print_sorted_dictionary(dict={}):
    lis=list(dict)
    lis.sort()
    for i in lis:
        print("{0}: {1}".format(i,dict.get(i)))

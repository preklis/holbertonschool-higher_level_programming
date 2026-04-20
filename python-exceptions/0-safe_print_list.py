#!/usr/bin/python3
def safe_print_list(l=[], i=0):
    count = 0
    for i in  range (0,i):
        try:
            print(l[i],end="")
            count += 1
        except IndexError:
            break
    print()
    return count;

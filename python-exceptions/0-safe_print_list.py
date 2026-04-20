#!/usr/bin/python3
def safe_print_list(my_list=[], index=0):
    count = 0
    for id in  range (0, index):
        try:
            print(my_list[id], end="")
            count += 1
        except IndexError:
            break
    print()
    return count;

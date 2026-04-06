#!/usr/bin/python3
def element_at(my_list=[], idx=0):
    if len(my_list)<idx:
        return None
    else:
        return(my_list[idx])

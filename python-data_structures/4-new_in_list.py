#!/usr/bin/python3
def new_in_list(my_list=[], idx=0, new_element=0):
    if idx < 0:
        return my_list
    new_list=[]
    for i in my_list:
        new_list.append(i)
    new_list[idx]=new_element
    return new_list

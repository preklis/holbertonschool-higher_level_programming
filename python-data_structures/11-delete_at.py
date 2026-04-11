#!/usr/bin/python3
def delete_at(my_list, idx):
    """Deletes an element at a specific index in a list, in place."""
    if 0 <= idx < len(my_list):
        del my_list[idx]  # deletes the element at index idx
    return my_list

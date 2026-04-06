#!/usr/bin/python3
def no_c(string=""):
    result = ""
    for char in string:
        if char != 'c' and char != 'C':
            result += char
    return result

#!/usr/bin/python3

def max_integer(list=[]):
    if len(list) == 0:
        return None
    output = list[0]
    i = 1
    while i < len(list):
        if list[i] > output:
            output = list[i]
        i += 1
    return output

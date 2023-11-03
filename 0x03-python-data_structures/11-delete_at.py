#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    a function to delete an element from a list at a given index
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    del my_list[idx]
    return (my_list)

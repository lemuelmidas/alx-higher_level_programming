#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at given index
    """
    if idx < 0 or len(my_list) <= idx:
        return (my_list)

    my_list[idx] = element
    return (my_list)

#!/usr/bin/python3

"""
File: 3-is_kind_of_class.py
"""

def is_kind_of_class(obj, a_class):
    """
    a function to check if object is an instance of class, or if the object is an instance\
        of a class that inherited from
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    return False

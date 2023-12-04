#!/usr/bin/python3

"""
File: 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """
    To check if two objects are the same class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (type(obj) is a_class)

#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    To print a full name

    Args:
        first_name (str): First string to print
        last_name (str): second string to print

    Raises:
        TypeError: Exception if arguments are not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

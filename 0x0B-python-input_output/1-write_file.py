#!/usr/bin/python3

"""
File: 1-write_file.py
"""


def number_of_lines(filename=""):
    """
    Counts the number of lines from the filename

    Arguments:
        filename (str): The name of the file to count in
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    return len(lines)

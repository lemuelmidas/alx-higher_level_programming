#!/usr/bin/python3

"""
File: 2-append_write.py
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads n lines from file and prints to stdout

    Arguments:
        filename (str): The name of the file to open
        nb_lines (int): The number of lines to print
    """
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
    if nb_lines >= len(lines) or nb_lines <= 0:
        nb_lines = len(lines)
    for i in range(nb_lines):
        print(lines[i], end='')

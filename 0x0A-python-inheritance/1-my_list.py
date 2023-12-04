#!/usr/bin/python3

"""
File: 1-my_list.py
"""

class MyList(list):
    """
     a class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints sorted list
        """
        list_copy = self[:]
        list_copy.sort()
        print(list_copy)

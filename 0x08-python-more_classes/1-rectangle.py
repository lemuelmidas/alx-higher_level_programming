#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 28th Nov 2023
File: 1-rectangle.py
"""

class Rectangle:
    """Rectangle: Define new class"""
    def __init__(self, width=0, height=0):
        """
        Init method for Rectangle

        Attributes:
            width (int, optional): rectangle's width
            height (int, optional): rectangle's height
        self.width = width
        self.height = height
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width (int): The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width (int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

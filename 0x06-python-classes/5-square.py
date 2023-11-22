#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size
    @property
    def size(self):
         @size.setter
    def size(self, value):
        """check errors and setter for size attribute

        Args:
            value: Value to checking errors

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print a square using # character
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()

#!/usr/bin/python3
class Square:   
    def __init__(self, size=0):
        try:
            if (size < 0):
             
            self.__size = size
        else:        
            raise TypeError("size must be an integer")
    
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value.isdigit():
            if (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
             raise TypeError("size must be an integer")

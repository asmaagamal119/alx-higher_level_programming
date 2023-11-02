#!/usr/bin/python3
"""Rectangle."""


class Rectangle:
    """Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__.

        :param width: width of the Rectangle.
        :param height: height of the Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width."""
        return self.__width

    @width.setter
    def width(self, value):
        """width.

        :param value: the value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height.

        :param value: the value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area."""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """__str__."""
        if self.__width == 0 or self.__height == 0:
            return ""
        ps = str(self.print_symbol)
        return '\n'.join([ps * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """__repr__."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """__del__."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal.

        :param rect_1:
        :param rect_2:
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        a1 = rect_1.area()
        a2 = rect_2.area()
        if a1 > a2:
            return rect_1
        elif a1 < a2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """square.

        :param size:
        """
        return cls(size, size)

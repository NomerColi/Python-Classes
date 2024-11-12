""" Stuffing for Thanksgiving dinner

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
import plate_decorator

class Stuffing(plate_decorator.PlateDecorator):
    def description(self) -> str:
        return_str = super().description()
        if "with" in return_str:
            return_str += " and "
        else:
            return_str += " with "
        return_str += self.__class__.__name__
        return return_str

    def area(self) -> int:
        return super().area() - 18

    def weight(self) -> int:
        return super().weight() - 7

    def count(self) -> int:
        return super().count() + 1
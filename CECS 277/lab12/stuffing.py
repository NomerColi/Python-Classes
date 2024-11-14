""" Stuffing for Thanksgiving dinner

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""
import plate_decorator

class Stuffing(plate_decorator.PlateDecorator):
    """Represents Stuffing.
    """
    def description(self) -> str:
        return_str = super().description()
        # if there is already an ingredient
        if "with" in return_str:
            return_str += " and "
        # if this is the first ingredient
        else:
            return_str += " with "
        return_str += "Stuffing"
        return return_str

    def area(self) -> int:
        return super().area() - 18

    def weight(self) -> int:
        return super().weight() - 7

    def count(self) -> int:
        return super().count() + 1
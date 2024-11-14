""" Pie for Thanksgiving Dinner

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import plate_decorator


class Pie(plate_decorator.PlateDecorator):
    """Represents Pie.
    """
    def description(self) -> str:
        return_str = super().description()
        # if there is already an ingredient
        if "with" in return_str:
            return_str += " and "
        # if this is the first ingredient
        else:
            return_str += " with "
        return_str += "Pie"
        return return_str

    def area(self) -> int:
        return super().area() - 19

    def weight(self) -> int:
        return super().weight() - 8

    def count(self) -> int:
        return super().count() + 1
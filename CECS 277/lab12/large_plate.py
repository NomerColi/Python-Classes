""" Large Plate for Thanksgiving Dinner

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import plate


class LargePlate(plate.Plate):
    def description(self) -> str:
        return "Flimsy 12 inch paper plate"

    def area(self) -> int:
        return 113

    def weight(self) -> int:
        return 24

    def count(self) -> int:
        return 0
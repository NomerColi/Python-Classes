""" Thanksgiving Dinner Puzzle Game

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

import check_input
import plate
import small_plate
import large_plate
import green_beans
import turkey
import stuffing
import potatoes
import pie


def examime_plate(p: plate.Plate):
    """Examines the plate.
    Args:
        p (Plate) - the Plate instance to examine
    Returns:
        a boolean whether if the plate fails to hold up the foods
    """
    print(p.description())
    
    weight = p.weight()
    # if area or weight capacity is less than or equal to 0
    if weight <= 0:
        print("Your plate isn't strong enough for this much food! The plate bends and spills the food.")
        return True
    area = p.area()
    if area <= 0:
        print("Your plate isn't big enough for this much food! Your food spills over the edge.")
        return True
    
    # weight hint
    weight_hint = ""
    if weight <= 6:
        weight_hint = "Bending"
    elif weight <= 12:
        weight_hint = "Weak"
    else:
        weight_hint = "Strong"

    # area hint
    area_hint = ""
    if area <= 20:
        area_hint = "A tiny bit"
    elif area <= 40:
        area_hint = "Some"
    else:
        area_hint = "Plenty"

    print("Sturdiness: " + weight_hint)
    print("Space available: " + area_hint)
    
    return False


def main():
    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")
    plate_type = check_input.get_int_range("Choose a plate:\n1. Small Sturdy Plate\n2. Large Flimsy Plate\n", 1, 2)
    if plate_type == 1:
        p = small_plate.SmallPlate()
    else:
        p = large_plate.LargePlate()
    
    end = False
    while end is False:
        food = check_input.get_int_range("1. Turkey\n2. Stuffing\n3. Potatoes\n4. Green Beans\n5. Pie\n6. Quit\n", 1, 6)
        if food == 1:
            p = turkey.Turkey(p)
        elif food == 2:
            p = stuffing.Stuffing(p)
        elif food == 3:
            p = potatoes.Potatoes(p)
        elif food == 4:
            p = green_beans.GreenBeans(p)
        elif food == 5:
            p = pie.Pie(p)
        # when the user wants to quit
        else:
            end = True
            print(p.description())
            print("Good job! You made it to the table with "+ str(p.count()) + " items.")
            print("There was still " + str(p.area()) + " square inches left on your plate.")
            print("Your plate could have held " + str(p.weight()) + " more ounces of food.")
            print("Don't worry, you can always go back for more. Happy Thanksgiving!")
            break
        
        if examime_plate(p):
            end = True

main()
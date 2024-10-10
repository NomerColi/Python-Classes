"""
Exceptions

1. ZeroDivisionError - divided by 0
2. NameError - variable not defined
3. TypeError - incorrect data type
4. ValueError - incorrect value
5. IndexError - index out of range
6. KeyError - key not existing in a dictionary


Handling Exceptions
try/except

Raising Exceptions
cause an exception


"""


def area(radius):
    if radius < 0:
        raise ValueError("Radius must not be negative")
    return 3.14 * radius * radius


def main():
    list = [1, 2, 3, 4, 5]
    valid = False
    while not valid:
        try:
            index = int(input("Enter #: "))

            if index == 4:
                raise IndexError("You cannot access the fifth element, just because I don't want you to")
            
            print("Item =", list[index])
            valid = True
        except ValueError:
            print("ValueError")
        except IndexError as err:
            #print("IndexError")
            print(err)
        except: # else
            print("ASD")
    


    try:
        val = int(input("Enter radius: "))
        try:
            print(area(val))
        except ValueError as err:
            print(err)
    except ValueError:
        print("Invalid input - must be a number")


main()


# Author: Yunjae Cho
# Date: Aug 27 2024
# Description: Displays sum and avg of 5 inputted values

import check_input

def main():
    print("Enter 5 numbers")

    count = 0
    sum = 0
    while count < 5:
        num = check_input.get_int_range("Enter #: ", 1, 100)
        if num >= 0:
            sum += num
            count += 1
        else:
            print("Invalid input")
    
    print(f"sum: {sum}, avg: {sum/count}")

main()
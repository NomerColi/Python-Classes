import random

max_meter_reading = 999999999

r_basic_cost = 5
r_cost_rate = 0.0005

c_basic_cost = 1000
c_dividing_gallon = 4000000
c_additional_cost_rate = 0.00025

i_basic_cost1 = 1000
i_dividing_gallon1 = 4000000
i_basic_cost2 = 2000
i_dividing_gallon2 = 10000000
i_additional_cost_rate = 0.00025

codes = ['R', 'C', 'I']

inputMsg_code = "Enter the customer code (R, C, or I): "
errorMsg_code = "Invalid customer code entry"

inputMsg_begin_reading = "Enter beginning reading between (0 and 999999999): "
inputMsg_end_reading = "Enter ending reading between (0 and 999999999): "
errorMsg_meter_reading = "Invalid reading meter entry"

inputMsg_name = "Enter name: "
errorMsg_name = "Invalid name"
inputMsg_address = "Enter address: "
errorMsg_address = "Invalid address"
inputMsg_phone_num = "Enter phone number: "
errorMsg_phone_num = "Invalid phone number"

'''
def GetCodeInput(codes, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        # check if the input value is one of the given codes
        if s in codes:
            return s
        else:
            print(errMsg)

def GetStringInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if not s.isnumeric():
            return s
        else:
            print(errMsg)

def GetIntInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if s.isnumeric():
            return int(s)
        else:
            print(errMsg)
    
def GetRangedIntInput(range, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if s.isnumeric() and int(s) in range:
            return int(s)
        else:
            print(errMsg)
'''

account_number = random.randint(1000, 9000)
run = True

while run:

    customer_code = ''
    while True:
        s = input(inputMsg_code)
        # check if the input value is one of the given codes
        if s in codes:
            customer_code = s
            break
        else:
            print(errorMsg_code)

    begin_reading = 0
    while True:
        s = input(inputMsg_begin_reading)
        if s.isnumeric() and int(s) in range(0, max_meter_reading + 1):
            begin_reading = int(s)
            break
        else:
            print(errorMsg_meter_reading)
    end_reading = 0
    while True:
        s = input(inputMsg_end_reading)
        if s.isnumeric() and int(s) in range(0, max_meter_reading + 1):
            end_reading = int(s)
            break
        else:
            print(errorMsg_meter_reading)

    # personal informations
    name = ""
    while True:
        s = input(inputMsg_name)
        if not s.isnumeric():
            name = s
            break
        else:
            print(errorMsg_name)
    address = ""
    while True:
        s = input(inputMsg_address)
        if not s.isnumeric():
            address = s
            break
        else:
            print(errorMsg_address)
    phone_num = 0
    while True:
        s = input(inputMsg_phone_num)
        if s.isnumeric():
            phone_num = int(s)
            break
        else:
            print(errorMsg_phone_num)

    # this will calculate the gallons used
    used_gallons = 0
    if begin_reading <= end_reading:
        used_gallons = end_reading - begin_reading
    else:  # when beginning meter reading is bigger than ending meter reading
        used_gallons = (max_meter_reading + 1) - begin_reading  # get leftmost value first
        used_gallons += end_reading  # add the rest values

    used_gallons *= 0.1  # reading meters record tenths of a gallon

    price_of_water = 0

    if customer_code == "R":  # residential
        price_of_water = r_basic_cost + (used_gallons * r_cost_rate)
    elif customer_code == "C":  # commercial
        price_of_water = c_basic_cost
        if used_gallons > c_dividing_gallon:  # if usage exceeds 4 million gallons
            price_of_water += (used_gallons - c_dividing_gallon) * c_additional_cost_rate
    else:  # industrial
        if (
            used_gallons <= i_dividing_gallon1
        ):  # if usage does not exceed 4 million gallons
            price_of_water = i_basic_cost1
        elif (
            used_gallons <= i_dividing_gallon2
        ):  # if usage exceeds 4 million gallons but does not exceed 10 million gallons
            price_of_water = i_basic_cost2
        else:  # if usage exceeds 10 million gallons
            price_of_water = (i_basic_cost2 + (used_gallons - i_dividing_gallon2) * i_additional_cost_rate)

    print("\n-------------------------------------")
    print("ASD Water Company - Billing Summary")
    print("-------------------------------------")

    print("Account Number :", account_number)
    print("Name:", name)
    print("Address:", address)
    print("Phone number:", phone_num)

    print("\nCustomer Code:", customer_code)
    print(f"Beginning meter reading: {begin_reading:09d}")
    print(f"Ending meter reading:    {end_reading:09d}")
    print(f"Gallons of water used: {used_gallons:.1f}")
    print(f"Amount billed: ${price_of_water:.2f}")

    s = input("\nDo you want to perform new calculation? If so, enter yes: ")
    run = s.lower() == "yes"

    print()

    account_number += 1

print("Thank you for using our program")

customer_code = input("Enter the customer code (R, C, or I): ")

# check if the customer code matches one of the three letters
if customer_code not in ["R", "C", "I"]:
    print("Invalid customer code entry")
    print(f"Gallons of water used: {0:.1f}")
    print(f"Amount billed: ${0:.2f}")
    exit()

begin_reading = int(input("Enter beginning reading between (0 and 999999999): "))
end_reading = int(input("Enter end reading between (0 and 999999999):       "))

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

# check to see if the numbers inputted are within range
if not ((0 <= begin_reading <= max_meter_reading) and (0 <= end_reading <= max_meter_reading)):
    print("Invalid reading meter entry")
    print(f"Gallons of water used: {0:.1f}")
    print(f"Amount billed: ${0:.2f}")
    exit()

# this will calculate the gallons used
used_gallons = 0
if begin_reading <= end_reading:
    used_gallons = end_reading - begin_reading
else:  # when beginning meter reading is bigger than ending meter reading
    used_gallons = (max_meter_reading + 1) - begin_reading  # get leftmost value first
    used_gallons += end_reading  # add the rest values

used_gallons *= 0.1  # reading meters record tenths of a gallon

print("Customer Code:", customer_code)
print(f"Beginning meter reading: {begin_reading:09d}")
print(f"Ending meter reading:    {end_reading:09d}")
print(f"Gallons of water used: {used_gallons:.1f}")

price_of_water = 0

if customer_code == "R":  # residential
    price_of_water = r_basic_cost + (used_gallons * r_cost_rate)
elif customer_code == "C":  # commercial
    price_of_water = c_basic_cost
    if used_gallons > c_dividing_gallon:  # if usage exceeds 4 million gallons
        price_of_water += (used_gallons - c_dividing_gallon) * c_additional_cost_rate
else:  # industrial
    if used_gallons <= i_dividing_gallon1:  # if usage does not exceed 4 million gallons
        price_of_water = i_basic_cost1
    elif (
        used_gallons <= i_dividing_gallon2
    ):  # if usage exceeds 4 million gallons but does not exceed 10 million gallons
        price_of_water = i_basic_cost2
    else:  # if usage exceeds 10 million gallons
        price_of_water = (
            i_basic_cost2 + (used_gallons - i_dividing_gallon2) * i_additional_cost_rate
        )

print(f"Amount billed: ${price_of_water:.2f}")
print("Process finished with exit code 0")

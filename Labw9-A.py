run = True

while run:

    upper_limit = 0
    lower_limit = 0

    valid = False
    while valid == False:
        upper_limit = int(input("Enter positive value for upper_limit: "))
        valid = upper_limit > 0

    valid = False
    while valid == False:
        lower_limit = int(input("Enter positive value for lower_limit: "))
        valid = lower_limit > 0

    # if upper_limit is lower than lower_limit
    if upper_limit < lower_limit:
        temp = upper_limit
        upper_limit = lower_limit
        lower_limit = temp

        i = 0
        while i <= upper_limit - lower_limit:
            even = upper_limit - i
            print(even)
            i += 2

    step = 0

    valid = False
    while valid == False:
        step = int(input("Input step value between 1 and 10: "))
        valid = 1 <= step <= 10

    i = 0
    while i <= upper_limit - lower_limit:
        value = upper_limit - i
        print(value)
        i += step

    r = input("Do you want to run the code again? If so, enter yes: ")
    run = r.upper() == "YES"

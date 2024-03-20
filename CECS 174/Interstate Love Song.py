while True:
    n = 0
    while True:
        n = int(input("Please enter a US Interstate Highway route number: "))
        if n in range(1000):
            break
    
    if n == 0:
        break

    s1 = ""
    s2 = ""

    if n < 100:
        o = n % 2 == 0
        l = n % 5 == 0
        
        s1 = " a long-distance arterial highway" if l else ""
        s2 = "oriented "
        s2 += "east-west" if o else "north-south"

    else:
        first_digit = int(n / 100)
        o = first_digit % 2 == 0
        s1 = " a loop highway" if o else " a spur highway"
        s2 = " of Interstate " + str(n % 100)

    print(f"Interstate {n} is{s1} {s2}.")
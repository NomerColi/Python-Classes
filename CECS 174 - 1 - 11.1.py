if __name__ == "__main__": # internal code
    name = "Donald"

    print(name[:3])

    lName = ["Donald", "Cho", "Bee"]
    for name in lName:
        name = "ASD"
        print(name)

    l = [5, "QSD", 4.2, [2, 3],] # list
    for i in l:
        print(i)

    t = ("ASD", "DFGA", "ASD") # tuple

    d = {"Boar": "Strong", "Shark":"Sharp", "day":13} # dictionary

    print(t + (2, 3))
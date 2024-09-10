"""

Lists
a collection of related variables of any type.
A list is created with an initial set of values and can later be expanded or contracted.

square brackets

Opeators - '+' or '+=' / 'in' or 'not in'

List Slicing - (start(inclusive), end(exclusive), increment)

Functions
list.append(item)
list.pop(item)
list.insert(item)
list.remove(item)
list.index(item)
list.count(item)
list.sort()
list.reverse()
len(list)
min(list)
max(list)
sum(list)

Two Dimensial Lists

"""

def func(list):
    i = 0
    while i < len(list):
        list[i] = 0
        i += 1

def main():
    evens = [2, 4, 6, 8, 10]
    print(evens[1:4])

    # Enumerate
    for count, val in enumerate(evens):
        print(count, val)

    # Function
    func(evens)
    print(evens)

    list2D = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] # 3x3 grid
    val4 = list2D[1][1] 

    print("Rows =", len(list2D))
    print("Cols =", len(list2D[0]))
    
main()



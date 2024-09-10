"""

File IO

gives you another way of receiving input and allows you to store data long term

Opening a file
in the same folder - the file name
or the full path
backslash - \\
forward slash - /

Mode
r - reading
w - writing
a - append

Reading from a file
- how many values
- what type
- what order
- multiple values per line
- how seperated

Function
file.read() - entire file as a single string
file.readline() - a single line as a string
file.readlines() - entire file as a list of strings

file.write(string)
file.writelines(list of strings)

strip() - remove whitespace
split() - split by a string

"""

def main():

    # Writing

    file = open("CECS 277/file.txt")
    print(file.read())

    file = open("names.txt")
    for i in range(5):
        print(file.readline())

    file = open("names.txt")
    names = file.readlines()
    for name in names:
        print(name)

    
    file = open("names.txt")
    for name in file:
        print(name)

    
    file = open("numbers.txt")
    sum = 0
    for number in file:
        sum += int(number)
    print(sum)


    file = open("letters.txt")
    list2d = []
    for row in file:
        list = []
        for item in row:
            if item != ' ' and item != '\n':
                list.append(item)
        list2d.append(list)
    print(list2d)


    file = open("grid.txt")
    list2d = []
    for row in file:
        items = row.strip().split(' ')
        list = []
        for item in items:
            list.append(int(item))
        list2d.append(list)
    print(list2d)

    file.close()

    line = "Mary,Smith,123 Fake st."
    items = line.split(',')
    

    # Reading

    file = open("numbers.txt", 'w')
    for val in range(10):
        file.write(str(val * val) + "\n")


    file = open("numbers.txt", 'w')
    file.write(str(11) + "\n")
    file.write(str(12) + "\n")


    list = [1, 2, 3, 4, 5]
    file = open("vals.txt", 'w')
    for item in list:
        file.write(str(item) + ' ')
    file.close()


    list = ["A", "B", "C"]
    file = open("letters.txt", "w")
    file.writelines(list)
    file.close()


    list = [1, 2, 3, 4, 5]
    file = open("vals.txt", 'w')
    for item in range(len(list) - 1):
        file.write(str(list[item]) + ',')
    file.write(str(list[len(list) - 1]))
    file.close()


    list2d = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    file = open("grid.txt", 'w')
    for row in list2d:
        for item in row:
            file.write(str(item) + ' ')
        file.write("\n")
    file.close()


    # Contact
    # reading in contacts to list
    contacts = []
    file = open("contacts.txt")
    for item in file:
        contact = item.strip().split(",")
        contacts.append(contact)
    file.close()

    # updating list
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    phone = input("Enter Phone Number: ")
    zip = input("Enter Zip Code: ")
    new_contact = [fname, lname, phone, zip]
    contacts.append(new_contact)
    print(contacts)

    # writing list back to file
    file = open("contacts.txt", "w")
    for row in contacts:
        for item in range(len(row) - 1):
            file.write(row[item] + ",")
        file.write(row[len(row) - 1] + "\n")
    file.close()

main()

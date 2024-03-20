i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

print(i1+i2)
print(i1/i2)
print(i1//i2)
print(i2/i1)
print(i2//i1)
print(i1*i3)
print(d1+d2)
print(d1/d2)
print(d2/d1)
print(d3*d1)
print(d1+i2)
print(i1/d2)
print(d2/i1)
print(i2/d1)
print(i1/i2*d1)
print(d1*i1/i2)
print(d1/d2*i1)
print(i1*d1/d2)
print(i2/i1*d1)
print(d1*i2/i1)
print(d2/d1*i1)
print(i1*d2/d1)

# Mad Lip Game
import array

wordNum = 10

print("Enter", wordNum, "words")

array = ["" for x in range(wordNum)]
i = 0
while i < wordNum:
    array[i] = input()
    i += 1

print("Text starts :")
print("Okay, hold up, wait a \'" + array[0] + "\', all \'" + array[1] + "\' just a week ago.")
print("\'" + array[2] + "\' at my \'" + array[3] + "\' and we \'" + array[4] + "\' every weekend so.")
print("On the \'" + array[5] + "\', that's my favorite \'" + array[6] + "\'.")
print("Made me \'" + array[7] + "\' around, like I don't know, like I won't be \'" + array[8] + "\' long.")
print("Now the \'" + array[9] + "\' is gone.")

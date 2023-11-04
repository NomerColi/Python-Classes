x, y, z = 3, 5, 7



x, y = 3, 5
b1, b2, b3, b4 = True, False, True, False

print(not b1 or b2 or b3)

x = 1
y = 2

print(not(x == y or x < 2))
print(x != y and x >= 2)

b = True
while (b):
    x = int(input())
    print(x < 10 and x > 20)
    print(x >= 10 or x <= 20)
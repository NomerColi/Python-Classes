# Q1
i = 10
while i > 0:
    print(i)
    i -= 2
print()

for i in range(10, 0, -2):
    print(i)
print()

# Q2
i = 2
while i < 10:
    i += 2
    print(i)
print()

# Q3
i = 5
n = 8
for i in range(n):
    print(i, i * 2)
print()

# Q4
print("ASD")
for i in range(8, 4, -2):
    print("QQQ")
print()

# Q5
i = 6

# Q6
'''
i = int(input())
n = 10
while i <= n:
    i = int(input())
    n = i + 1
    print(n)
print()
'''

# Q7
a = 5
b = 3
while a >= b:
    print(a ** 2)
    a -= 1
print()

# Q8
i = 1
n = 3
while i <= n:
    print(i + n)
    i += 1
print()

# Q9
a = 2
for i in range(1, 5 + 1):
    a += 2 * i
print(a)
print()

# Q10
for i in range(1, 3):
    for j in range(3, 5):
        print(i * j)
print()

# Q11
g = 7
while g <= 8:
    h = 6
    while h <= 7:
        print(g + h)
        h += 1
    g += 1
print()

# Q12
a = 3
while a <= 6:
    b = 2 * a - 1
    print(b)
    c = a
    while c <= a + 1:
        print(c)
        c += 1
    a += 2
print()

# Q13
sum = 0
for i in range(1, 50):
    sum += i
print(sum)
print()

# Q14
n = 12
for i in range(10, n, -1):
    print(n + i)

# Q15
for i in range(1, 3):
    for j in range(1, 4):
        print(f"{i} and {j}")

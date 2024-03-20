import math
import random

#anyKey = input() # type is string


diceRoll = random.randint(1, 6)
print("Dice Num:", diceRoll)

l1 = [3, 6.8, "ASD"]
x = random.choice(l1)
print("random value:", x)


#r = math.e ** (math.pi * float(random.seed)) * diceRoll

print("Input number between 1 and 10")
num = random.randint(1, 10)
correct = False
while not correct:
    print("correct : " + str(correct))
    g = int(input("enter a number"))
    if num == g:
        print("You got it right")
        correct = True
    else:
        print("You are wrong. L")


import math
import cmath

#1
pi = math.pi
radius = eval(input("enter the radius of a circle and I will calculate the area:"))
area = math.pi * radius ** 2
print("Area =", area) #format the output to have 2 digits to the right of the decimal point

#2
tau = 2 * pi

#3
PV = eval(input("enter present value:")) # 50000
r = eval(input("enter interest rate:")) # (0. 1)
t = int(input("enter time in years:")) # 3
FV = PV * math.e ** (r * t)
print("Future value=", FV)

#4
print("nan value=", math.nan, "type=", type(math.nan))
print("nan value=", math.inf, "type=", type(math.inf))

#5
a = eval(input("enter value for floor and ceiling:"))
print("entered value=", a, "floor=", math.floor(a), "ceiling=", math.ceil(a))

#6
print("gcd(25, 120) =", math.gcd(25, 120))

#7
print(f"fabs(-3.2)={math.fabs(-3.2)} fabs(5.4)={math.fabs(5.4)}")

#8
print("log(10)=", math.log(10), "log(144)=", math.log(144), "log(20, 5)=", math.log(20, 5))

#9
x = eval(input("enter value for trigonometric functions:"))
print("calculated value=", (math.sin(x) ** 2 + math.cos(x) ** 2))

#10
a = eval(input("enter value for hyperbolic function:"))
print(f"cosh {a} + sinh {a} = {math.cosh(a) + math.sinh(a)} and e square {a} = {math.pow(math.e, a)}")


# Complex Numbers
print((4-5j) * (12+11j))
print((-3-1j) - (6-7j))
print((1+4j) - (-16+9j))
print(8j * (10+2j))
print((-3-9j) * (1+10j))
print((2+7j) * (8+3j))
print(7 - 1j**2 + 10j)
print(1 + 5j - 3j)
print(6 + 7j**8 - 1j)
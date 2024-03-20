var = 100

def Multiply(a = 5, b = 10):
    global var
    var = 50
    print(var)
    return a * b

m = Multiply(10, 20)
print(m)
print(var)

m = Multiply(b = 3)
print(m)
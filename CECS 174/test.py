def block(L, W, character):
    s = ""
    for i in range(L):
        for j in range(W):
            s += character
        print(s)
        s = ""

#l = int(input("Input a length of your rectangle"))
#w = int(input("Input a width of your rectangle"))
#ch = input("Input a character of your rectangle")
#block(l, w, ch)

def odd(limit):
    s = ""
    for i in range(1, limit + 1):
        s += str(i*2 - 1) + " "
        print("ASD")
    return s


lim = int(input("Input a limit for your odd numbers"))
print(odd(lim))
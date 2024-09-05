# Global Variable
z = 10 # read only


def print_word(word="hello", num=5):
    for val in range(num):
        print(word)
    return 

def add(a, b):
    return a + b

def test():
    return 1,2

def main():
    a, b = test()
    print(a, b)


main()

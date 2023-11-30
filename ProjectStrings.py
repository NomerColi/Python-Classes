import math

## Part 1

vowels = "aeiou"

def Contains(s, c):
    return s.lower().find(c.lower()) != -1

def Sort(s):
    return str(''.join(sorted(s)))

def Remove_Char(s, i):
    s = s[:i] + s[i + 1:]

def Get_Word_Num(s):
    bInSpace = s[0] == ' '
    num = 0 if bInSpace else 1
    for c in s:
        if bInSpace and c != ' ':
            num += 1
            bInSpace = False
        elif not bInSpace and c == ' ':
            bInSpace = True

    return num

def Get_First_Name(s):
    firstName = ""
    for c in s:
        if c != ' ':
            firstName += c
        else:
            break
    return firstName

def Is_Vowel(c):
    return Contains(vowels, c)

def Get_Vowel_Num(s):
    num = 0
    for c in s:
        if Is_Vowel(c):
            num += 1

    return num

def Get_Vowel_Capitialized_Name(s):
    name = ""
    for c in s:
        if Is_Vowel(c):
            name += c.upper()
        else:
            name += c.lower()
    return name

#name = input("Please enter your name: ")
name = "John Jacob Jingleheimer Schmidt"

length = len(name)
print(f"\nYour name is {length} characters long.")

lastChar = name[len(name):]
print(f"\nThe last character is: {lastChar}")

firstEIndex = name.lower().find('e')
print(f"\nThe first \'e\' is at position {firstEIndex}.")

numOfWords = Get_Word_Num(name)
print(f"\nYour name has {numOfWords} words.")

firstName = Get_First_Name(name)
print(f"\nYour first name is {firstName}.")

numOfVowels = Get_Vowel_Num(name)
print(f"\nYour name contains {numOfVowels} vowels.")

vowel_capitalized_name = Get_Vowel_Capitialized_Name(name)
print(f"\nYour name with uppercase vowels is: {vowel_capitalized_name}")

centeredName = '+' * 10 + '~' * 10 + name + '~' * 10 + '+' * 10
print(f"\n{centeredName}")

midIdx = math.floor(length / 2)
splitName = name[:midIdx] + '*' * (70 - length) + name[midIdx:]
print(f"\n{splitName}")


## Part 2
ascii_a = 97
ascii_z = 122

# A
def Get_Mirrored(s):
    return s + s[::-1]

# B
def Remove_Char_From_String(s, c):
    return s.replace(c, '')

# C, D
def Char_Num(s, char):
    numOfAlphabet = 0
    numOfChar = 0
    for c in s:
        lowerC = c.lower()
        if ascii_a <= ord(lowerC) <= ascii_z:
            numOfAlphabet += 1
            if lowerC == char:
                numOfChar += 1

    charRate = numOfChar / numOfAlphabet * 100
    print(f"Your text contains {numOfAlphabet} alphabetic characters, of which {numOfChar}({charRate:.1f}%) are \'{c}\'.")

# E, F, G
def No_Char_Extended(s, char):
    wordList = s.split()
    wordList = [w for w in wordList if w.lower().find(char) == -1]
    print(" ".join(wordList))

    numOfWords = Get_Word_Num(s)
    noCharRate = len(wordList) / numOfWords * 100
    print(f"Your text contains {numOfWords} words, of which {len(wordList)}({noCharRate:.1f}%) are \'{char}\'.")
    pass

# H
def Avoids(w, s):
    for c in s:
        if Contains(w, c):
            return False
        
    return True

# I
def Uses_Only(w, s):
    for c in w:
        if not Contains(s, c):
            return False
    return True

# J
def Uses_All(w, s):
    for c in s:
        if not Contains(w, c):
            return False
        
    return True

# K
def Is_Abecedarian(s):
    return Is_Sorted(s)

def Find(s: str, c: chr, i: int):
    idx = s[i:].find(c)
    if idx != -1:
        idx += i
    return idx

def Is_Sorted(s):
    return s == Sort(s)

def Is_Anagram(s1, s2):
    return Sort(s1) == Sort(s2)

def Has_Duplicates(s):
    sortedS = Sort(s)
    c = ''
    for i in sortedS:
        if c == i:
            return True
        c = i
    return False

# Q
def Remove_Duplicates(s):
    _s = s
    for i in range(0, len(s)):
        c = s[i]
        if Find(s, c, i + 1) != -1:
            print(f"Found {c} in {s}")
            Remove_Char(s, i)
        if i >= len(s):
            break

text = '''
As an AdBlock user, you know firsthand the value that our software brings to your online experience.
By blocking unwanted and intrusive ads, AdBlock helps you browse the web faster, safer, and with fewer distractions.
But did you know that AdBlock is completely free, with no hidden fees or upgrades?
We believe that everyone should have access to a better, ad-free internet, which is why we offer AdBlock for free to all users.
'''

mirror = Get_Mirrored(text)
print(mirror)

removed = Remove_Char_From_String(text, 'a')
print(removed)

Char_Num(text, 'e')

print(No_Char_Extended(text, 'a'))

word = input("Enter a word to test Avoids function: ")
avoidStr = input("Enter a string of forbidden letters: ")
bAvoid = Avoids(word, avoidStr)
print(f"{word} avoids {avoidStr}, {bAvoid}")


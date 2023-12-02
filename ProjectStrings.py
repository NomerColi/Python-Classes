## Part 1

vowels = "aeiou"

def contains(text, char):
    return text.lower().find(char.lower()) != -1

def sort(text):
    return str(''.join(sorted(text)))

def remove_char_idx(text, i):
    return text[:i] + text[i + 1:]

def remove_char(text, char, startIdx):
    i = find(text, char, startIdx)
    if i != -1:
        return remove_char_idx(text, i)
    else:
        return text

def get_word_num(text):
    bInSpace = text[0] == ' '
    num = 0 if bInSpace else 1
    for c in text:
        if bInSpace and c != ' ':
            num += 1
            bInSpace = False
        elif not bInSpace and c == ' ':
            bInSpace = True

    return num

def get_first_name(text):
    firstName = ""
    for c in text:
        if c != ' ':
            firstName += c
        else:
            break
    return firstName

def is_vowel(char):
    return contains(vowels, char)

def get_vowel_num(text):
    num = 0
    for c in text:
        if is_vowel(c):
            num += 1

    return num

def get_vowel_capitialized_name(text):
    capitalizedName = ""
    for c in text:
        if is_vowel(c):
            capitalizedName += c.upper()
        else:
            capitalizedName += c.lower()
    return capitalizedName

#name = input("Please enter your name: ")
name = "John Jacob Jingleheimer Schmidt"

length = len(name)
print(f"\nYour name is {length} characters long.")

lastChar = name[len(name):]
print(f"\nThe last character is: {lastChar}")

firstEIndex = name.lower().find('e')
print(f"\nThe first \'e\' is at position {firstEIndex}.")

numOfWords = get_word_num(name)
print(f"\nYour name has {numOfWords} words.")

firstName = get_first_name(name)
print(f"\nYour first name is {firstName}.")

numOfVowels = get_vowel_num(name)
print(f"\nYour name contains {numOfVowels} vowels.")

vowel_capitalized_name = get_vowel_capitialized_name(name)
print(f"\nYour name with uppercase vowels is: {vowel_capitalized_name}")

centeredName = '+' * 10 + '~' * 10 + name + '~' * 10 + '+' * 10
print(f"\n{centeredName}")

midIdx = length // 2
splitName = name[:midIdx] + '*' * (70 - length) + name[midIdx:]
print(f"\n{splitName}")


## Part 2
ascii_a = 97
ascii_z = 122

forbidden_letter_num = 5

# A
def get_mirrored(text):
    return text + text[::-1]

# B
def remove_char_from_string(text, char):
    return text.replace(char, '')

# C, D
def char_num(text, char):
    numOfAlphabet = 0
    numOfChar = 0
    for c in text:
        lowerC = c.lower()
        if ascii_a <= ord(lowerC) <= ascii_z:
            numOfAlphabet += 1
            if lowerC == char:
                numOfChar += 1

    charRate = numOfChar / numOfAlphabet * 100
    print(f"\nYour text contains {numOfAlphabet} alphabetic characters, of which {numOfChar}({charRate:.1f}%) are \'{char}\'.")

# E, F, G
def no_char(text, char):
    wordList = text.split()
    wordList = [w for w in wordList if w.lower().find(char) == -1]
    textWithoutChar = " ".join(wordList)
    print(f"\nA text without words that contain {char} is \"{textWithoutChar}\"")

    numOfWords = get_word_num(text)
    noCharRate = len(wordList) / numOfWords * 100
    print(f"Your text contains {numOfWords} words, of which {len(wordList)}({noCharRate:.1f}%) are \'{char}\'.")

# H
def avoids(word, avoidLetters):
    for c in avoidLetters:
        if contains(word, c): # w.contains(c)
            return False
        
    return True

# H extended
def find_least_forbidden_letters(text, avoidLetters):
    if len(avoidLetters) <= forbidden_letter_num:
        return avoidLetters
    
    words = text.split()
    counts = [0] * len(avoidLetters)
    for i in range(len(avoidLetters)):
        for word in words:
            if not avoids(word, avoidLetters[i]):
                counts[i] += 1
    
    sortedCounts = list(counts)
    sortedCounts.sort()

    least_forbidden_letters = []
    lastIdx = -1
    lastCount = -1
    for count in sortedCounts:
        
        idx = 0
        if lastCount == count:
            idx = counts[lastIdx + 1:].index(count) + lastIdx + 1
        else:
            idx = counts.index(count)

        least_forbidden_letters.append(avoidLetters[idx])

        lastIdx = idx
        lastCount = count

        if len(least_forbidden_letters) == forbidden_letter_num:
            break

    return least_forbidden_letters

# I
def uses_only(word, letters):
    for c in word:
        if not contains(letters, c):
            return False
    return True

# J
def uses_all(word, letters):
    for c in letters:
        if not contains(word, c):
            return False
        
    return True

# K
def is_abecedarian(text):
    return is_sorted(text)

# L
def find(text: str, char: chr, i: int):
    idx = text[i:].find(char)
    if idx != -1:
        idx += i
    return idx

# M
def is_sorted(text):
    return text == sort(text)

# O
def is_anagram(text1, text2):
    return sort(text1) == sort(text2)

# P
def has_duplicates(text):
    sortedS = sort(text)
    c = ''
    for i in sortedS:
        if c == i:
            return True
        c = i
    return False

# Q
def remove_duplicates(text):
    _s = text
    for i in range(0, len(text)):
        if i >= len(_s):
            break
        c = _s[i]
        #if c == ' ':
        #    continue
        #print(f"[Remove_Duplicates] i: {i} c: {c} count: {_s.count(c)}")
        for j in range(_s.count(c) - 1):
            _s = remove_char(_s, c, i + 1)
    return _s

quote = '''
As an AdBlock user, you are the best.
I hate ads.
'''

# A
mirror = get_mirrored(quote)
print(f"Mirrored text: \"{mirror}\"")

# B
removed = remove_char_from_string(quote, 'a')
print(f"\nA text after removing all \'{'a'}\' : \"{removed}\"")

# C, D
char_num(quote, 'e')

# E, F, G
no_char(quote, 'a')

# H
#word = input("Enter a word to test Avoids function: ")
#avoidStr = input("Enter a string of forbidden letters: ")
word = "abcd"
avoidStr = "apoiuy"
bAvoid = avoids(word, avoidStr)
print(f"\n\"{word}\" avoids \"{avoidStr}\", {bAvoid}")

# I
letters = "abc"
bUseOnly = uses_only(word, letters)
print(f"\n\"{word}\" uses only \"{letters}\", {bUseOnly}")

# J
bUseAll = uses_all(word, letters)
print(f"\n\"{word}\" uses all \"{letters}\", {bUseAll}")

# K
bIsAbecedarian = is_abecedarian(quote)
print(f"\n\"{quote}\" is abecedarian, {bIsAbecedarian}")

# L, M
idx = find(quote, 'a', 3)
print(f"\n\'{'a'}\' is found at {idx} in \"{quote}\"")

# N
bIsSorted = is_sorted(quote)
print(f"\n\"{quote}\" is sorted, {bIsSorted}")

# O
word1 = "abc"
word2 = "cba"
bIsAnagram = is_anagram(word1, word2)
print(f"\n\"{word1}\" and \"{word2}\" are anagram, {bIsAnagram}")

# P
bHasDuplicates = has_duplicates(quote)
print(f"\n\"{quote}\" has duplicates, {bHasDuplicates}")

# Q
uniqueText = remove_duplicates(quote)
print(f"\nDuplicates removed text: \"{uniqueText}\"")

quote = "abcde"
quote = remove_char_idx(quote, 2)
print("\n" + quote)


quote = '''
I do not feel any need to do something like: 
get_user_by_id(id) and get_user_by_name(name) 
when I could just do get_user(id) and get_user(name) overload.
The parameter list is there to distinguish the two, it's clear and concise.
Without overloading you can get ridiculous unction names.
I hope Python adds overloading in future.
'''
avoidText = "abcdefgzlu"
print(find_least_forbidden_letters(quote, avoidText))
## Part 1

vowels = "aeiou"

# returns True if 'text' contains 'char'
def contains(text, char):
    return text.lower().find(char.lower()) != -1

# returns sorted string of 'text'
def sort(text):
    return str(''.join(sorted(text)))

# returns 'text' after removing 'char' that is found from 'startIdx'
def remove_char(text, char, startIdx):
    i = find(text, char, startIdx)
    if i != -1:
        # removing the character in the index 'i'
        return text[:i] + text[i + 1:]
    else:
        return text

# 1
# returns the number of characters in 'text' 
def get_character_num(text):
    return len(text)

# 2
# returns the last character in 'text'
def get_last_character(text):
    return text[len(text):]

# 3
# returns the first index of 'char' in 'text'
def get_first_index(text, char):
    return text.lower().find(char)

# 4
# returns the number of words in 'text'
def get_word_num(text):
    bInSpace = text[0] == ' '
    num = 0 if bInSpace else 1
    for c in text:
        # when a word is detected
        if bInSpace and c != ' ':
            num += 1
            bInSpace = False
        # when a space is detected
        elif not bInSpace and c == ' ':
            bInSpace = True

    return num

# 5
# returns the first name(word) in 'text'
def get_first_name(text):
    firstName = ""
    for c in text:
        if c != ' ':
            firstName += c
        else:
            break
    return firstName

# returns True if 'char' is a vowel
def is_vowel(char):
    return contains(vowels, char)

# 6
# return the number of vowels in 'text'
def get_vowel_num(text):
    num = 0
    for c in text:
        if is_vowel(c):
            num += 1

    return num

# 7
# returns 'text' after capitalizing all vowels and uncapitalizing the others
def get_vowel_capitialized_name(text):
    capitalizedName = ""
    for c in text:
        if is_vowel(c):
            capitalizedName += c.upper()
        else:
            capitalizedName += c.lower()
    return capitalizedName

# 8
# returns 'text' after centering it between + and ~
def get_centered_string(text):
    return '+' * 10 + '~' * 10 + text + '~' * 10 + '+' * 10

# 9
# returns 'text' after splitting it with *
def get_split_string(text):
    length = get_character_num(text)
    midIdx = length // 2
    return text[:midIdx] + '*' * (70 - length) + text[midIdx:]

# Part 1 main code
while True:
    name = input("Please enter your name, enter quit if you want to quit: ")
    
    if name.lower() == "quit":
        break

    name = "John Jacob Jingleheimer Schmidt"

    # 1
    length = get_character_num(name)
    print(f"\nYour name is {length} characters long.")

    # 2
    lastChar = get_last_character(name)
    print(f"\nThe last character is: {lastChar}")

    # 3
    firstEIndex = get_first_index(name, 'e')
    print(f"\nThe first \'e\' is at position {firstEIndex}.")

    # 4
    numOfWords = get_word_num(name)
    print(f"\nYour name has {numOfWords} words.")

    # 5
    firstName = get_first_name(name)
    print(f"\nYour first name is {firstName}.")

    # 6
    numOfVowels = get_vowel_num(name)
    print(f"\nYour name contains {numOfVowels} vowels.")

    # 7
    vowel_capitalized_name = get_vowel_capitialized_name(name)
    print(f"\nYour name with uppercase vowels is: {vowel_capitalized_name}")

    # 8
    centeredName = get_centered_string(name)
    print(f"\n{centeredName}")

    # 9
    midIdx = length // 2
    splitName = name[:midIdx] + '*' * (70 - length) + name[midIdx:]
    print(f"\n{splitName}")


## Part 2
ascii_a = 97
ascii_z = 122

forbidden_letter_num = 5

# A
# returns a mirrored text of 'text'
def get_mirrored(text):
    return text + text[::-1]

# B
# returns 'text' after removing all 'char'
def remove_char_from_string(text, char):
    return text.replace(char, '')

# C, D
# find the number of 'char' in 'text' and print a stat of it
def char_num(text, char):
    numOfAlphabet = 0
    numOfChar = 0
    for c in text:
        lowerC = c.lower()
        # if 'lowerC' is an alphabet between a and z
        if ascii_a <= ord(lowerC) <= ascii_z:
            numOfAlphabet += 1
            if lowerC == char:
                numOfChar += 1

    charRate = numOfChar / numOfAlphabet * 100
    print(f"\nYour text contains {numOfAlphabet} alphabetic characters, of which {numOfChar}({charRate:.1f}%) are \'{char}\'.")

# E, F, G
# print only words that don't contain 'char' in 'text' and print a stat of it
def no_char(text, char):
    # a list that only has words that don't contain char
    wordList = text.split()
    wordList = [w for w in wordList if w.lower().find(char) == -1]
    textWithoutChar = " ".join(wordList)
    print(f"\nA text without words that contain {char} is \"{textWithoutChar}\"")

    numOfWords = get_word_num(text)
    noCharRate = len(wordList) / numOfWords * 100
    print(f"Your text contains {numOfWords} words, of which {len(wordList)}({noCharRate:.1f}%) are \'{char}\'.")

# H
# returns True if 'word' avoids 'avoidLetters'
def avoids(word, avoidLetters):
    for c in avoidLetters:
        if contains(word, c): # w.contains(c)
            return False
        
    return True

# H extended
# returns the five forbidden letters that excludes the smallest number of words in 'text'
def find_least_forbidden_letters(text, avoidLetters):
    # if the length of 'avoidLetters' is less than or equal to 5, just return it
    if len(avoidLetters) <= forbidden_letter_num:
        return avoidLetters
    
    # count the number of words that avoid each character of 'avoidLetters'
    words = text.split()
    counts = [0] * len(avoidLetters)
    for i in range(len(avoidLetters)):
        for word in words:
            if not avoids(word, avoidLetters[i]):
                counts[i] += 1
    
    # sort 'counts' and assign the value to 'sortedCounts'
    sortedCounts = list(counts)
    sortedCounts.sort()

    least_forbidden_letters = []
    lastIdx = -1
    lastCount = -1
    for count in sortedCounts:
        
        idx = 0
        # if it is checking the same value as the last loop
        if lastCount == count:
            # find the index of the count from the right side of the last value
            idx = counts[lastIdx + 1:].index(count) + lastIdx + 1
        else:
            idx = counts.index(count)

        # add the avoid letter to a list
        least_forbidden_letters.append(avoidLetters[idx])

        lastIdx = idx
        lastCount = count

        if len(least_forbidden_letters) == forbidden_letter_num:
            break

    return least_forbidden_letters

# I
# returns True if 'word' only uses characters in 'letters'
def uses_only(word, letters):
    for c in word:
        if not contains(letters, c):
            return False
    return True

# J
# returns True if 'word' uses all characters in 'letters'
def uses_all(word, letters):
    for c in letters:
        if not contains(word, c):
            return False
        
    return True

# K
# returns True if 'text' is in alphabetical order
def is_abecedarian(text):
    return is_sorted(text)

# L
# returns the index of the first occurrence of 'char' in 'text' after the index 'i'
def find(text: str, char: chr, i: int):
    idx = text[i:].find(char)
    if idx != -1:
        idx += i
    return idx

# M
# returns True if 'text' is sorted
def is_sorted(text):
    return text == sort(text)

# O
# returns True if 'text1' and 'text2' are anagram
def is_anagram(text1, text2):
    return sort(text1) == sort(text2)

# P
# returns True if 'text' has any duplicated character
def has_duplicates(text):
    sortedS = sort(text)
    c = ''
    for i in sortedS:
        if c == i:
            return True
        c = i
    return False

# Q
# return 'text' after removing leaving only unique characters
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


# Part 2 main code
quote = '''
I do not feel any need to do something like: 
get_user_by_id(id) and get_user_by_name(name) 
when I could just do get_user(id) and get_user(name) overload.
The parameter list is there to distinguish the two, it's clear and concise.
Without overloading you can get ridiculous unction names.
I hope Python adds overloading in future.
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
# H extended
avoidStr = "abcdefgzlu"
least_forbidden_letters = find_least_forbidden_letters(quote, avoidStr)
print(f"\nThe 5 least forbidden letters from \"{avoidStr}\" are \"{least_forbidden_letters}\"")

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

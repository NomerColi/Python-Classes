import random
#from nltk.corpus import words
#allWords = words.words()

# from PyDictionary import PyDictionary
#dic1 = Pydictionary("Fun", "Name")
#meanings

words = ["clone", "floor", "doggy"]
fileR = open("WordleWords.txt", 'r')
dataC = fileR.read()
words = dataC.split("\n")
cWord = random.choice(words).lower()
print("Chosen words :", cWord)

attempt = 6

greenColorStr = "\033[2;32;48m"
yellowColorStr = "\033[3;33;48m"
grayColorStr = "\033[0;30;48m"

def print_a_character(colorStr, c):
    print(colorStr, c, sep="", end="")

for i in range(attempt):
    uWord = ""
    while True:
        uWord = input("\n-> ")
        #if uWord in allWords:
        if len(uWord) == 5:
            uWord = uWord.lower()
            break
        else:
            print("Enter a word with a length of five")
    print("The user word is:" , uWord)

    if uWord == cWord:
        print("You won")
        break
    else:
        for i in range(len(uWord)):
            c = uWord[i]
            idx = cWord.find(c)
            #print(c, idx)
            if idx != -1:
                if i == idx:
                    # Green
                    print_a_character(greenColorStr, c)
                else:
                    # Yellow
                    print_a_character(yellowColorStr, c)
            else:
                # Gray
                print_a_character(grayColorStr, c)
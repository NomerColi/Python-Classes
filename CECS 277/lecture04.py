"""

Dictionary

collections where which each item is stored as a key-value pair

cannot be indexed

Functions
len(dict)
dict.clear()
dict.get(key, msg) # err msg
dict1.update(dict2)
dict.pop(key, msg)
dict.popitem() # last inserted
list(dict.values()) # return a list of all values
list(dict.items()) # return a list made up of tuples(each key and value)
list(dict.keys()) # return a list of all keys


"""

def func(sounds):
    sounds["Fish"] = "Glub"
    sounds["Pig"] = "Oink"
    sounds["Cow"] = "Mooo"

def main():
    sounds = {"Cat": "Meow", "Dog": "Bark", "Bird": "Chirp"}

    if "Cat" in sounds:
        print(sounds["Cat"])

    sounds["Lion"] = "Grrr" # Addition
    sounds["Bird"] = "Beep" # Modification

    del sounds["Dog"] # Deletion

    func(sounds)

    for k in sounds:
        print(k, sounds[k])



    

main()
def hash_code(key):
    code = 0
    for char in key:
        if char.isNumeric():
            code += int(char)
    return code

print(hash_code("Jonah Nguyen"))
x=input("Enter any sequence")
y=x[::-1] # list[<start_index>:<stop_index>:<step>]  reverse
if x==y:
    print("Palindrome")
else:
    print("Not a palindrome")
    

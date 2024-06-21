import string
import random

def generate_password(min_length, numbers=True, special_charaters=True):
    alpha = string.ascii_letters
    num = string.digits
    special = string.punctuation
    
    char = alpha
    if numbers:
        char += num
    if special_charaters:
        char += special
        
    pwd = ""
    criteria = False
    has_number = False
    has_special = False
    
    while not criteria or len(pwd) < min_length:
        new_char = random.choice(char)
        pwd += new_char
        
        
        if new_char in num:
            has_number = True
        elif new_char in special:
            has_special = True
            
        criteria = True
        if numbers:
            criteria = has_number
        if special_charaters:
            criteria = criteria and has_special        
    return pwd
min_length = int(input("Enter Minimum Length:"))
has_number = input("Do you want to have Numbers(y/n)?").lower() =="y"
has_special = input("Do you want to have Special Characters(y/n)?").lower() == "y"
pwd = generate_password(min_length ,has_number, has_special)
print("The Generated Password is:", pwd)
    
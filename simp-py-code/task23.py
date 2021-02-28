# creating a passord generator
import random # importing the module random
import string # importing set of diff strings; uppercase letters, lowercase letters, digits, punctuation/symbols

print(" a)Okay\n b)Strong")

secure = input("Please how strong do you want you password to be: ")

uppercase_letters = string.ascii_uppercase
lowecase_letters = string.ascii_lowercase
num = string.digits
sym = string.punctuation

okay_chars = lowecase_letters + num + sym
strong_chars = uppercase_letters + num + lowecase_letters + sym

if secure == "a" :
    okay_password = ''.join(random.sample(okay_chars,8))
    print(okay_password)
elif secure == "b" :
    strong_password = ''.join(random.sample(strong_chars,8))
    print(strong_password)
          
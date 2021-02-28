# Password Validation : You are interviewing to join a security team. They want to see you build a password evaluator for your technical interview to validate 
#the input.
#task: Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has a minimum 2 numbers, 2 of 
#the following special characters('!', '@', '#', '$', '%', '%', '*'), and a length of at least 7 characters. if the password passes the check, output 'Strong'
#else output 'Weak'.
#Input Format: A string representing the password to evaluate.
#Output Format: A string that says 'Strong' if the input meets the requirements, or 'Weak', if not.
#Sample Input: Hello@$World19
#Sample Output: Strong

import string
password = input("Enter password \n")
numbers = 0
sym = string.punctuation
no_of_sym = 0
for char in password: 
    if char.isnumeric():
        numbers += 1
    elif char in sym:
        no_of_sym += 1
if no_of_sym >= 2 and numbers >= 2 and len(password) >= 7:
    print("Strong")
else: 
    print("Weak")



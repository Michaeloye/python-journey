# Just a little math game
from random import *
print("Click 'enter after each step'\nThink of a number")
step1 = input("Done?" )
a = randint(0,30)
b = randint(0,30)
c = randint(0,30)
if step1 == "":
    print("Add " + str(a))

step2 = input("Done? ")

if step2 == "":
    print("Add " + str(b))

step3 = input("Done? ")

if step3 == "":
    print("Add " + str(c))
step4 = input("Done? ")
if step4 == "":
    print("Subtract the number you thought of")

step5 = input("Done?")
if step5 == "":   
    print("Your answer is " + str(a+b+c))
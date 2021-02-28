x="This is used to assign a Variable to a String"
print("i love to write what i wrote \"" + x.lower())
print(x.isupper())
term="david"
#this is to print a particular letter in the string assigned to var term
print(term[1])
#this is to print a particular index in the string assigned to var term
print(term.index("v"))
#this is to replace a letter or word in the string assigned to var term
print(term.replace("v","j"))
#to print maximum number 
print(max(5,3,6,35,6,3,6,356,2,5))
from math import pi
print(pi)
from math import floor
print(floor(5.2))
from math import *
print(sqrt(49))
'''name= input("Enter your name:")
print("Hello " +  name)
age=int(input("Dear " + name + " please type your age:"))
print("Hello "+ name +" you are " + str(age) +" yrs old")
#creating a List'''
boys = ["kelvin", "Daniel", "David"]
print(boys[1])
print(boys[1:3])
#to chand values in a list
boys[0]="Dave"
print(boys)
boys.sort()
print(boys)
ages= [2,5,6]
boys.extend(ages)
print(boys)
#tuples
coordinates = (2,5,2)
tuples=[(2,5),(3,5),(4,2)]
print(tuples)
print(coordinates)
tuples[1]=3
print(tuples)
#functions
def hi(name):
    print("hi " + name)
hi("dane")
#return
def cube(num):
    return(print(num*num*num))

cube(4)
#or
def cube(num):
    return (num*num*num)
print(cube(3))

def hello(name):
    return name
print(hello("boss"))
#if statments
a=5
if a==3:
    print("a is equal to "+ str(a))
else:
    print("a is not equal to " + str(a))
#for loop
x=["a", "b", "c"]
for x in "michael":
    print("abc is present in michael")


    
    
num = 4
    # To take input from the user
    #num = int(input("Enter a number: "))
factorial = 1
    # check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
###
class Student:
    
    def __init__(self, name, course, gpa):
        self.name = name
        self.course = course
        self.gpa = gpa
astudent = Student("md", "business", 4.78)
print(astudent.name)
# Given 2 strings, create a new string by appending the second string in the 
#middle of the 1st string
string1 = "david"
string2 = "fish"
middle = int((len(string1)/2))
print(string1[0:middle] + string2 + string1[middle:])


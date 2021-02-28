# Given 2 strings, give a new string made of the fist, middle and last character
#each string
string1 = "david"
string2 = "fishe"
middle1 = int((len(string1)/2))
middle2 = int((len(string2)/2))

print(string1[0] + string2[0] + string1[middle1] + string2[middle2] + string1[-1:] + string2[-1:])

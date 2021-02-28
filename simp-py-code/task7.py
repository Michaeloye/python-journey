# Given a string input count all lower case, upper case, digits, and special symbols
def findingchars(string):
    ucharcount = 0
    lcharcount = 0
    intcount = 0
    symcount = 0
    for char in string:
        if char.isupper():
            ucharcount+=1
        elif char.islower():
            lcharcount+=1
        elif char.isnumeric():
            intcount+=1
        else:
            symcount+=1
        
    print("Number of lowercase characters is ", lcharcount, 
            " Number of uppercase characters is ", ucharcount,
            " Number of integers is ", intcount, 
            " Number of symbols is ", symcount,) 
findingchars("GUioKJio*$%#124")
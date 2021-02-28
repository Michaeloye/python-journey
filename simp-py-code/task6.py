# Arrange string character such that lowercase letters should come first
string = "ARaNge"
lower = []
upper = []
for letter in string:
    if letter.islower():
        lower.append(letter)
    else:
        upper.append(letter)
sortedstring = ''.join(lower + upper)
print(sortedstring)
    


 
    

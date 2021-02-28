# string char balance test: if s1 and s2 is balanced if all the chars in s1 are in s2.
string1 = "va"
string2 = "David"

for char1 in string1:
     if char1.upper() in string2.upper():
          print(True)
     else:
          print(False)
        
    
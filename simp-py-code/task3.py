# A string of odd length greater 7, return a string made of the middle three
#character of a given string
word = input(" Enter a word: ")
if len(word) < 7:
    print ("The number of letters of word must be odd numbered from 7" )

if " " in word: # if user inputs a space between letters
    print("Pleae enter a word, thank you!")
    
if ( len(word) % 2 == 1 ) and ( len(word) >= 7 ) and ( " " not in word ): 
        middleindex = int(len(word)/2)
        #the middleindex+2 is there because it will not include the middleindex+2
        middlethree = word[middleindex-1 : middleindex+2]   
        print (middlethree)
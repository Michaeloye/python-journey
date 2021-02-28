#this is a guessing game 
correct_word = "Lion"
tried_word = ""
try_count=0
try_limit=5
while tried_word.upper() != correct_word.upper() and try_count < try_limit:
    tried_word = input("Enter guess for the word: ")
    try_count+= 1
    if tried_word.upper() == correct_word.upper():
        print("You Win")
    elif tried_word != correct_word and try_count==1:
        print("Try again \nHint: an animal ")
    elif tried_word != correct_word and try_count==2:
        print("Try again \nHint: the king of the jungle")
    elif tried_word != correct_word and try_count==3:
        print("Try again \nHint: when in group they are called a Pride")
    elif tried_word != correct_word and try_count==4:
        print("Try again, this is your last chance")
    else:
        print("You did not get the word, try again.")
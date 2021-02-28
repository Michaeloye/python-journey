# Pig Latin 
# You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in the same order except that you take the first letter of each
#word and put it on the end, then you add "ay" to the end of that. ("road" = "oadray")
#Task: Your task is to take sentence in English and turn it into the same sentence in Pig Latin!
#InputFormat: A string of the sentence in English that you need to translate into pig Latin. (no punctuation or capitalization)
#OutputFormat: A string of the same sentence in pig Latin.
#SampleInput: "nevermind youve got them"
#SampleOutput: "evermindnay ouveyay otgay hemtay"

word = input("Enter a word: \n")
list1 = []
for letter in word:
    list1.append(letter)

string1 = "".join(list1[1::])
print(string1 + list1[0] + "ay")


sentence = input("Enter a sentence: \n")
sentence_split = sentence.split( )
list_word = []
i = 0

for word in sentence_split:
    list_word.append(word)
    
    pig_latin = str(list_word[i])[1::] + str(list_word[i])[0] + "ay"
    print(pig_latin, end=" ")
    
    i += 1

        

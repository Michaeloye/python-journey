# Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards 
# order. For example, say I type the string:
# 'My name is dave' Then I would see the string: 'dave is name My' shown back to me.

statement = input("Please enter a sentence: ")
statement_split = statement.split() # to split the string in terms of the words in it
print(statement_split)
print(statement_split[::-1])
string = ' '.join(statement_split[::-1]) # to join the words like a string ' ' before join is used to space the words 
print(string)
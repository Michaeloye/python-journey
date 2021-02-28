# Fing all occurences of "nigeria" in given string ignoring the case

word = "nigeria"
string = "NIGERIA is a country in Africa. nigeria are good."
string1 = string.lower()
word1 = word.lower()
nig_count = string1.count(word1) 
print("Nigeria is present in string " + str(nig_count) + " times")

# or

string_split = string1.split() # to split the string1 in to each word
print(string_split)
n_count = 0
for chars in string_split: 
    if word1 == chars:
        n_count += 1 # add one to n_count if the condition is satisfied
print(n_count)
# Average Word Length:
#You are in a college level English class, your professor woants to write an essay, but you need to find out the average length of all the words you use. It is
#up to you to figure out how long each word is and to average it out.
#Task: take in a string, figure out the average length of all the words and return a number representing the average length. Remove all puntuation. Round up to
#the nearest whole number.
#Input Format: A string containing multiple words. 
#Output Format: A number representing the average length of each word, rounded up to the neares whole number.
#Sample Input: this phrase has multiple words
#Sample output: 6 that is 26/5 = 5.2 that is rounded to 6
import math

sentence = input("Please Enter sentence:  ")
words = sentence.split()
num_of_letter = 0
num_of_word = 0
for letter in sentence:
    if letter.isalpha():
        num_of_letter += 1
for word in words:
    num_of_word += 1
        
print(math.ceil(num_of_letter/num_of_word))
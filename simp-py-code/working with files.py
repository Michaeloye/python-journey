# opening a file
# the syntax for opening a file is
# flieVariable = open(filename, mode)
# the open function returns a file object for filename. The mode parameter is a string that specifies how the file will be used(for reading or writing)

file = open("C:\\Users\\HP\\Documents\\Python\\testforpy.txt", "a")
# the double backslash is because of the escape sequence in python
# to avoid the using the double backslack use
# file = open(r"C:\Users\HP\Documents\Python\testforpy.txt")
# the r before the starting of the directory tells python that the strint is a raw string which causes the python interpreter to treat backslash characters as literal backslashes
file.write("Hello there")
file.close()

# testing a file's existence
import os.path

if os.path.isfile("testforpy.txt"):
    print(True)
else:
    print(False)
# to read a document 
file = open("C:\\Users\\HP\\Documents\\Python\\testforpy.txt", "r")
s1 = file.read() #read entire document
print(s1)
file.close()

file = open("C:\\Users\\HP\\Documents\\Python\\testforpy.txt","r")
s2 = file.read(5) #read 5 characters
print(repr(s2))
file.close

file = open("C:\\Users\\HP\\Documents\\Python\\testforpy.txt","r")
s3 = file.readline() # read a line
print(s3)
file.close()

# To read all data from a file
# if the file is a big file and the contents can't be stored in memory through using 1) read() method or 2) readlines() method use a while loop or for loop
# as shown:
# while loop
# line = infile.readline() 
# while line != '':
#    line = infile.readline()

# for loop
# for line in infile:
#    process the line here...

# checking how many lines and char are in a file
file = open("C:\\Users\\HP\\Documents\\Python\\testforpy.txt","r")
countline = 0
countline_2 = 0
countchar = 0
countchar_2 = 0
for line in file:
    countline += 1
    countchar += len(line)
    if line != ' ':
        countline_2 += 1
    for char in line:
        countchar_2 += 1

# blank spaces are counted as lines
print(countline)
print(countline_2)
print(countchar)
print(countchar_2)
file.close

# APPENDING data
# the a mode can be used to open a file for appending data to the end of the existing file
# e.g
# outfile = open("text.txt", "a")
# outfile.write("i want to append to this document")
# outfile.close()

# WriteReadNumbers
from random import randint

def main():
    #open file for writing data
    outfile = open("Numbers.txt", "w")
    for i in range(10):
        outfile.write(str(randint(0, 9)) + " ")
    outfile.close() #close file
    
    # Open file for reading data
    
    infile = open("Numbers.txt", "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number, end = " ")
    print(s)
    infile.close() # close the file
    
    # print(number, end = " ") and print(s) give the same output
main()

# file dialogs
# tkinter.filedialog module contains functions askopenfilename and asksaveasfilename for displaying the file open and save as dialog boxes
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


filenameforreading = askopenfilename()
print("You can read from " + filenameforreading)
filenameforwriting = asksaveasfilename()
print("You can write data to " + filenameforwriting)

import urllib.request

infile = urllib.request.urlopen("https://www.jetbrains.com/academy/")
print(infile.read().decode())

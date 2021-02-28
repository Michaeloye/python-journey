# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200(both included). 
# The numbers obtained should be printed in a comma seperated sequence on a single line
# Hints: Consider use range(#begin, #end) method

print("Numbers between 2000 and 3200, 2000 and 3200 included, that are multiples of 7 but not 5")

for num in range(2000,3200+1):
    if num%7==0 and num%5 != 0:
        print(num,end=',') #to print the results in a way the output will be on a line seperated by comma
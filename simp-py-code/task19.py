# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma seperated form while n is input by
# console.
# Example:
# If the following n is given as input of the program:
# 100
# Then, the output of the program should be:
# 0, 35, 70
# Hints: Use yield to produce the next value in generator. In case of input data being supplied to the question, it should be assumed to be a console input.
max_num = 4000
for num in range(0,max_num):
    if (num%5) == 0 and (num % 7) ==0 :
        print(num, end=",")

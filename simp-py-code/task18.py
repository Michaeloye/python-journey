# Write a program that allows you to sort randomly inputted numbers in ascending order, preferably integers..
# for example: input: 2,3,1,5,4,6,8,7,9,10 output: 1,2,3,4,5,6,7,8,9,10
num = eval(input("Enter a list of numbers: "))
list1 = []
for chars in num:
    result = list1.append(chars)
list1.sort()
print(list1)
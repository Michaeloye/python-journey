# Sequence
numbers = 1,2,3,4 
list_of_num = []
for num in numbers:
    list_of_num.append(num)
if list_of_num[1]-list_of_num[0] == list_of_num[2] - list_of_num[1]:
    print("The sequence is an Arithmetic sequence with common difference of " + str(list_of_num[1] -list_of_num[0]))
# Given a string, return the sum and average of the digits that appear in the string.
num = "mth = 99 eng = 98 lit = 99"

sum_of_num = 0
num_of_ints = 0
num_split = num.split() # this is to split the string into its various words/symbols/ints

print(num_split)

for digt in num_split:
    if digt.isnumeric():
        sum_of_num = sum_of_num + int(digt) # to add the digits in the string
        num_of_ints += 1 # to get the number of integers in the string
avg_of_num = ( sum_of_num / num_of_ints )

print("The sum of the numbers in the str is " + str(sum_of_num))
print("The average of the numbers in the str is " + str(avg_of_num))
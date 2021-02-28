sum_of_squares = 0
for i in range(1,101):
    sum_of_squares += i**2
print(sum_of_squares)
sum_of_num = 0
for j in range(1,101):
    sum_of_num += j
squared_num = sum_of_num**2
answer = (squared_num - sum_of_squares)
print(answer)
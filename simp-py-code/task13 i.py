# Question: If we list all the natural numbers below 10 that are the multiples of 3 or 5, we get 3, 5, 6, 9. The sum of these is 23 Find the sum of all the multiples of 3 or 5
# This won't work because there are terms alike in multiples of 3 and 5 
answer_3 = 0
answer_5 = 0
for char3 in range(0,1000,3):
      answer_3 = answer_3 + char3

for char5 in range(0,1000,5):
      answer_5 = answer_5 + char5
print(answer_3)
print(answer_5)
print(answer_3 + answer_5)

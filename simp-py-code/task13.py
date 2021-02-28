# Question: If we list all the natural numbers below 10 that are the multiples of 3 or 5, we get 3, 5, 6, 9. The sum of these is 23 Find the sum of all the multiples of 3 or 5
i = 0
num = 1000
count = 0

while i < num:
    if i%3==0 or i%5==0:
        print(i)
        count = count + i # when i satisfies the condition there is an increment in i
    i+=1
print(count)
# Reverse a given number and return true if it is hte same as the original number
x = []
y = []
num = input("Please enter a number: ")

for val in num:
    x.append(val)

print(x[::1])
print(x[::-1])

if x[::1] == x[::-1]:
    print(True)
else:
    print(False)
reverse = "".join(x[::-1]) # to reverse the inputted number
print(reverse)

"""correct
number = int(input("Please enter a number: "))
reverse = 0
while number > 0: 
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    number = number // 10
if number == reverse:
    print("theis")
print("The reverse of the number is " + str(reverse))"""
  
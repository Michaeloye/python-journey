 # Credit card numbers follow certain patterns: It must have between 13 and 16 digits, and the number must start with:
#4 for Visa cards
#5 for Mastercard credit cards
#37 for American Express cards
#6 for Discover cards

#in 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. THe algorithm is useful to determine whether a card number is entered
#correctly or whether a credit card is scanned correctly by a scanner. Credit card numbers are generated following this validity check, commonly known as the 
#Luhn check or the Mod 10 check, which can be described as follows (for illustration, consider the card number 4388576018402626):
#1 Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the two digits to get a single-digit number.
#2 Now add all single-digit numbers from step 1.
#3 Add all digits in the odd places from right to left in the card number.
#4 Sum the results from step 2 and 3.
#5 If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. For example, the number 4388576018402626 is invalid, but
#the number 4388576018410707 is valid.

#Write a program that prompts the user to enter a credit card number as an integer. Display whether the number is valid or invalid. 


credit_card = int(input("Please Enter a credit card number:     "))
list1 = []
i = 0
for_double = 0
sum_of_odd = 0
sum_of_even = 0
for num in reversed(str(credit_card)):
    list1.append(num)

for char in list1:
    
    if i%2!=0 and i<(len(list1)):
        check = int(list1[i]) * 2
        if check<10:
            sum_of_odd += check
        else:
            for inte in str(check):
                for_double += int(inte)
    
    elif i%2 == 0 and i<(len(list1)):
        check1 = int(list1[i])
        sum_of_even += check1
    
    i += 1
        
print(sum_of_odd)
print(for_double)
print(sum_of_even)
answer = sum_of_odd + sum_of_even + for_double
print(answer)

if answer%10 == 0:
    print("Valid credit card number")
elif answer%10 != 0:
    print("Invalid credit card number")
    
### Using function to check credit card number daniel liang
def valid_credit_card_num(num):
    print(divisible_by_ten(num))
    print(sum_of_odd_placed_num(num))
    print(sum_of_double_even_placed_num(num))
def divisible_by_ten(num):
    answer = add_results(num)
    if answer % 10 == 0:
        return("This credit card number is Valid")
    else:
        return("This credit card number is Invalid")
def add_results(num):
    odd = sum_of_odd_placed_num(num)
    even = sum_of_double_even_placed_num(num)
    added_odd_and_even = odd + even
    return added_odd_and_even
    
def sum_of_odd_placed_num(num):
    result = 0
    while num > 0:
        odd_placed_num = num % 10 # you get 8... you get 8...you 6
        number = num // 10 # if num is 4567898 to get 8,8,6 and 4 the odd placed numbers from the right after running you get 456789... 45678 you get 4567
        num = number // 10 # 456789: you will get 45678... 4567: you get 456
        
        result += odd_placed_num
    return result
  
def sum_of_double_even_placed_num(num):
    result = 0
    while num > 0:
        number = num // 10 # if num is 4567898 to get 9,7 and 5 the even placed numbers from the right after running you get 456789... 45678 you get 4567
        even_placed_num = number % 10 # you get 9... you get 7
        num = number // 10 # 456789: you will get 45678 back to var number 
        
        double_even_placed_num = even_placed_num * 2
        
        if double_even_placed_num > 9:
            answer = double_even_placed_num % 10
            double_even_placed_num = double_even_placed_num // 10   
            result += answer
        if double_even_placed_num < 10:
            result += double_even_placed_num
    return result
    
def main():
    num = int(input("Please enter a credit card number:   "))
    valid_credit_card_num(num)

main()
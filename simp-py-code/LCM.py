# lowest common multiple
def LCM(num1,num2):
    if num1 > num2:
        greater = num2
    else:
        greater = num1
        
    
    while True:
        if (greater % num1 == 0) and (greater % num2 == 0): 
            # I the two nums are 2 and 3 then greater is 3 therefore if 3%2 == 0 and 3%3 == 0 lcm is the greater num  but if not satisfied add 1 to greater; that is, is 4%2 == 0 and 4%3 == 0 satisfied? no, then add 1 to the greater again; is 5%2 == 0 and 5%3 == 0 satisfied? no, then add 1 to the greater again; is 6%2 == 0 and 6%3 == 0 satisfied? yes, then 6 is the lcm of 2 and 3
            lcm = greater
            break
        greater += 1
    return lcm

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(LCM(num1,num2))

   
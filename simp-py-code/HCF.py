no_of_digits = int(input("Enter the number of numbers you want to calculate for: "))
if no_of_digits == 2:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    def hcf(num1, num2):
        if num1 < num2:
            smaller = num1 
        else:
            smaller = num2
        for k in range(1, smaller+1):
            if (num1 % k == 0) and (num2 % k == 0):
                hcf = k
        return hcf  
    print( "The hcf of " + str(num1) + ", "+ str(num2)  + " is " + str(hcf(num1,num2)))
if no_of_digits == 3:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter a third number: "))
    def hcf(num1, num2, num3):
        if num1 < num2 and num1 < num3:
            smaller = num1 #to get the smaller num
        elif num2 < num3 and num2 < num1:
            smaller = num2
        else:
            smaller = num3
        for k in range(1, smaller+1):
            if ((num1 % k == 0) and (num2 % k == 0) and (num3 % k==0)):
                hcf = k
        return hcf 
        
    print( "The hcf of " + str(num1) + ", "+ str(num2) + " and " + str(num3) + " is " + str(hcf(num1,num2,num3)))
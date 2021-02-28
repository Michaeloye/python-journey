#This is to get the factorial of a particular number]

num = int(input("Enter the number to calculate the factorial: ")) 
'''while i<5:
    num = int(input("Enter the number to calculate the factorial: ")) 
    
    def fact(num):
        if num == 0:
            return 1
        return num * fact(num-1)
    print(fact(num))
    i+=1'''
def fact(num):
    
    if num < 0:
        print("error")
    elif num == 0:
        return 1       
    else:
        result = 1
        for k in range(1,num+1):

            result = result * (k)
        return result
    
print(fact(num))
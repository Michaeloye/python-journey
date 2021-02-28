num = int(input("Please enter the number to calculater factorial: "))
def fact(num):
    if num < 0:
        print("Error")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        answer = 1
        for int in range(1,num + 1):
#to calculate the tutorial you have to start the range at 1 so that the answer 
#will no give you 0 continually bcos if it starts at 0 the int will start at 0
# * 1 and the for loop continues based on range
            answer = answer * int
    return answer
print(fact(num))
            
        
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    elif num3>=num1 and num3>=num2:
        print(num3)

max_num(num1, num2, num3)
         
k=0
a=int(input("Enter the number of times you would like to perform a calculation:"))
while a>k:
    num1=float(input("Enter first number:"))
    op=input("Ener operator:")
    num2=float(input("Enter second number:"))
    
    if op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "+":
        print(num1 + num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid input")
    k+=1

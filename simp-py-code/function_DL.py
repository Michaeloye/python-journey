def sqrt(num):
    answer = (num ** (1/2))
    return answer
def main():
    print(sqrt(47))
main()



def main():
    i = 0
    while i <= 4:
        functionl(i)
        i += 1
        
        print("i is", i)
def functionl(i):
    line = " "
    while i >= 1:
        if i % 3 != 0:
            line += str(i) + " "
            i -= 1
    print(line)

main()

#####
# global attribute
x = 1
def increase():
    global x
    x += 1
    print(x)
increase()
print(x)


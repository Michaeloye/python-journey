#prime numbers
k = 2
num = 6
ans = ""
while k<num:
    if num%k != 0:
        ans = "prime"
        break
    else:
        ans = "not prime"
    k += 1
    
print(ans)
    
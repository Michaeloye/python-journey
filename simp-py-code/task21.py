# Bob has a strange counter. At the first second t=1, it displays the number 3. At each subsequent second, the number displayed by the counter decrements by 1.
# the counter counts down in cycles. In the second after the counter counts down to 1, the number becomes 2 times the initial number for that countdown cycle
# and then continues counting down from the new initial number in a cycle.
# Given a time, t. Find and print the value displayed by the counter at time t.
v = 3
t = 1
time = int(input("Enter the time at which you want to know the value: "))
while time < t :
    if v == 1:
        break
    t += 1
    v -= 1
    t = t * 2
        
print(t)
 # LCM
x = 2
y = 3
if x < y:
    smaller = x
else:
    smaller = y
for x in range(1, smaller+1):
    if x % smaller == 0 or y % smaller == 0:
        print(smaller)
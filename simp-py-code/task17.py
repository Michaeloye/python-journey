# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
# Hint: Use for loop to iterate all possible solutions.
def solve(numheads, numlegs):
    for x in range(numheads+1):
        y = numheads-x # y is the number of heads of rabbits x is the number of heads of chickens
        if (x+y) == numheads and (2*x + 4*y) == numlegs: # since chickens have 2 legs it will 2x and since rabbits have 4 legs it will be 4y
            print("The number of chicken is " + str(x) + " while the number of rabbits is " + str(y)) 
solve(35,94)



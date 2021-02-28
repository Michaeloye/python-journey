# New Driver's License
#You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in 
#alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now and they can each see one customer at a
#time. How long will it take for you to walk out of the office with your new license?
# Task: Given everyon's name that showed up at the same time, determine how long it will take to get your new license.
# Input Format: Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names 
#seperated by spaces.
# Output Format: You will output an integer of the number of minutes that it will take to get your license.
# Sample Input:
# "Eric"
# 2
# "Adam Caroline Rebecca Frank"
# Sample Output:
# 40 Explanation it will take 40 minutes to get your license because you are in the second group of two to be seen by one of the two available agents.


name = input("Please enter your name: ")
no_of_agents = int(input("Please enter the number of agents: "))
others = input("Please enter the names of the rest people: ")
list1 = []
others_split = others.split()
list1.extend(others_split)
list1.append(name)
list1.sort()
answer = int(((list1.index(name)/no_of_agents)*20) + 20)
print(answer)
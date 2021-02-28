"""Staircase detail

This is a staircase of size n = 4:

   #
  ##
 ###
####
"""

def staircase(n):
    space = " "
    count = n -1
    num_of_hash = 1 # the has "#" has to increase so start from 1
    for num in range(n):
        if count >= 0: # this is to make sure that the last line has no space before the # tags
            print((space * count) + ("#" * num_of_hash))
            count -= 1 # to reduce the space between the starting of each line of "#"
            num_of_hash += 1 # to make sure with each following line the number of "#" increases by 1
if __name__ == '__main__':
    n = int(input())

    staircase(n)
#!/bin/python3
# link to apple and orange question
"""   https://www.hackerrank.com/challenges/apple-and-orange/problem    """
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    no_of_apples_in_sams_house = 0
    no_of_oranges_in_sams_house = 0
    true_apple_point = []
    true_orange_point = []
    for i in range(0, len(apples)): # getting distance of the apples
        total = a + apples[i] # getting the distane of the apples from the main point
        true_apple_point.append(total) # putting the calculated distance of the apples from the main point in a list
    for i in range(0, len(oranges)): # getting distance of the oranges
        total = b + oranges[i] # getting the distance of the oranges from the main point
        true_orange_point.append(total) # putting the calculated distance of the oranges from the main point in a list
    
    # wanting to compare the true distance of the apples if it landed within sam's house
    for number_of_apples in true_apple_point:
        if number_of_apples >= s and number_of_apples <= t:
            no_of_apples_in_sams_house += 1
            
    # wanting to compare the true distance of the oranges if it landed within sam's house
    for number_of_oranges in true_orange_point:
        if number_of_oranges in range(s, t + 1): # another way to check if the orange lands in sam's house
            no_of_oranges_in_sams_house += 1
    
    print(no_of_apples_in_sams_house)
    print(no_of_oranges_in_sams_house)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
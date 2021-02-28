#!/bin/python3
"""Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1 + 5 + 9. The right to left diagonal = 3 + 5 + 9 . Their absolute difference is 2."""
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                left_diagonal += arr[i][j] 
    for a in range(0, len(arr)):
        for b in range(0, len(arr)):
            if a + b == len(arr) - 1:
                right_diagonal += arr[a][b]
    answer = abs(left_diagonal - right_diagonal)
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

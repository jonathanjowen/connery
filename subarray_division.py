#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    n = len(s)
    sums_equal_to_d = 0
    
    if n == m:
        if sum(s) == d:
            sums_equal_to_d += 1   
    else:
        for i in range(n-m+1):
            if sum(s[i:(i+m)]) == d:
                sums_equal_to_d += 1

    return sums_equal_to_d



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = 19

    # s = list(map(int, input().rstrip().split())) 
    s = list(map(int, "2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1".rstrip().split()))

    # first_multiple_input = input().rstrip().split()
    first_multiple_input = "18 7".rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    # fptr.write(str(result) + '\n')
    print(result)



# https://www.hackerrank.com/challenges/the-birthday-bar/problem

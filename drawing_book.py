#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    forward_flips = (p-1)//2 + (p-1)%2
    total_flips = (n-1)//2 + (n-1)%2
    return min(forward_flips, total_flips - forward_flips)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    input_0 = '5'
    n = int(input_0.strip())

    # p = int(input().strip())
    input_1 = '4'
    p = int(input_1.strip())

    result = pageCount(n, p)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()

    # https://www.hackerrank.com/challenges/drawing-book/problem/
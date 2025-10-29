#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # Write your code here
    return max(0, max(height) - k)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()
    input_0 = '5 7'
    first_multiple_input = input_0.rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    # height = list(map(int, input().rstrip().split()))
    input_1 = '2 5 4 5 2'
    height = list(map(int, input_1.rstrip().split()))

    result = hurdleRace(k, height)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()


# https://www.hackerrank.com/challenges/the-hurdle-race/problem
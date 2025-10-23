#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    in_valley = False
    valley_count = 0

    for  p in path:
        if p == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude < 0 and in_valley is False:
            in_valley = True
        if altitude == 0 and in_valley is True:
            valley_count += 1
            in_valley = False
    
    return valley_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    # steps = int(input().strip())
    input_0 ='8'
    steps = int(input_0.strip())

    # path = input()
    input_1 = 'UDDDUDUU'
    path = input_1

    result = countingValleys(steps, path)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()

# https://www.hackerrank.com/challenges/counting-valleys/problem

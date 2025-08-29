#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairs = itertools.combinations((ar), 2)
    divisible_by_k = [pair for pair in pairs if sum(pair)%k == 0]
    return len(divisible_by_k)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()
    input_1 = "6 3"
    first_multiple_input = input_1.rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    # ar = list(map(int, input().rstrip().split()))
    input_2 = "1 3 2 6 1 2"
    ar = list(map(int, input_2.rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    # fptr.write(str(result) + '\n')
    # fptr.close()
    print(result)
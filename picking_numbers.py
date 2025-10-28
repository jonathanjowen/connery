#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    max_subarray_length = 0
    counts = Counter(a)
    for i in counts.keys():
        if counts[i] + counts[i+1] > max_subarray_length:
            max_subarray_length = counts[i] + counts[i+1] 
    return max_subarray_length



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    input_0 = '6'
    n = int(input_0.strip())

    # a = list(map(int, input().rstrip().split()))
    input_1 = '1 2 2 3 1 2'
    a = list(map(int, input_1.rstrip().split()))

    result = pickingNumbers(a)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()



# https://www.hackerrank.com/challenges/picking-numbers/problem
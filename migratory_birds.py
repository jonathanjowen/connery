#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    counts = Counter(sorted(arr))
    return counts.most_common(1)[0][0]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())
    input_1 = "11"
    arr_count = int(input_1.strip())

    # arr = list(map(int, input().rstrip().split()))
    input_2 = "1 2 4 3 5 4 3 2 1 3 4"
    arr = list(map(int, input_2.rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()


# https://www.hackerrank.com/challenges/migratory-birds/problem
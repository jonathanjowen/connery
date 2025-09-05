#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    sock_counts = Counter(ar)
    pairs_count = 0
    for sock_count in sock_counts.most_common():
        pairs_count += sock_count[1] // 2
    return pairs_count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    input_0 = '9'
    n = int(input_0.strip())

    # ar = list(map(int, input().rstrip().split()))
    input_1 = '10 20 20 10 10 30 50 10 20'
    ar = list(map(int, input_1.rstrip().split()))

    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()

# https://www.hackerrank.com/challenges/sock-merchant/problem
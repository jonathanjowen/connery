#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    tree_height = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            tree_height *= 2
        else:
            tree_height += 1
    return tree_height

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)
        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()


# https://www.hackerrank.com/challenges/utopian-tree/problem
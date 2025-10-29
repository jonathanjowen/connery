#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    total_likes = 2
    daily_likes = 2
    for day in range(2, n+1):
        daily_shares = 3 * daily_likes
        daily_likes = daily_shares // 2
        total_likes += daily_likes
    
    return total_likes


if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)
    print(result)
 

# https://www.hackerrank.com/challenges/strange-advertising/problem
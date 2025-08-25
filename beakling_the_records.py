#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    high_record = scores[0]
    beat_high_record = 0
    low_record = scores[0]
    beat_low_record = 0
    for score in scores[1:]:
        if score > high_record:
            beat_high_record += 1
            high_record = score
        if score < low_record:
            beat_low_record += 1
            low_record = score
    return (beat_high_record, beat_low_record)
   

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    n = 9

    # scores = list(map(int, input().rstrip().split()))
    scores = list(map(int, "10 5 20 20 4 5 2 25 1".rstrip().split()))

    result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()

    print(' '.join(map(str, result)))

# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/
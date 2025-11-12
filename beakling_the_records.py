#!/bin/python3

import math
import os
import random
import re
import sys

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

    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(' '.join(map(str, result)))


# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
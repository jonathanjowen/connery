#!/bin/python3

import math
import os
import random
import re
import sys

def appendAndDelete(s, t, k):
    common_length = len(os.path.commonprefix([s, t]))
    deletions = len(s) - common_length
    appends = len(t) - common_length
    total_ops = deletions + appends
    if total_ops == k:
        is_possible = 'Yes'
    elif k > total_ops and  (k - total_ops) % 2 == 0:
        is_possible = 'Yes'
    elif k >= len(s) + len(t):
        is_possible = 'Yes'
    else:
        is_possible = 'No'
    return is_possible
    

if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input().strip())

    result = appendAndDelete(s, t, k)
    print(result)

# https://www.hackerrank.com/challenges/append-and-delete/problem
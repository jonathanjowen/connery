#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def equalizeArray(arr):
    most_common = Counter(arr).most_common()[0]
    min_deletions = len(arr) - most_common[1]
    return min_deletions

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)

 # https://www.hackerrank.com/challenges/equality-in-a-array/problem
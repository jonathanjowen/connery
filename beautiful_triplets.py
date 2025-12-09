#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    max_i = len(arr) - 2
    beautiful_count = 0
    for i in range(max_i):
        if (arr[i] + d in arr) and (arr[i] + 2 * d in arr):
            beautiful_count += 1
    return beautiful_count


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)
    print(result)

# https://www.hackerrank.com/challenges/beautiful-triplets/problem
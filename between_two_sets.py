#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):

    max_a = max(a)
    min_b = min(b)

    a_multiples = set(range(max_a, min_b + 1))
    for i in a:
        i_multiples = [i * m for m in range(1, math.ceil(min_b/i)+1)]
        a_multiples = a_multiples.intersection(set(i_multiples))

    between_set = set()
    for j in a_multiples:
        if sum(map(lambda x: x % j, b)) == 0:
            between_set = between_set.union({j})

    return len(between_set)
        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)


# https://www.hackerrank.com/challenges/between-two-sets/problem
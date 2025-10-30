#!/bin/python3

import math
import os
import random
import re
import sys

def permutationEquation(p):
    y_list = []
    for x in range(1, len(p) + 1):
        idx_of_x = p.index(x) + 1
        y_list.append(p.index(idx_of_x) + 1)
    return y_list

if __name__ == '__main__':

    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    print(result)

# https://www.hackerrank.com/challenges/permutation-equation/problem
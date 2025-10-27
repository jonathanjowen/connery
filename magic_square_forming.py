#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
from itertools import combinations, permutations

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    n = len(s[0])
    magic_number = int((n**3 + n)/2)
    number_sequence = list(range(1, 1 + (n**2)))
    magic_squares = []
    perms = list(permutations(number_sequence, n))
    magic_perms = [list(p) for p in perms if sum(p) == magic_number]
    occurrences = {}
    for i in number_sequence:
        count_i = len([p for p in magic_perms if i in p])
        if count_i in occurrences.keys():
            occurrences[count_i] += [i]
        else:
            occurrences[count_i] = [i]
    occurrences_order = sorted(occurrences.keys(), reverse=True)
    
    center = occurrences[occurrences_order[0]]
    corners = occurrences[occurrences_order[1]]
    edges = [i for i in number_sequence if i not in center + corners]
    corner_perms = [p for p in magic_perms if (p[0] in corners) and (p[1] not in center + corners)]
    for first_row in corner_perms:
        last_row = [p for p in corner_perms 
                    if (len(set(first_row) & set(p)) == 0) 
                    and (first_row[0] + p[0] != magic_number - center[0])
                    ][0]
        middle_row = [p for p in magic_perms 
                      if (p[1] == center[0]) 
                      and p[0] == magic_number - first_row[0] - last_row[0]
                    ][0]
        magic_square = [first_row, middle_row, last_row]
        magic_squares.append(magic_square)

    costs = []
    for sq in magic_squares:
        # diffs = np.subtract(np.array(sq), np.array(s))
        cost = 0
        for row in range(n):
            difference = [x - y for x, y in zip(sq[row], s[row])]
            print(difference)
            abs_difference = [int(math.sqrt(x**2)) for x in difference]
            cost += sum(abs_difference)
        costs.append(cost)
        
    return min(costs)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        # s.append(list(map(int, input().rstrip().split())))
        input_0 = ['4 8 2', '4 5 7', '6 1 6']
        s.append(list(map(int, input_0[_].rstrip().split())))

    result = formingMagicSquare(s)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()


# https://www.hackerrank.com/challenges/magic-square-forming/problem
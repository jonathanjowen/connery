#!/bin/python3

from itertools import permutations

S, k = input().split()
k = int(k)

permutations_list = list(permutations(S, k))
permutations_list.sort()
for p in permutations_list:
    print(''.join(p))



# https://www.hackerrank.com/challenges/itertools-permutations/problem

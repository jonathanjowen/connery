#!/bin/python3

from itertools import combinations

S, k = input().split()
S_sorted = ''.join(sorted(S))
k = int(k)

for i in range(k):
    combinations_list = list(combinations(S_sorted, i+1))
    for c in combinations_list:
        print(''.join(c))



# https://www.hackerrank.com/challenges/itertools-combinations/problem

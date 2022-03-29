#!/bin/python3

from itertools import combinations_with_replacement

S, k = input().split()
S_sorted = ''.join(sorted(S))
k = int(k)

combinations_list = list(combinations_with_replacement(S_sorted, k))
for c in combinations_list:
    print(''.join(c))





# www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

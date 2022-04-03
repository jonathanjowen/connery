#!/bin/python3

from collections import defaultdict

n, m = map(int, input().split())

# Creates d using [] as default value
# 1st instance of each key k is appended to []
d = defaultdict(list)
for i in range(n):
    k = input()
    d[k].append(i+1)

# To return -1 when key l isn't in d requires new defaultdict with arguments
#   default_factory = lambda:[-1]
#   mapping         = dict(d)      i.e. mappings from d as standard dictionary
d = defaultdict(lambda:[-1], dict(d))

# Redifined dictionary now returns list of positions or -1
for _ in range(m):
    l = input()
    print(* d[l])



# www.hackerrank.com/challenges/defaultdict-tutorial/problem

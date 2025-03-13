#!/bin/python3

from itertools import groupby

s = list(input())

groups = []
for k, g in groupby(s):
    # Note: group iterator is consumed, leavin each g empty
    groups.append('(' + str(sum(1 for _ in list(g))) + ', ' + k + ')')

print(*groups)

# https://www.hackerrank.com/challenges/compress-the-string/problem
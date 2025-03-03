#!/bin/python3

from bisect import bisect_left, bisect_right

n,m = map(int, input().split())

x = sorted([int(i) for i in input().split()])
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])

happiness = 0

for i in a.intersection(x):
    happiness += bisect_right(x, i) - bisect_left(x, i)
for i in b.intersection(x):
    happiness -= bisect_right(x, i) - bisect_left(x, i)

print(happiness)

# www.hackerrank.com/challenges/no-idea/problem
#!/bin/python3

import itertools
from collections import deque
from functools import reduce

# Get number of lists K, modular divisor M
k, m = [int(x) for x in input().split()] 

# Create iterator of K lists containing possible Xi^2 values 
x2_lists = deque()
for i in range(k):
    # Read and split input lines, square each value
    x2_values = deque(map(lambda x: pow(int(x), 2), input().split()))
    # Drop first value from each list because its actually Ni^2 
    x2_values.popleft()
    # Append list of remaining Xi^2 values to iterator
    x2_lists.append(x2_values)

# Create cartesian product containg all possible Xi^2 combinations
x2_combs = deque(itertools.product(*x2_lists))

# Sum each combination of Xi^2 values, modular divide by M
f_values = deque()
for x2_comb in x2_combs:
    f_values.append(reduce(lambda x2, y2: x2 + y2, x2_comb) % m)

print(max(f_values))


# https://www.hackerrank.com/challenges/maximize-it/problem
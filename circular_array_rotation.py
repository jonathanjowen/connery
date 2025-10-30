#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque


def circularArrayRotation(a, k, queries):
    deque_a = deque(a)
    deque_a.rotate(k)
    b = list(deque_a)
    query_results = []
    for q in queries:
        query_results.append(b[q])
    return query_results

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print(result)

   # https://www.hackerrank.com/challenges/circular-array-rotation/problem

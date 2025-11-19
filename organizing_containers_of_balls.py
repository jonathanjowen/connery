#!/bin/python3

import math
import os
import random
import re
import sys

def organizingContainers(container):

    n_of_ball_types = len(container[0])
    container_sums = list(map(sum, container))
    ball_sums = [0] * n_of_ball_types
    for c in container:
        ball_sums = [x + y for x, y in zip(ball_sums, c)]
    if sorted(container_sums) == sorted(ball_sums):
        return 'Possible'
    else:
        return 'Impossible'


if __name__ == '__main__':

    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        container = []
        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)

# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
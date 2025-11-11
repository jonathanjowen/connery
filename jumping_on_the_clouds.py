#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    n_of_clouds = len(c)
    jumps = 0
    cloud_idx = 0
    print(f'jump: {jumps}  cloud: {cloud_idx}')
    while cloud_idx < (n_of_clouds - 1):
        jumps += 1
        if cloud_idx < (n_of_clouds - 2) and c[cloud_idx + 2] == 0:
            cloud_idx += 2
        else:
            cloud_idx += 1
        print(f'jump: {jumps}  cloud: {cloud_idx}')
    return jumps

if __name__ == '__main__':

    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

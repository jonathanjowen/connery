#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    cloud_idx = k % n
    jump = 1
    energy = 99 - 2 * c[cloud_idx]
    print(f'jump: {jump}  cloud: {cloud_idx}  energy: {energy}')
    while cloud_idx != 0:
        jump += 1
        cloud_idx = (cloud_idx + k) % n
        energy -= 1 + 2 * c[cloud_idx]
        print(f'jump: {jump}  cloud: {cloud_idx}  energy: {energy}')
    return energy

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)
    print(result)

# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

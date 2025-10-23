#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    xz = z - x
    print('xz =', xz)
    yz = z - y
    print('yz =', yz)
    if abs(xz) == abs(yz):
        outcome = 'Mouse C'
    elif abs(xz) < abs(yz):
        outcome = 'Cat A'
    else:
        outcome = 'Cat B'
    return outcome

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input())
    input_0 = '1'
    q = int(input_0)

    for q_itr in range(q):
        # xyz = input().split()
        input_1 = '1 2 3'
        xyz = input_1.split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()

# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
#!/bin/python3

import math
import os
import random
import re
import sys

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
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        result = catAndMouse(x, y, z)
        print(result)



# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
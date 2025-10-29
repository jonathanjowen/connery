#!/bin/python3

import math
import os
import random
import re
import sys


def saveThePrisoner(n, m, s):
    bad_candy_chair = (s + m - 1) % n
    if bad_candy_chair < 1:
        bad_candy_chair += n
    return bad_candy_chair

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)
        print(result)




# https://www.hackerrank.com/challenges/save-the-prisoner/problem
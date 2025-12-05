#!/bin/python3

import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    
    kaprekars = []

    for n in range(p, q+1):
        d = len(str(n))
        square_string = str(n ** 2)
        r_string = square_string[len(square_string)-d:]
        l_string = square_string[0:len(square_string)-d]
        if len(r_string) > 0:
            r = int(r_string)
        else:
            r = 0
        if len(l_string) > 0:
            l = int(l_string)
        else:
            l = 0
        if (l + r) == n:
            kaprekars.append(n)

    if len(kaprekars) > 0:
        print(*kaprekars)
    else:
        print('INVALID RANGE')  


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)


# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
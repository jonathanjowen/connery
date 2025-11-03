#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def findDigits(n):
    digit_counts = dict(Counter(str(n)))
    divisors = 0
    for digit, count in digit_counts.items():
        if digit != '0' and n % int(digit) == 0:
            divisors += count
    return divisors

    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
        print(result)



































# https://www.hackerrank.com/challenges/find-digits/problem
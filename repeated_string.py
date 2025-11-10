#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    length_of_s = len(s)
    a_in_s = length_of_s - len(s.replace('a',''))
    part_s =  s[0: (n % length_of_s)]
    a_in_part_s = len(part_s) - len(part_s.replace('a',''))
    a_in_n = a_in_s * (n // length_of_s)  + a_in_part_s
    return a_in_n

if __name__ == '__main__':

    s = input()
    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)


# https://www.hackerrank.com/challenges/repeated-string/problem
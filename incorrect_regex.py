#!/bin/python3

import re 

n_tests = int(input())

for _ in range(n_tests):
    pattern_str = input()
    try:
        re.compile(pattern_str)
    except Exception as err:
        print('False')
    else:
        print('True')

# https://www.hackerrank.com/challenges/incorrect-regex/problem

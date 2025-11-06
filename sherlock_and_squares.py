#!/bin/python3

import math
import os
import random
import re
import sys

def squares(a, b):
    min_square_root = int(math.ceil(math.sqrt(a)))
    max_square_root = int(math.floor(math.sqrt(b)))
    n_of_squares = 1 + max_square_root - min_square_root
    return n_of_squares

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        print(result)

# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

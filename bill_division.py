#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    del bill[k]
    b_actual = int(sum(bill)/2)
    if b - b_actual > 0:
        print(b - b_actual)
    else:
        print('Bon Appetit')

if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    input_0 = '4 1'
    first_multiple_input = input_0.rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    # bill = list(map(int, input().rstrip().split()))
    input_1 = '3 10 2 9'
    bill = list(map(int, input_1.rstrip().split()))

    # b = int(input().strip())
    input_2 = '5'
    b = int(input_2.strip())

    bonAppetit(bill, k, b)


# https://www.hackerrank.com/challenges/bon-appetit/problem
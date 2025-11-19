#!/bin/python3

import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    del bill[k]
    b_actual = int(sum(bill)/2)
    if b - b_actual > 0:
        print(b - b_actual)
    else:
        print('Bon Appetit')

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())

    bonAppetit(bill, k, b)


# https://www.hackerrank.com/challenges/bon-appetit/problem
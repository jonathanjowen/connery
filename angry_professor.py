#!/bin/python3

import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    students_present = len([time for time in a if time <= 0 ])
    if students_present < k:
        is_cancelled = 'YES'
    else:
        is_cancelled = 'NO'
    
    return is_cancelled

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):

        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)
        print(result)


# https://www.hackerrank.com/challenges/angry-professor/problem
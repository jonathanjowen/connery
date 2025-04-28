#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_as_string = ''   
for column in range(m):
    column_as_string = ''.join([row[column] for row in matrix])
    matrix_as_string += column_as_string
    
decoded_string = re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])', r'\1 \2', matrix_as_string)

print(decoded_string)



# https://www.hackerrank.com/challenges/matrix-script/problem
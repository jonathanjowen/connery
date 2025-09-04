#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year % 400 == 0:
        day_256 = '12.09'
    elif year % 4 == 0:
        if (year < 1918) or (year % 100 != 0):
            day_256 = '12.09'
        else:
            day_256 = '13.09'
    elif year == 1918:
        day_256 = '26.09'
    else:
        day_256 = '13.09'
    
    return f'{day_256}.{year}'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # year = int(input().strip())
    input_0 = '1918'
    year = int(input_0.strip())

    result = dayOfProgrammer(year)
    
    # fptr.write(result + '\n')
    print(year, result)

    # fptr.close()



# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
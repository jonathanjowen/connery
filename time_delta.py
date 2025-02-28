#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    date_time_1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    date_time_2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    time_delta = date_time_1 - date_time_2
    return (str(round(abs(time_delta.total_seconds()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



# www.hackerrank.com/challenges/python-time-delta/problem

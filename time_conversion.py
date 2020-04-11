#!/bin/python3

# https://www.hackerrank.com/challenges/time-conversion/problem

import os


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ampm = s[-2:]
    hr = int(s[:2])
    if ampm == "PM" and hr < 12:
        hr += 12
        return(str(hr) + s[2:8])
    elif ampm == "AM" and hr == 12:
        return("00" + s[2:8])
    else:
        return(s[:8])


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

#!/bin/python3

import os


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    x_gap = x2 - x1
    v_rel = v1 - v2
    if v_rel <= 0:
        if x_gap == 0:
            return "YES"
        else:
            return "NO"
    elif x_gap%v_rel == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


# https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def taumBday(b, w, bc, wc, z):
    total_costs = (b * min(bc, (wc + z))) + (w * min(wc, (bc + z)))
    return total_costs
        

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):

        first_multiple_input = input().rstrip().split()
        b = int(first_multiple_input[0])
        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()
        bc = int(second_multiple_input[0])
        wc = int(second_multiple_input[1])
        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)
        print(result)


# https://www.hackerrank.com/challenges/taum-and-bday/problem
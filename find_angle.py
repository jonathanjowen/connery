#!/bin/python3

import math

# inputs
ab = int(input())
bc = int(input())

# calc
m   = math.sqrt(ab**2 + bc**2)
mbc = math.degrees(math.acos(bc / m))

# output
print("{:.0f}".format(mbc), chr(176), sep="")



# www.hackerrank.com/challenges/find-angle/problem

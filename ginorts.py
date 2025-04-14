#!/bin/python3


import re

if __name__ == '__main__':

    s = input()

    sorting = sorted(re.findall('[a-z]', s))
    sorting += sorted(re.findall('[A-Z]', s))
    sorting += sorted(re.findall('[13579]', s))
    sorting += sorted(re.findall('[02468]', s))

    print(*sorting, sep='')


# https://www.hackerrank.com/challenges/ginorts
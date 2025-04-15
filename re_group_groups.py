#!/bin/python3


import re

if __name__ == '__main__':
    # s = input()
    s = '__commit__'
    # alphanumeric_only = re.sub(r'[^a-zA-Z0-9]', '', s)
    m = re.search(r'([a-zA-Z0-9])\1', s)
    # m = re.search(r'(\w)\1', alphanumeric_only)
    if m is not None:
        print(m.group(1))
    else:
        print('-1')


# https://www.hackerrank.com/challenges/re-group-groups/problem
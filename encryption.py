#!/bin/python3

import math
import os
import random
import re
import sys


def encryption(s):
    s_no_spaces = s.replace(' ', '')
    n_of_letters = len(s)
    n_columns = math.ceil(math.sqrt(n_of_letters))
    encrypted_strings = [''] * n_columns
    for i in range(n_of_letters):
        encrypted_strings[i % n_columns] += s_no_spaces[i]
    
    return ' '.join(encrypted_strings)


if __name__ == '__main__':

    s = input()

    result = encryption(s)
    print(result)

# https://www.hackerrank.com/challenges/encryption/problem
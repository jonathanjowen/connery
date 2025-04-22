#!/bin/python3

import re

if __name__ == '__main__':

    regex_pattern = r'^(?=[MDCLXVI])M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$'
    print(str(bool(re.match(regex_pattern, input()))))

# Regex pattern based on https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/ch06s09.html

# https://www.hackerrank.com/challenges/validate-a-roman-number/problem
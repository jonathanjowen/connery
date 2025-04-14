#!/bin/python3

import re

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
if __name__ == '__main__':
    
    # n_of_tests = read_integer()
    n_of_tests = 1
    
    floating_point_pattern = r'^[\+\-]?[0-9]*\.[0-9]+$'
    
    for _ in range(n_of_tests):
        # test_string = input()
        test_string = '+ab.000'
        print(re.match(floating_point_pattern, test_string) is not None)


# https://www.hackerrank.com/challenges/introduction-to-regex/problem
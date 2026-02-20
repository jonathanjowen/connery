#!/bin/python3

import re



def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))

def match_floating_point(string):
    """Returns a match object if string is a floating point number or None otherwise"""       
    floating_point_pattern = r'^[\+\-]?[0-9]*\.[0-9]+$'
    return re.match(floating_point_pattern, string)

  
    
if __name__ == '__main__':
    
    n_of_tests = read_integer()

    for _ in range(n_of_tests):
        test_string = input()
        print(match_floating_point(test_string) is not None)



# https://www.hackerrank.com/challenges/introduction-to-regex/problem
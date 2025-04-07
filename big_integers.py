#!/bin/python3

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
    
if __name__ == '__main__':
    
    a = read_integer()
    b = read_integer()
    c = read_integer()
    d = read_integer()
    
    result = pow(a, b) + pow(c, d)
    
    print(result)



# https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem
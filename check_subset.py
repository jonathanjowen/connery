#!/bin/python3

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))

    
if __name__ == '__main__':
    n_of_tests = read_integer()
    for _ in range(n_of_tests):
        unused_integer = read_integer()
        a = set(read_integers())
        unused_integer = read_integer()
        b = set(read_integers()) 
        print(a.issubset(b))
        

# https://www.hackerrank.com/challenges/py-check-subset/problem
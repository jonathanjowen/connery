#!/bin/python3

import numpy

def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    n, m = read_integers()

    initial_array = []
    for _ in range(n):
        initial_array += [list(read_integers())]
        
    print(numpy.array(initial_array).transpose())
    print(numpy.array(initial_array).flatten())


# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
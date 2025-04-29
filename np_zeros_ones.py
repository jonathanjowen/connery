#!/bin/python3

import numpy

def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    array_shape = tuple(read_integers())
    print(numpy.zeros(array_shape, dtype=int))
    print(numpy.ones(array_shape, dtype=int))



# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
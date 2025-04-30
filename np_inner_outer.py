#!/bin/python3

import numpy


def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    a = numpy.array(list(read_integers()))
    b = numpy.array(list(read_integers()))
    
    print(numpy.inner(a, b))
    print(numpy.outer(a, b))

    

# https://www.hackerrank.com/challenges/np-inner-and-outer/problem
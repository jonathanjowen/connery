#!/bin/python3

import numpy

def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    n, unused_integer = read_integers()
    
    list_a = []
    for _ in range(n):
        list_a += [list(read_integers())]
    a = numpy.array(list_a)
    
    list_b = []
    for _ in range(n):
        list_b += [list(read_integers())]
    b = numpy.array(list_b)
    
    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))

# https://www.hackerrank.com/challenges/np-array-mathematics/problem
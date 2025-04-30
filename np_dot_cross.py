#!/bin/python3

import numpy

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    n = read_integer()
    
    list_a = []
    for _ in range(n):
        list_a += [list(read_integers())]
    a = numpy.array(list_a)

    list_b = []
    for _ in range(n):
        list_b += [list(read_integers())]
    b = numpy.array(list_b)
    
    print(numpy.matmul(a, b))

    

# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
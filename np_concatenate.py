#!/bin/python3

import numpy

def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    n, m, p = read_integers()

    rows_1 = []
    for _ in range(n):
        rows_1 += [list(read_integers())]
    array_1 = numpy.array(rows_1)

    rows_2 = []
    for _ in range(m):
        rows_2 += [list(read_integers())]
    array_2 = numpy.array(rows_2)

    print(numpy.concatenate((array_1, array_2)))

    

# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
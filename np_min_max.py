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
    
    min_axis_1 = numpy.min(a, axis=1)
    print(numpy.max(min_axis_1))



# https://www.hackerrank.com/challenges/np-min-and-max/problem
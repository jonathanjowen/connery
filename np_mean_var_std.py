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
    
    print(numpy.mean(a, axis=1))
    print(numpy.var(a, axis=0))
    print(numpy.round(numpy.std(a), 11))


    
# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
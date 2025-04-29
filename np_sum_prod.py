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
    
    sum_a = numpy.sum(a, axis=0)
    print(numpy.prod(sum_a))



# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
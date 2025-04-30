#!/bin/python3

import numpy
numpy.set_printoptions(legacy='1.13')


def read_floats(sep=None):
    """Return an iterator of floats from a STDIN line."""  
    return(map(float, input().split(sep)))
    
if __name__ == '__main__':
    a = numpy.array(list(read_floats()))
    print(numpy.floor(a))
    print(numpy.ceil(a))
    print(numpy.rint(a))



# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
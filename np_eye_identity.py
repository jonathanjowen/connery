#!/bin/python3

import numpy
numpy.set_printoptions(legacy='1.13')


def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    n, m = read_integers()
    print(numpy.eye(n, m))


# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
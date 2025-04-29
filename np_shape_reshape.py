#!/bin/python3

import numpy as np

def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))

if __name__ == '__main__':
    initial_array = np.array(list(read_integers()))
    print(np.reshape(initial_array, (3, 3)))

# https://www.hackerrank.com/challenges/np-shape-reshape/problem
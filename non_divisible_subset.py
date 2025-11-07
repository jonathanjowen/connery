#!/bin/python3

import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):
    n = len(s)
    # Initialize array & fill with frequency of remainders
    remainder_freqs = [0 for remainder in range(k)]
    for i in range(n):
        remainder_freqs[s[i] % k] += 1
    # Adjust array to ensure remainder k/2 can only be used once
    if (k % 2 == 0):
        remainder_freqs[k//2] = min(remainder_freqs[k//2], 1)
    
    # Limit result to include no more than 1 element exactly divisble by k
    length_of_subset = min(remainder_freqs[0], 1)
    # Iterate to midpoint of remainders array 
    # adding the maximum count of elements with remainder i or k-i
    for i in range(1, (k//2) + 1):
        length_of_subset += max(remainder_freqs[i], 
                                remainder_freqs[k-i])
    
    return length_of_subset


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)


# https://www.hackerrank.com/challenges/non-divisible-subset/problem

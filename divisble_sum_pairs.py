#!/bin/python3

import itertools



def divisibleSumPairs(n, k, ar):

    """
    Docstring for divisibleSumPairs
    
    :param n:   INTEGER length of ar
                2 <= n <= 100
    :param k:   INTEGER divisor
                1 <= k <= 100
    :param ar:  INTEGER_ARRAY of n integers
                1 <= ar[i] <= 100                          
    """
    
    pairs = itertools.combinations((ar), 2)
    divisible_by_k = [pair for pair in pairs if sum(pair)%k == 0]
    return len(divisible_by_k)



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    print()
    result = divisibleSumPairs(n, k, ar)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
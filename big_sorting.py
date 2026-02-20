#!/bin/python3

from collections import defaultdict



def bigSorting(unsorted):

    """
    Docstring for bigSorted
    
    :param unsorted: STRING_ARRAY n integers cast as strings
                        1 <= n <= 2 * 10^5
                        1 <= string length <= 10^6
                        1 <= sum of string lengths <= 10^6
    """
    
    sorted_integers = []

    # Group integer strings by length
    length_groups = defaultdict(list)
    for i in unsorted:
        length_groups[len(i)].append(i)
    
    # Iterate through groups from fewest to most integer digits
    lengths = sorted(list(length_groups.keys()))
    for l in lengths:
        # Sort group & append integers to sorted list 
        sorted_integers += sorted(length_groups[l])
    
    return sorted_integers



if __name__ == '__main__':

    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    print()
    result = bigSorting(unsorted)

    print('OUTPUT')
    print()
    for i in result:
        print(i)



# https://www.hackerrank.com/challenges/big-sorting/problem
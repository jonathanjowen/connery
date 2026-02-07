#!/bin/python3

import itertools

def stones(n, a, b):
    
    n_stones = n
    differences = [a, b]

    if a == b:
        combination_sums = [a * (n_stones - 1)]
    else:
        combinations = itertools.combinations_with_replacement(
            differences,
            n_stones - 1
            )

        combination_sums = []
        for c in combinations:
            combination_sums.append(sum(c))
            combination_sums.sort()

    return combination_sums




if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        

        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())

        result = stones(n, a, b)
        print(result)
        print()



# https://www.hackerrank.com/challenges/manasa-and-stones/problem

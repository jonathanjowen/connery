#!/bin/python3



def absolutePermutation(n, k):

    """
    Docstring for absolutePermutation
    
    :param n: INTEGER number of natural numbers in permutation
    :param k: INTEGER absolute difference |i - position(i)|
              for all i in permuatation where 1 <= position(i) <= n, i.e. is one-based
    """
    
    if k == 0:
        permutation = list(range(1, n + 1))
    elif n % (2 * k) != 0:
        permutation = [-1]
    else:
        permutation = [None] * n
        for i in range(n):
            if permutation[i] is None:
                permutation[i] = i + k + 1
                permutation[i + k] = i + 1
    
    return permutation



if __name__ == '__main__':
 
    n_tests = int(input().strip())

    for _ in range(n_tests):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        print()
        result = absolutePermutation(n, k)
        print(result)



# https://www.hackerrank.com/challenges/absolute-permutation/problem
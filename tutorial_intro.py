#!/bin/python3



def introTutorial(V, arr):
    
    """
    Docstring for introTutorial
    
    :param V: INTEGER value to find in arr
              -1000 <= V <= 1000      
    :param arr: INTEGER_ARRAY n integers
                1 <= n <= 1000
    """

    return arr.index(V)



if __name__ == '__main__':

    V = int(input().strip())
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print()
    result = introTutorial(V, arr)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/tutorial-intro/problem
#!/bin/python3



def insertionSort1(n, arr):
    
    """
    Docstring for insertionSort1
    
    :param n:   INTEGER size of array
                1 <= n <= 1000    
    :param arr: INTEGER_ARRAY n integers
                -1000 <= arr[i] <= 1000
    """

    x = arr[n - 1]
    i = n - 1
    while i > 0 and arr[i - 1] >= x:
        arr[i] = arr[i - 1]
        print(*arr)
        i -= 1
    arr[i] = x
    print(*arr)



if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    print()
    print('OUTPUT')
    insertionSort1(n, arr)



# https://www.hackerrank.com/challenges/insertionsort1/problem
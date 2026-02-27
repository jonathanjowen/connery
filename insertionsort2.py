#!/bin/python3



def insertionSort2(n, arr):
    
    """
    Docstring for insertionsort2
    
    :param n:       INTEGER length of array
                    1 <= n <= 1000
    :param arr:     INTEGER_ARRAY of n unsorted integers
                    -1000 <= arr[i] <= 1000 for 0 <= i <= n            
    """

    
    for i in range(2, n + 1):
        x = arr[i - 1]
        j = i - 1
        while j > 0 and arr[j - 1] >= x:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = x
        print(*arr)


if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    print()
    print('OUTPUT')
    insertionSort2(n, arr)



# https://www.hackerrank.com/challenges/insertionsort2/problem



# Note
# insertionsort2 adapts function for inserting an element into 
# a sorted array (see insertionsort1.py) by iteratively
#  building a sorted array from left to right, i.e. 1st & 2nd
# elements are sorted, then 3rd is inserted & sorted into 
# that previously sorted array, etc
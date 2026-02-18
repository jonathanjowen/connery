#!/bin/python3



def almostSorted(arr):

    """
    Docstring for almostSorted
    
    :param arr: INTEGER_ARRAY of n distinct integers
    """

    # Case when array is already sorted
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print('yes')
    
    # Search for inversions
    else:
        invert_idxs = []
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                invert_idxs.append(i)
        n_invert = len(invert_idxs)

        # One inversion: Test swap with next integer
        if  n_invert == 1:
            idx = invert_idxs[0]
            temp = arr[idx]
            arr[idx] = arr[idx + 1]
            arr[idx + 1] = temp
            if arr == sorted_arr:
                print('yes')
                print('swap', idx + 1, idx + 2)
            else:
                print('no')

        # Two inversions: Test swap at inversions
        elif n_invert == 2:
            idx_1 = invert_idxs[0]
            idx_2 = invert_idxs[1] + 1
            temp = arr[idx_1]
            arr[idx_1] =  arr[idx_2]
            arr[idx_2] = temp
            if arr == sorted_arr:
                print('yes')
                print('swap', idx_1 + 1, idx_2 + 1)
            else:
                print('no')

        # More than two inversions: Test for single sequence
        elif invert_idxs[-1] == invert_idxs[0] + n_invert - 1:
            print('yes')
            print('reverse', invert_idxs[0] + 1, invert_idxs[-1] + 2)
        
        else:
            print('no')



if __name__ == '__main__':
    

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)



# https://www.hackerrank.com/challenges/almost-sorted/problem
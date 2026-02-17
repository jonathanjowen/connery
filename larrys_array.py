#!/bin/python3



def larrysArray(A):
    
    """
    Docstring for larrysArray
    
    :param A: INTEGER_ARRAY of n natural numbers A[i]: 1 <= A[i] <= n
    """

    # Count number of occurrences of greater numbers before each 
    # array element (inversions)
    # Example
    # [1, 4, 5, 2, 3]
    #       before         inversions
    # 1                        0
    # 4     1                  0
    # 5     1, 4               0
    # 2     1, 4*, 5*          2
    # 3     1, 4*, 5*, 2       2
    #                   total  4
    
    inversion_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                inversion_count += 1
    
    # Even number of inversions: array can be sorted
    if inversion_count % 2 == 0:
        return 'YES'
    # Odd number of inversions: array cannot be sorted
    else:
        return 'NO'



if __name__ == '__main__':

    results = []

    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        results.append((result, A))

    print()
    print('OUTPUT')
    for x in results:
        print(x[0], x[1])

    



# https://www.hackerrank.com/challenges/larrys-array/problem
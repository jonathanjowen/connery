#!/bin/python3


# Complete the plusMinus function below.
def plusMinus(arr):
    arr_n = len(arr)
    arr_pos = len([i for i in arr if i > 0]) / arr_n
    arr_neg = len([i for i in arr if i < 0]) / arr_n
    print(arr_pos)
    print(arr_neg)
    print(1 - arr_pos - arr_neg)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

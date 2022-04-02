#!/bin/python3

def average(array):
    distinct_array = set(array)
    return(sum(distinct_array) / len(distinct_array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



# www.hackerrank.com/challenges/py-introduction-to-sets/problem

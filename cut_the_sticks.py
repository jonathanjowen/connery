#!/bin/python3



def cutTheSticks(arr):
    n_of_sticks = []
    while len(arr) > 0:
        n_of_sticks.append(len(arr))
        shortest_stick = min(arr)
        arr = [stick - shortest_stick for stick in arr if stick > shortest_stick]
    return n_of_sticks

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    print(result)

# Note
# SUbtraction of shortest_stick is consistent with description of
# the problem but not necessary. If lengths aren't needed, the 
# following definition of arr is sufficient
# arr = [stick for stick in arr if stick > shortest_stick]

# https://www.hackerrank.com/challenges/cut-the-sticks/problem
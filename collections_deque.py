#!/bin/python3

from collections import deque

n_operations = int(input())

deq = deque()

for _ in range(n_operations):
    operation = input().split()   
    if operation[0] == 'pop':
        deq.pop()
    elif operation[0] == 'popleft':
        deq.popleft()
    elif operation[0] == 'append':
        deq.append(int(operation[1]))
    else:
        deq.appendleft(int(operation[1]))
       
print(*deq)


# https://www.hackerrank.com/challenges/py-collections-deque/problem
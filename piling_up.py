#!/bin/python3

from collections import deque

n_tests = int(input())

for _ in range(n_tests):
       
    n_blocks = int(input())
    blocks = deque(map(int, input().split()))
    
    if blocks[-1] > blocks[0]:
        top_block = blocks.pop()
    else:
        top_block = blocks.popleft()
    
    success = 1
    while (len(blocks) > 0) and (success == 1):
        if blocks[-1] < blocks[0]:
            blocks.rotate(-1)
        if blocks[-1] <= top_block:
            top_block = blocks.pop()
        else:
            print("No")
            success = 0
            
    if success == 1:
        print("Yes")

# https://www.hackerrank.com/challenges/piling-up/problem
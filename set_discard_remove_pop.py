#!/bin/python3

n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))
       
set_sum = 0
for i in s:
    set_sum += i
        
print(set_sum)


# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
#!/bin/python3

# Note: acceptable solutions needed to use only 2 lines of code, 1 for loop, no string functions
for i in range(1,int(input())): 
    print(i * sum([10**0, 10**1, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8][0:i])) 
# Better: print(i*10**i//9)

# https://www.hackerrank.com/challenges/python-quest-1/problem
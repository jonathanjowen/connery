#!/bin/python3

n = 3

# for i in range(1,int(input())+1):
for i in range(1, n+1):
    # solution
    # print(((10**i - 1)//9)**2)
    # using list comprehension: not accepted due to 2nd for loop
    # print(sum([(10**p) for p in range(i)])**2)
    # using sequences: not accepted due to string formatting
    print(* range(1, i+1), * range(i-1, 0, -1), sep="")



# www.hackerrank.com/challenges/find-angle/problem

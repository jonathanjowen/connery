#!/bin/python3

m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

symm_diff_set = a.symmetric_difference(b)
symm_diff_list = sorted(list(symm_diff_set))

for i in symm_diff_list:
    print(i)



# https://www.hackerrank.com/challenges/symmetric-difference/problem
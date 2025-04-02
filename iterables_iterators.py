#!/bin/python3

import itertools

n_letters = int(input())           # N in problem description
letters = input().replace(' ','')
comb_length = int(input())         # K in problem description

letters_without_a = letters.replace('a', '')

count_comb_with_a = 0
for combination in itertools.combinations(letters, comb_length):
    count_comb_with_a += 1  

count_comb_without_a = 0
for combination in itertools.combinations(letters_without_a, comb_length):
    count_comb_without_a += 1

p_comb_contains_a = 1 - (count_comb_without_a / count_comb_with_a)

print(p_comb_contains_a)


# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
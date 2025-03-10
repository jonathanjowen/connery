#!/bin/python3

from collections import Counter 

n_words = int(input())

word_counter = Counter()

for _ in range(n_words):
    word_counter.update({input(): 1})

word_count_list = [count for count in word_counter.values()]  
print(len(word_count_list))
print(' '.join(map(str, word_count_list)))

# https://www.hackerrank.com/challenges/word-order/problem
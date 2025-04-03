#!/bin/python3

if __name__ == '__main__':
    n_english = int(input())
    english = input().split()
    n_french = int(input())
    french = input().split()
    print(len(set(english).intersection(french))) 


# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
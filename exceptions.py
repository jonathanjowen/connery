#!/bin/python3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        a, b = input().split()
        try:
            print(int(a)//int(b))
        except Exception as e:
            print('Error Code:', e)

# https://www.hackerrank.com/challenges/exceptions/problem
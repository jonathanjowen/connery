#!/bin/python3

def wrapper(f):
    def fun(l):
        return f([' '.join(['+91', phone[-10:-5], phone[-5:]]) for phone in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
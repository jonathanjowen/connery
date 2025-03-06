#!/bin/python3

n_countries = int(input())

countries = set()
for _ in range(n_countries):
    countries.add(input())
    
print(len(countries))

# https://www.hackerrank.com/challenges/py-set-add/problem
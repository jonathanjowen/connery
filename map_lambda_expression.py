#!/bin/python3


cube = lambda x: pow(x, 3)

def fibonacci(n):
    fibonacci_numbers = [0, 1]
    while len(fibonacci_numbers) < n:
        fibonacci_numbers += [sum(fibonacci_numbers[-2:])]
    return fibonacci_numbers[0:n]
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

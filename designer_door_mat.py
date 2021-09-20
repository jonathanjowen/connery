#!/bin/python3


if __name__ == '__main__':
#    n, m = input(), int(input())
    n, m = int(7), int(27)
    pattern_rows = int((n - 1) / 2)
    for i in range(0, pattern_rows):
        print((('.|.'*i)+'.|.'+('.|.'*i)).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(pattern_rows-1, -1, -1):
        print((('.|.'*i)+'.|.'+('.|.'*i)).center(m, '-'))


# https://www.hackerrank.com/challenges/designer-door-mat/problem

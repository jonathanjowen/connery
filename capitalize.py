#!/bin/python3

def solve(s):
    previous = ' '
    capitalized = ''
    for i in range(0, len(s)):
        if previous == ' ':
            capitalized = capitalized + s[i].upper()
        else:
            capitalized = capitalized + s[i]
        previous = s[i]
    return capitalized


if __name__ == '__main__':

    s = input()

    result = solve(s)
    print(result)


# https://www.hackerrank.com/challenges/capitalize/problem

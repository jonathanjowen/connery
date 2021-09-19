#!/bin/python3

if __name__ == '__main__':
    s = input()
    alnum_result = False
    alpha_result = False
    digit_result = False
    lower_result = False
    upper_result = False
    for element in s:
        if not(alnum_result):
            alnum_result = alnum_result or element.isalnum()
        if not(alpha_result):
            alpha_result = alpha_result or element.isalpha()
        if not(digit_result):
            digit_result = digit_result or element.isdigit()
        if not(lower_result):
            lower_result = lower_result or element.islower()
        if not(upper_result):
            upper_result = upper_result or element.isupper()
    print(alnum_result)
    print(alpha_result)
    print(digit_result)
    print(lower_result)
    print(upper_result)


# https://www.hackerrank.com/challenges/string-validators/problem

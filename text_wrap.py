#!/bin/python3

import textwrap

def wrap(string, max_width):
    paragraph = [string[i : i + max_width] for i in range(0, len(string), max_width)]
    return '\n'.join(paragraph)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# https://www.hackerrank.com/challenges/text-wrap/problem

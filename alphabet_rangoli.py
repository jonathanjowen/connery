#!/bin/python3

import string

az_list = list(string.ascii_lowercase)

def print_rangoli(size):
    rangoli_list = az_list[0:size]
    for i in range(-1, -1 * (size + 1), -1):
        forward_i = rangoli_list[i:]
        reverse_i = forward_i[::-1]
        letters_i = reverse_i[: -1] + forward_i
        print('-'.join(letters_i).center(4 * size - 3, '-'))
    for i in range(1, size):
        forward_i = rangoli_list[i:]
        reverse_i = forward_i[::-1]
        letters_i = reverse_i[: -1] + forward_i
        print('-'.join(letters_i).center(4 * size - 3, '-'))
    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

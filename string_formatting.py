#!/bin/python3

def print_formatted(number):
    binary_width = str(len(bin(number)) - 2)
    for i in range(1, number + 1):
         dec_str = ("{:" + binary_width + "}").format(i)
         oct_str = ("{:" + binary_width + "o}").format(i)
         hex_str = ("{:" + binary_width + "X}").format(i)
         bin_str = ("{:" + binary_width + "b}").format(i)
         print(" ".join((dec_str, oct_str, hex_str, bin_str)))
    return

if __name__ == '__main__':
    # n = int(input())
    n = 17
    print_formatted(n)


# https://www.hackerrank.com/challenges/python-string-formatting/problem

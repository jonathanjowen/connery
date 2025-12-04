#!/bin/python3

import math
import os
import random
import re
import sys


def biggerIsGreater(w):

    if len(w) == 1:
        answer = 'no answer'
    else:
        i = len(w) - 1
        while (i > 0) and (w[i-1] >= w[i]):
            i -= 1

        if (i < 1) and (w[0] >= w[1]):
            answer = 'no answer'

        else:
            answer_left = w[0:(i-1)]
            letter_to_swap = w[i-1]
            remaining_letters = sorted(w[(i-1):])
            reversed_swap_index = remaining_letters[::-1].index(letter_to_swap)
            swap_index = len(remaining_letters) - reversed_swap_index - 1
            replacement_letter = remaining_letters[swap_index + 1]
            del remaining_letters[swap_index + 1]    
            answer = answer_left + replacement_letter + ''.join(remaining_letters)
    
    return answer
    

if __name__ == '__main__':
    
    T = int(input().strip())

    for T_itr in range(T):
        w = input()
        print()
        result = biggerIsGreater(w)
        print(result)


# https://www.hackerrank.com/challenges/bigger-is-greater/problem
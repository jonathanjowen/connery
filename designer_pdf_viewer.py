#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    max_letter_height = 0

    for letter in word:
        alphabet_idx = string.ascii_lowercase.find(letter)
        letter_height = h[alphabet_idx]
        if letter_height > max_letter_height:
            max_letter_height = letter_height
    
    return(max_letter_height * len(word))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # h = list(map(int, input().rstrip().split()))
    input_0 = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7'
    h = list(map(int, input_0.rstrip().split()))

    # word = input()
    input_1 = 'zaba'
    word = input_1

    result = designerPdfViewer(h, word)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()


# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
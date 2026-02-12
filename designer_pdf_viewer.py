#!/bin/python3

import string



def designerPdfViewer(h, word):
    
    max_letter_height = 0

    for letter in word:
        alphabet_idx = string.ascii_lowercase.find(letter)
        letter_height = h[alphabet_idx]
        if letter_height > max_letter_height:
            max_letter_height = letter_height
    
    return(max_letter_height * len(word))



if __name__ == '__main__':
    
    h = list(map(int, input().rstrip().split()))
    word = input()

    result = designerPdfViewer(h, word)
    print()
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
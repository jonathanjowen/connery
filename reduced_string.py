#!/bin/python3

import re



def superReducedString(s):

    """
    Docstring for superReducedString
    
    :param s:   STRING of lowercase letters
                1 <= length of s <= 100    
    """

    reduced = re.sub(r'([a-z])\1', '', s)
    while len(reduced) < len(s):
        s = reduced
        reduced = re.sub(r'([a-z])\1', '', s)
   
    if reduced == '':
        return  'Empty String'
    else:
        return reduced



if __name__ == '__main__':

    s = input()

    print()
    result = superReducedString(s)
    print('OUTPUT')
    print(result)


# https://www.hackerrank.com/challenges/reduced-string/problem
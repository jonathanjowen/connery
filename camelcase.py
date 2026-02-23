#!/bin/python3

import re



def camelcase(s):
    
    """
    Docstring for camelcase
    
    :param s:   STRING of lowercase letters
                1 <= length of s <= 10^5   
    """

    lower = re.sub(r'[A-Z]', '', s)
    return 1 + len(s) - len(lower)



if __name__ == '__main__':

    s = input()

    print()
    result = camelcase(s)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/camelcase/problem
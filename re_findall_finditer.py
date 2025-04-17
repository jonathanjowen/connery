#!/bin/python3

import re

if __name__ == '__main__':
    
    vowels_pattern = r'(?<=[bcdfghjklmnpqrstvwxyz])[aeiou]{2,}(?=[bcdfghjklmnpqrstvwxyz])'
    
    input_string = input()
    
    vowels_matches = re.findall(vowels_pattern, input_string, re.IGNORECASE)
    
    if len(vowels_matches ) > 0:
        print(*vowels_matches, sep ='\n')
    else:
        print('-1')


# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
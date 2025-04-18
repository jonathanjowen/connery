#!/bin/python3

import re

if __name__ == '__main__':
    
    longer_string = input()
    shorter_string = input()
    
    match_string = r'(?=(' + shorter_string + r'))'
    
    if re.search(shorter_string, longer_string) is not None:
        matches = re.finditer(match_string, longer_string)
        for m in matches:
            print('(', m.start(), ', ', m.start() + len(shorter_string) -1, ')', sep = '')
    else:
        print('(-1, -1)')



# https://www.hackerrank.com/challenges/re-start-re-end/problem
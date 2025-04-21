#!/bin/python3

import re


def spell_and_or(regex_match):
    """ Returns and, or as replacements for &&, ||."""  
    if regex_match.group(0) == r'&&':
        replacement_string = 'and'
    else:
        replacement_string = 'or'
    return replacement_string
    


if __name__ == '__main__':
    
    and_or_pattern = r'(?<=\s)([&|])\1(?=\s)'
    
    n_of_lines = int(input())
    for _ in range(n_of_lines):
        line_of_code = input()
        print(re.sub(and_or_pattern, spell_and_or, line_of_code))



# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
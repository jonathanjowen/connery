#!/bin/python3

import re

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def print_hex_colors(string):
    """Print matches to hex color code pattern"""
    hex_color_pattern = r'#[0-9ABCDEF]{6}|#[0-9ABCDEF]{3}'
    hex_color_matches = re.findall(hex_color_pattern, string, re.IGNORECASE)
    if len(hex_color_matches) > 0:
        print(*hex_color_matches, sep='\n')
    return None

if __name__ == '__main__':
    in_selector_flag = False
    n_of_css_lines = read_integer()    
    for _ in range(n_of_css_lines):
        css_line = input().strip()
        # print(css_line)
        if in_selector_flag is True:
            print_hex_colors(css_line)
        if bool(re.search(r'\{', css_line)):
            in_selector_flag = True
        if bool(re.search(r'\}', css_line)):
            in_selector_flag = False
            

# https://www.hackerrank.com/challenges/hex-color-code/problem
#!/bin/python3

import re


def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))

    
def validate_mobile_number(string):
    """Print YES for a valid mobile number or NO otherwise"""
    mobile_number_pattern = r'^[789][0-9]{9}$'
    if (bool(re.match(mobile_number_pattern, string))):
        print('YES')
    else:
        print('NO')
    return None


if __name__ == '__main__':
    
    n_of_phone_numbers = read_integer()
    
    for _ in range(n_of_phone_numbers):
        phone_number = input()
        validate_mobile_number(phone_number)

# Problem defines a valid mobile phone number as 10 digits starting with 7, 8, or 9

# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

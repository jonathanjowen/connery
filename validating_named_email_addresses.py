#!/bin/python3

import email.utils
import re

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))

def validate_email_address(string):
    """Return True if string matches valid email pattern or False otherwise"""
    email_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9_\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    is_email = re.match(email_pattern, string) is not None
    return is_email

if __name__ == '__main__':    
    n_of_email_addresses = read_integer()
    for _ in range(n_of_email_addresses):
        parsed_input = email.utils.parseaddr(input())
        if validate_email_address(parsed_input[1]):
            print(email.utils.formataddr(parsed_input))
            

# See problem for definition of a valid email address

# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
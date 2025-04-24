#!/bin/python3

import re


def read_integer():
    """ Return an integer read from STDIN """
    return(int(input()))
    
    
def validate_string_length(string_length, min_length=1, max_length=None):
    """ Return boolean
        True: string length is between minimum and any maximum
        False: string length is outside minimum and any maximum
    """
    pass_min_length = (min_length <= string_length)
    if max_length is not None:
        pass_max_length = (string_length <= max_length)
    else:
        pass_max_length = True
    return pass_min_length and pass_max_length
    
    
def count_unique_chars(string):  
    """ Return number of unique characters"""
    unique_chars = set(string)
    return len(unique_chars)
    
    
def get_all_matches(regex_pattern, string):  
    """ Return all matches to a regular expression"""
    return re.findall(regex_pattern, string)


def count_matches(regex_pattern, string):  
    """ Return number of matches to a regular expression"""
    matches = get_all_matches(regex_pattern, string)
    return len(matches)
    


if __name__ == '__main__':  
      
    valid_uid_length = 10
    valid_uppercase_min = 2
    valid_numeric_min = 3
    
    nonalphanumeric_chars = r'[^a-zA-Z0-9]'
    uppercase_chars = r'[A-Z]'
    numeric_chars = r'[0-9]'
    
    n_of_tests = read_integer()
    for _ in range(n_of_tests):
        test_uid = input()
        uid_length = len(test_uid)
        if (
            (validate_string_length(uid_length, valid_uid_length)
            and (count_matches(nonalphanumeric_chars, test_uid) == 0)
            and (count_unique_chars(test_uid) == uid_length)
            and (count_matches(uppercase_chars, test_uid) >= valid_uppercase_min)
            and (count_matches(numeric_chars, test_uid) >= valid_numeric_min))
            ):
            print('Valid')
        else:
            print('Invalid')
        


# https://www.hackerrank.com/challenges/validating-uid/problem
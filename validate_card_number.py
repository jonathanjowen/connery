#!/bin/python3

import re


def read_integer():
    """ Return an integer read from STDIN """
    return(int(input()))
    


if __name__ == '__main__':  
         
    credit_card_pattern = r'^[456][0-9]{3}\-?([0-9]{4}\-?){2}[0-9]{4}$'
    consecutive_digits = r'([0-9])\1{3}'
    nonnumeric = r'[^0-9]'
    
    n_of_credit_cards = read_integer()
    for _ in range(n_of_credit_cards):
        test_credit_card = input()
        numbers_only = re.sub(nonnumeric, '', test_credit_card)
        if (
            (re.match(credit_card_pattern, test_credit_card) is not None)
            and (re.search(consecutive_digits, numbers_only) is None)
            ):
            print('Valid')
        else:
            print('Invalid')
        
        
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem    
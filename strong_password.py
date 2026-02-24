#!/bin/python3

import re



def minimumNumber(n, password):
    
    """
    Docstring for minimumNumber
    
    :param n:        INTEGER length of password
                     1 <= n <= 100
    :param password: STRING password containing n characters from
                     [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ]               
    """
        
    addl_lower = 1 * (n == len(re.sub(r'[a-z]', '', password)))
    print('additional lower', addl_lower)
    addl_upper = 1 * (n == len(re.sub(r'[A-Z]', '', password)))
    print('additional upper', addl_upper)
    addl_digit = 1 * (n == len(re.sub(r'[0-9]', '', password)))
    print('additional digit', addl_digit)
    addl_special = 1 * (n == len(re.sub(r'[!@#$%^&*()\-+ ]', '', password)))
    print('additional special', addl_special)

    addl_char = addl_lower + addl_upper + addl_digit + addl_special

    if n + addl_char >= 6:
        return addl_char
    else:
        return 6 - n



if __name__ == '__main__':

    n = int(input().strip())
    password = input()

    print()
    answer = minimumNumber(n, password)
    print('OUTPUT')
    print(answer)
    print()



# https://www.hackerrank.com/challenges/strong-password/problem

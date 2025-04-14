#!/bin/python3


def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))

    
if __name__ == '__main__':
    
    unused_integer = read_integer()
    integer_list = list(read_integers())
    
    if all(i > 0 for i in integer_list):
        print(any(str(i) == str(i)[::-1] for i in integer_list))
    else:
        print(False)


# https://www.hackerrank.com/challenges/any-or-all/problem
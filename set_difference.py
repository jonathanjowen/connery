#!/bin/python3

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))

    
if __name__ == '__main__':
    n_english = read_integer()
    english_students = set(read_integers())
    n_french = read_integer()
    french_students = set(read_integers())
    
    english_only = english_students.difference(french_students)

    print(len(english_only))



# https://www.hackerrank.com/challenges/py-set-difference-operation/problem
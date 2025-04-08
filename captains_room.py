#!/bin/python3

from itertools import groupby


def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))

    
if __name__ == '__main__':
    unused_integer = read_integer()
    room_assignments = sorted(list(read_integers()))   
    for key, group in groupby(room_assignments):
        if len(list(group)) == 1:
            print(key)
    

# https://www.hackerrank.com/challenges/py-the-captains-room/problem
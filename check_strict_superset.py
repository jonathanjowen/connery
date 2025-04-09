#!/bin/python3

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))
    
if __name__ == '__main__':
    a = set(read_integers())
    n_other_sets = read_integer()

    for _ in range(n_other_sets):
        other_set = set(read_integers())
        if (a.issuperset(other_set)) and not (a.issubset(other_set)):
            result = True
        else:
            result = False
            break
        
print(result)

# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
    
#!/bin/python3

def read_integer():
    """Return an integer read from STDIN."""
    return(int(input()))
    
def read_integers(sep=None):
    """Return an iterator of integers from a STDIN line."""  
    return(map(int, input().split(sep)))

def read_split_line(sep=None):
    """Return an iterator of strings from a STDIN line."""
    return(input().split(sep))
  
    
if __name__ == '__main__':
    
    unused_integer = read_integer()
    a = set(read_integers())
    n_of_mutations = read_integer()
    
    for _ in range(n_of_mutations):
        mutation_type, unused_string = read_split_line()
        mutation_set = set(read_integers())      

        if mutation_type == 'update':
            a.update(mutation_set)
        elif mutation_type == 'intersection_update':
            a.intersection_update(mutation_set)
        elif mutation_type == 'difference_update':
            a.difference_update(mutation_set)
        elif mutation_type ==  'symmetric_difference_update':
            a.symmetric_difference_update(mutation_set)
        else:
            raise Exception("Unmatched operation")
 
    print(sum(a))


# https://www.hackerrank.com/challenges/py-set-mutations/problem     
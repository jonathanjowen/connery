#!/bin/python3

import itertools
from collections import Counter 



def happyLadybugs(b):
    
    # Rename variables for clarity
    board = b

    # Remove empty cells to leave only cells with ladybugs 
    ladybugs = board.replace('_', '')

    # Case 0: no ladybugs means none are unhappy, all are happy
    if not ladybugs:
        return 'YES'
    
    # Case 1: a ladybug whose color appears once will always be unhappy
    ladybug_counts = Counter(ladybugs).most_common()
    least_common_ladybug_count = ladybug_counts[-1][1]
    if least_common_ladybug_count == 1:
        return 'NO'
    
    # Case 2: one empty cell is sufficient to make all ladybugs happy eventually
    n_cells = len(board)
    n_ladybugs = len(ladybugs)
    n_empty_cells = n_cells - n_ladybugs
    if n_empty_cells > 0:
        return 'YES'

    # Case 3: if no moves are available check whether or not all ladybugs started happy   
    ladybug_groups = []
    for key, group in itertools.groupby(ladybugs):
         ladybug_groups.append(list(group))
    unhappy_ladybugs = [group for group in ladybug_groups if len(group) == 1]
    if len(unhappy_ladybugs) == 0:
        return 'YES'
    else:
        return 'NO'



if __name__ == '__main__':

    n_games = int(input().strip())

    results = []

    for _ in range(n_games):

        unused_input = int(input().strip())
        b = input()

        print()
        result = happyLadybugs(b)
        results.append(result)

    
    print(results)



# https://www.hackerrank.com/challenges/happy-ladybugs/problem
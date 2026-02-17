#!/bin/python3

import re



def bomberMan(n, grid):
    
    """
    Docstring for bomberMan
    
    :param n: INTEGER elapsed time until final state of bomb grid
    :param grid: STRING ARRAY initial state of bomb grid
                 O = bomb
                 . = empty cell
    """
 
    rows = len(grid)      # could use global r
    cols = len(grid[0])   # could use global c

    # case when elapesed time = 1s 
    # final state of grid is just the initial state
    if n == 1:
        return grid
    
    # case when elapsed time is even
    # all cells contain bombs (with either 3s or 1s on timer)
    if n % 2 == 0:
        grid = ['O' * cols for i in range(rows)]
        return grid
    
    # case for odd times > 1
    # grid alternates between two states
    n //= 2
    for alt_state in range((n + 1) % 2 + 1):
        # initialize new grid of bombs similar to even n case
        new_grid = [['O'] * cols for i in range(rows)]

        # function for detonating bomb (applied in new grid)
        def detonate(x, y):

            """
            Docstring for detonate
            
            :param x: INTEGER row index of cell
            :param y: INTEGER column index of cell
            """

            # check cell is within grid 
            if 0 <= x < rows and 0 <= y < cols:
                # set cell as empty cell
                new_grid[x][y] = '.'

        # identify cells affected by detonating bomb
        x_offsets = [0, 0, 0, 1, -1]
        y_offsets = [0, 1, -1, 0, 0]

        # iterate through grid
        for x in range(rows):
            for y in range(cols):
                # check cell for bomb
                if grid[x][y] == 'O':
                    # detonate bomb in cell & adjacent cells
                    for i, j in zip(x_offsets, y_offsets):
                        detonate(x + i, y + j)

        # after all bombs detonated update grid to new grid
        grid = new_grid

    return [''.join(row) for row in grid]



if __name__ == '__main__':
  
    first_multiple_input = input().rstrip().split()
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    n = int(first_multiple_input[2])

    grid = []
    for _ in range(r):
        grid_item = input()
        print(grid_item)
        grid.append(grid_item)
    result = bomberMan(n, grid)
    print()
    print('OUTPUT')
    for row in result:
        print(row)



# https://www.hackerrank.com/challenges/bomber-man/problem



# LEARNING ________________________________________________________

# Though definition for bomberMan() below should still correctly 
# iterate through state of bomb grid until time n, HackerRank tests 
# with larger n timed out

 # This approach, involving adding a margin to the bomb grid & 
 # tracking timers on the bombs, was not a good choice for a simple 
 # working solution, which could then have been optimized to 
 # execute without timing out



# FAILED SOLUTION _________________________________________________

# def bomberMan(n, grid):
    
#     rows = len(grid)      
#     cols = len(grid[0])  

#     if n < 2:
#         return grid

#     bombs = ['-' * (cols + 2)]
#     for row in grid:
#         initial_bombs = re.sub(r'O', '1', row)
#         bombs_row = re.sub(r'\.', '3', initial_bombs)
#         bombs.append('|' + bombs_row + '|')
#     bombs.append('-' * (cols + 2))
 
#     for _ in range(n - 2):

#         new_bombs = bombs.copy()
#         for i in range(1, rows + 1):

#             detonations = [match.span()[0] for match in re.finditer('1', bombs[i])]
#             for j in detonations:
#                 new_bombs[i - 1] = new_bombs[i - 1][:j] + '*' + new_bombs[i - 1][j + 1:]
#                 new_bombs[i] = new_bombs[i][:j - 1] + '***' + new_bombs[i][j + 2:]
#                 new_bombs[i + 1] = new_bombs[i + 1][:j] + '*' + new_bombs[i + 1][j + 1:]
            
#             new_bombs[i] = re.sub('2', '1', new_bombs[i])
#             new_bombs[i] = re.sub('3', '2', new_bombs[i])
#             new_bombs[i] = re.sub(r'\.', '3', new_bombs[i])
                

#             new_bombs[i] = '|' + new_bombs[i][1: cols + 1] + '|'
            
#         for i in range(1, rows + 1):
#             new_bombs[i] = re.sub(r'\*', '.', new_bombs[i]) 

#         bombs = ['-' * (cols + 2)] + new_bombs[1:rows + 1].copy() + ['-' * (cols + 2)]

#     for i in range(1, rows + 1):
#         bombs[i] = re.sub(r'[1-3]', 'O', bombs[i][1: cols + 1])

#     return bombs[1: rows + 1]



# HELPFUL ANALYSIS OF PROBLEM _____________________________________

# Grid size constraint: 1 <= r, c <= 200

    # Moderate upper limits on rows & columns suggest limited
    # iterations over the bomb grid will be acceptable

# Elapsed time constraint: 1 <= n <= 10^9

    # n = 1
    # trivial solution returns unchanghed initial grid

    # n = 2 & generally all even n
    # bomberman always fills grid with bombs when time is even,
    # return grid filled with 'O'

    # odd n > 1
    # high upper limit should immediately rule out solutions 
    # involving iteration until time n

        # could state of each cell depend only on n?
            # unlikely due to bombs detonating adjacent cells

        # does bomb grid reach a steady state?
            # possibly but "steady" state would still mean 
            # alternating between all bombs & all empty cells

        # does bomb grid alternate between a few states having 
        # different patterns of bombs & empty cells?
            # seems intuitive based on cycle
            #
            #       >>>>>>>> empty <<<<<<<<
            #      ^           v           ^
            #      ^           v       adjacent
            #      ^           v       detonates
            #      ^           v           ^
            #      ^       bomb (3s) >>>>>>
            #      ^           v
            #    self          v
            #  detonates       v
            #      ^           v
            #      ^       bomb (2s) 
            #      ^           v
            #      ^           v 
            #      ^           v
            #      ^           v
            #       <<<<<< bomb (1s) 
            #
            # test over multiple cycles with simple patterns, 
            # e.g. sample inputs 
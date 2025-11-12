#!/bin/python3

import math
import os
import random
import re
import sys
import time


def queensAttack(board_size, k, queen_y, queen_x, obstacles):

    # Store queen's allowed moves in dictionary of direction keys
    # Initialize values with squares from queen's position to edge of board
    moves = {
        'R': board_size - queen_x,
        'L': queen_x - 1,
        'U': board_size - queen_y,
        'D': queen_y - 1,
        'UR': min(board_size - queen_y, board_size - queen_x),
        'UL': min(board_size - queen_y, queen_x - 1),
        'DL': min(queen_y - 1, queen_x - 1),
        'DR': min(queen_y - 1, board_size - queen_x)       
    }

    # Iterate through obstacles determining direction of queen's move (if any) 
    # Update values with squares to closest obstacle in each direction
    for obstacle in obstacles:
        y = obstacle[0]
        x = obstacle[1]
        if (y - queen_y) == 0:
            if (x - queen_x) > 0:
                moves['R'] = min(moves['R'], x - queen_x - 1)
            else:
                moves['L'] = min(moves['L'], queen_x - x - 1)
        elif (x - queen_x) == 0:
            if (y - queen_y) > 0:
                moves['U'] = min(moves['U'], y - queen_y - 1)
            else:
                moves['D'] = min(moves['D'], queen_y - y - 1)
        elif (y - queen_y) / (x - queen_x) == 1:
            if (y - queen_y) > 0:
                moves['UR'] = min(moves['UR'], y - queen_y - 1)
            else:
                moves['DL'] = min(moves['DL'], queen_y - y - 1)
        elif (y - queen_y) / (x - queen_x) == -1:
            if (y - queen_y) > 0:
                moves['UL'] = min(moves['UL'], y - queen_y - 1)
            else:
                moves['DR'] = min(moves['DR'], queen_y - y - 1)

    # Sum allowable squares for all queen's moves
    return sum(moves.values())s
   

if __name__ == '__main__':

    start_time = time.perf_counter()

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    r_q = int(second_multiple_input[0])
    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
    print()
    print(time.perf_counter() - start_time)

# Note
# Alternative approach of iterating along each direction until 
# an obstacle is encountered runs slower and times out on 
# several Hackerrank test cases -- even with logic to skip iteration for the slowest scenario of no obstacles, presumably 
# because it doesn't skip scenarios that are almost or just as slow,
# e.g. some obstacles but none located where the queen can move, a few
# obstacles that the queen encounters near the edge of the board 
# 
# https://www.hackerrank.com/challenges/queens-attack-2/problem
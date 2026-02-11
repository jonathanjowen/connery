#!/bin/python3

import math



def strangeCounter(t):

    cycle = int(1 + math.log((t + 2) / 3, 2))
    cycle_start_seconds = 1 - 3 * (1 - 2 ** (cycle - 1))
    cycle_start_value = 3 * 2 ** (cycle - 1)
    seconds_since_start = t - cycle_start_seconds
    counter_display = cycle_start_value - seconds_since_start
    
    return counter_display


if __name__ == '__main__':

    t = int(input().strip())

    print()
    result = strangeCounter(t)
    print(result)



# https://www.hackerrank.com/challenges/strange-code/problem
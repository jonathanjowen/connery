#!/bin/python3

def chocolateFeast(n, c, m):
    
    money = n
    chocolate_bar_cost = c
    wrappers_for_free_bar = m

    wrappers = chocolate_bars = money // chocolate_bar_cost

    while (wrappers >= wrappers_for_free_bar):
        free_bars = wrappers // wrappers_for_free_bar
        chocolate_bars += free_bars
        wrappers = (wrappers % wrappers_for_free_bar) + free_bars

    return chocolate_bars



if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)
        print(result)


# https://www.hackerrank.com/challenges/chocolate-feast/problem
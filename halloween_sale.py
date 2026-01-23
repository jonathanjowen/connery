#!/bin/python3

import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    price = p
    discount = d
    min_price = m
    money = s
    games = 0
    counter = 0
    while (money - price >= 0) and (counter < 102):
        counter += 1
        games += 1
        money -= price
        price = max(price - discount, min_price)
        if price == min_price:
            games += money // min_price
            money -= games * min_price
            
    return games
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)
    print(answer)

# https://www.hackerrank.com/challenges/halloween-sale/problem
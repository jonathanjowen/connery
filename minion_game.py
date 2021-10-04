#!/bin/python3

def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    stuart = 0
    kevin  = 0
    for i in range(0, len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart:
        return print('Kevin' + ' ' + str(kevin))
    elif stuart > kevin:
        return print('Stuart' + ' ' + str(stuart))
    else:
        return print('Draw')




if __name__ == '__main__':
    # s = input()
    s = 'BANANA'
    minion_game(s)




# https://www.hackerrank.com/challenges/the-minion-game/problem

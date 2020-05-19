#!/bin/python3

if __name__ == '__main__':
    the_list = []
    n = int(input())
    for _ in range(n):
        cmd, *line = input().split()
        args = list(map(int, line))
        if (cmd == "print"):
            print(the_list)
        else:
            action = "the_list." + cmd + "(" + ",".join(map(str, args)) + ")"
            eval(action)

# https://www.hackerrank.com/challenges/python-lists/problem

#!/bin/python3

def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        if string[i:(i+len(sub_string))].find(sub_string) > -1:
            counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# https://www.hackerrank.com/challenges/find-a-string/problem

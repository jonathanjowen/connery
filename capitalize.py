#!/bin/python3

def solve(s):
    previous = ' '
    capitalized = ''
    for i in range(0, len(s)):
        if previous == ' ':
            capitalized = capitalized + s[i].upper()
        else:
            capitalized = capitalized + s[i]
        previous = s[i]
    return capitalized


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = 'hello   world  lol'

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()



# https://www.hackerrank.com/challenges/capitalize/problem

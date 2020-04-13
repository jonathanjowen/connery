#!/bin/python3


# countApplesAndOranges
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Calculate distance each apple and orange falls from trees a and b
    d_apples = [apple + a for apple in apples]
    d_oranges = [orange + b for orange in oranges]
    # Compare distances to house wall s and t then count number of hits
    n_apples = len([d_apple for d_apple in d_apples
                    if (d_apple >= s and d_apple <= t)])
    n_oranges = len([d_orange for d_orange in d_oranges
                    if (d_orange >= s and d_orange <= t)])
    # Print number of hits
    print(n_apples)
    print(n_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)


# https://www.hackerrank.com/challenges/apple-and-orange/problem

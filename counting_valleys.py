#!/bin/python3



def countingValleys(steps, path):
 
    altitude = 0
    in_valley = False
    valley_count = 0

    for  p in path:
        if p == 'U':
            altitude += 1
        else:
            altitude -= 1

        if altitude < 0 and in_valley is False:
            in_valley = True
        if altitude == 0 and in_valley is True:
            valley_count += 1
            in_valley = False
    
    return valley_count



if __name__ == '__main__':

    steps = int(input().strip())
    path = input()

    print()
    result = countingValleys(steps, path)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/counting-valleys/problem

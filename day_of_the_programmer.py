#!/bin/python3



def dayOfProgrammer(year):

    if year % 400 == 0:
        day_256 = '12.09'
    elif year % 4 == 0:
        if (year < 1918) or (year % 100 != 0):
            day_256 = '12.09'
        else:
            day_256 = '13.09'
    elif year == 1918:
        day_256 = '26.09'
    else:
        day_256 = '13.09'
    
    return f'{day_256}.{year}'



if __name__ == '__main__':
    
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print()
    print('OUTPUT')
    print(year, result)



# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
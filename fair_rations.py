#!/bin/python3



def fairRations(B):

    bread_by_person = B

    bread_given_before_loop = 0
    bread_given = 0
    loop_counter = 0
    loop_limit = 20
  
    while (sum([bread % 2 for bread in bread_by_person]) > 1) and (loop_counter < loop_limit + 1):
        bread_given_before_loop = bread_given
        for i in range(len(bread_by_person) - 1):
            if bread_by_person[i] % 2 == 1:
                bread_by_person[i] += 1
                bread_by_person[i+1] += 1
                bread_given += 2
        loop_counter += 1
        print('LOOP', loop_counter)
        print(f'{bread_given - bread_given_before_loop} additional loaves of bread given this loop')
        print(f'{bread_given} loaves of bread given in total so far')
        print()

    if (sum([bread % 2 for bread in bread_by_person]) > 1) and (loop_counter == loop_limit + 1):
        return r'WARNING.  Preset limit of {loop_limit} while loops reached before calculation completed'
    
    if sum([bread % 2 for bread in bread_by_person]) == 0:
        print('Bread distributed until everyone has an even number of loaves')
        print('Returning numer of loaves given out')
        print()
        return str(bread_given)
    else:
        print('Bread distributed until all but one person has an even number of loaves')
        print('Returning message idnicating not everyone can have an even number of loaves')
        print()
        return 'NO'
    


if __name__ == '__main__':

    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))

    print()
    result = fairRations(B)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/fair-rations/problem

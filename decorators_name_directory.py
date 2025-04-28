#!/bin/python3

import operator
def person_lister(f):
    def inner(people):
        get_age = operator.itemgetter(2)
        sorted_people = sorted(people, key=lambda x: int(get_age(x)))
        return [f(person) for person in sorted_people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')



# Note: Solution required definion of person_lister wrapper all other code was provided and locked

# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem
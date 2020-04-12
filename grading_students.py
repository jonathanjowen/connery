#!/bin/python3

import os


def gradingStudents(grades):
    rounded_grades = []
    for g in grades:
        # Don't round grades below 38
        if g >= 38:
            # Round up to next multiple of 5 if grade is less than 3 below it
            if g % 5 >= 3:
                g = 5 * (1 + g // 5)
        rounded_grades.append(g)
    return(rounded_grades)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import calendar

# m, d, y = map(int, input().split())
m, d, y = map(int, ("08", "05", "2015"))

day = calendar.weekday(y, m, d)

print(calendar.day_name[day].upper())


# www.hackerrank.com/challenges/calendar-module/problem

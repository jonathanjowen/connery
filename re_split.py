#!/bin/python3

regex_pattern = r"[,\.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# https://www.hackerrank.com/challenges/re-split/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    # s = input()
    s = 'caabbbcde'
    s_sorted = ''.join(sorted(s))
    chr_counter = Counter()
    chr_counter.update(s_sorted)
    for tpl in chr_counter.most_common(3):
        print(*tpl)



# https://www.hackerrank.com/challenges/most-commons/problem
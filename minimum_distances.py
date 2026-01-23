#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations


def minimumDistances(a):
    counter = Counter(a)
    most_common = counter.most_common()
    if most_common[0][1] == 1:
        distance = -1
    else:
        min_distances = []
        for value_count in most_common:
            if value_count[1] > 1:
                value_indices = [index for index, value in enumerate(a) if value == value_count[0]]
                min_distance = max(value_indices) - min(value_indices)
                for index_pair in combinations(value_indices, 2):
                    min_distance = min([min_distance, abs(index_pair[1] - index_pair[0])])
                min_distances.append(min_distance)
        distance = min(min_distances)
        
    return distance

    

if __name__ == '__main__':

    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)
    print(result)



# https://www.hackerrank.com/challenges/minimum-distances/problem
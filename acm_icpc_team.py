#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


def acmTeam(topic):
    teams = list(combinations(topic, 2))
    most_topics = 0
    n_of_teams_with_most_topics = 0
    for team in teams:
        binary_0 = int(team[0], 2)
        binary_1 = int(team[1], 2)
        team_topics_binary = bin(binary_0 | binary_1)
        team_topics = str(team_topics_binary).replace('0b','')
        topics_count = len(team_topics.replace('0', ''))
        if topics_count == most_topics:
            n_of_teams_with_most_topics += 1
        elif topics_count > most_topics:
            most_topics = topics_count
            n_of_teams_with_most_topics = 1
            
    return [most_topics, n_of_teams_with_most_topics]


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    topic = []
    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)
    print(result)


# https://www.hackerrank.com/challenges/acm-icpc-team/problem

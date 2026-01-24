#!/bin/python3

def climbingLeaderboard(ranked, player):

    distinct_ranks = sorted(list(set(ranked)), reverse=True)
    rank_idx = len(distinct_ranks) - 1

    player_ranks = []
    for score in player:
        while rank_idx >= 0 and score >= distinct_ranks[rank_idx]:
            rank_idx -= 1
        player_ranks.append(rank_idx + 2)
    
    return player_ranks



if __name__ == '__main__':
    
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)


# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
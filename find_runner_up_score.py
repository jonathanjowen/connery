if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)
    win_score = max(scores)
    winners = scores.count(win_score)
    sorted_scores = sorted(scores, reverse=True)
    print(sorted_scores[winners])

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

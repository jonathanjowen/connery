if __name__ == '__main__':
    scores = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores += [score]
        students += [[name, score]]
    lowest = sorted(scores)[0]
    count_lowest = scores.count(lowest)
    lowest_2nd = sorted(scores)[count_lowest]
    names = []
    for s in students:
        if s[1] == lowest_2nd:
            names += [s[0]]
    [print(n) for n in sorted(names)]

# https://www.hackerrank.com/nested-list/problem

#!/bin/python3



def surfaceArea(stacks):
    
    n_rows = len(stacks)
    n_cols = len(stacks[0])

    top_area = bottom_area = n_rows * n_cols

    row_area = 0
    for row in range(n_rows):
        if row == 0:
            row_area += sum(stacks[row])
        else:
            row_area += sum([abs(x - y) for x, y in zip(stacks[row], stacks[row - 1])])
        if row == n_rows - 1:
            row_area += sum(stacks[row])

    transposed_stacks = [list(row) for row in zip(*stacks)]
    col_area = 0
    for col in range(n_cols):
        if col == 0:
            col_area += sum(transposed_stacks[col])
        else:
            col_area += sum([abs(x - y) for x, y in zip(transposed_stacks[col], transposed_stacks[col - 1])])
        if col == n_cols - 1:
            col_area += sum(transposed_stacks[col])

    return top_area + bottom_area + row_area + col_area



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n_rows = int(first_multiple_input[0])
    unused_input = int(first_multiple_input[1])

    stacks = []
    for _ in range(n_rows):
        stacks.append(list(map(int, input().rstrip().split())))

    print()
    result = surfaceArea(stacks)
    print('OUTPUT')
    print(result)




# https://www.hackerrank.com/challenges/3d-surface-area/problem
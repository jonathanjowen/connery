#!/bin/python3

def gridSearch(grid, pattern):
    
    n_grid_rows = len(grid)
    n_pattern_rows = len(pattern)
    n_rows_to_search = 1 + n_grid_rows - n_pattern_rows

    n_grid_cols = len(grid[0])
    n_pattern_cols = len(pattern[0])
    n_possible_pattern_col_0 = n_grid_cols - n_pattern_cols

    possible_matches = []
    for row in range(n_rows_to_search):
        col = 0
        while col <= n_possible_pattern_col_0:
            search_result = grid[row].find(pattern[0], col)
            if search_result > -1:
                possible_matches.append([row, search_result])
                col = search_result + 1
            else:
                break
    
    if len(possible_matches) == 0:
        return 'NO'
    else:
        for possible_match in possible_matches:
            pattern_row = 1
            row = possible_match[0] + 1
            pattern_col_0 = possible_match[1]
            while pattern_row < n_pattern_rows:
                search_result = grid[row].find(pattern[pattern_row], pattern_col_0)
                if (search_result == -1):
                    break
                elif (pattern_row == n_pattern_rows - 1):
                    return 'YES'
                else:   
                    pattern_row += 1
                    row += 1
        
    return 'NO'
    
    
    



if __name__ == '__main__':
 
    results = []

    n_test_cases = int(input().strip())

    for test_case in range(n_test_cases):

        grid = []
        first_multiple_input = input().rstrip().split()
        n_grid_rows = int(first_multiple_input[0])
        unused_input_1 = int(first_multiple_input[1])       
        for _ in range(n_grid_rows):
            grid_item = input()
            grid.append(grid_item)

        pattern = []
        second_multiple_input = input().rstrip().split()
        n_pattern_rows = int(second_multiple_input[0])
        unused_input_2 = int(second_multiple_input[1])
        for _ in range(n_pattern_rows):
            pattern_item = input()
            pattern.append(pattern_item)

        result = gridSearch(grid, pattern)
        results.append(result)

    print(results)

# https://www.hackerrank.com/challenges/the-grid-search/problem
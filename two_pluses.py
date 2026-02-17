#!/bin/python3



def twoPluses(grid):

    """
    Docstring for twoPluses
    
    :param grid: STRING_ARRAY n strings of m characters that are
                 either B (bad) or G (good)
    """

    # Simplify cell checking by adding border to grid 
    temp_grid = []
    temp_grid.append([' '] * (m + 2))
    for i in range(n):
        temp_grid.append([' '] + list(grid[i]) + [' '])
    temp_grid.append([' '] * (m + 2))
    grid = temp_grid

    # Initialize product of plus areas
    area_product = 0

    # Search for 1st plus of potential pair
    for i in range(1, n + 1):
        for j in range(1, m + 1):
                       
            # Start with initial size of 1st plus = 1
            k = 0
            # Identify 1st plus
            while (grid[i][j - k] == 'G' and
                   grid[i][j + k] == 'G' and
                   grid[i - k][j] == 'G' and
                   grid[i + k][j] == 'G'):
                # Mark cells already used in 1st plus with 'x' to 
                # ensure 2nd plus won't overlap
                grid[i][j - k] = '.'
                grid[i][j + k] = '.'
                grid[i - k][j] = '.'
                grid[i + k][j] = '.'

                # Now search for 2nd plus
                for u in range(1, n + 1):
                    for v in range(1, m + 1):
                        w = 0
                        #  Identify 2nd plus
                        while (grid[u][v - w] == 'G' and
                               grid[u][v + w] == 'G' and
                               grid[u - w][v] == 'G' and
                               grid[u + w][v] == 'G'):
                            
                            # Calculate area product & update 
                            # maximum if needed
                            area_product = max(area_product,
                                               (4*k + 1) * (4*w + 1))

                            # Try to extend 2nd plus 
                            w += 1

                # Try to extend 1st plus
                k += 1

            # After locating all possible pairs featuring 1st plus,
            # reset grid before searching for next 1st plus
            k = 0 
            while (grid[i][j - k] == '.' and
                   grid[i][j + k] == '.' and
                   grid[i - k][j] == '.' and
                   grid[i + k][j] == '.'):
                grid[i][j - k] = 'G'
                grid[i][j + k] = 'G'
                grid[i - k][j] = 'G'
                grid[i + k][j] = 'G'
                k += 1
    
    return area_product

               

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    grid = []
    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    print()
    result = twoPluses(grid)
    print('OUTPUT')
    print(result)



# https://www.hackerrank.com/challenges/two-pluses/problem
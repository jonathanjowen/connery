#!/bin/python3



def cavityMap(grid):
    
    depth_map = grid

    map_size = len(depth_map)
    
    cavity_map = depth_map
    for row, row_depths in enumerate(depth_map):
        if (row > 0) and (row < map_size - 1):
            for col in range(1, map_size - 1):
                current_depth = row_depths[col]
                edge_depths = list(
                    depth_map[row - 1][col] + 
                    row_depths[col - 1] + 
                    row_depths[col + 1] + 
                    depth_map[row + 1][col]
                )
                
                if current_depth > max(edge_depths):
                    cavity_map[row] = cavity_map[row][0:col] + \
                    cavity_map[row][col].replace(
                        str(current_depth), 'X', 1
                    ) + \
                   cavity_map[row][col + 1:] 

    return cavity_map


if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    
    print()
    result = cavityMap(grid)
    print('OUTPUT')
    for row in result:
        print(row)
    



# https://www.hackerrank.com/challenges/cavity-map/problem
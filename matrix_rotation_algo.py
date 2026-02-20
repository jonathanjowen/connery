#!/bin/python3



def matrixRotation(matrix, r):
    
    """
    Docstring for matrixRotation
    
    :param matrix: INTEGER_ARRAY   m rows of n integers where
                                   2 <= m, n <= 300 
                                   min(m, n) % 2 = 0
    :param r: INTEGER   # of anticlockwise rotations of matrix where 
                        1 <= r <= 10^9
    """
     
    # Map matrix rows & columns to locations based on ring & 
    # zero-based, clockwise index in ring
    # Example
    #                                   index
    #   A B C D                  0 1 2 3 4 5 6 7 8 9
    #   E F G H   --->   ring 0  A B C D H L K J I E
    #   I J K L               1  F G
    rings = {}
    rotated  = {}
    n_rings = min(m, n) // 2
    for k in range(n_rings):
        rings[k] = dict()
        rotated[k] = dict()
    matrix_to_rings = [] 
    for i in range(m):
        row = []
        for j in range(n):
            ring = min(min(i, m - i - 1), 
                       min(j, n - j - 1)) 
            ring_length = 2 * ((n - 2 * ring) +  (m - 2 - 2 * ring))
            if (i - ring == 0) or (j == n - ring - 1):
                idx_in_ring = (i - ring) + (j - ring)
            else:
                idx_in_ring = ring_length - (i - ring) - (j - ring)
            row.append((ring, idx_in_ring))
            # Store values for lookup by ring & index
            rings[ring][idx_in_ring] = matrix[i][j]
        matrix_to_rings.append(row)
        
    # Rotate rings, move values to new indices after rotation
    for ring in range(n_rings):
        for k in rings[ring].keys():
            ring_length = 2 * ((n - 2 * ring) +  (m - 2 - 2 * ring))
            # Only rotations after last complete cycle are relevant
            # Example  2, 7, & 12 rotations all map ABCDE --> CDEAB
            moves = r % ring_length
            rotated_k = (k - moves) % ring_length
            rotated[ring][rotated_k] = rings[ring][k]

    # Get value after rotation at ring & index for each row & column
    for i in range(m):
        row = []
        for j in range(n):
            ring = matrix_to_rings[i][j][0]
            idx_in_ring = matrix_to_rings[i][j][1]
            row.append(rotated[ring][idx_in_ring])
        print(*row)



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    print()
    matrixRotation(matrix, r)



# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
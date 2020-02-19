def parse_matrix_input():
    dimensions = input().strip().split()
    width = int(dimensions[0])
    height = int(dimensions[1])

    matrix = []
    for j in range(height):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    return matrix

def find_matrix_min(matrix):
    minimum = matrix[0][0]
    index = (0,0)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < minimum:
                minimum = matrix[row][col]
                index = (row, col)

    return [index, minimum]

def matrix_look_around(matrix, pos):

    row = pos[0]
    col = pos[1]

    N, E, S, W = None, None, None, None

    if row > 0:
        N = matrix[row-1][col]
    if col > 0:
        W = matrix[row][col-1]
    if row < len(matrix)-1:
        S = matrix[row+1][col]
    if col < len(matrix[0]-1):
        E = matrix[row][col+1]

    return [N, E, S, W]

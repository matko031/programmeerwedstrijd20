from useful_functions import *

number_test_cases = int(input())

for i in range(number_test_cases):
    print(i)
    matrix = parse_matrix_input()

    start = find_matrix_min(matrix)[0]

    N, E, S, W = matrix_look_around(matrix, start)


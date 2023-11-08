#!/usr/bin/python3
def square_matrix_simple(matrix):
    arr = []
    for i in matrix:
        mat = []
        for j in i:
            a = (j * j)
            mat.append(a)
        arr.append(mat)
    return arr

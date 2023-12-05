#!/usr/bin/python3
def primt_matric_Integer(matrix=[[]]):
    if not matrix:
        return None
    for submatrix in matrix:
        if len(submatrix) == 0:
            print()
        for i in range(len(submatrix)):
            print("{:d}".format(submatrix[i]),
                    end="\n" if i is len(submatrix) - 1 else " ")


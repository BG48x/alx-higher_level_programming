#!/usr/bin/python3
def primt_matric_Integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col). end=" " if col != row[-1] else "")
        print()

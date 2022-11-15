import numpy as numpy

visited = []


# def reduceMatrix(matrix, nodes):
#     sumR = 0
#     sumC = 0
#     for r in range(nodes):
#         minR = min(matrix[r])
#         sumR += int(minR)
#         for c in range(nodes):
#             if r != c:
#                 matrix[r][c] -= minR
#     return matrix


def readFromFile(file):
    file = open(file, "r")
    rows = file.read().splitlines()
    data = []
    for r in range(1, len(rows)):
        data.append(list(map(int, rows[r].split())))
    file.close()
    return data


def diagonalLine(data):
    for r in range(0, len(data)):
        for c in range(0, len(data)):
            if r == c: data[r][c] = -1
    return data


def printMatrix(data):
    for r in range(0, len(data)):
        print(data[r])


if __name__ == '__main__':

    file = "tsp_6_1.txt"
    matrix = diagonalLine(readFromFile(file))
    printMatrix(matrix)

import copy

import numpy as numpy

visited = []
n = 0


def readFromFile(file):
    file = open(file, "r")
    n = file.read().splitlines()
    data = []
    for r in range(1, len(n)):
        data.append(list(map(int, n[r].split())))
    file.close()
    return data


def diagonalLine(matrix):
    for r in range(len(matrix)):
        for c in range(0, len(matrix)):
            if r == c: matrix[r][c] = -1
    return matrix


def secondSmallest(list):
    return sorted(set(list))[1]


def listOfColumns(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        column = []
        for row in matrix:
            column.append(row[i])
        new_matrix.append(column)
    return new_matrix


def reduceMatrix(matrix):
    cost = 0
    for r in range(len(matrix)):
        minR = secondSmallest(matrix[r])
        if minR != 0:
            cost += minR
            for c in range(len(matrix)):
                if matrix[r][c] != -1: matrix[r][c] -= minR

    columns = listOfColumns(matrix)
    for c in range(len(matrix)):
        minC = secondSmallest(columns[c])
        if minC != 0:
            cost += minC
            for r in range(len(matrix)):
                if columns[c][r] != -1: columns[c][r] -= minC

    return listOfColumns(columns), cost


def printMatrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])


def BnB(matrix):
    upper = -1
    nodes = len(matrix)
    copy_of_matrix = copy.deepcopy(matrix)
    reduced_matrix = reduceMatrix(matrix)[0]
    cost = reduceMatrix(matrix)[1]

    for n in range(nodes):
        for p in range(nodes):
            if n != p:
                pass




if __name__ == '__main__':
    file = "tsp_6_1.txt"
    matrix = diagonalLine(readFromFile(file))
    for r in range(len(matrix)-1):
        print(matrix[r])
    print(" ")
    # printMatrix(listOfColumns(matrix))
    printMatrix(reduceMatrix(matrix))
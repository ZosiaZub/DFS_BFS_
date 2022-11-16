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


def infinity(matrix, row, column):
    for i in range(len(matrix)):
        matrix[row][i] = -1
        matrix[i][column] = -1

    matrix[row][column] = -1
    return matrix


def BnB(matrix):
    upper = -1
    start_node = 0
    nodes = len(matrix)
    main_matrix = copy.deepcopy(matrix)

    # lista zredukowanych macierzy dla każdego z wierzchłków
    reduced_matrix = [reduceMatrix(matrix)[0]]

    # lista kosztów dotarcia do danego wierzchołka
    cost_of_nodes = [reduceMatrix(matrix)[1]]

    for n in range(1, nodes):
        reduced_matrix.append(infinity(copy.deepcopy(reduced_matrix[start_node]), start_node, n))

        # koszt dotarcia do poprzedniego wierzchołka
        a = cost_of_nodes[start_node]

        # koszt ścieżki od poprzedniego do aktualnego wierzchołka z aktualnej macierzy kosztów
        b = 0

        # suma powstała ze zredukowania aktualnej macierzy kosztów
        c = 0

    return reduced_matrix[0], cost_of_nodes




if __name__ == '__main__':
    file = "tsp_6_1.txt"
    matrix = diagonalLine(readFromFile(file))
    for r in range(len(matrix)-1):
        print(matrix[r])
    print(" ")
    # printMatrix(listOfColumns(matrix))
    # printMatrix(reduceMatrix(matrix))
    # printMatrix(BnB(matrix))
    # print(BnB(matrix))
import copy

import numpy as numpy

# to nic nie robi, potrzebuję zrobić commita jeszcze raz tego samego, ale z poprawna nazwą
x = 0

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
    s = sorted(set(list))
    if s == [-1]:
        return -1
    else:
        return s[1]


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
    m = copy.deepcopy(matrix)
    for row in range(len(m)):
        minR = secondSmallest(m[row])
        if minR != -1 and minR != 0:
            cost += minR
            for c in range(len(m[row])):
                if m[row][c] != -1:
                    m[row][c] -= minR

    columns = listOfColumns(m)
    for col in range(len(m)):
        minC = secondSmallest(columns[col])
        if minC != -1 and minC != 0:
            cost += minC
            for r in range(len(m)):
                if columns[col][r] != -1:
                    columns[col][r] -= minC

    return listOfColumns(columns), cost


# -1 w danym wierszu i danej kolumnie oraz w komórce dla ścieżki odwrotnej
def infinity(matrix, row, column):
    for i in matrix:
        matrix[row][matrix.index(i)] = -1
        i[column] = -1

    matrix[column][row] = -1
    return matrix


def BnB(matrix):
    upper = -1
    start_node = 0
    nodes = len(matrix)
    main_matrix = copy.deepcopy(matrix)

    # lista zredukowanych macierzy dla każdego z wierzchłków
    reduced_matrix, cost_of_node = reduceMatrix(main_matrix)
    reduced_matrices = []
    reduced_matrices.append(reduced_matrix)
    cost_of_nodes = []
    cost_of_nodes.append(cost_of_node)
    # lista kosztów dotarcia do danego wierzchołka

    for n in range(1, nodes):
        copied_matrix = []
        # zczytanie zredukowanej kopii poprzedniej macierzy i kosztu tej akcji
        copied_matrix = copy.deepcopy(reduced_matrices[0])
        inf_matrix = infinity(copied_matrix, 0, n)
        rm, cost = reduceMatrix(inf_matrix)

        # dodanie aktualnej, zredukowanej macierzy do listy
        # reduced_matrix.append(reduceMatrix(infinity(copy.deepcopy(reduced_matrix[start_node]), start_node, n))[0])
        reduced_matrices.append(rm)

        # koszt dotarcia do poprzedniego wierzchołka
        a = cost_of_nodes[start_node]

        # koszt ścieżki od poprzedniego do aktualnego wierzchołka z poprzedniej macierzy kosztów
        b = reduced_matrices[start_node][start_node][n]

        # suma powstała ze zredukowania aktualnej macierzy kosztów
        c = cost

        suma = a + b + c
        cost_of_nodes.append(suma)

    return reduced_matrices, cost_of_nodes


def printMatrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])


def writeToFile(list_of_matrices, list_of_costs, file):
    for m in list_of_matrices:
        index = list_of_matrices.index(m)
        file.write("macierz " + str(index) + "\n" )
        for r in m:
            file.write(str(r))
            file.write("\n")
        file.write(str(list_of_costs[index]))
        file.write("\n\n\n")


if __name__ == '__main__':
    file = "hindus.txt"
    # matrix = diagonalLine(readFromFile(file))
    matrix = readFromFile(file)
    start = 0
    # printMatrix(matrix)
    # print(" ")
    # printMatrix(BnB(matrix))
    file = open("wyniki.txt", "w")

    # file.write("macierz glowna\n")
    # writeToFile(matrix, str(0), file)

    rum, co = BnB(matrix)
    writeToFile(rum, co, file)

    # main_matrix = reduceMatrix(copy.deepcopy(matrix))
    # # printMatrix(reduceMatrix(infinity(main_matrix, 0, 2)))
    # printMatrix(infinity(main_matrix, 0, 2))
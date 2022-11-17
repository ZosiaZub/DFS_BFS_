import copy

import numpy as numpy


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


def infinity(matrix, row, column, path):
    for i in matrix:
        matrix[row][matrix.index(i)] = -1
        i[column] = -1

    matrix[column][row] = -1
    return matrix


def nonVisitedList(nodes):
    list = []
    for i in range(nodes):
        list.append(i)
    return list


def findIndex(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return i


def reductionAndSumPerNode(matrix, n, start_node, start_cost, path):
    # zczytanie zredukowanej kopii poprzedniej macierzy i kosztu tej akcji
    copied_matrix = copy.deepcopy(matrix)
    inf_matrix = infinity(copied_matrix, 0, n, path)
    rm, cost = reduceMatrix(inf_matrix)

    # koszt dotarcia do poprzedniego wierzchołka
    a = start_cost

    # koszt ścieżki od poprzedniego do aktualnego wierzchołka z poprzedniej macierzy kosztów
    b = matrix[start_node][n]

    # suma powstała ze zredukowania aktualnej macierzy kosztów
    c = cost

    suma = a + b + c

    return rm, suma


# def choosingPath(first_matrix, start_node, start_cost, non_visited):
#     upper = start_cost
#     path = [0]
#     # costs_of_nodes = copy.deepcopy(cs_list)
#     # reduced_matrices = copy.deepcopy(rms_list)
#     while non_visited > 0:
#         costs_of_nodes = []
#         reduced_matrices = []
#         for n in non_visited:
#             p = copy.deepcopy(path)
#             rm, suma = reductionAndSumPerNode(first_matrix, n, start_node, start_cost, p)
#             reduced_matrices.append(rm)
#             costs_of_nodes.append(suma)
#         id = costs_of_nodes.index(min(costs_of_nodes))
#         path.append(id)
#     return reduced_matrices[id], costs_of_nodes[id], id, path


def choosingPath(first_matrix, start_node, start_cost):
    upper = start_cost
    non_visited = nonVisitedList(len(first_matrix))
    non_visited.pop(start_node)
    path = [0]
    # costs_of_nodes = copy.deepcopy(cs_list)
    # reduced_matrices = copy.deepcopy(rms_list)
    costs_of_nodes = []
    reduced_matrices = []
    while len(non_visited) > 0:
        costs_of_nodes.clear()
        reduced_matrices.clear()
        for n in non_visited:
            p = copy.deepcopy(path)
            rm, suma = reductionAndSumPerNode(first_matrix, n, start_node, start_cost, p)
            reduced_matrices.append(rm)
            costs_of_nodes.append(suma)
        idx = costs_of_nodes.index(min(costs_of_nodes))
        first_matrix = reduced_matrices[idx]
        start_node = non_visited[idx]
        start_cost = costs_of_nodes[idx]
        path.append(non_visited[idx])
        non_visited.pop(idx)
    upper = min(costs_of_nodes)

    return path, upper


def BnB(matrix):
    list_of_nodes = nonVisitedList(len(matrix))
    nodes = len(matrix)
    main_matrix = copy.deepcopy(matrix)
    reduced_matrix, cost_of_node = reduceMatrix(main_matrix)
    # lista zredukowanych macierzy dla każdego z wierzchłków
    # reduced_matrices = []
    # reduced_matrices.append(reduced_matrix)
    #
    # # lista kosztów dotarcia do danego wierzchołka
    # costs_of_nodes = []
    # costs_of_nodes.append(cost_of_node)
    start_node = 0
    path, minimal_cost = choosingPath(reduced_matrix, start_node, cost_of_node)

    return reduced_matrix, cost_of_node, path, minimal_cost


# def BnB(matrix):
#     list_of_nodes = visitedList(len(matrix))
#     nodes = len(matrix)
#     main_matrix = copy.deepcopy(matrix)
#     reduced_matrix, cost_of_node = reduceMatrix(main_matrix)
#     # lista zredukowanych macierzy dla każdego z wierzchłków
#     reduced_matrices = []
#     reduced_matrices.append(reduced_matrix)
#
#     # lista kosztów dotarcia do danego wierzchołka
#     costs_of_nodes = []
#     costs_of_nodes.append(cost_of_node)
#
#     non_visited = visitedList(len(matrix))
#
#     start_node = 0
#     non_visited.pop(start_node)
#
#     rm, c, id, path = choosingPath(reduced_matrices[start_node], start_node, costs_of_nodes[start_node], non_visited)
#     non_visited.pop(id)
#     reduced_matrices.append(rm)
#     costs_of_nodes.append(c)
#
#     rm1, c1, id1, path1 = choosingPath(reduced_matrices[1], start_node, costs_of_nodes[1], non_visited)
#     non_visited.pop(id1)
#     reduced_matrices.append(rm1)
#     costs_of_nodes.append(c1)
#
#     return reduced_matrices, costs_of_nodes


def printMatrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])


def writeMatrixToFile(list_of_matrices, list_of_costs, file):
    for m in list_of_matrices:
        index = list_of_matrices.index(m)
        file.write("_______________________MACIERZ " + str(index) + "\n" )
        for r in m:
            file.write(str(r))
            file.write("\n")
        file.write(str(list_of_costs[index]))
        file.write("\n\n")


def writeAnswerToFile(path, cost, file):
    file.write(str(path))
    file.write("\n")
    file.write(str(cost))


if __name__ == '__main__':
    file = "hindus.txt"
    matrix = readFromFile(file)
    file = open("wyniki.txt", "w")

    rm, c, path, minimal_cost = BnB(matrix)
    # writeMatrixToFile(rm, c, file)
    writeAnswerToFile(path, minimal_cost, file)

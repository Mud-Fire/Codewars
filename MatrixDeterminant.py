from copy import deepcopy


def determinant(matrix):
    # your code here
    if len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        result = 0
        for i in range(len(matrix[0])):
            a = matrix[0][i] * ((-1) ** (i % 2))
            b = deepcopy(matrix[1:len(matrix[0])])
            for j in b:
                j.pop(i)
            result += a * determinant(b)
        return result


m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
print(determinant(m2))

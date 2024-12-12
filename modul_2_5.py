def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append ([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result_matrix1 = get_matrix(10, 10, 75)
result_matrix2 = get_matrix(2, 5, 7)
result_matrix3 = get_matrix(1, 9, 36)
print(result_matrix1)
print(result_matrix2)
print(result_matrix3)

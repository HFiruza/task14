# def get_matrix (n, m, value):
#     matrix = []
#     for i in range(n):
#         matrix.append([]) # добавляем список
#         for j in range(m):
#             matrix[i].append(value) # Пишем в список значение
#     print(matrix)
# get_matrix(2, 2, 10)
#
# # [[10, 10], [10, 10]]

def get_matrix(n,m,value):
    matrix = []
    for i in range(0, n):
        matrix_1 = []
        for j in range(0, m):
            matrix_1.append(value)
        matrix.append(matrix_1)
    return matrix



result_1 = get_matrix(2,2,10)
result_2 = get_matrix(3,5, 42)
result_3 = get_matrix(4, 2, 13)
print(result_1)
print(result_2)
print(result_3)

# def get_matrix(n, m, value):
#     matrix = []
#     for a in range(0, n):
#         mat1 = []
#         for b in range(0, m):
#             mat1.append(value)
#         matrix.append(mat1)
#     return matrix





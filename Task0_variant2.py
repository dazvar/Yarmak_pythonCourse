import random

rows = 3
cols = 4

# matrix = [
#     [1, 2, 3, 5],
#     [4, 5, 6, 2],
#     [7, 8, 9, 6]
# ]

matrix = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

print(' ')

cols_without_zero = cols

for rows in matrix:
    print(rows)

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[j][i] == 0:
            cols_without_zero -= 1
            break

print('cols without zero= ', cols_without_zero)
print(' ')

summa = 0
characteristics = []

for i in range(len(matrix)):
    summa = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] > 0 or matrix[i][j] == 0:
            summa += matrix[i][j]
    print(summa)
    characteristics.append(summa)
print(' ')

for i in range(len(characteristics)):
    for j in range(i + 1, len(characteristics)):
        if characteristics[i] > characteristics[j]:
            matrix[j], matrix[i] = matrix[i], matrix[j]
            characteristics[j], characteristics[i] = characteristics[i], characteristics[j]

for row in matrix:
    print(row)
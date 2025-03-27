import random

from Tools.scripts.summarize_stats import print_title

rows = 3
cols = 4

matrix = [
    [-330, -45, -129, -1],
    [-220, -90, -190, -100],
    [-115, -65, -115, 6]
]

#matrix = [[random.randint(-3, 3) for _ in range(cols)] for _ in range(rows)]

print(' ')

for i in range(len(matrix)):
        print (matrix[i])

for i in range(len(matrix)):
    quantity = 0
    examination = 0
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            quantity += 1
        elif matrix[i][j] == 0:
            examination += 1
    if examination > 0 and quantity > 0:
        print('row', i, '=', quantity)

saddle_points = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):

        coefficient = matrix[i][j]
        min_point = 0
        max_point = 0

        for si in range(i, i + 1):
            for sj in range(len(matrix[si])):
                if coefficient <= matrix[si][sj]:
                    min_point += 1

        for ti in range(len(matrix)):
            for tj in range(j, j + 1):
                if coefficient >= matrix[ti][tj]:
                    max_point += 1

        if min_point == cols and max_point == rows:
            saddle_points.append ([i, j])

print(saddle_points)
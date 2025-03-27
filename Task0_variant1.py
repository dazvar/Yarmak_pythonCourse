import random

rows = 3
cols = 4

matrix = [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]

for rows in matrix:
    print(rows)

print(' ')

rows_without_zero = 0

for i in matrix:
    x = 0
    for j in i:
        if j != 0:
            x += 1
            if x == cols:
                rows_without_zero += 1

print('rows without zero= ', rows_without_zero)

numbers = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        number = matrix[i][j]
        place = (i, j)
        found = False
        for si in range(len(matrix)):
            for sj in range(len(matrix[si])):
                if (si, sj) != place and number == matrix[si][sj]:
                    if number not in numbers:
                        numbers.append(number)
                        found = True
                        break
            if found: break
print(numbers)

some = 0
MAX = 0

for i in range(len(numbers)):
    some = numbers[i]
    for j in range(len(numbers)):
        if some > numbers[j]:
            MAX = some
if MAX != 0:
    print(MAX)
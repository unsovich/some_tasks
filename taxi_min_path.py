"""
Дано поле в клеточку MxN, заполненное случайными числами, соответствующими времени движения.
Водитель находится в левом-верхнем углу и должен попасть в правый нижний.
Ходить он может либо на 1 клетку вниз, либо на 1 вправо.
Нужно перебрать все возможные маршруты и найти маршрут с наименьшей суммой.
"""
import random


def fill_grid(rows, cols, min_value, max_value):
    grid_to_fill = []
    for _ in range(rows):
        row = [random.randint(min_value, max_value) for _ in range(cols)]
        grid_to_fill.append(row)
    return grid_to_fill


def find_min_path(grid, i, j, M, N):
    if i == M - 1 and j == N - 1:  # если мы уже в конце маршрута
        return grid[i][j], [(i, j)]

    if i < M - 1 and j < N - 1:  # вниз или вправо?
        down_time, down_path = find_min_path(grid, i + 1, j, M, N)  # вниз
        right_time, right_path = find_min_path(grid, i, j + 1, M, N)  # вправо

        if down_time < right_time:  # наименьшее время движения
            return grid[i][j] + down_time, [(i, j)] + down_path
        else:
            return grid[i][j] + right_time, [(i, j)] + right_path

    elif i < M - 1:  # вниз
        down_time, down_path = find_min_path(grid, i + 1, j, M, N)
        return grid[i][j] + down_time, [(i, j)] + down_path

    elif j < N - 1:  # вправо
        right_time, right_path = find_min_path(grid, i, j + 1, M, N)
        return grid[i][j] + right_time, [(i, j)] + right_path


m, n = int(input()), int(input())
min_time, max_time = 1, 10  # границы для генерации времени
grid = fill_grid(m, n, min_time, max_time)  # заполняем матрицу

print('Матрица маршрутов:')
for i in range(m):
    for j in range(n):
        print(str(grid[i][j]).ljust(3), end='')
    print()

min_time, min_path = find_min_path(grid, 0, 0, m, n)
print("Минимальное время:", min_time)
print("Маршрут:", *min_path)

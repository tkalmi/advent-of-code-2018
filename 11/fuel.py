import math


def get_grid(serial):
    grid = []
    for x in range(1, 301):
        grid.append([])
        for y in range(1, 301):
            cell = x + 10
            cell *= y
            cell += serial
            cell *= x + 10
            cell /= 100
            cell = int(str(int(cell))[-1])
            cell -= 5
            grid[x-1].append(cell)
    return grid


def get_largest_square(grid):
    largest = -math.inf
    largest_coord = (-1, -1)
    for x_start in range(0, 298):
        for y_start in range(0, 298):
            square = 0
            for x in range(x_start, x_start+3):
                for y in range(y_start, y_start+3):
                    square += grid[x][y]
            if square > largest:
                largest = square
                largest_coord = (x_start + 1, y_start + 1)
    print('Largest square starts at', largest_coord)


serial = 9445
grid = get_grid(serial)
get_largest_square(grid)

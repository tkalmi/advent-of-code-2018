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


lookup_table = [[0 for __ in range(0, 300)] for _ in range(0, 300)]
lookup_table_size = 0


def get_largest_square(grid, size):
    global lookup_table
    global lookup_table_size
    largest = -math.inf
    largest_coord = (-1, -1)
    for x_start in range(0, 301-size):
        for y_start in range(0, 301-size):
            square = lookup_table[x_start][y_start]
            for x in range(x_start+lookup_table_size, x_start+size):
                square += sum(grid[x][y_start:y_start+size])
            for y in range(y_start+lookup_table_size, y_start+size):
                for x in range(x_start, x_start+lookup_table_size):
                    square += grid[x][y]
            lookup_table[x_start][y_start] = square
            if square > largest:
                largest = square
                largest_coord = (x_start + 1, y_start + 1)
    lookup_table_size = size
    return (largest, largest_coord)


serial = 9445
grid = get_grid(serial)

largest = -math.inf
largest_grid = (-1, -1, -1)
for size in range(1, 301):
    (square, (square_x, square_y)) = get_largest_square(grid, size)
    if size is 3:
        print('Largest square of size 3x3 starts at',
              (square_x, square_y), 'Amount of fuel:', square)
    if square > largest:
        largest = square
        largest_grid = (square_x, square_y, size)
print('Largest grid of varying size is',
      largest_grid, 'Amount of fuel:', largest)

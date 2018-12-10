def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.replace(' velocity=<', '').strip('position=<>\n ').replace('>', ',').split(',')
               for x in content]
    content = [list(map(int, line)) for line in content]
    content = [(complex(line[0], line[1]), complex(line[2], line[3]))
               for line in content]
    return content


def move_second(points):
    new_points = []
    for (coord, velocity) in points:
        new_points.append((coord + velocity, velocity))
    return new_points


def get_coord_lims(stars):
    x_max = max(stars.keys())
    x_min = min(stars.keys())
    y_max = max(map(max, stars.values()))
    y_min = min(map(min, stars.values()))
    return ((x_min, x_max), (y_min, y_max))


def check_neighbors(x, y, stars, coord_lims):
    for x_coord in range(x-1, x+2):
        if x_coord in stars.keys():
            for y_coord in range(y-1, y+2):
                if x_coord == x and y_coord == y:
                    continue
                if y_coord in stars[x_coord]:
                    return True
    return False


def print_message(stars, coord_lims):
    ((x_min, x_max), (y_min, y_max)) = coord_lims
    for x in range(x_min, x_max+1):
        row = ''
        for y in range(y_min, y_max+1):
            row += '#' if x in stars and y in stars[x] else '.'
        print(row)


def check_message(points):
    ''' Message is valid if there's no stray points? '''
    stars = {}
    for (point, _) in points:
        if int(point.imag) in stars:
            stars[int(point.imag)].append(int(point.real))
        else:
            stars[int(point.imag)] = [int(point.real)]
    coord_lims = get_coord_lims(stars)
    for x in stars.keys():
        for y in stars[x]:
            if check_neighbors(x, y, stars, coord_lims) is False:
                return False
    print_message(stars, coord_lims)
    return True


def find_message(points):
    second = 0
    while True:
        if check_message(points) is True:
            break
        points = move_second(points)
        second += 1
    print('\nHad to wait for', second, 'seconds')


content = get_content('input.txt')
print('')
find_message(content)

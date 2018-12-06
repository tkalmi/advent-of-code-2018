import math


def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def parse_areas(content):
    areas = []
    for row in content:
        (area_x, area_y) = (int(coord) for coord in row.split(', '))
        area = (area_x, area_y)
        areas.append(area)
    return areas


def get_dist(point, area):
    return abs(point[0] - area[0]) + abs(point[1] - area[1])


def get_closest_area(point, areas):
    closest_area = ()
    closest_dist = math.inf
    duplicate = False
    for area in areas:
        dist = get_dist(point, area)
        if dist < closest_dist:
            closest_area = area
            closest_dist = dist
            duplicate = False
        elif dist is closest_dist:
            duplicate = True
    return closest_area if not duplicate else None


def get_limits(areas):
    x_min = math.inf
    y_min = math.inf
    x_max = 0
    y_max = 0
    for area in areas:
        if (area[0] < x_min):
            x_min = area[0]
        if (area[0] > x_max):
            x_max = area[0]
        if (area[1] < y_min):
            y_min = area[1]
        if (area[1] > y_max):
            y_max = area[1]
    return (x_min, x_max, y_min, y_max)


def get_areas(areas):
    closest_points = {}
    for area in areas:
        closest_points[area] = 0
    (x_min, x_max, y_min, y_max) = get_limits(areas)

    infinite_areas = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            closest_point = get_closest_area((x, y), areas)
            if closest_point:
                is_on_edge = x is x_max or x is x_min or y is x_max or y is y_min
                if is_on_edge:
                    infinite_areas.add(closest_point)
                closest_points[closest_point] = closest_points[closest_point] + 1
    for key in closest_points.keys():
        if key in infinite_areas:
            closest_points[key] = 0
    print('Largest area', max(closest_points.values()))


def find_safe_areas(areas):
    MAX_DIST = 10000
    (_, x_max, _, y_max) = get_limits(areas)
    safe_areas_count = 0
    for x in range(0, x_max + 1):
        for y in range(0, y_max + 1):
            sum = 0
            for area in areas:
                sum += get_dist((x, y), area)
            if sum < MAX_DIST:
                safe_areas_count += 1
    print('Safe areas', safe_areas_count)


content = get_content('input.txt')
areas = parse_areas(content)
get_areas(areas)
find_safe_areas(areas)

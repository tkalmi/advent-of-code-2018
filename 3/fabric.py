def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def get_overlap(content):
    used_area = {}
    ids_not_overlapping = []
    for line in content:
        (id, start_point, size) = line.replace(
            '@ ', '').replace(':', '').split(' ')
        (start_x, start_y) = (int(coord) for coord in start_point.split(','))
        (width, height) = (int(length) for length in size.split('x'))
        overlaps = False
        for x in range(start_x, start_x + width):
            if x not in used_area:
                used_area[x] = {}
            for y in range(start_y, start_y + height):
                if y in used_area[x]:
                    if used_area[x][y] in ids_not_overlapping:
                        ids_not_overlapping.remove(used_area[x][y])
                    used_area[x][y] = 'x'
                    overlaps = True
                else:
                    used_area[x][y] = id
        if not overlaps:
            ids_not_overlapping.append(id)
    count = 0
    for col in used_area.values():
        for val in col.values():
            if val is 'x':
                count += 1
    return (count, ids_not_overlapping[0])


content = get_content('input.txt')

(overlapping_square_inches, non_overlapping_id) = get_overlap(content)

print('Overlap', overlapping_square_inches, 'square inches')
print('Non overlapping id', non_overlapping_id)

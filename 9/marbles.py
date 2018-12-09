from llist import dllist


def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = content[0].split(' ')
    return (int(content[0]), int(content[-2]))


def get_prev(llist, el, times=1):
    for _ in range(times):
        el = llist.last if el.prev is None else el.prev
    return el


def get_next(llist, el, times=1):
    for _ in range(times):
        el = llist.first if el.next is None else el.next
    return el


def marble_game(player_count, marble_count):
    points = {}
    for player in range(1, player_count+1):
        points[player] = 0
    current_player = 0
    marbles = dllist([0])
    current_marble = marbles.first
    for marble in range(1, marble_count+1):
        current_player = current_player % player_count + 1
        if marble % 23 is 0:
            marble_to_delete = get_prev(marbles, current_marble, 7)
            points[current_player] += marble + marble_to_delete.value
            current_marble = get_next(marbles, marble_to_delete)
            marbles.remove(marble_to_delete)
        else:
            current_marble = get_next(marbles, current_marble, 2)
            current_marble = marbles.insert(marble, current_marble)
    print('Max points', max(points.values()))


(player_count, marble_count) = get_content('input.txt')
marble_game(player_count, marble_count)
print('Part 2 (= Part1 x 100)')
marble_game(player_count, marble_count * 100)

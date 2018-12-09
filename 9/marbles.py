def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = content[0].split(' ')
    return (int(content[0]), int(content[-2]))


def marble_game(player_count, marble_count):
    points = {}
    for player in range(1, player_count+1):
        points[player] = 0
    current_marble = 0
    marbles = [0]
    for marble in range(1, marble_count+1):
        current_player = (marble-1) % player_count + 1
        if marble % 23 is 0:
            points[current_player] += marble
            idx_to_delete = marbles.index(current_marble) - 7
            points[current_player] += marbles[idx_to_delete]
            del marbles[idx_to_delete]
            current_marble = marbles[idx_to_delete] if idx_to_delete >= 0 else marbles[idx_to_delete + 1]
        else:
            idx = (marbles.index(current_marble) + 2) % len(marbles)
            marbles = marbles[:idx] + [marble] + marbles[idx:]
            current_marble = marble
    print('Max points', max(points.values()))


(player_count, marble_count) = get_content('input.txt')
marble_game(player_count, marble_count)

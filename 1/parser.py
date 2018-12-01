def read_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def get_content_sum(content):
    freq = 0
    for x in content:
        freq += int(x)
    return freq


def find_collision(content):
    reached_freqs = [0]
    freq = 0
    while True:
        for x in content:
            freq += int(x)
            if (freq in reached_freqs):
                return freq
            reached_freqs.append(freq)


content = read_content('input.txt')

print('Combined frequency', get_content_sum(content))
print('First collision', find_collision(content))

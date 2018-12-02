def read_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def get_checksum(content):
    two_count = 0
    three_count = 0
    for str in content:
        chars = {}
        for char in str:
            chars[char] = chars[char] + 1 if char in chars else 1
        if 2 in chars.values():
            two_count += 1
        if 3 in chars.values():
            three_count += 1
    return two_count * three_count


content = read_content('input.txt')

print('Checksum', get_checksum(content))

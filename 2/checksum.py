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


def get_common_chars_in_almost_matching_ids(content):
    content_len = len(content)
    str_len = len(content[0])
    for i in range(content_len):
        for j in range(content_len - i):
            diff_count = 0
            common_chars = ''
            for c in range(str_len):
                if content[i][c] is not content[j][c]:
                    diff_count += 1
                else:
                    common_chars += content[i][c]
            if diff_count is 1:
                return common_chars


content = read_content('input.txt')

print('Checksum', get_checksum(content))
print('Common chars', get_common_chars_in_almost_matching_ids(content))

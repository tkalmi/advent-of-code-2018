def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = content[0].strip()
    return content


def remove_pairs(polymer):
    i = 0
    while i < len(polymer) - 1:
        if polymer[i].capitalize() == polymer[i+1].capitalize() and polymer[i] != polymer[i+1]:
            if len(polymer) is not i+2:
                polymer = polymer[:i] + polymer[i+2:]
            else:
                polymer = polymer[:i]
            i = max(i-2, -1)
        i += 1
    return polymer


def nuke(polymer, character):
    cap_char = character.capitalize()
    i = 0
    while i < len(polymer) - 1:
        if polymer[i].capitalize() == cap_char:
            if len(polymer) is not i + 1:
                polymer = polymer[:i] + polymer[i+1:]
            else:
                polymer = polymer[:i]
        else:
            i += 1
    return polymer


content = get_content('input.txt')
print('Polymer result length', len(remove_pairs(content)))

chars = 'abcdefghijklmnopqrstuvwxyz'

min_len = len(content)
min_char = ''
for char in chars:
    nuked_content = nuke(content, char)
    length = len(remove_pairs(nuked_content))
    if length < min_len:
        min_len = length
        min_char = char

print('Polymer result length after removing optimal char', min_len)

def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [int(x.strip()) for x in content[0].split(' ')]
    return content


def get_metadata(content):
    children_count = content[0]
    metadata_count = content[1]
    metadata = []
    child_content = content[2:]
    child_values = []
    for i in range(children_count):
        (child_metadata, child_content, child_value) = get_metadata(child_content)
        child_values.append(child_value)
        metadata += child_metadata
    own_metadata = child_content[:metadata_count]
    metadata += own_metadata
    if children_count is 0:
        return (metadata, child_content[metadata_count:], sum(metadata))
    value = 0
    for i in own_metadata:
        if i > 0 and i <= len(child_values):
            value += child_values[i-1]
    return (metadata, child_content[metadata_count:], value)


content = get_content('input.txt')
(metadata, _, value) = get_metadata(content)
print('Metadata sum', sum(metadata), 'root node value', value)

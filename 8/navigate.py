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
    for _ in range(children_count):
        (child_metadata, child_content) = get_metadata(child_content)
        metadata += child_metadata
    metadata += child_content[:metadata_count]
    return (metadata, child_content[metadata_count:])


content = get_content('input.txt')
(metadata, rest) = get_metadata(content)
print('Metadata sum', sum(metadata))

import pdb


def get_content(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


class Node:

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def remove_parent(self, parent):
        self.parents.remove(parent)


def get_tree(content):
    tree = {}
    for row in content:
        parent = row.replace('Step ', '')[0]
        child = row.replace(' can begin.', '')[-1]
        if parent not in tree.keys():
            node = Node(parent)
            tree[parent] = node
        if child not in tree.keys():
            node = Node(child)
            tree[child] = node
        tree[parent].add_child(child)
        tree[child].add_parent(parent)
    return tree


def traverse(tree):
    order = []
    while len(tree.keys()) > 0:
        sorted_keys = sorted(tree.keys())
        for key in sorted_keys:
            if len(tree[key].parents) is 0:
                order.append(key)
                for child in tree[key].children:
                    tree[child].remove_parent(key)
                tree.pop(key, None)
                break
    print('Order in which parts should be assembled', ''.join(order))


content = get_content('input.txt')
tree = get_tree(content)
traverse(tree)

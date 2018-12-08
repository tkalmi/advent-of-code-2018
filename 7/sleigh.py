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
    return order


class Elf:
    def __init__(self):
        self.working_on = None
        self.time_to_finish = 0


def traverse_time(tree):
    time = -1
    elves = [Elf(), Elf(), Elf(), Elf(), Elf()]
    worked_nodes = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while len(tree.keys()) > 0:
        time += 1
        for elf in elves:
            elf.time_to_finish = max(0, elf.time_to_finish - 1)
            if elf.time_to_finish is 0 and elf.working_on:
                node = elf.working_on
                for child in tree[node].children:
                    tree[child].remove_parent(node)
                worked_nodes.remove(node)
                elf.working_on = None
                tree.pop(node, None)

        sorted_keys = sorted(tree.keys())
        for key in sorted_keys:
            if key not in worked_nodes and len(worked_nodes) < 5 and len(tree[key].parents) is 0:
                worked_nodes.append(key)
                for elf in elves:
                    if not elf.working_on:
                        elf.working_on = key
                        elf.time_to_finish = 60 + alphabet.index(key) + 1
                        break
    print('Time taken to assemble', time)
    return time


content = get_content('input.txt')
tree = get_tree(content)
traverse(tree)
tree = get_tree(content)
traverse_time(tree)

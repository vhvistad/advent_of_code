from typing import ClassVar
import sys


class Node:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.children = []

def make_tree(string):
    root = None
    current_node = None
    name = ''
    for i, char in enumerate(string):
        if char == '(':
            if root is None:
                root = Node(name, None)
                current_node = root
            else:
                child = Node(name, current_node)
                current_node.children.append(child)
                current_node = child
            name = ''
        elif char == ' ':
            if string[i-1] != ')':
                child = Node(name, current_node)
                current_node.children.append(child)
            name = ''
        elif char == ')':
            if name != '':
                child = Node(name, current_node)
                current_node.children.append(child)
            current_node = current_node.parent
            name = ''
        else:
            name += char
    
    return root

def recursive_depth(node):
    prev_gen = 1
    if len(node.children) > 0:
        for child in node.children:
            candidate = recursive_depth(child)
            if candidate > prev_gen:
                prev_gen = candidate
        if node.name == 'Grinch':
            return prev_gen
        else:
            return prev_gen + 1
    else:
        return prev_gen


if __name__ == "__main__":
    file = 'knowit/2021/5/tree2.txt'
    with open(file, 'r') as f:
        string = f.readline()

    root = make_tree(string)
    sys.setrecursionlimit(10**6)
    print(recursive_depth(root) - 1)
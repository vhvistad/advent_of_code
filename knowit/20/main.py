class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def get_name(self):
        return self.name
    
    def add_child(self, name):
        child = Node(name)
        self.children.append(child)
    
    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return False
    
    def __repr__(self):
        return f'{self.name}'

def read_input(filename):
    with open('knowit/20/'+filename, 'r', encoding='UTF-8') as f:
        tree = []
        for line in f:
            tree.append(line.strip().split('🎄'))
    return tree

def create_tree(treelist):
    root = Node('Julenissen')
    for line in treelist:
        cur = root
        for elf in line[:-1]:
            next_node =  cur.get_child(elf)
            if next_node:
                cur = next_node
            else:
                print(f"Error, {elf} not found!")
        cur.add_child(line[-1])
    return root

def print_tree(node, level):
    print(' '*level, end='')
    print(node)
    for child in node.children:
        # print('  ', end='')
        print_tree(child, level+1)

def count_nodes(node):
    workers, admin = 0, 0
    if len(node.children) == 0:
        return workers+1, admin
    else:
        for child in node.children:
            ret1, ret2 = count_nodes(child)
            workers += ret1
            admin += ret2
    return workers, admin+1

if __name__ == "__main__":
    treelist = read_input('test.txt')
    treelist = sorted(treelist, key=len)
    root = create_tree(treelist)
    workers, admin = count_nodes(root)
    print(f'Workers: {workers}, Admin: {admin}')
    
    # print_tree(root, 0)
    # print('t'*5)
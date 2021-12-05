file = 'knowit/2021/5/tree.txt'

with open(file, 'r') as f:
    tree = f.readline()

level = 0
max_level = 0
grinch_depth = None
skipped_levels = []
for i, char in enumerate(tree):
    if char == '(':
        pass
    elif char == ')':
        pass
print(max_level)
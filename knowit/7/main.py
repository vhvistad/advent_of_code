def read_forest(file):
  matrix = []
  width = 0
  with open(file, 'r') as f:
    for line in f:
      if line[-1] == '\n':
        line = line[:-1]
      matrix.append(list(line))
      if len(line) > width:
        width = len(line)
  for x in range(len(matrix)):
    if len(matrix[x]) < width:
      diff = width - len(matrix[x])
      for d in range(diff):
        matrix[x].append(' ')
  return matrix

def transpose(matrix):
  transposed = []
  for i in range(len(matrix[0])):
    transposed.append([])
  for j in range(len(matrix)):
    for i in range(len(matrix[0])):
      transposed[i].append(matrix[j][i])
  return transposed

def print_forest(matrix):
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      print(matrix[x][y], end='')
    print()

def split_trees(matrix):
  trees = []
  tree = []
  for line in matrix:
    if '#' in line:
      tree.append(line)
    elif len(tree) > 0:
      trees.append(tree)
      tree = []
  return trees

def mirror_tree(tree):
  mirr = tree.copy()
  for i in range(len(tree)//2):
    j = len(tree) - i - 1
    mirr[i], mirr[j] = mirr[j], mirr[i]
  return mirr

if __name__ == "__main__":
  m = read_forest('knowit/7/forest.txt')
  m = transpose(m)
  trees = split_trees(m)
  not_symmetric = 0
  for tree in trees:
    mirrored = mirror_tree(tree)
    for line in range(len(tree)):
      if tree[line] != mirrored[line]:
        not_symmetric += 1
        break
  symmetric = len(trees) - not_symmetric
  print(f'Result: {symmetric}')
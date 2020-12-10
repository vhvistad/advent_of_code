def symmetric(line, stem):
  n, d = 0, 0
  while n < 2:
    d += 1
    # print(f'L={line[stem-d]}, R={line[stem+d]}')
    if line[stem-d] != line[stem+d]:
      return False
    if line[stem-d] == ' ' and line[stem+d] == ' ':
      n += 1
    else:
      n = 0
  return True

def read_trees(file):
  with open(file, 'r') as f:
    forest = []
    for line in f:
      forest.append('  ' + line + '  ')
    forest.reverse()
    
    length = len(forest[1]) + 10
    for x in range(len(forest)):
      diff = length - len(forest[x])
      for i in range(diff):
        forest[x] = forest[x] + ' '

    empty_line = ''
    for e in range(len(forest[1])):
      empty_line = empty_line + ' '
    forest.append('  ' + empty_line + '  ')
    # print(forest[-2])
  return forest

def find_stems(forest):
  stems_index = []
  i = 0
  for char in forest[1]:
    if char == '#':
      stems_index.append(i)
    i += 1
  return stems_index



if __name__ == "__main__":
  forest = read_trees('knowit/7/test2.txt')
  stems = find_stems(forest)
  symmetric_trees = 0
  # for line in forest:
  #   print(line)
  line_no = 0
  for line in forest[1:]:
    line_no+=1
    # print(f'i = {i}')
    # for stem in stems:
    i = 0
    while i < len(stems):
      stem = stems[i]
      if not symmetric(line, stem):
        # print(f'Not symmetric, remove: {stem}')
        stems.remove(stem)
        i -= 1
      if line[stem] == ' ' and stem in stems:
        # print(f'Remove: {stem}')
        symmetric_trees += 1
        stems.remove(stem)
        i -= 1
      i += 1
    # i = 0
    # while i < len(stems):
    #   stem = stems[i]

      
      # print(f'Line {line_no} --- Stems: {len(stems)} --- Symmetric: {symmetric_trees}')
  print(f'Result: {symmetric_trees}')


  test = '     ###               #######               ####              #######  '
  print(symmetric(test, 48))
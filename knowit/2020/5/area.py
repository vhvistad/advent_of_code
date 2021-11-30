def dimensions(dir_str):
  x_min, x_max, y_min, y_max = 0, 0, 0, 0
  x, y = 0, 0
  for letter in dir_str:
    if letter == 'H':
      x += 1
    elif letter == 'V':
      x -= 1
    elif letter == 'O':
      y += 1
    elif letter == 'N':
      y -= 1 

    if x > x_max:
      x_max += 1
    elif x < x_min:
      x_min -= 1
    elif y > y_max:
      y_max += 1
    elif y < y_min:
      y_min -= 1
  width = x_max - x_min + 3
  height = y_max - y_min + 3
  start = (abs(x_min)+1, abs(y_min)+1)
  return width, height, start

def make_matrix(width, height):
  matrix = []
  for x in range(width):
    column = []
    for y in range(height):
      column.append(None)
    matrix.append(column)
  return matrix

def turn_direction(prev, next_dir):
  direction = prev + next_dir
  right = ['HN', 'NV', 'VO', 'OH']
  if direction in right:
    return 'right'
  else:
    return 'left'

def translate(prev, next_dir):
  vectors = {
    'H': (1,0),
    'V': (-1,0),
    'O': (0, 1),
    'N': (0, -1)
  }
  if next_dir == prev:
    right_dir = vectors[next_dir]
    left_dir = vectors[next_dir]
  elif turn_direction(prev, next_dir) == 'right':
    left_dir = (vectors[prev][0] + vectors[next_dir][0], vectors[prev][1] + vectors[next_dir][1])
    right_dir = (0,0)
  elif turn_direction(prev, next_dir) == 'left':
    right_dir = (vectors[prev][0] + vectors[next_dir][0], vectors[prev][1] + vectors[next_dir][1])
    left_dir = (0,0)
  return right_dir, left_dir

def draw(dir_str, matrix, start_pos):
  init = {
    'H': (0, 1),
    'V': (0, -1),
    'O': (-1, 0),
    'N': (1, 0)
  }
  print_matrix(matrix)
  prev = dir_str[0]
  right_x = start_pos[0]
  right_y = start_pos[1]
  matrix[right_x][right_y] = 'right'
  left_x = right_x + init[dir_str[0]][0] # Get x-position of first left cell
  left_y = right_y + init[dir_str[0]][1] # Get y-position of first left cell
  matrix[left_x][left_y] = 'left'
  print_matrix(matrix)
  for next_dir in dir_str[1:]:
    right_dir, left_dir = translate(prev, next_dir)
    right_x += right_dir[0]
    right_y += right_dir[1]
    left_x += left_dir[0]
    left_y += left_dir[1]
    matrix[right_x][right_y] = 'right'
    matrix[left_x][left_y] = 'left'
    prev = next_dir
    print_matrix(matrix)
  return matrix

def find_area(matrix):
  area = 0
  for x in range(len(matrix)):
    outside_type = None
    inside = False
    for y in range(len(matrix[x])):
      cell = matrix[x][y]
      if outside_type is None and cell is not None:
        if cell == 'right':
          outside_type = 'right'
        else:
          outside_type = 'left'
      if not inside and cell is not outside_type and cell is not None:
        inside = True
      if inside and cell is outside_type:
        inside = False
      if inside:
        area += 1
  return area

def print_matrix(matrix):
  if not PRINT_ALLOWED:
    return
  for y in reversed(range(len(matrix[0]))):
    for x in range(len(matrix)):
      cell = matrix[x][y]
      if cell == 'right':
        print(' + ', end='')
      elif cell == 'left':
        print(' # ', end='')
      else:
        print(' . ', end='')
    print()
  print()

def main(dir_str):
  size = dimensions(dir_str)
  matrix = make_matrix(size[0], size[1])
  matrix = draw(dir_str, matrix, size[2])
  return find_area(matrix)

PRINT_ALLOWED = False

if __name__ == "__main__":
  with open('knowit/5/rute.txt', 'r') as f:
    line = f.read()
  area = main(line)
  print(area)
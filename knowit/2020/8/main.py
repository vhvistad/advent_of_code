def read_input(file):
  with open(file, 'r') as f:
    locations = {}
    route = []
    for line in f:
      if ':' in line:
        line = line.strip().split(': ')
        locations[line[0]] = list(int(x) for x in line[1][1:-1].split(', '))
      else:
        route.append(line.strip())
  return locations, route

def get_matrix(locations):
  x_max = 0
  y_max = 0
  for loc in locations.values():
    if loc[0] > x_max:
      x_max = loc[0]
    if loc[1] > y_max:
      y_max = loc[1]
  matrix = [[0.0 for y in range(y_max+1)] for x in range(x_max+1)]
  return matrix

def distance(a, b):
  return abs(a[0]-b[0]) + abs(a[1]-b[1])

def tick(pos, matrix):
  for x in range(len(matrix)):
    for y in range(len(matrix[x])):
      d = distance(pos, (x,y))
      if d < 5:
        matrix[x][y] += 0.25
      elif d < 20:
        matrix[x][y] += 0.5
      elif d < 50:
        matrix[x][y] += 0.75
      else:
        matrix[x][y] += 1.0
  return matrix

def travel(pos, dest, matrix):
  while pos != dest:
    if pos[0] < dest[0]:
      pos[0] += 1
    elif pos[0] > dest[0]:
      pos[0] -= 1
    elif pos[1] < dest[1]:
      pos[1] += 1
    elif pos[1] > dest[1]:
      pos[1] -= 1
    matrix = tick(pos, matrix)
  return matrix

def max_difference(locations, matrix):
  max_diff = 0.0
  locations = locations.values()
  for i in locations[:-1]:
    j_start = locations.index(i) + 1
    for j in locations[j_start:]:
      a = matrix[i[0]][i[1]]
      b = matrix[j[0]][j[1]]
      if abs(a-b) > max_diff:
        max_diff = abs(a-b)
  return max_diff

def main(locations, route):
  matrix = get_matrix(locations)
  pos = [0,0]
  for visit in route:
    print(f'Traveling to {visit}...')
    dest = locations[visit]
    matrix = travel(pos, dest, matrix)
    pos = dest
  max_diff = max_difference(locations, matrix)
  return max_diff

if __name__ == "__main__":
  file = 'knowit/8/input.txt'
  locations, route = read_input(file)
  result = main(locations, route)
  print(f'Result: {result}')

import time

def read_input(file):
  with open(file, 'r') as f:
    locations = {}
    route = []
    for line in f:
      if ':' in line:
        line = line.strip().split(': ')
        locations[line[0]] = [list(int(x) for x in line[1][1:-1].split(', ')), 0]
      else:
        route.append(line.strip())
  return locations, route

def distance(a, b):
  return abs(a[0]-b[0]) + abs(a[1]-b[1])

def tick(pos, matrix):
  for loc in locations:
    if locations[loc][0] == pos:
      continue
    d = distance(pos, locations[loc][0])
    if d < 5:
      locations[loc][1] += 0.25
    elif d < 20:
      locations[loc][1] += 0.5
    elif d < 50:
      locations[loc][1] += 0.75
    else:
      locations[loc][1] += 1.0
  return locations

def travel(pos, dest, locations):
  while pos != dest:
    if pos[0] < dest[0]:
      pos[0] += 1
    elif pos[0] > dest[0]:
      pos[0] -= 1
    elif pos[1] < dest[1]:
      pos[1] += 1
    elif pos[1] > dest[1]:
      pos[1] -= 1
    locations = tick(pos, locations)
  return locations 

def max_difference(locations):
  max_diff = 0.0
  locations = list(locations.values())
  for i in locations[:-1]:
    j_start = locations.index(i) + 1
    for j in locations[j_start:]:
      diff = abs(i[1] - j[1])
      if diff > max_diff:
        max_diff = diff
  return max_diff

def main(locations, route):
  pos = [0,0]
  for visit in route:
    print(f'Traveling to {visit}...')
    dest = locations[visit][0].copy()
    locations = travel(pos, dest, locations)
    pos = dest
  max_diff = max_difference(locations)
  return max_diff

if __name__ == "__main__":
  start_time = time.time()
  file = 'knowit/8/input.txt'
  locations, route = read_input(file)
  result = main(locations, route)
  print(f'Result: {result}')
  print("--- %s seconds ---" % (time.time() - start_time))
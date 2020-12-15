import time
from copy import deepcopy

def read_input(file):
  with open(file, 'r') as f:
    # line = f.readline().strip()
    # width = len(line) + 2
    elves = []
    # elves.append()
    for line in f:
      line = line.strip()
      row = [None]
      for elf in line:
        row.append(elf)
      row.append(None)
      elves.append(row)
    width = len(line) + 2
    elves.insert(0, [None]*width)
    end  =[None] * width
    elves.append(end)
    
    # lines = f.read().split('\n')
  return elves

def print_elves(elves):
  for line in elves:
    print(line)

def infected(x, y, lines):
  infected_neighbors = 0
  neighbors = [
    lines[x+1][y],
    lines[x-1][y],
    lines[x][y+1],
    lines[x][y-1]
  ]
  for n in neighbors:
    if n == "S":
      infected_neighbors += 1
  return infected_neighbors >= 2

def update(elves):
  # stopped = True
  new_elves = deepcopy(elves)
  new_inf = 0
  for x in range(1, len(elves) - 1):
    for y in range(1, len(elves[x]) - 1):
      if infected(y, x, elves) and elves[y][x] == 'F':
        new_elves[y][x] = 'S'
        new_inf += 1
        # stopped = False
  print(f'Newly infected = {new_inf}')
  return new_elves, new_inf


if __name__ == "__main__":
  file = 'knowit/9/elves.txt'
  lines = read_input(file)
  print('--- Start ---')
  # print_elves(lines)
  # print()
  days = 0
  new_inf = 1
  while new_inf != 0:
    lines, new_inf = update(lines)
    # print_elves(lines)
    # print()
    days += 1
    # time.sleep(0.8)

  # print_elves(lines)
  print(f'Days: {days}')
  # x = 3
  # y = 1
  # print(lines[x][y])
  # inf = infected(x, y, lines)
  # print(inf)
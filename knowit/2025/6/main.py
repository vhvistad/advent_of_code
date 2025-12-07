import collections
from scipy.sparse import csr_array
from scipy.sparse.csgraph import dijkstra
import numpy as np

filepath = '/home/vegard/repos/advent_of_code/knowit/2025/6/perfeksjonsruten.txt'
test = '/home/vegard/repos/advent_of_code/knowit/2025/6/test.txt'

zones = []
starting_points = []
dimensions = []

wall, clear, goal = "#", ".", "*"

def bfs(grid, start, width, height):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

with open(filepath, 'r') as f:
    zone_grid = []
    y = 0
    x = 0
    found_start = False
    for line in f.readlines():
        row = line.strip()
        if row == ';':
            if found_start:
                zones.append(zone_grid)
                dimensions.append([width, y])
            zone_grid = []
            x = 0
            y = 0
            found_start = False
            continue

        width = len(row)
        for c in row:
            if c == 'S':
                starting_points.append([x, y])
                row = row.replace('S', '.')
                found_start = True
            x += 1
        zone_grid.append(row)
        x = 0
        y += 1
            
total = 0

for i, zone in enumerate(zones):
    start = tuple(starting_points[i])
    width, height = dimensions[i]

    print(f'i = {i}, width = {width}, height = {height}')
    path = bfs(zone, start, width, height)

    if path is not None:
        total += len(path) - 1


print(f'Result = {total}')
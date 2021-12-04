filename = "3/input.txt"
coords = []

f = open(filename, "r")
for line in f:
  l = list(line)
  if l[-1] == "\n":
    l.pop()
  coords.append(l)
f.close()

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
result = 1

for i in range(len(slopes)):
  x = 0
  y = 0
  trees = 0
  while y < len(coords) - slopes[i][1]:
    y += slopes[i][1]
    x += slopes[i][0]
    if x >= len(coords[y]):
      x = x - len(coords[y])
    if coords[y][x] == "#":
      trees += 1
  result *= trees
  print("Trees: {}, result = {}".format(str(trees), str(result)))

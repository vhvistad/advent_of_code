import turtle

# d = 100

# wn = turtle.Screen()
# wn.title("Turtle")
# t = turtle.Turtle()

# t.forward(d)

# turtle.done()

dir_translation = {
  'H': (1,0),
  'V': (-1,0),
  'O': (0,1),
  'N': (0,-1)
}
turns = {
  'HH': (1, 0, [0, 0, 0, 1]),
  'VV': (-1,0, [0, 1, 0, 0]),
  'OO': (0, 1, [0, 0, 1, 0]),
  'NN': (0,-1, [1, 0, 0, 0]),
  'HN': (0, 0, [1, 0, 0, 0]),
  'NV': (0, 0, [0, 1, 0, 0]),
  'VO': (0, 0, [0, 0, 1, 0]),
  'OH': (0, 0, [0, 0, 0, 1]),
  'OV': (-1, 1,[0, 1, 0, 0]),
  'VN': (-1,-1,[1, 0, 0, 0]),
  'NH': (1, -1,[0, 0, 0, 1]),
  'HO': (1, 1, [0, 0, 1, 0])
}

class Cell:
  def __init__(self):
    self.edges = [0, 0, 0, 0] # Edges: [Right, Bottom, Left, Top]
    self.top_edge = False
    self.bottom_edge = False
    self.start = False
    self.inside = False
  
  def update_edge(self, edge):
    if edge == 'top':
      self.top_edge = True
    elif edge == 'bottom':
      self.bottom_edge = True
    # edges = self.edges
    # for i in range(len(edges)):
    #   edges[i] = edges[i] + new[i]
    # self.edges = edges
  
  def change_side(self):
    self.inside = True

  def __repr__(self):
    if self.inside:
      return ' # '
    return ' . '

  def __str__(self):
    if self.inside:
      return ' # '
    return ' . '
  # def __repr__(self):
  #   if self.top_edge and not self.bottom_edge:
  #     return " - "
  #   elif self.bottom_edge and not self.top_edge:
  #     return ' _ '
  #   elif self.bottom_edge and self.top_edge:
  #     return ' = '
  #   return " . " 
  
  # def __str__(self):
  #   if self.top_edge and not self.bottom_edge:
  #     return " - "
  #   elif self.bottom_edge and not self.top_edge:
  #     return ' _ '
  #   elif self.bottom_edge and self.top_edge:
  #     return ' = '
  #   return " . " 
  
def area_size(string):
  x, y, x_min, x_max, y_min, y_max = 0, 0, 0, 0, 0, 0
  for direction in string:
    if direction == 'H':
      x += 1
      if x > x_max:
        x_max = x
    elif direction == 'V':
      x -= 1
      if x < x_min:
        x_min = x
    elif direction == 'O':
      y += 1
      if y > y_max:
        y_max = y
    elif direction == 'N':
      y -= 1
      if y < y_min:
        y_min = y
  return x_min, x_max, y_min, y_max

def translate(x, y, direction):
  turn = turns[direction]
  new_x = x + turn[0]
  new_y = y + turn[1]
  # edges = turn[2]
  return new_x, new_y

def draw(area, directions):
  start_cells = {
    'H': (2,1),
    'V': (1,2),
    'O': (2,2),
    'N': (1,1)
  }
  
  # start = start_cells[directions[0]]
  start = (250, 250)
  prev = directions[0]
  x, y = start[0], start[1]
  # edge = turns[prev+prev][2]
  for d in directions:
    x, y = translate(x, y, prev+d)
    # print(f'd={d}\nx={x}, y={y}')
    if d == "H":
      area[x][y+1].update_edge('bottom')
      # print(f'Bottom Edge: {area[x][y].bottom_edge}')
      area[x][y].update_edge('top')
    elif d == 'V':
      area[x][y].update_edge('bottom')
      area[x][y-1].update_edge('top')
    
    prev = d
    # print_area(area)
    # print()
  # area[x][y].update_edge(edge)
  return area

def scan(area):
  total = 0
  for x in range(len(area)):
    inside = False
    count = 0
    for y in range(len(area[x])):
      cell = area[x][y]
      if inside:
        count += 1
        area[x][y].change_side()
      if cell.top_edge:
        inside = not inside
      if not inside:
        total += count
        count = 0
      
  return total

def print_area(area):
  for y in reversed(range(len(area[0]))):
    for x in range(len(area)):
      print(area[x][y], end='')
    print()

def main(string):
  
  x_min, x_max, y_min, y_max = area_size(string)
  # height = y_max - y_min + 10
  # width = x_max - x_min + 10
  height = 500
  width = 500


  area = []
  for x in range(width):
    column = []
    for y in range(height):
      column.append(Cell())
    area.append(column)

  # print_area(area)
  area = draw(area, string)
  # print_area(area)
  size = scan(area)
  # print_area(area)
  return size
  # print(f'Width = {width}, height = {height}')


if __name__ == "__main__":
  with open('knowit/5/rute.txt') as f:
    line = f.read()
  # print(line)
  ex2 = 'HHHHHHOOOOVVNNNVVOVVNN' # 14
  ex3 = 'HHOVOHOVOHOVVNNNNN'
  ex4 = 'OOHOVVOHOVOHHHHHNNVOVVNHNNNNVV' # 15
  ex5 = 'OOHNHOHNNVVV' # 5
  ex6 = 'OVOHHNNV' # 3
  ex7 = 'VVNHNVNHHOOO'
  print(main(line))
  # print(len(line))
  # if 0:
  #   test = "Yes"
  # else:
  #   test = "No"
  # print(f'Test: {test}')
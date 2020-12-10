def search(string):
  column = None
  row = None
  upper = 127
  lower = 0
  # print("{}-{}".format(lower, upper))
  for direction in string[:-3]:
    # print(direction)
    if direction == "F":
      upper = lower + (upper - lower) // 2
    elif direction == "B":
      lower = lower + (upper - lower + 1) // 2
    # print("{}-{}".format(lower, upper))
  row = upper
  upper = 7
  lower = 0
  # print("{}-{}".format(lower, upper))
  for direction in string[-3:]:
    if direction == "L":
      upper = lower + (upper - lower) // 2
    elif direction == "R":
      lower = lower + (upper - lower + 1) // 2
    # print("{}-{}".format(lower, upper))
  column = upper
  s_id = row * 8 + column
  return row, column, s_id



if __name__ == "__main__":
  seats = []
  test = 'FFFFFFFRRR\n'
  for r in range(128):
    for c in range(8):
      seats.append(r*8+c)
  print(len(seats))
  with open('5/input.txt') as f:
    for line in f:
      if line == test:
        print("Found 7")
      seat = search(line.strip())[2]
      # print(seat)
      seats.remove(seat)
  print(seats)
  print(search(test))

  highest = 0
  with open('5/input.txt') as f:
    for line in f:
      sid = search(line.strip())[2]
      # print(sid > highest)
      if sid > highest:
        highest = sid

print("Highest: " + str(highest))
from os.path import dirname, abspath, join

filename = 'input.txt'
path = join(dirname(abspath(__file__)), filename)

course = []
with open(path, 'r') as f:
    for line in f:
        course.append(line.strip())

# Part 1
depth = 0
horizontal = 0

for command in course:
    direction, x = command.split(' ')
    x = int(x)
    if direction == 'forward':
        horizontal += x
    elif direction == 'down':
        depth += x
    elif direction == 'up':
        depth -= x

print(f'Part 1 Result: {depth*horizontal}')

# Part 2
depth = 0
horizontal = 0
aim = 0

for command in course:
    direction, x = command.split(' ')
    x = int(x)
    if direction == 'forward':
        horizontal += x
        depth += aim*x
    elif direction == 'down':
        aim += x
    elif direction == 'up':
        aim -= x

print(f'Part 2 Result: {depth*horizontal}')
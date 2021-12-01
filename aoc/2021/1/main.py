# Part 1
file = 'aoc/2021/1/input.txt'
result = 0

with open(file, 'r') as f:
    previous = int(f.readline().strip())
    f.seek(0)
    for line in f:
        current = int(line.strip())
        if current > previous:
            result += 1
        previous = current

print(f'Part 1: {result}')

# PART 2
readings = []
with open(file, 'r') as f:
    for reading in f:
        readings.append(int(reading.strip()))

result = 0
previous_sum = sum(readings[0:3])
for i in range(1, len(readings) - 2):
    window_sum = sum(readings[i:i+3])
    if window_sum > previous_sum:
        result += 1
    previous_sum = window_sum

print(f'Part 2: {result}')

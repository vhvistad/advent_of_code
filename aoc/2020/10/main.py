file = 'aoc/2020/10/input.txt'
numbers = []

with open(file) as f:
    for line in f:
        numbers.append(int(line.strip()))
        
numbers.append(0)
numbers.sort()
numbers.append(numbers[-1] + 3)

one_diff = 0
three_diff = 0

for i in range(0, len(numbers)-1):
    diff = numbers[i+1] - numbers[i]
    if diff == 1:
        one_diff += 1
    elif diff == 3:
        three_diff += 1

print(one_diff*three_diff)
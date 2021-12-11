filename = 'aoc/2021/3/test.txt'

# Part 1
with open(filename, 'r') as f:
    line_length = len(f.readline().strip())
    f.seek(0)
    num_lines = 0
    sum_list = [0]*line_length
    for line in f:
        for i, char in enumerate(line.strip()):
            sum_list[i] += int(char)
        num_lines += 1

gamma = ''
epsilon = ''
for bit in sum_list:
    if bit > num_lines/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(f'Result = {int(gamma, 2)*int(epsilon, 2)}')

# Part 2
numbers = []
with open(filename, 'r') as f:
    for line in f:
        numbers.append(line.strip())

result = numbers
i = 0
while len(numbers) > 1:
    number = numbers[0]
    for index, bit in enumerate(number):
        print(bit)
        if bit != gamma[index]:
            numbers.pop(0)
    i += 1

print(numbers)

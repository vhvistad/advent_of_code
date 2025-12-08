from sympy import *
j = [0, 1, 1]


numbers = []

with open('C:/Users/vvistad/repos/advent_of_code/knowit/2025/8/input.txt', 'r') as f:
    for line in f.readlines():
        num = [int(s) for s in line.strip().split(' ')]
        numbers.extend(num)

numbers.sort()

missing = []

for i in range(1,len(numbers)+1):
    if i != numbers[i-1]:
        missing.append(i)
        print(f'Missing: {i}')


# with open('C:/Users/vvistad/repos/advent_of_code/knowit/2025/8/sorted.txt', 'w') as f:
#     for n in numbers:
#         f.write(str(n)+'\n')

print(len(missing))




# count = 0

# for n in numbers:
#     while n > j[-1]:
#         j.append(j[-1] + 2*j[-2])
    
#     if n == j[-1] and isprime(n):
#         count += 1

# print(f'Result: {count}')
# print(isprime(171))
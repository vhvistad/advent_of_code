with open('input.txt', 'r') as f:
    left = []
    right = []
    for line in f.readlines():
        numbers = line.strip().split('   ')
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

left.sort()
right.sort()

diff = 0
for i, n in enumerate(left):
    m = right[i]
    diff += abs(n-m)

print(f'Answer part 1: {diff}')

sim_score = 0
for n in left:
    cnt = 0
    for m in right:
        if n == m:
            cnt += 1
    sim_score += n*cnt

print(f'Answer part 2: {sim_score}')

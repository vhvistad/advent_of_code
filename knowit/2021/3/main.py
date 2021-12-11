import time

start_time = time.time()
file = 'knowit/2021/3/input.txt'
with open(file, 'r') as f:
    children = f.readline()

neutral = []
for index in range(len(children)):
    good_or_bad = { 'J': 0, 'N': 0 }
    for size, child in enumerate(children[index:]):
        good_or_bad[child] += 1
        if good_or_bad['J'] == good_or_bad['N']:
            neighborhood = [size+1, index]
            neutral.append(neighborhood)

largest = [0,0]
for neighborhood in neutral:
    if neighborhood[0] > largest[0]:
        largest = neighborhood
    elif neighborhood[0] == largest[0] and neighborhood[1] < largest[1]:
        largest = neighborhood

print(f'Largest neighborhood: {largest}')
print("--- %s seconds ---" % (time.time() - start_time))

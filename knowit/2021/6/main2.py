file = 'knowit/2021/6/pakker.txt'
area = [0]*20
fallen = 0

with open(file, 'r') as f:
    for line in f:
        block = [int(s) for s in line.strip().split(',')]
        # First and last index of new block
        start = block[0]
        end = start + block[1]
        # Area below new block
        below_block = area[start:end]
        below_block_rev = [i for i in reversed(below_block)]
        # Top blocks below new block
        max_height = max(below_block)
        # "Weight": (length) of each side without support
        weight_1 = len(below_block[0:below_block.index(max_height)])
        weight_2 = len(below_block_rev[0:below_block_rev.index(max_height)])
        # Check if "weight" of either side is less than half of new block
        if weight_1 < len(below_block)/2 and weight_2 < len(below_block)/2:
            for i in range(start, end): # Add new block
                area[i] = max_height + 1
        else:
            fallen += 1

print(f'Fallen blocks = {fallen}')
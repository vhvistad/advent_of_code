def place_block_old(block, area):
    start = block[0]
    end = start + block[1]
    height = max(area[start:end])
    for i in range(start, end):
        area[i] = height + 1
    return area

def balanced(block, area):
    start = block[0]
    end = start + block[1]
    area = area[start:end]
    area_reversed = [i for i in reversed(area)]
    height = max(area)
    weight_1 = len(area[0:area.index(height)])
    weight_2 = len(area_reversed[0:area_reversed.index(height)])
    
    return weight_1 < len(area)/2 and weight_2 < len(area)/2

def place_block(block, area):
    start = block[0]
    end = start + block[1]
    height = max(area[start:end])
    for i in range(start, end):
        area[i] = height + 1
    return area
    
if __name__ == "__main__":
    file = 'knowit/2021/6/pakker.txt'
    blocks = []
    with open(file, 'r') as f:
        for line in f:
            blocks.append([int(s) for s in line.strip().split(',')])
            
    area = [0]*20
    fallen = 0
    for block in blocks:
        if balanced(block, area):
            area = place_block(block, area)
        else:
            fallen += 1
    print(f'Fallen blocks = {fallen}')
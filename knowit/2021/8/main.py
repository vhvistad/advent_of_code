import numpy as np

def correction(start, end):
    if start[0] > end[0]: # Direction: down
        start[0] += 1
        end[0] += 1
    if start[1] > end[1]: # Direction: left
        start[1] += 1
        end[1] += 1
    return start, end

def bl_tr(start, end):
    start, end = correction(start, end)
    bl = (min(start[0], end[0]), min(start[1], end[1]))
    tr = (max(start[0], end[0]), max(start[1], end[1]))
    return bl, tr

coords = np.zeros( (10, 10) )

start = (1, 1)
end = (6, 6)

coords[start[0]:end[0], start[1]:end[1]] += 1


print(np.rot90(coords))
print(f'Sum = {coords[start[0]:end[0], start[1]:end[1]].sum()}')
print()

start = [6, 6]
end = [3, 2]

# coords[start[0]:end[0], start[1]:end[1]] += 1

bl, tr = bl_tr(start, end)
print(bl, tr)
coords[bl[0]:tr[0], bl[1]:tr[1]] += 1

print(np.rot90(coords))
print(f'Sum = {coords[bl[0]:tr[0], bl[1]:tr[1]].sum()}')
# print(bl_tr(start, end))
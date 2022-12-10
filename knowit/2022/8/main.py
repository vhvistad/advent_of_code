from scipy.spatial import ConvexHull

poles = []
with open('knowit/2022/8/data.txt', 'r') as f:
    for line in f:
        poles.append([int(s) for s in line.strip().split(' ')])

print(ConvexHull(poles).volume) 
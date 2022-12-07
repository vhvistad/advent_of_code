from PIL import Image

def count_ones(n):
    ones = bin(n).count(1)
    return ones % 2 == 0

width = 0
height = 0

encrypted = []
with open('knowit/2022/7/encrypted.txt') as f:
    for line in f:
        height += 1
        encrypted.append(line.strip().split(' '))

width = len(encrypted[0])

print(f'({width}, {height})')
img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
pixels = img.load()
for y, row in enumerate(encrypted):
    for x, pixel in enumerate(row):
        if bin(int(pixel)).count('1') % 2 == 0:
            pixels[x, y] = (0, 0, 0)

img.show()
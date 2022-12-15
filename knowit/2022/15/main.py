gifts = []

with open('knowit/2022/15/data.csv') as f:
    f.readline()
    for line in f:
        gifts.append([int(s) for s in line.strip().split(',')])

bag_volume = 0
bag_value = 0
trips = 1

while len(gifts) > 0:
    for i, gift in enumerate(gifts):
        value, volume = gift[0], gift[1]
        if bag_volume + volume <= 120 or bag_value + value <= 1700:
            bag_volume += volume
            bag_value += value
            del gifts[i]
    trips += 1
    bag_value = 0
    bag_volume = 0
    if len(gifts) % 1000 == 0:
        print(len(gifts))

print(trips)
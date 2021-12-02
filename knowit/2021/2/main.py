from os.path import dirname, abspath, join
from math import floor, pi, sin, cos, atan2, sqrt
import csv
from types import new_class
from haversine import haversine


def read_csv(path):
    coords = []
    with open(path, 'r', encoding='cp850') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for city in csv_reader:
            point = [float(p) for p in city[1][6:-1].split(' ')]
            point = [point[1], point[0]]
            coords.append(point)
    return coords

def find_route(coords):
    total_distance = 0
    north_pole = [90.0, 0.0]
    position = north_pole
    while len(coords) > 0:
        nearest_city_index = 0
        smallest_distance = haversine(position, coords[0])
        for i, c in enumerate(coords[1:]):
            distance = haversine(position, c)
            if distance < smallest_distance:
                smallest_distance = distance
                nearest_city_index = i + 1
        position = coords.pop(nearest_city_index)
        total_distance += smallest_distance
        print(len(coords))
    total_distance += haversine(position, north_pole)
    return total_distance
        

if __name__ == "__main__":
    filename = 'cities.csv'
    path = join(dirname(abspath(__file__)), filename)
    coords = read_csv(path)
    result = find_route(coords)
    print(f'Result: {result}')
import math

r = 5
h = 16
area = math.pi * r * (r + math.sqrt(h*h + r*r)) - math.pi * r*r
cost = area * (0.04*10 + 0.04*15 + 0.02*30 + 0.05*15)
print(cost)
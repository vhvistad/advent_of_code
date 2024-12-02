

alv = []
teppe = []

with open('joe.txt', 'r') as a:
    for line in a.readlines():
        alv.append(line[:-1])

with open('teppe.txt', 'r') as t:
    for line in t.readlines():
        teppe.append(line[:-1])


width1 = max([len(l) for l in alv])
width2 = max(map(len, alv))



print(f'Width: {width2}')